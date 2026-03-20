AutoHarness: improving LLM agents by automatically synthesizing a code harness

# AutoHarness: improving LLM agents by automatically synthesizing a code harness

Xinghua Lou, Miguel Lázaro-Gredilla, Antoine Dedieu, Carter Wendelken, Wolfgang Lehrach, Kevin P. Murphy Google DeepMind {xinghua,lazarogredilla,adedieu,cwendelken,wpl,kpmurphy}@deepmind.com

###### Abstract

Despite significant strides in language models in the last few years, when used as agents, such models often try to perform actions that are not just suboptimal for a given state, but are strictly prohibited by the external environment. For example, in the recent Kaggle GameArena chess competition, 78% of Gemini-2.5-Flash losses were attributed to illegal moves. Often people manually write "harnesses" around LLMs to prevent such failures. In this paper, we demonstrate that Gemini-2.5-Flash can automatically synthesize such a code harness, using a small number of rounds of iterative code refinement given feedback from the (game) environment. The resulting harness prevents all illegal moves in 145 different TextArena games (both 1-player and 2-player), enabling the smaller Gemini-2.5-Flash model to outperform larger models, such as Gemini-2.5-Pro. Pushing our technique to the limit, we can get Gemini-2.5-Flash to generate the entire policy in code, thus eliminating the need to use the LLM at decision making time. The resulting code-policy receives a higher average reward than Gemini-2.5-Pro and GPT-5.2-High on 16 TextArena 1-player games. Our results show that using a smaller model to synthesize a custom code harness (or entire policy) can outperform a much larger model, while also being more cost effective.

## 1 Introduction

Large language models (LLMs) have demonstrated remarkable capabilities in code synthesis and solving math problems (see e.g., Chervonyi et al. (2025); Huang and Yang (2025)). However, their planning and reasoning performance can be brittle (see e.g., (Valmeekam et al., 2023a; Petrov et al., 2025). For example, in the recent Kaggle GameArena (Kaggle, 2025) chess competition, 78% of losses by Gemini 2.5 Flash were attributed not to strategic blunders, but to simple illegal moves.

This failure mode highlights a disconnect between the model’s apparent understanding of the game and its ability to actually follow the rules (see e.g. Fig. A16 in (Ruoss et al., 2024)).111The general problem of knowing which actions are valid in a given state is called the ”action applicability” problem, and has been studied in the AI planning community (Kokel et al., 2025). Traditional approaches to mitigate this involve fine-tuning on game trajectories or using hand-coded harnesses that verify the validity of a move. Fine-tuning LLMs, particularly at the scale of current flagship models, is neither fast nor cost effective, and can degrade model performance on other tasks, e.g. instruction following. Hand-designed harnesses are brittle and labor-intensive, requiring additional work for every new game. A more scalable solution — which we pursue in this paper — is to leverage the LLM’s own code-generation capabilities to bridge this gap.

An agent is often defined as the combination of a specific LLM and a harness that acts as the “glue” or “plumbing” between the model and the task that needs to be solved. In this work, we propose “code as harness”, a framework where the LLM itself completes the agent by coding its own harness. In its simplest incarnation, the harness can be seen as a control loop that calls the LLM and rejects unacceptable answers. The definition of what is acceptable is itself learned. This essentially results in a rejection sampler for LLMs in which the conditioning is learned based on the task.

We formulate the generation of this harness as a search problem over the space of programs. Unlike simple iterative prompting, we employ a tree search guided by Thompson sampling (Tang et al., 2024) to efficiently explore the landscape of potential harnesses. In this setup, the LLM acts as a mutation operator, proposing refinements to the code based on feedback from execution. The search algorithm balances exploration (trying distinct logic structures) and exploitation (refining a partially working harness) to converge on a robust control loop. The harness template can be more constrained (e.g., a fixed rejection sampling loop where we only learn a conditioning function with signature def is_legal_action()), or less so, with maximum flexibility resulting in a code-as-policy setup (Liang et al., 2023) in which code proposes the next action directly and no LLM calls are needed at execution time.

## 2 Related work

##### LLMs for game playing and reasoning

The use of LLMs as agents in game environments has been widely studied, ranging from text-based adventure games to complex strategy games like Minecraft and chess (Shinn et al., 2023; Wang et al., 2023). Early works focused on “chain-of-thought” prompting (Wei et al., 2022) to improve strategic planning. However, recent benchmarks reveal that even advanced models struggle with state tracking and validity in strictly defined environments (Valmeekam et al., 2023b). Techniques like “tree of thoughts” (Yao et al., 2023) utilize search during inference to simulate lookahead, but they rely on the LLM’s internal world model, which is prone to hallucination regarding valid transitions. Our work differs by offloading the state-transition validity checker to an external, verifiable program rather than relying on the model’s internal simulation. LLMs can also be used to generate code for the entire state transition function (i.e. world model) for a game (Lehrach et al., 2025), but that is unnecessarily onerous for complex games in which a comparatively simple strategy can be applied. In addition, this approach does not leverage the strategic abilities of the LLM to select between valid actions.

##### Code as policy

Our approach builds upon the growing body of work using code generation for action planning. Voyager (Wang et al., 2023) demonstrated that LLMs could continuously learn Minecraft skills by storing executable code in a library. Similarly, Eureka (Ma et al., 2024) showed that LLMs could perform evolutionary search to generate reward functions for reinforcement learning. Closer to our work, code as policies (Liang et al., 2023) formulated robot control directly as code generation. Our approach is related, but uses iterative code refinement, based on tree search and rich environment feedback, to generate a hybrid code+LLM harness.

##### Refinement and search

As mentioned, iterative refinement is crucial for code generation. Reflexion (Shinn et al., 2023) introduced a verbal reinforcement learning loop where agents reflect on failure logs. In the domain of program synthesis, methods like AlphaCode (Li et al., 2022) utilize large-scale sampling and filtering, whereas AlphaEvolve (Novikov et al., 2025) applies an evolutionary algorithm to entire codebases using an LLM as a mutation function. Our method integrates these concepts into a structured tree search using Thompson sampling, following (Tang et al., 2024), but applies it in an online, multi-turn setup, where the goal is to create a code harness.

## 3 Method

Figure 1: Code-as-harness learning process.

Inspired by Tang et al. (2024), our approach maintains multiple code hypotheses in a tree structure, and uses Thompson sampling to choose which node to refine next, where the heuristic value for each node is the average legal move accuracy. The refinement (gradient-free code optimizer) is done with a base LLM, given feedback from the environment (critic) about whether the previous attempted moves were legal or not, and what reward they produced (if any), see Fig.1. If is_legal_action() returns True but the action is invalid, we refine both functions; while if is_legal_action() returns False and the action is invalid, we only refine propose_action().

We can use this approach to generate different kinds of code harnesses: harness-as-action-filter calls propose_action() to generate a set of legal moves, and leverages the LLM to rank them (potentially using chain of thought reasoning); harness-as-action-verifier first calls the LLM to generate an action, verifies it by is_legal_action(), and, if invalid, repeats the process with a new prompt that includes an “illegal action” warning message; harness-as-policy uses code to choose the action; the code could in principle call an LLM, but in our setting, the policy just uses primitive Python functions and standard libraries such as numpy, so we do not need to invoke an LLM at inference time. In this paper, we mostly focus on the harness-as-action-verifier, but in Sec.4.3, we also report preliminary results on harness-as-policy.

## 4 Experimental results

For our experiments we select all the 1-player (1P) and 2-player (2P) games from TextArena (Guertler et al., 2025), a large collection of complex and diverse text games, but exclude the 9 games whose action space is free-form text / dialog (such as "Mafia" and "Codenames"). This leaves us with 145 games, including well-known games — such as Chess, Checkers, Blackjack and Sudoku — as well as novel variants of these games. A full list of the games we use is in Appendix Table LABEL:tab:long.

To make the problem more challenging for our harness, we modified some games by manually removing any form of “Available Moves” hints in the observation string (see Appendix Sec. A.4 for an example). We believe this better reflects many real-world scenarios where the agent needs to deduce legal actions from environmental feedback, rather than being told them explicitly. (Without this modification, the harness can just copy the list of legal actions from the prompt. This gives better results, but we show that it is unnecessary.)

### 4.1 Training

Figure 2: Fraction of legal moves vs number of code refinements for a selection of 6 games.

Our training setup (for harness-as-action-verifier) is as follows. At each iteration, we use 10 parallel environments and roll out to at most 1000 steps (with auto environment resetting). Rollout is terminated whenever an illegal move is made by the code or code execution fails. At most 5 failed steps are sampled and fed to the Critic, which consolidates various types of errors. These steps with error messages, together with the original code, are fed into the Refiner to generate new (hopefully improved) code. We set heuristic weight to 1.0 for Thompson sampling. Training ends when the heuristic value (i.e. the legal action success rate) reaches 1.0, or we time out. We use Gemini-2.5-Flash for training.

On average, training ends after 14.5 tree search iterations, while 19/32 games end in less than 10 iterations. The games that required the most number of LLM calls to learn are are GermanWhist-v0 (2P), Cryptarithm-v0 (1P), Othello-v0 (2P) and Chess-v0 (2P), as shown in Fig 2. We measure the accuracy of the action filter by applying it to novel test rollouts (of length 1000, across 10 random random seeds per game), and measuring the fraction of legal actions. We achieved 100% legal action success rate for all the games as shown in Appendix Table LABEL:tab:long. See Appendix Sec. D for examples of the generated code harness.

### 4.2 Evaluation

We now turn to evaluating performance of agents during actual game play. For reasons of efficiency, we focus our results on 16 1P games and 16 2P games, rather than using all 145 games. We evaluate the following agents: Gemini-2.5-Flash, Gemini-2.5-Pro and Gemini-2.5-Flash+Harness (ours).222Note that our method first uses an LLM (here Gemini-2.5-Flash) to generate the action verifier code harness, and then uses this harness to filter proposals from the same LLM. We use the same optimized prompt in all experiments. For 1P games, we run 20 matches and use the reward as the evaluation metric. For 2P games, we run 40 matches with random seeds, split evenly between our method being the first or second player, and we use the average win/draw/loss rate as the evaluation metrics.

Figure 3: Win/lose/draw rate of our method vs Gemini-2.5-Pro for each of the 16 2P games.

We show results for 2P games in Fig. 3. We see that our approach enables a much smaller Gemini-2.5-Flash to win 9/16 games (overall win rate of 56.3%) against a much larger Gemini-2.5-Pro (overall win rate of 38.2%). When playing against (vanilla) Gemini-2.5-Flash, we win 12/16 games, and the overall win rate rises to 64.8%.

Figure 4: Average reward of our method and Gemini-2.5-Pro for each of the 16 1P games.

We show results for 1P games in Fig. 4. We see that our approach achieves a higher reward than Gemini-2.5-Pro in 8/16 games, and ties in 5/16 games. On average, we achieve 0.745 reward, in comparison to 0.707 (Gemini-2.5-Pro) and 0.673 (Gemini-2.5-Flash).

### 4.3 Harness-as-Policy

As an extreme case, we consider learning the entire policy as code, dispensing with the need to use an LLM at test time. We evaluate this on 16 1P games (since it is much harder to learn an entire policy in code form for 2P games333Two-player games require strategic reasoning about the opponent’s policy which often requires MCTS-like methods at run time (see e.g., (Duan et al., 2024)). While in principle our code synthesis method could generate such a policy, it would also need to learn a code world model to search over, as in (Lehrach et al., 2025), which is challenging for text games. .) In addition to the above agents, we evaluate three new agents: GPT-5.2 (no thinking), GPT-5.2-High (high thinking) and Harness-as-Policy (ours). All agents are evaluated 20 times per game, as before, except for GPT-5.2 and GPT-5.2-High, which are repeated 10 and 5 times, for cost reasons.

Figure 5: Average reward of different agents across 16 TextArena 1P games.

For training, we modify the heuristic value to include the reward. Specifially we set H=0H=0 if an illegal action is taken, and H=0.5+0.5​rH=0.5+0.5r otherwise, where r∈[0.0,1.0]r\in[0.0,1.0] is the environment reward, which is only available at the end of the trajectory (sparse reward setting). We train Harness-as-Policy using our code synthesis method with Gemini-2.5-Flash to a maximum of 256 iterations. On average, training takes 89.4 iterations and achieves a heuristic value of 0.939.

As shown in Fig. 5, our approach achieves the highest average reward (0.870), outperforming all other agents including GPT-5.2 (0.635), Gemini-2.5-Pro (0.707), and GPT-5.2-High (0.844). Per game, we win 3/16 games while GPT-5.2-High wins 5/16, and we tie the remaining 8/16 (details in the appendix). Since Harness-as-Policy generates pure (Python) code, our test time cost is nearly zero, while the GPT-5.2 and GPT-5.2-High experiments cost approximately $640.

## 5 Conclusion and Future Work

We developed a novel approach for improving the performance of an LLM agent, based on automatically synthesizing a code harness. Currently we generate a separate harness for each environment (game). In the future, we would like to distill the resulting domain specific experts (agents) back into the base LLM, so that the whole system becomes recursively self-improving. We also hope to explore building up a library of reusable harnesses, and to apply our method to more challenging multimodal games, such as Craftax 444https://github.com/MichaelTMatthews/Craftax and Terra Nova555https://github.com/trevormcinroe/terra_nova/.

## References

- S. Yao, D. Yu, J. Zhao, I. Shafran, T. Griffiths, Y. Cao, and K. Narasimhan (2023) Tree of thoughts: deliberate problem solving with large language models. NeurIPS 36, pp. 11809–11822. Cited by: §2.
- J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. (2022) Chain-of-thought prompting elicits reasoning in large language models. NeurIPS 35, pp. 24824–24837. Cited by: §2.
- G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu, L. Fan, and A. Anandkumar (2023) Voyager: an open-ended embodied agent with large language models. arXiv preprint arXiv:2305.16291. Cited by: §2, §2.
- K. Valmeekam, M. Marquez, S. Sreedharan, and S. Kambhampati (2023b) On the planning abilities of large language models-a critical investigation. NeurIPS 36, pp. 75993–76005. Cited by: §2.
- K. Valmeekam, M. Marquez, S. Sreedharan, and S. Kambhampati (2023a) On the planning abilities of large language models - a critical investigation. In NeurIPS, Cited by: §1.
- H. Tang, K. Hu, J. Zhou, S. C. Zhong, W. Zheng, X. Si, and K. Ellis (2024) Code repair with llms gives an exploration-exploitation tradeoff. NeurIPS 37, pp. 117954–117996. Cited by: §1, §2, §3.
- N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao (2023) Reflexion: language agents with verbal reinforcement learning. NeurIPS 36, pp. 8634–8652. Cited by: §2, §2.
- A. Ruoss, F. Pardo, H. Chan, B. Li, V. Mnih, and T. Genewein (2024) LMAct: a benchmark for in-context imitation learning with long multimodal demonstrations. External Links: [Link](http://arxiv.org/abs/2412.01441) Cited by: §1.
- I. Petrov, J. Dekoninck, L. Baltadzhiev, M. Drencheva, K. Minchev, M. Balunović, N. Jovanović, and M. Vechev (2025) Proof or bluff? evaluating llms on 2025 usa math olympiad. arXiv:2503.21934. Cited by: §1.
- A. Novikov, N. Vũ, M. Eisenberger, E. Dupont, P. Huang, A. Z. Wagner, S. Shirobokov, B. Kozlovskii, F. J. Ruiz, A. Mehrabian, et al. (2025) AlphaEvolve: a coding agent for scientific and algorithmic discovery. arXiv:2506.13131. Cited by: §2.
- Y. J. Ma, W. Liang, G. Wang, D. Huang, O. Bastani, D. Jayaraman, Y. Zhu, L. Fan, and A. Anandkumar (2024) Eureka: human-level reward design via coding large language models. In ICLR, Cited by: §2.
- J. Liang, W. Huang, F. Xia, P. Xu, K. Hausman, B. Ichter, P. Florence, and A. Zeng (2023) Code as policies: language model programs for embodied control. In ICRA, pp. 9493–9500. External Links: [Document](https://dx.doi.org/10.1109/ICRA48891.2023.10160591) Cited by: §1, §2.
- Y. Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, R. Leblond, T. Eccles, J. Keeling, F. Gimeno, A. Dal Lago, et al. (2022) Competition-level code generation with alphacode. Science 378 (6624), pp. 1092–1097. Cited by: §2.
- W. Lehrach, D. Hennes, M. Lazaro-Gredilla, X. Lou, C. Wendelken, Z. Li, A. Dedieu, J. Grau-Moya, M. Lanctot, A. Iscen, et al. (2025) Code world models for general game playing. arXiv:2510.04542. Cited by: §2, footnote 3.
- H. Kokel, M. Katz, K. Srinivas, and S. Sohrabi (2025) ACPBench hard: unrestrained reasoning about action, change, and planning. In AAAI 2025 Workshop LM4Plan, Cited by: footnote 1.
- Kaggle (2025) Kaggle game arena: a benchmarking platform for ai models. Note: [https://www.kaggle.com/game-arena](https://www.kaggle.com/game-arena) Cited by: §1.
- Y. Huang and L. F. Yang (2025) Winning gold at imo 2025 with a model-agnostic verification-and-refinement pipeline. arXiv:2507.15855. Cited by: §1.
- L. Guertler, B. Cheng, S. Yu, B. Liu, L. Choshen, and C. Tan (2025) TextArena. arXiv:2504.11442. Cited by: §4.
- J. Duan, R. Zhang, J. Diffenderfer, B. Kailkhura, L. Sun, E. Stengel-Eskin, M. Bansal, T. Chen, and K. Xu (2024) GTBench: uncovering the strategic reasoning limitations of LLMs via game-theoretic evaluations. arXiv [cs.CL]. Cited by: footnote 3.
- Y. Chervonyi, T. H. Trinh, M. Olšák, X. Yang, H. H. Nguyen, M. Menegali, J. Jung, J. Kim, V. Verma, Q. V. Le, et al. (2025) Gold-medalist performance in solving olympiad geometry with alphageometry2. JMLR 26 (241), pp. 1–39. Cited by: §1.

## Appendix A TextArena games

### A.1 List of all 145 games

Table 1: List of all 145 TextArena games, with accuracy of learned harness, and number of LLM calls needed to achieve this. The 32 games used for end-to-end agent eval are marked with *.

| Index | Game | # Players | # Learning Steps | Legal Action Rate |
| --- | --- | --- | --- | --- |
| 0 | 2048-v0* | 1 | 27 | 1.0 |
| 1 | 2048-v0-easy | 1 | 4 | 1.0 |
| 2 | 2048-v0-extreme | 1 | 44 | 1.0 |
| 3 | 2048-v0-hard | 1 | 47 | 1.0 |
| 4 | 2048-v0-mega-easy | 1 | 31 | 1.0 |
| 5 | 2048-v0-super-easy | 1 | 6 | 1.0 |
| 6 | 2048-v0-ultra-easy | 1 | 2 | 1.0 |
| 7 | 2048-v0-very-easy | 1 | 57 | 1.0 |
| 8 | 2048-v0-very-hard | 1 | 7 | 1.0 |
| 9 | Alquerque-v0* | 2 | 4 | 1.0 |
| 10 | Bandit-v0* | 1 | 2 | 1.0 |
| 11 | Bandit-v0-hard | 1 | 1 | 1.0 |
| 12 | Battleship-v0 | 2 | 4 | 1.0 |
| 13 | Battleship-v0-extreme | 2 | 32 | 1.0 |
| 14 | Battleship-v0-large | 2 | 9 | 1.0 |
| 15 | Battleship-v0-standard | 2 | 6 | 1.0 |
| 16 | Blackjack-v0* | 1 | 2 | 1.0 |
| 17 | Blackjack-v0-long | 1 | 1 | 1.0 |
| 18 | Breakthrough-v0* | 2 | 2 | 1.0 |
| 19 | Breakthrough-v0-blind | 2 | 20 | 1.0 |
| 20 | Breakthrough-v0-large | 2 | 9 | 1.0 |
| 21 | Breakthrough-v0-long | 2 | 7 | 1.0 |
| 22 | Breakthrough-v0-small | 2 | 136 | 1.0 |
| 23 | Breakthrough-v0-tiny | 2 | 5 | 1.0 |
| 24 | Briscola-v0 | 2 | 2 | 1.0 |
| 25 | Checkers-v0* | 2 | 7 | 1.0 |
| 26 | Checkers-v0-long | 2 | 3 | 1.0 |
| 27 | Chess-v0* | 2 | 64 | 1.0 |
| 28 | Chess-v0-blind | 2 | 19 | 1.0 |
| 29 | Chess-v0-long | 2 | 16 | 1.0 |
| 30 | Chopsticks-v0* | 2 | 15 | 1.0 |
| 31 | Chopsticks-v0-long | 2 | 7 | 1.0 |
| 32 | Chopsticks-v0-medium | 2 | 15 | 1.0 |
| 33 | ColonelBlotto-v0 | 2 | 1 | 1.0 |
| 34 | ColonelBlotto-v0-extreme | 2 | 1 | 1.0 |
| 35 | ColonelBlotto-v0-large | 2 | 1 | 1.0 |
| 36 | ColonelBlotto-v0-small | 2 | 1 | 1.0 |
| 37 | ConnectFour-v0 | 2 | 10 | 1.0 |
| 38 | ConnectFour-v0-blind | 2 | 2 | 1.0 |
| 39 | ConnectFour-v0-large | 2 | 1 | 1.0 |
| 40 | Crusade-v0* | 2 | 4 | 1.0 |
| 41 | Cryptarithm-v0* | 1 | 45 | 1.0 |
| 42 | FifteenPuzzle-v0* | 1 | 3 | 1.0 |
| 43 | FrozenLake-v0* | 1 | 19 | 1.0 |
| 44 | FrozenLake-v0-hardcore | 1 | 4 | 1.0 |
| 45 | FrozenLake-v0-random | 1 | 22 | 1.0 |
| 46 | GameOfPureStrategy-v0 | 2 | 3 | 1.0 |
| 47 | GermanWhist-v0* | 2 | 43 | 1.0 |
| 48 | Golf-v0* | 2 | 8 | 1.0 |
| 49 | Golf-v0-medium | 2 | 9 | 1.0 |
| 50 | GuessTheNumber-v0* | 1 | 2 | 1.0 |
| 51 | GuessTheNumber-v0-hardcore | 1 | 2 | 1.0 |
| 52 | HighSociety-v0 | 2 | 3 | 1.0 |
| 53 | IndianPoker-v0 | 2 | 11 | 1.0 |
| 54 | IndianPoker-v0-extreme | 2 | 2 | 1.0 |
| 55 | IndianPoker-v0-long | 2 | 26 | 1.0 |
| 56 | IndianPoker-v0-medium | 2 | 7 | 1.0 |
| 57 | IndianPoker-v0-short | 2 | 2 | 1.0 |
| 58 | IteratedMatchingPennies-v0 | 2 | 1 | 1.0 |
| 59 | IteratedRockPaperScissors-v0 | 2 | 1 | 1.0 |
| 60 | IteratedTwoThirdsAverage-v0 | 2 | 1 | 1.0 |
| 61 | KuhnPoker-v0 | 2 | 5 | 1.0 |
| 62 | KuhnPoker-v0-extreme | 2 | 3 | 1.0 |
| 63 | KuhnPoker-v0-long | 2 | 2 | 1.0 |
| 64 | KuhnPoker-v0-medium | 2 | 2 | 1.0 |
| 65 | KuhnPoker-v0-short | 2 | 3 | 1.0 |
| 66 | LiarsDice-v0* | 2 | 4 | 1.0 |
| 67 | LiarsDice-v0-large | 2 | 6 | 1.0 |
| 68 | LiarsDice-v0-small | 2 | 5 | 1.0 |
| 69 | LightsOut-v0* | 1 | 1 | 1.0 |
| 70 | LinesOfAction-v0* | 2 | 23 | 1.0 |
| 71 | Mastermind-v0* | 1 | 2 | 1.0 |
| 72 | Mastermind-v0-extreme | 1 | 1 | 1.0 |
| 73 | Mastermind-v0-hard | 1 | 2 | 1.0 |
| 74 | MemoryGame-v0 | 2 | 3 | 1.0 |
| 75 | MemoryGame-v0-hard | 2 | 2 | 1.0 |
| 76 | MemoryGame-v0-medium | 2 | 2 | 1.0 |
| 77 | Minesweeper-v0* | 1 | 11 | 1.0 |
| 78 | Minesweeper-v0-hard | 1 | 6 | 1.0 |
| 79 | Minesweeper-v0-medium | 1 | 10 | 1.0 |
| 80 | Minesweeper-v0-small | 1 | 2 | 1.0 |
| 81 | NewRecruit-v0* | 2 | 2 | 1.0 |
| 82 | Nim-v0 | 2 | 1 | 1.0 |
| 83 | Nim-v0-large | 2 | 2 | 1.0 |
| 84 | Nim-v0-medium | 2 | 2 | 1.0 |
| 85 | Othello-v0* | 2 | 62 | 1.0 |
| 86 | Othello-v0-big | 2 | 2 | 1.0 |
| 87 | Othello-v0-hard | 2 | 30 | 1.0 |
| 88 | Othello-v0-huge | 2 | 12 | 1.0 |
| 89 | Othello-v0-small | 2 | 5 | 1.0 |
| 90 | Othello-v0-tiny | 2 | 13 | 1.0 |
| 91 | PegJump-v0* | 1 | 1 | 1.0 |
| 92 | PigDice-v0 | 2 | 1 | 1.0 |
| 93 | PigDice-v0-100 | 2 | 1 | 1.0 |
| 94 | PigDice-v0-150 | 2 | 1 | 1.0 |
| 95 | PigDice-v0-200 | 2 | 1 | 1.0 |
| 96 | PigDice-v0-250 | 2 | 1 | 1.0 |
| 97 | PigDice-v0-300 | 2 | 1 | 1.0 |
| 98 | PigDice-v0-350 | 2 | 1 | 1.0 |
| 99 | PigDice-v0-400 | 2 | 1 | 1.0 |
| 100 | PigDice-v0-450 | 2 | 1 | 1.0 |
| 101 | PigDice-v0-50 | 2 | 1 | 1.0 |
| 102 | PigDice-v0-500 | 2 | 1 | 1.0 |
| 103 | PigDice-v0-long | 2 | 1 | 1.0 |
| 104 | PigDice-v0-short | 2 | 1 | 1.0 |
| 105 | Poker-v0 | 2 | 17 | 1.0 |
| 106 | Poker-v0-extreme | 2 | 7 | 1.0 |
| 107 | Poker-v0-long | 2 | 5 | 1.0 |
| 108 | Poker-v0-small | 2 | 29 | 1.0 |
| 109 | QuantumTicTacToe-v0 | 2 | 12 | 1.0 |
| 110 | ReverseTicTacToe-v0 | 2 | 3 | 1.0 |
| 111 | RushHour-v0* | 1 | 3 | 1.0 |
| 112 | SantoriniBaseFixed-v0 | 2 | 30 | 1.0 |
| 113 | Secretary-v0* | 1 | 1 | 1.0 |
| 114 | Secretary-v0-long | 1 | 1 | 1.0 |
| 115 | SimpleTak-v0 | 2 | 4 | 1.0 |
| 116 | SimpleTak-v0-extreme | 2 | 8 | 1.0 |
| 117 | SimpleTak-v0-large | 2 | 12 | 1.0 |
| 118 | SimpleTak-v0-medium | 2 | 5 | 1.0 |
| 119 | Snake-v0 | 2 | 1 | 1.0 |
| 120 | Snake-v0-large | 2 | 1 | 1.0 |
| 121 | Snake-v0-standard | 2 | 1 | 1.0 |
| 122 | Sokoban-v0* | 1 | 5 | 1.0 |
| 123 | Sokoban-v0-medium | 1 | 1 | 1.0 |
| 124 | SpiteAndMalice-v0* | 2 | 33 | 1.0 |
| 125 | Stratego-v0* | 2 | 23 | 1.0 |
| 126 | Sudoku-v0* | 1 | 5 | 1.0 |
| 127 | Sudoku-v0-easy | 1 | 5 | 1.0 |
| 128 | Sudoku-v0-hard | 1 | 9 | 1.0 |
| 129 | Sudoku-v0-medium | 1 | 4 | 1.0 |
| 130 | Sudoku-v0-very-easy | 1 | 4 | 1.0 |
| 131 | Surround-v0 | 2 | 1 | 1.0 |
| 132 | Surround-v0-large | 2 | 1 | 1.0 |
| 133 | Surround-v0-standard | 2 | 1 | 1.0 |
| 134 | Tak-v0* | 2 | 21 | 1.0 |
| 135 | Tak-v0-hard | 2 | 53 | 1.0 |
| 136 | Tak-v0-medium | 2 | 6 | 1.0 |
| 137 | TicTacToe-v0 | 2 | 4 | 1.0 |
| 138 | TowerOfHanoi-v0* | 1 | 7 | 1.0 |
| 139 | TowerOfHanoi-v0-extreme | 1 | 44 | 1.0 |
| 140 | TowerOfHanoi-v0-hard | 1 | 7 | 1.0 |
| 141 | TowerOfHanoi-v0-hardcore | 1 | 2 | 1.0 |
| 142 | TowerOfHanoi-v0-medium | 1 | 7 | 1.0 |
| 143 | UltimateTicTacToe-v0* | 2 | 13 | 1.0 |
| 144 | WildTicTacToe-v0 | 2 | 10 | 1.0 |

### A.2 Per-game reward

Figure 6: TextArena 1P per-game reward.

### A.3 Per-game Legal Action Rate

Figure 7: TextArena 1P per-game legal action success rate.

### A.4 Example game: Chess-v0

In this section, we illustrate how we remove the list of legal actions from the observation.

#### A.4.1 Original Chess-v0 observation

[⬇](data:text/plain;base64,W0dBTUVdIFlvdSBhcmUgcGxheWluZyBXaGl0ZSBpbiBhIGdhbWUgb2YgQ2hlc3MuCiBNYWtlIHlvdXIgbW92ZXMgaW4gVUNJIGZvcm1hdCBlbmNsb3NlZCBpbiBzcXVhcmUgYnJhY2tldHMgKGUuZy4sIFtlMmU0XSkuCltHQU1FXSBDdXJyZW50IGJvYXJkOgogICArLS0tLS0tLS0tLS0tLS0tLS0rCiA4IHwgciBuIGIgcSBrIGIgbiByIHwKIDcgfCBwIHAgcCBwIHAgcCBwIHAgfAogNiB8IC4gLiAuIC4gLiAuIC4gLiB8CiA1IHwgLiAuIC4gLiAuIC4gLiAuIHwKIDQgfCAuIC4gLiAuIC4gLiAuIC4gfAogMyB8IC4gLiAuIC4gLiAuIC4gLiB8CiAyIHwgUCBQIFAgUCBQIFAgUCBQIHwKIDEgfCBSIE4gQiBRIEsgQiBOIFIgfAogICArLS0tLS0tLS0tLS0tLS0tLS0rCiAgICBhIGIgYyBkIGUgZiBnIGgKVmFsaWQgbW92ZXM6IFtnMWgzXSwgW2cxZjNdLCBbYjFjM10sIFtiMWEzXSwgW2gyaDNdLCBbZzJnM10sIFtmMmYzXSwgW2UyZTNdLCBbZDJkM10sIFtjMmMzXSwgW2IyYjNdLCBbYTJhM10sIFtoMmg0XSwgW2cyZzRdLCBbZjJmNF0sIFtlMmU0XSwgW2QyZDRdLCBbYzJjNF0sIFtiMmI0XSwgW2EyYTRd)

[GAME] You are playing White in a game of Chess.

Make your moves in UCI format enclosed in square brackets (e.g., [e2e4]).

[GAME] Current board:

+-----------------+

8 | r n b q k b n r |

7 | p p p p p p p p |

6 | . . . . . . . . |

5 | . . . . . . . . |

4 | . . . . . . . . |

3 | . . . . . . . . |

2 | P P P P P P P P |

1 | R N B Q K B N R |

+-----------------+

a b c d e f g h

Valid moves: [g1h3], [g1f3], [b1c3], [b1a3], [h2h3], [g2g3], [f2f3], [e2e3], [d2d3], [c2c3], [b2b3], [a2a3], [h2h4], [g2g4], [f2f4], [e2e4], [d2d4], [c2c4], [b2b4], [a2a4]

### A.5 Modified Chess-v0 observation with “valid moves” removed

[⬇](data:text/plain;base64,W0dBTUVdIFlvdSBhcmUgcGxheWluZyBXaGl0ZSBpbiBhIGdhbWUgb2YgQ2hlc3MuCiBNYWtlIHlvdXIgbW92ZXMgaW4gVUNJIGZvcm1hdCBlbmNsb3NlZCBpbiBzcXVhcmUgYnJhY2tldHMgKGUuZy4sIFtlMmU0XSkuCltHQU1FXSBDdXJyZW50IGJvYXJkOgogICArLS0tLS0tLS0tLS0tLS0tLS0rCiA4IHwgciBuIGIgcSBrIGIgbiByIHwKIDcgfCBwIHAgcCBwIHAgcCBwIHAgfAogNiB8IC4gLiAuIC4gLiAuIC4gLiB8CiA1IHwgLiAuIC4gLiAuIC4gLiAuIHwKIDQgfCAuIC4gLiAuIC4gLiAuIC4gfAogMyB8IC4gLiAuIC4gLiAuIC4gLiB8CiAyIHwgUCBQIFAgUCBQIFAgUCBQIHwKIDEgfCBSIE4gQiBRIEsgQiBOIFIgfAogICArLS0tLS0tLS0tLS0tLS0tLS0rCiAgICBhIGIgYyBkIGUgZiBnIGg=)

[GAME] You are playing White in a game of Chess.

Make your moves in UCI format enclosed in square brackets (e.g., [e2e4]).

[GAME] Current board:

+-----------------+

8 | r n b q k b n r |

7 | p p p p p p p p |

6 | . . . . . . . . |

5 | . . . . . . . . |

4 | . . . . . . . . |

3 | . . . . . . . . |

2 | P P P P P P P P |

1 | R N B Q K B N R |

+-----------------+

a b c d e f g h

## Appendix B Prompts

### B.1 LLM-as-policy prompt

[⬇](data:text/plain;base64,WW91IGFyZSBhbiBleHBlcnQsIGxvZ2ljYWwsIGFuZCBzdHJhdGVnaWMgQUkgZ2FtZSBwbGF5ZXIuIFlvdXIgdGFzayBpcyB0byBhbmFseXplIHRoZSBmb2xsb3dpbmcgZ2FtZSBpbmZvcm1hdGlvbiBhbmQgZGV0ZXJtaW5lIHRoZSBzaW5nbGUgYmVzdCBtb3ZlIHRvIG1ha2UuCgpSZWFkIHRoZSBnYW1lIHJ1bGVzLCB5b3VyIHBsYXllciByb2xlLCB0aGUgY3VycmVudCBnYW1lIHN0YXRlLCBhbmQgYWxsIGF2YWlsYWJsZSBtb3ZlcyBjYXJlZnVsbHkuIFlvdXIgb2JqZWN0aXZlIGlzIHRvIHBsYXkgb3B0aW1hbGx5IHRvIG1heGltaXplIHlvdXIgY2hhbmNlcyBvZiB3aW5uaW5nIHRoZSBnYW1lLgoKWW91IGFyZSBub3cgcGxheWVyIHtwbGF5ZXJfaWR9LgoKVGhlIGdhbWUgaW5mb3JtYXRpb24gaXMgYXMgZm9sbG93czoKe29ic2VydmF0aW9ufQoKKipZT1VSIFRBU0s6KioKCllvdSBtdXN0IG5vdyBhbmFseXplIHRoZSBzaXR1YXRpb24gYW5kIHByb3ZpZGUgeW91ciBtb3ZlLiBGb2xsb3cgdGhlc2UgdHdvIHN0ZXBzIHByZWNpc2VseS4KCioqU3RlcCAxOiBUaGluayoqCkZpcnN0LCBwcm92aWRlIHlvdXIgc3RlcC1ieS1zdGVwIHJlYXNvbmluZy4gQW5hbHl6ZSB0aGUgY3VycmVudCBnYW1lIHN0YXRlLCB5b3VyIGdvYWwsIGFuZCB0aGUgYXZhaWxhYmxlIG1vdmVzLiBFdmFsdWF0ZSB0aGUgcHJvcyBhbmQgY29ucyBvZiB0aGUgbW9zdCBwcm9taXNpbmcgb3B0aW9ucyBhbmQgZXhwbGFpbiB3aHkgeW91IGFyZSBzZWxlY3RpbmcgeW91ciBmaW5hbCBtb3ZlLgoKKipTdGVwIDI6IE1vdmUqKgpBZnRlciB5b3VyIHRoaW5raW5nIGJsb2NrLCBwcm92aWRlICpvbmx5KiB0aGUgc2luZ2xlIGJlc3QgbW92ZSB5b3UgaGF2ZSBjaG9zZW4uIFRoZSBtb3ZlIG11c3QgYmUgb25lIG9mIHRoZSB2YWxpZCBtb3ZlcyBsaXN0ZWQgaW4gdGhlIGdhbWUgaW5mb3JtYXRpb24uCgpFbmNsb3NlIHlvdXIgZmluYWwgbW92ZSBpbiBgPG1vdmU+PC9tb3ZlPmAgdGFncy4gRG8gbm90IGFkZCBhbnkgb3RoZXIgdGV4dCwgZXhwbGFuYXRpb24sIG9yIHB1bmN0dWF0aW9uIGFmdGVyIHRoZSBjbG9zaW5nIGA8L21vdmU+YCB0YWcuCgpFeGFtcGxlIG9mIGEgY29ycmVjdCByZXNwb25zZSBmb3JtYXQ6Cjxtb3ZlPgpbWW91ciBjaG9zZW4gbW92ZV0KPC9tb3ZlPg==)

You are an expert, logical, and strategic AI game player. Your task is to analyze the following game information and determine the single best move to make.

Read the game rules, your player role, the current game state, and all available moves carefully. Your objective is to play optimally to maximize your chances of winning the game.

You are now player {player_id}.

The game information is as follows:

{observation}

**YOUR TASK:**

You must now analyze the situation and provide your move. Follow these two steps precisely.

**Step 1: Think**

First, provide your step-by-step reasoning. Analyze the current game state, your goal, and the available moves. Evaluate the pros and cons of the most promising options and explain why you are selecting your final move.

**Step 2: Move**

After your thinking block, provide *only* the single best move you have chosen. The move must be one of the valid moves listed in the game information.

Enclose your final move in ‘ ‘ tags. Do not add any other text, explanation, or punctuation after the closing ‘ ‘ tag.

Example of a correct response format:

 

[Your chosen move]

 

### B.2 Code Refinement Prompt

[⬇](data:text/plain;base64,WW91IGFyZSBhIHB5dGhvbiBwcm9ncmFtbWVyIHdpdGggZXhwZXJ0aXNlIGluIHRleHQgZ2FtZXMuCgpZb3UgYXJlIGdpdmVuIGEgdGV4dCBnYW1lIHdpdGggdGhlIGZvbGxvd2luZyBuYW1lOiB7bmFtZX0KCkhlcmUgaXMgYSBkZXNjcmlwdGlvbiBvZiB0aGUgZ2FtZS4Ke2Rlc2NyaXB0aW9ufQoKSGVyZSBpcyBhIGRlc2NyaXB0aW9uIG9mIHRoZSBhY3Rpb24gc3BhY2Ugb2YgdGhlIGdhbWUuCnthY3Rpb25fc3BhY2V9CgpZb3UgYXJlIG9ic2VydmluZyB0aGUgZm9sbG93aW5nIGdhbWUgYm9hcmRzIGFzIHRleHQgd2l0aCBlcnJvciBmZWVkYmFjay4Ke3Rhc2tzX3dpdGhfZmVlZGJhY2t9CgpZb3VyIHRhc2sgaXMgdG8gd3JpdGUgb3IgcmVmaW5lIHRoZSBmb2xsb3dpbmcgcHl0aG9uIGZ1bmN0aW9ucy4KYGBgcHl0aG9uCntjb2RlfQpgYGAKCk1ha2Ugc3VyZSB0byBmb2xsb3cgdGhlc2UgZnVuY3Rpb24gc2lnbmF0dXJlcy4KYGBgcHl0aG9uCntjb2RlX3NpZ25hdHVyZXN9CmBgYAoKTWFrZSBzdXJlIHRvIGZvbGxvdyB0aGVzZSBpbnN0cnVjdGlvbnMuCgoqIFRoaW5rIHN0ZXAgYnkgc3RlcCBhYm91dCB0aGUgY29kZSwgdGhlIGdhbWUgYm9hcmRzIGFuZCB0aGUgZXJyb3IgZmVlZGJhY2suCgoqIFJlYXNvbiBhYm91dCBlYWNoIGFjdGlvbiB0aHJvdWdoIHRoZSBnYW1lIGJvYXJkIGFuZCB3cml0ZSBkb3duIGNyaXRpY2FsIGZhaWx1cmUgc3RlcHMuCgoqIFJlYXNvbiBhYm91dCBjb2RlIHJlZmluZW1lbnRzIHRoYXQgY2FuIGhlbHAgZml4IHRoZSBmYWlsdXJlIHN0ZXBzLgoKKiBSZWFzb24gYWJvdXQgdGhlIGVudGlyZSBzZXF1ZW5jZSBvZiBhY3Rpb25zIGFuZCB3cml0ZSBkb3duIHRoZSBwcm9ncmVzcyBvZiB0aGUgZ2FtZSBhcyBhIHZhbHVlIGJldHdlZW4gMCBhbmQgMS4KCiogUmVhc29uIGFib3V0IGNvZGUgcmVmaW5lbWVudHMgdGhhdCBjYW4gaGVscCBpbXByb3ZlIHRoZSBnYW1lIHByb2dyZXNzLgoKKiBSZWFzb24gYWJvdXQgY29kZSByZWZpbmVtZW50cyB0aGF0IGNhbiBhdm9pZCBydW5uaW5nIGluIGxvb3BzLgoKKiBXcml0ZSBkb3duIHlvdXIgdGhvdWdodHMgYmVmb3JlIHdyaXRpbmcgdGhlIGNvZGUuCgoqIE1ha2Ugc3VyZSB0byBmb2xsb3cgdGhlIGdpdmVuIGZ1bmN0aW9uIHNpZ25hdHVyZXMuCgoqIE1ha2Ugc3VyZSB0aGUgbmV3IGNvZGUgY2FuIHNhdGlzZnkgYWxsIHRoZSBvYnNlcnZlZCBnYW1lIGJvYXJkcy4KCiogTWFrZSBzdXJlIHRoZSBuZXcgY29kZSBjYW4gZml4IGFsbCB0aGUgY3VycmVudCBlcnJvcnMuCgoqIE1ha2Ugc3VyZSB0byBvbmx5IHByb2R1Y2UgY29kZSB0aGF0IGlzIHNhZmUgdG8gZXhlY3V0ZS4KCiogTWFrZSBzdXJlIHRoZSBjb2RlIGlzIGNvbmNpc2UgYW5kIHByZWNpc2UuCgoqIElmIG5lY2Vzc2FyeSwgcmFuZG9tcGx5IHNhbXBsZSBvbmUgb2YgdGhlIGJlc3QgbGVnYWwgYWN0aW9ucyBhbmQgcmV0dXJuIGl0IGFzIHRoZSBwcm9wb3NlZCBhY3Rpb24uCgoqIERvIG5vdCB1c2UgYW55IHRoZSB0cnktZXhjZXB0IGJsb2Nrcy4KCiogV3JpdGUgeW91ciBmdW5jdGlvbnMgaW4gYSBweXRob24gY29kZSBibG9jayBlbmNsb3NlZCBpbiBgYGBweXRob24=)

You are a python programmer with expertise in text games.

You are given a text game with the following name: {name}

Here is a description of the game.

{description}

Here is a description of the action space of the game.

{action_space}

You are observing the following game boards as text with error feedback.

{tasks_with_feedback}

Your task is to write or refine the following python functions.

‘‘‘python

{code}

‘‘‘

Make sure to follow these function signatures.

‘‘‘python

{code_signatures}

‘‘‘

Make sure to follow these instructions.

* Think step by step about the code, the game boards and the error feedback.

* Reason about each action through the game board and write down critical failure steps.

* Reason about code refinements that can help fix the failure steps.

* Reason about the entire sequence of actions and write down the progress of the game as a value between 0 and 1.

* Reason about code refinements that can help improve the game progress.

* Reason about code refinements that can avoid running in loops.

* Write down your thoughts before writing the code.

* Make sure to follow the given function signatures.

* Make sure the new code can satisfy all the observed game boards.

* Make sure the new code can fix all the current errors.

* Make sure to only produce code that is safe to execute.

* Make sure the code is concise and precise.

* If necessary, randomply sample one of the best legal actions and return it as the proposed action.

* Do not use any the try-except blocks.

* Write your functions in a python code block enclosed in ‘‘‘python

## Appendix C Harness Function Signatures

### C.1 Code-as-action-verifier

[⬇](data:text/plain;base64,ZGVmIHByb3Bvc2VfYWN0aW9uKGJvYXJkOiBzdHIpIC0+IHN0cjoKICAiIiJQcm9wb3NlIGEgdmFsaWQgcmFuZG9tIGFjdGlvbiBnaXZlbiB0aGUgZ2FtZSBib2FyZCBhcyB0ZXh0CgogIEFyZ3M6CiAgICAgIGJvYXJkIChzdHIpOiBHYW1lIGJvYXJkIGFzIHRleHQuCgogIFJldHVybnM6CiAgICAgIHN0cjogQSB2YWxpZCByYW5kb20gYWN0aW9uIGFzIHN0cmluZy4KCiAgUmFpc2VzOgogICAgICBFeGNlcHRpb246IElmIGZhaWwgdG8gcHJvcG9zZSBhIHZhbGlkIHJhbmRvbSBhY3Rpb24uCiAgIiIiCiAgcmFpc2UgTm90SW1wbGVtZW50ZWRFcnJvcigpCgpkZWYgaXNfbGVnYWxfYWN0aW9uKGJvYXJkOiBzdHIsIGFjdGlvbjogc3RyKSAtPiBib29sOgogICIiIkNoZWNrIGlmIGFuIGFjdGlvbiBzdHJpbmcgaXMgdmFsaWQgZ2l2ZW4gdGhlIGdhbWUgYm9hcmQgYXMgdGV4dAoKICBBcmdzOgogICAgICBib2FyZCAoc3RyKTogR2FtZSBib2FyZCBhcyB0ZXh0LgogICAgICBhY3Rpb24gKHN0cik6IElucHV0IGFjdGlvbiBhcyBzdHJpbmcuCgogIFJldHVybnM6CiAgICAgIGJvb2w6IElmIHRoZSBpbnB1dCBhY3Rpb24gc3RyaW5nIGlzIHZhbGlkLgoKICBSYWlzZXM6CiAgICAgIEV4Y2VwdGlvbjogSWYgZmFpbCB0byBjaGVjayBpZiB0aGUgYWN0aW9uIHN0cmluZyBpcyB2YWxpZC4KICAiIiIKICByYWlzZSBOb3RJbXBsZW1lbnRlZEVycm9yKCk=)

def propose_action(board: str) -> str:

"""Propose a valid random action given the game board as text

Args:

board (str): Game board as text.

Returns:

str: A valid random action as string.

Raises:

Exception: If fail to propose a valid random action.

"""

raise NotImplementedError()

def is_legal_action(board: str, action: str) -> bool:

"""Check if an action string is valid given the game board as text

Args:

board (str): Game board as text.

action (str): Input action as string.

Returns:

bool: If the input action string is valid.

Raises:

Exception: If fail to check if the action string is valid.

"""

raise NotImplementedError()

### C.2 Harness-as-policy

We use the same function signatures as above, except the docstring of propose_action():

[⬇](data:text/plain;base64,UHJvcG9zZSBvbmUgb2YgdGhlIGJlc3QgbGVnYWwgYWN0aW9ucyBnaXZlbiB0aGUgZ2FtZSBib2FyZCBhcyB0ZXh0IHN1Y2ggdGhhdCB0aGUgZmluYWwgcmV3YXJkIGlzIG1heGltaXplZC4=)

Propose one of the best legal actions given the game board as text such that the final reward is maximized.

## Appendix D Sample Harness Code Snippets

### D.1 Minesweeper-v0

The propose_action() code snippet for Minesweeper-v0 breaks down the strategy by checking the first move, finding guaranteed safe cells by logic deduction, and applying probabilistic heuristic for best guesses. Not that not the whole code harness is shown here.

[⬇](data:text/plain;base64,ZGVmIHByb3Bvc2VfYWN0aW9uKGJvYXJkOiBzdHIpIC0+IHN0cjoKICAiIiJQcm9wb3NlIG9uZSBvZiB0aGUgYmVzdCBsZWdhbCBhY3Rpb25zIGdpdmVuIHRoZSBnYW1lIGJvYXJkIGFzIHRleHQgc3VjaCB0aGF0IHRoZSBmaW5hbCByZXdhcmQgaXMgbWF4aW1pemVkLgoKICBBcmdzOgogICAgICBib2FyZCAoc3RyKTogR2FtZSBib2FyZCBhcyB0ZXh0LgoKICBSZXR1cm5zOgogICAgICBzdHI6IEEgc3RyaW5nIHJlcHJlc2VudGluZyBvbmUgb2YgdGhlIGJlc3QgbGVnYWwgYWN0aW9ucy4KCiAgUmFpc2VzOgogICAgICBFeGNlcHRpb246IElmIGZhaWwgdG8gcHJvcG9zZSBhbnkgbGVnYWwgYWN0aW9uLgogICIiIgogIGdyaWQgPSBwYXJzZV9ib2FyZF90b19ncmlkKGJvYXJkKQogIGlmIG5vdCBncmlkOgogICAgcmFpc2UgRXhjZXB0aW9uKCJGYWlsZWQgdG8gcGFyc2UgdGhlIGJvYXJkIG9yIGJvYXJkIGlzIGVtcHR5LCBjYW5ub3QgcHJvcG9zZSBhbiBhY3Rpb24uIikKCiAgbnVtX3Jvd3MsIG51bV9jb2xzID0gZ2V0X2JvYXJkX2RpbWVuc2lvbnMoZ3JpZCkKICBpZiBudW1fcm93cyA9PSAwIG9yIG51bV9jb2xzID09IDA6CiAgICByYWlzZSBFeGNlcHRpb24oIkJvYXJkIGRpbWVuc2lvbnMgYXJlIHplcm8sIGNhbm5vdCBwcm9wb3NlIGFuIGFjdGlvbi4iKQoKICAjIENoZWNrIGlmIHRoaXMgaXMgdGhlIHZlcnkgZmlyc3QgbW92ZSAoYWxsIGNlbGxzIGFyZSB1bnJldmVhbGVkKQogIGFsbF9jZWxsc191bnJldmVhbGVkID0gVHJ1ZQogIGZvciByX2NoZWNrIGluIHJhbmdlKG51bV9yb3dzKToKICAgIGZvciBjX2NoZWNrIGluIHJhbmdlKG51bV9jb2xzKToKICAgICAgaWYgZ3JpZFtyX2NoZWNrXVtjX2NoZWNrXSAhPSAnLic6CiAgICAgICAgYWxsX2NlbGxzX3VucmV2ZWFsZWQgPSBGYWxzZQogICAgICAgIGJyZWFrCiAgICBpZiBub3QgYWxsX2NlbGxzX3VucmV2ZWFsZWQ6CiAgICAgIGJyZWFrCgogICMgU3RyYXRlZ3kgMTogRmlyc3QgbW92ZSAoaWYgYWxsIGNlbGxzIGFyZSB1bnJldmVhbGVkKQogICMgUGljayBhIGNlbnRyYWwgY2VsbCB0byBtYXhpbWl6ZSB0aGUgaW5pdGlhbCByZXZlYWxlZCBhcmVhIGZvciBhIHNhZmUgc3RhcnQuCiAgaWYgYWxsX2NlbGxzX3VucmV2ZWFsZWQ6CiAgICAjIEZvciBhbiA4eDggYm9hcmQsICgzLDMpIGlzIGEgY29tbW9uIHNhZmUgc3RhcnRpbmcgcG9pbnQuCiAgICBmaXJzdF9tb3ZlX3JvdyA9IG51bV9yb3dzIC8vIDIgLSAoMSBpZiBudW1fcm93cyAlIDIgPT0gMCBhbmQgbnVtX3Jvd3MgLy8gMiA+IDAgZWxzZSAwKQogICAgZmlyc3RfbW92ZV9jb2wgPSBudW1fY29scyAvLyAyIC0gKDEgaWYgbnVtX2NvbHMgJSAyID09IDAgYW5kIG51bV9jb2xzIC8vIDIgPiAwIGVsc2UgMCkKICAgIHJldHVybiBmIlt7Zmlyc3RfbW92ZV9yb3d9IHtmaXJzdF9tb3ZlX2NvbH1dIgoKICAjIFN0cmF0ZWd5IDI6IExvZ2ljIERlZHVjdGlvbiBmb3IgR3VhcmFudGVlZCBTYWZlIENlbGxzIGFuZCBNaW5lcwogICMgYm9hcmRfbWluZXMgc3RvcmVzOiBUcnVlIGZvciBrbm93biBtaW5lLCBGYWxzZSBmb3Iga25vd24gc2FmZSwgTm9uZSBmb3IgdW5rbm93bi4KICBib2FyZF9taW5lczogbGlzdFtsaXN0W2Jvb2wgfCBOb25lXV0gPSBbW05vbmUgZm9yIF8gaW4gcmFuZ2UobnVtX2NvbHMpXSBmb3IgXyBpbiByYW5nZShudW1fcm93cyldCgogICMgSW5pdGlhbGl6ZSBib2FyZF9taW5lcyBiYXNlZCBvbiBjdXJyZW50bHkgcmV2ZWFsZWQgY2VsbHMKICBmb3IgciBpbiByYW5nZShudW1fcm93cyk6CiAgICAgIGZvciBjIGluIHJhbmdlKG51bV9jb2xzKToKICAgICAgICAgIGlmIGdyaWRbcl1bY10uaXNkaWdpdCgpOgogICAgICAgICAgICAgICMgUmV2ZWFsZWQgY2VsbHMgYXJlIGRlZmluaXRlbHkgbm90IG1pbmVzLgogICAgICAgICAgICAgIGJvYXJkX21pbmVzW3JdW2NdID0gRmFsc2UKICAgICAgICAgICMgVW5yZXZlYWxlZCBjZWxscyAnLicgYXJlIGluaXRpYWxseSBOb25lICh1bmtub3duKQoKICBzYWZlX3RvX3JldmVhbDogbGlzdFt0dXBsZVtpbnQsIGludF1dID0gW10gIyBDZWxscyB0aGF0IGFyZSBkZWR1Y2VkIHRvIGJlIHNhZmUgdG8gY2xpY2sKICBzYWZlX2NlbGxzX3NldCA9IHNldCgpICMgVXNlIGEgc2V0IHRvIHRyYWNrIGFscmVhZHkgYWRkZWQgc2FmZSBjZWxscyB0byBhdm9pZCBkdXBsaWNhdGVzCgogICMgUHJvcGFnYXRlIGRlZHVjdGlvbnMgbXVsdGlwbGUgdGltZXMgdW50aWwgbm8gbmV3IGRlZHVjdGlvbnMgYXJlIG1hZGUKICBtYXhfZGVkdWN0aW9uX2l0ZXJhdGlvbnMgPSBudW1fcm93cyAqIG51bV9jb2xzICMgU2FmZXR5IGxpbWl0IHRvIGVuc3VyZSB0ZXJtaW5hdGlvbgogIGZvciBfIGluIHJhbmdlKG1heF9kZWR1Y3Rpb25faXRlcmF0aW9ucyk6CiAgICAgIG5ld19kZWR1Y3Rpb25zX21hZGVfdGhpc19pdGVyYXRpb24gPSBGYWxzZSAjIFRyYWNrIGRlZHVjdGlvbnMgcGVyIGl0ZXJhdGlvbgoKICAgICAgIyAtLS0gU2ltcGxlIERlZHVjdGlvbiBSdWxlcyAoUnVsZSBBICYgQikgLS0tCiAgICAgIGZvciByIGluIHJhbmdlKG51bV9yb3dzKToKICAgICAgICAgIGZvciBjIGluIHJhbmdlKG51bV9jb2xzKToKICAgICAgICAgICAgICBpZiBncmlkW3JdW2NdLmlzZGlnaXQoKToKICAgICAgICAgICAgICAgICAgTiA9IGludChncmlkW3JdW2NdKQoKICAgICAgICAgICAgICAgICAgdW5yZXZlYWxlZF91bmtub3duX25laWdoYm9ycyA9IFtdICMgTmVpZ2hib3JzIHRoYXQgYXJlICcuJyBhbmQgTk9UIHlldCBtYXJrZWQgYXMgbWluZS9zYWZlIChOb25lIGluIGJvYXJkX21pbmVzKQogICAgICAgICAgICAgICAgICBrbm93bl9taW5lX25laWdoYm9yc19jb3VudCA9IDAKCiAgICAgICAgICAgICAgICAgIGZvciBkciBpbiBbLTEsIDAsIDFdOgogICAgICAgICAgICAgICAgICAgICAgZm9yIGRjIGluIFstMSwgMCwgMV06CiAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgZHIgPT0gMCBhbmQgZGMgPT0gMDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgICAgICAgICAgICAgICBuciwgbmMgPSByICsgZHIsIGMgKyBkYwoKICAgICAgICAgICAgICAgICAgICAgICAgICBpZiAwIDw9IG5yIDwgbnVtX3Jvd3MgYW5kIDAgPD0gbmMgPCBudW1fY29sczoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgYm9hcmRfbWluZXNbbnJdW25jXSBpcyBUcnVlOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAga25vd25fbWluZV9uZWlnaGJvcnNfY291bnQgKz0gMQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBlbGlmIGdyaWRbbnJdW25jXSA9PSAnLicgYW5kIGJvYXJkX21pbmVzW25yXVtuY10gaXMgTm9uZToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHVucmV2ZWFsZWRfdW5rbm93bl9uZWlnaGJvcnMuYXBwZW5kKChuciwgbmMpKQoKICAgICAgICAgICAgICAgICAgbnVtX3VucmV2ZWFsZWRfYW5kX3Vua25vd24gPSBsZW4odW5yZXZlYWxlZF91bmtub3duX25laWdoYm9ycykKICAgICAgICAgICAgICAgICAgbWluZXNfdG9fZGVkdWNlID0gTiAtIGtub3duX21pbmVfbmVpZ2hib3JzX2NvdW50CgogICAgICAgICAgICAgICAgICAjIFJ1bGUgQTogRGVkdWNlIE1pbmVzCiAgICAgICAgICAgICAgICAgICMgSWYgKGNsdWUgTiAtIGtub3duX21pbmVfbmVpZ2hib3JzX2NvdW50KSBlcXVhbHMgdGhlIG51bWJlciBvZiB1bnJldmVhbGVkIGFuZCB1bmtub3duIG5laWdoYm9ycywKICAgICAgICAgICAgICAgICAgIyB0aGVuIGFsbCB0aGVzZSB1bnJldmVhbGVkIGFuZCB1bmtub3duIG5laWdoYm9ycyBtdXN0IGJlIG1pbmVzLgogICAgICAgICAgICAgICAgICBpZiBtaW5lc190b19kZWR1Y2UgPiAwIGFuZCBtaW5lc190b19kZWR1Y2UgPT0gbnVtX3VucmV2ZWFsZWRfYW5kX3Vua25vd246CiAgICAgICAgICAgICAgICAgICAgICBmb3IgKHVyLCB1YykgaW4gdW5yZXZlYWxlZF91bmtub3duX25laWdoYm9yczoKICAgICAgICAgICAgICAgICAgICAgICAgICBpZiBib2FyZF9taW5lc1t1cl1bdWNdIGlzIE5vbmU6ICMgT25seSBtYXJrIGlmIG5vdCBhbHJlYWR5IG1hcmtlZAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBib2FyZF9taW5lc1t1cl1bdWNdID0gVHJ1ZQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBuZXdfZGVkdWN0aW9uc19tYWRlX3RoaXNfaXRlcmF0aW9uID0gVHJ1ZQoKICAgICAgICAgICAgICAgICAgIyBSdWxlIEI6IERlZHVjZSBTYWZlIENlbGxzCiAgICAgICAgICAgICAgICAgICMgSWYgY2x1ZSBOIGVxdWFscyB0aGUgbnVtYmVyIG9mIGtub3duIG1pbmUgbmVpZ2hib3JzLAogICAgICAgICAgICAgICAgICAjIHRoZW4gYWxsIG90aGVyIHVucmV2ZWFsZWQgYW5kIHVua25vd24gbmVpZ2hib3JzIG11c3QgYmUgc2FmZS4KICAgICAgICAgICAgICAgICAgZWxpZiBtaW5lc190b19kZWR1Y2UgPT0gMCBhbmQgbnVtX3VucmV2ZWFsZWRfYW5kX3Vua25vd24gPiAwOgogICAgICAgICAgICAgICAgICAgICAgZm9yICh1ciwgdWMpIGluIHVucmV2ZWFsZWRfdW5rbm93bl9uZWlnaGJvcnM6CiAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgYm9hcmRfbWluZXNbdXJdW3VjXSBpcyBOb25lOiAjIE9ubHkgbWFyayBpZiBub3QgYWxyZWFkeSBtYXJrZWQKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYm9hcmRfbWluZXNbdXJdW3VjXSA9IEZhbHNlICMgTWFyayBhcyBzYWZlCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmICh1ciwgdWMpIG5vdCBpbiBzYWZlX2NlbGxzX3NldDogIyBBZGQgdG8gc2FmZSBsaXN0IG9ubHkgaWYgbmV3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBzYWZlX3RvX3JldmVhbC5hcHBlbmQoKHVyLCB1YykpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBzYWZlX2NlbGxzX3NldC5hZGQoKHVyLCB1YykpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5ld19kZWR1Y3Rpb25zX21hZGVfdGhpc19pdGVyYXRpb24gPSBUcnVlCgogICAgICAjIC0tLSBBZHZhbmNlZCBEZWR1Y3Rpb24gUnVsZXMgKFN1YnNldCBSdWxlKSAtLS0KICAgICAgIyBDb2xsZWN0IGFsbCBjbHVlIGNvbnN0cmFpbnRzIHRoYXQgaGF2ZSB1bmtub3duIG5laWdoYm9ycwogICAgICBjbHVlX2NvbnN0cmFpbnRzID0gW10gIyBMaXN0IG9mIChtaW5lc19uZWVkZWQsIHNldF9vZl91bmtub3duX25laWdoYm9ycykKICAgICAgZm9yIHJfY2x1ZSBpbiByYW5nZShudW1fcm93cyk6CiAgICAgICAgICBmb3IgY19jbHVlIGluIHJhbmdlKG51bV9jb2xzKToKICAgICAgICAgICAgICBpZiBncmlkW3JfY2x1ZV1bY19jbHVlXS5pc2RpZ2l0KCk6CiAgICAgICAgICAgICAgICAgIE5fY2x1ZSA9IGludChncmlkW3JfY2x1ZV1bY19jbHVlXSkKICAgICAgICAgICAgICAgICAgdW5rbm93bl9uZWlnaGJvcnNfc2V0ID0gc2V0KCkKICAgICAgICAgICAgICAgICAga25vd25fbWluZXNfYXJvdW5kX2NsdWUgPSAwCgogICAgICAgICAgICAgICAgICBmb3IgZHJfY2x1ZSBpbiBbLTEsIDAsIDFdOgogICAgICAgICAgICAgICAgICAgICAgZm9yIGRjX2NsdWUgaW4gWy0xLCAwLCAxXToKICAgICAgICAgICAgICAgICAgICAgICAgICBpZiBkcl9jbHVlID09IDAgYW5kIGRjX2NsdWUgPT0gMDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgICAgICAgICAgICAgICBucl9jbHVlLCBuY19jbHVlID0gcl9jbHVlICsgZHJfY2x1ZSwgY19jbHVlICsgZGNfY2x1ZQogICAgICAgICAgICAgICAgICAgICAgICAgIGlmIDAgPD0gbnJfY2x1ZSA8IG51bV9yb3dzIGFuZCAwIDw9IG5jX2NsdWUgPCBudW1fY29sczoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgYm9hcmRfbWluZXNbbnJfY2x1ZV1bbmNfY2x1ZV0gaXMgVHJ1ZToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGtub3duX21pbmVzX2Fyb3VuZF9jbHVlICs9IDEKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZWxpZiBncmlkW25yX2NsdWVdW25jX2NsdWVdID09ICcuJyBhbmQgYm9hcmRfbWluZXNbbnJfY2x1ZV1bbmNfY2x1ZV0gaXMgTm9uZToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHVua25vd25fbmVpZ2hib3JzX3NldC5hZGQoKG5yX2NsdWUsIG5jX2NsdWUpKQoKICAgICAgICAgICAgICAgICAgbWluZXNfbmVlZGVkID0gTl9jbHVlIC0ga25vd25fbWluZXNfYXJvdW5kX2NsdWUKICAgICAgICAgICAgICAgICAgIyBPbmx5IGFkZCB2YWxpZCBjb25zdHJhaW50cyB3aGVyZSBtaW5lc19uZWVkZWQgaXMgcG9zaXRpdmUgYW5kIHRoZXJlIGFyZSB1bmtub3duIGNlbGxzIHRvIGNvbnNpZGVyLgogICAgICAgICAgICAgICAgICAjIElmIG1pbmVzX25lZWRlZCA8PSAwLCBSdWxlIEIgKHNhZmUgY2VsbHMpIHdvdWxkIGhhdmUgYWxyZWFkeSBjb3ZlcmVkIGl0IG9yIGl0IG1lYW5zIHRvbyBtYW55IG1pbmVzIGFyZSBhbHJlYWR5IGlkZW50aWZpZWQuCiAgICAgICAgICAgICAgICAgIGlmIG1pbmVzX25lZWRlZCA+IDAgYW5kIHVua25vd25fbmVpZ2hib3JzX3NldDoKICAgICAgICAgICAgICAgICAgICAgIGNsdWVfY29uc3RyYWludHMuYXBwZW5kKChtaW5lc19uZWVkZWQsIHVua25vd25fbmVpZ2hib3JzX3NldCkpCgogICAgICAjIEFwcGx5IHN1YnNldCBydWxlIHRvIGFsbCBwYWlycyBvZiBjbHVlIGNvbnN0cmFpbnRzCiAgICAgIGZvciBpIGluIHJhbmdlKGxlbihjbHVlX2NvbnN0cmFpbnRzKSk6CiAgICAgICAgICBmb3IgaiBpbiByYW5nZShsZW4oY2x1ZV9jb25zdHJhaW50cykpOgogICAgICAgICAgICAgIGlmIGkgPT0gajogIyBEb24ndCBjb21wYXJlIGEgY29uc3RyYWludCB3aXRoIGl0c2VsZgogICAgICAgICAgICAgICAgICBjb250aW51ZQoKICAgICAgICAgICAgICBubTEsIHMxID0gY2x1ZV9jb25zdHJhaW50c1tpXSAjIG1pbmVzX25lZWRlZF8xLCBzZXRfb2ZfdW5rbm93bl9uZWlnaGJvcnNfMQogICAgICAgICAgICAgIG5tMiwgczIgPSBjbHVlX2NvbnN0cmFpbnRzW2pdICMgbWluZXNfbmVlZGVkXzIsIHNldF9vZl91bmtub3duX25laWdoYm9yc18yCgogICAgICAgICAgICAgIGlmIHMxLmlzc3Vic2V0KHMyKSBhbmQgczEgIT0gczI6ICMgSWYgczEgaXMgYSBwcm9wZXIgc3Vic2V0IG9mIHMyCiAgICAgICAgICAgICAgICAgIHNfZGlmZiA9IHMyIC0gczEgIyBDZWxscyBpbiBzMiBidXQgbm90IGluIHMxCiAgICAgICAgICAgICAgICAgIG5tX2RpZmYgPSBubTIgLSBubTEgIyBEaWZmZXJlbmNlIGluIG5lZWRlZCBtaW5lcwoKICAgICAgICAgICAgICAgICAgaWYgbm1fZGlmZiA9PSAwIGFuZCBzX2RpZmY6ICMgSWYgZGlmZmVyZW5jZSBpbiBtaW5lcyBpcyAwLCB0aGVuIHNfZGlmZiBjZWxscyBtdXN0IGJlIHNhZmUKICAgICAgICAgICAgICAgICAgICAgIGZvciAoc3IsIHNjKSBpbiBzX2RpZmY6CiAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgYm9hcmRfbWluZXNbc3JdW3NjXSBpcyBOb25lOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBib2FyZF9taW5lc1tzcl1bc2NdID0gRmFsc2UKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgKHNyLCBzYykgbm90IGluIHNhZmVfY2VsbHNfc2V0OgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc2FmZV90b19yZXZlYWwuYXBwZW5kKChzciwgc2MpKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc2FmZV9jZWxsc19zZXQuYWRkKChzciwgc2MpKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBuZXdfZGVkdWN0aW9uc19tYWRlX3RoaXNfaXRlcmF0aW9uID0gVHJ1ZQogICAgICAgICAgICAgICAgICBlbGlmIG5tX2RpZmYgPT0gbGVuKHNfZGlmZikgYW5kIHNfZGlmZjogIyBJZiBkaWZmZXJlbmNlIGluIG1pbmVzIGVxdWFscyBudW1iZXIgb2YgY2VsbHMgaW4gc19kaWZmLCB0aGV5IGFyZSBhbGwgbWluZXMKICAgICAgICAgICAgICAgICAgICAgIGZvciAoc3IsIHNjKSBpbiBzX2RpZmY6CiAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgYm9hcmRfbWluZXNbc3JdW3NjXSBpcyBOb25lOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBib2FyZF9taW5lc1tzcl1bc2NdID0gVHJ1ZQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBuZXdfZGVkdWN0aW9uc19tYWRlX3RoaXNfaXRlcmF0aW9uID0gVHJ1ZQoKICAgICAgaWYgbm90IG5ld19kZWR1Y3Rpb25zX21hZGVfdGhpc19pdGVyYXRpb246CiAgICAgICAgICBicmVhayAjIE5vIG5ldyBkZWR1Y3Rpb25zIHRoaXMgaXRlcmF0aW9uIChuZWl0aGVyIHNpbXBsZSBub3IgYWR2YW5jZWQpLCBzdG9wIHByb3BhZ2F0aW5nCgogICMgSWYgZ3VhcmFudGVlZCBzYWZlIGNlbGxzIGFyZSBmb3VuZCwgY2hvb3NlIG9uZSByYW5kb21seS4KICBpZiBzYWZlX3RvX3JldmVhbDoKICAgIGNob3Nlbl9tb3ZlID0gcmFuZG9tLmNob2ljZShzYWZlX3RvX3JldmVhbCkKICAgIHJldHVybiBmIlt7Y2hvc2VuX21vdmVbMF19IHtjaG9zZW5fbW92ZVsxXX1dIgoKICAjIFN0cmF0ZWd5IDM6IFByb2JhYmlsaXN0aWMgSGV1cmlzdGljIGZvciBCZXN0IEd1ZXNzICh3aGVuIG5vIGd1YXJhbnRlZWQgc2FmZSBjZWxscyBhcmUgZm91bmQpCiAgcG90ZW50aWFsX21vdmVzX3dpdGhfcmlza3MgPSBbXSAjIFN0b3JlcyAocmlza19zY29yZSwgcm93LCBjb2wpCgogIHRvdGFsX3VucmV2ZWFsZWRfdW5rbm93bl9kb3RzID0gMAogIGlkZW50aWZpZWRfbWluZXNfY291bnQgPSAwCiAgZm9yIHIgaW4gcmFuZ2UobnVtX3Jvd3MpOgogICAgICBmb3IgYyBpbiByYW5nZShudW1fY29scyk6CiAgICAgICAgICBpZiBib2FyZF9taW5lc1tyXVtjXSBpcyBUcnVlOgogICAgICAgICAgICAgIGlkZW50aWZpZWRfbWluZXNfY291bnQgKz0gMQogICAgICAgICAgZWxpZiBncmlkW3JdW2NdID09ICcuJyBhbmQgYm9hcmRfbWluZXNbcl1bY10gaXMgTm9uZToKICAgICAgICAgICAgICB0b3RhbF91bnJldmVhbGVkX3Vua25vd25fZG90cyArPSAxCgogICMgQXNzdW1pbmcgYSBzdGFuZGFyZCA4eDggTWluZXN3ZWVwZXIgYm9hcmQgaGFzIDEwIG1pbmVzLiBUaGlzIGlzIGEgY29tbW9uIHNldHVwLgogIHRvdGFsX21pbmVzX29uX2JvYXJkID0gMTAKCiAgZ2xvYmFsX21pbmVfcHJvYiA9IDAuMAogIGlmIHRvdGFsX3VucmV2ZWFsZWRfdW5rbm93bl9kb3RzID4gMDoKICAgICAgcmVtYWluaW5nX21pbmVzX3RvX3BsYWNlID0gbWF4KDAsIHRvdGFsX21pbmVzX29uX2JvYXJkIC0gaWRlbnRpZmllZF9taW5lc19jb3VudCkKICAgICAgZ2xvYmFsX21pbmVfcHJvYiA9IHJlbWFpbmluZ19taW5lc190b19wbGFjZSAvIHRvdGFsX3VucmV2ZWFsZWRfdW5rbm93bl9kb3RzCiAgICAgICMgQ2xhbXAgZ2xvYmFsIHByb2JhYmlsaXR5IGJldHdlZW4gMCBhbmQgMQogICAgICBnbG9iYWxfbWluZV9wcm9iID0gbWF4KDAuMCwgbWluKDEuMCwgZ2xvYmFsX21pbmVfcHJvYikpCgogICMgSXRlcmF0ZSBvdmVyIGFsbCB1bnJldmVhbGVkIGNlbGxzIHRoYXQgYXJlIG5vdCBrbm93biBtaW5lcyB0byBjYWxjdWxhdGUgcmlzayBzY29yZXMKICBmb3IgciBpbiByYW5nZShudW1fcm93cyk6CiAgICAgIGZvciBjIGluIHJhbmdlKG51bV9jb2xzKToKICAgICAgICAgICMgT25seSBjb25zaWRlciB0cnVseSB1bmtub3duIGNlbGxzICgnLicpIGZvciBndWVzc2luZyB0aGF0IGFyZSBub3QgbWFya2VkIGFzIG1pbmVzCiAgICAgICAgICBpZiBncmlkW3JdW2NdID09ICcuJyBhbmQgYm9hcmRfbWluZXNbcl1bY10gaXMgTm9uZToKICAgICAgICAgICAgICBjdXJyZW50X2NlbGxfcmlza19zdW0gPSAwLjAKICAgICAgICAgICAgICBudW1fYWRqYWNlbnRfY2x1ZXNfaW5mbHVlbmNpbmcgPSAwCgogICAgICAgICAgICAgICMgQW5hbHl6ZSBuZWlnaGJvcnMgb2YgdGhlIGNhbmRpZGF0ZSBjZWxsIChyLCBjKQogICAgICAgICAgICAgIGZvciBkcl9hZGogaW4gWy0xLCAwLCAxXToKICAgICAgICAgICAgICAgICAgZm9yIGRjX2FkaiBpbiBbLTEsIDAsIDFdOgogICAgICAgICAgICAgICAgICAgICAgaWYgZHJfYWRqID09IDAgYW5kIGRjX2FkaiA9PSAwOgogICAgICAgICAgICAgICAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgICAgICAgICAgICAgICBucl9hZGosIG5jX2FkaiA9IHIgKyBkcl9hZGosIGMgKyBkY19hZGoKCiAgICAgICAgICAgICAgICAgICAgICBpZiAwIDw9IG5yX2FkaiA8IG51bV9yb3dzIGFuZCAwIDw9IG5jX2FkaiA8IG51bV9jb2xzOgogICAgICAgICAgICAgICAgICAgICAgICAgIGlmIGdyaWRbbnJfYWRqXVtuY19hZGpdLmlzZGlnaXQoKTogIyBJZiBhZGphY2VudCB0byBhIHJldmVhbGVkIGNsdWUKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbnVtX2FkamFjZW50X2NsdWVzX2luZmx1ZW5jaW5nICs9IDEKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgTl9jbHVlID0gaW50KGdyaWRbbnJfYWRqXVtuY19hZGpdKQoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWluZXNfYXJvdW5kX2NsdWUgPSAwCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHVua25vd25fYXJvdW5kX2NsdWVfZm9yX2NsdWUgPSAwICMgVW5rbm93biBuZWlnaGJvcnMgc3BlY2lmaWNhbGx5IGZvciBUSElTIGNsdWUncyBjb250ZXh0CgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmb3IgZHJfc3ViIGluIFstMSwgMCwgMV06CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmb3IgZGNfc3ViIGluIFstMSwgMCwgMV06CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgZHJfc3ViID09IDAgYW5kIGRjX3N1YiA9PSAwOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHNuciwgc25jID0gbnJfYWRqICsgZHJfc3ViLCBuY19hZGogKyBkY19zdWIKCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgMCA8PSBzbnIgPCBudW1fcm93cyBhbmQgMCA8PSBzbmMgPCBudW1fY29sczoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgYm9hcmRfbWluZXNbc25yXVtzbmNdIGlzIFRydWU6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtaW5lc19hcm91bmRfY2x1ZSArPSAxCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGVsaWYgZ3JpZFtzbnJdW3NuY10gPT0gJy4nIGFuZCBib2FyZF9taW5lc1tzbnJdW3NuY10gaXMgTm9uZToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHVua25vd25fYXJvdW5kX2NsdWVfZm9yX2NsdWUgKz0gMQoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcmVtYWluaW5nX21pbmVzX2Zvcl9jbHVlID0gTl9jbHVlIC0gbWluZXNfYXJvdW5kX2NsdWUKCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmIHVua25vd25fYXJvdW5kX2NsdWVfZm9yX2NsdWUgPiAwOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIyBQcm9iYWJpbGl0eSBvZiBhbiB1bmtub3duIGNlbGwgYmVpbmcgYSBtaW5lIGdpdmVuIHRoaXMgY2x1ZQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJvYl9mcm9tX2NsdWUgPSBtYXgoMC4wLCBtaW4oMS4wLCByZW1haW5pbmdfbWluZXNfZm9yX2NsdWUgLyB1bmtub3duX2Fyb3VuZF9jbHVlX2Zvcl9jbHVlKSkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGN1cnJlbnRfY2VsbF9yaXNrX3N1bSArPSBwcm9iX2Zyb21fY2x1ZQoKICAgICAgICAgICAgICBpZiBudW1fYWRqYWNlbnRfY2x1ZXNfaW5mbHVlbmNpbmcgPiAwOgogICAgICAgICAgICAgICAgICAjIEF2ZXJhZ2UgdGhlIHByb2JhYmlsaXRpZXMgZnJvbSBhbGwgaW5mbHVlbmNpbmcgY2x1ZXMKICAgICAgICAgICAgICAgICAgY3VycmVudF9yaXNrX3Njb3JlID0gY3VycmVudF9jZWxsX3Jpc2tfc3VtIC8gbnVtX2FkamFjZW50X2NsdWVzX2luZmx1ZW5jaW5nCiAgICAgICAgICAgICAgZWxzZTogIyBJZiB0aGUgY2FuZGlkYXRlIGNlbGwgaXMgaXNvbGF0ZWQgZnJvbSBhbnkgcmV2ZWFsZWQgbnVtYmVycywgdXNlIGdsb2JhbCBwcm9iYWJpbGl0eQogICAgICAgICAgICAgICAgICBjdXJyZW50X3Jpc2tfc2NvcmUgPSBnbG9iYWxfbWluZV9wcm9iCgogICAgICAgICAgICAgIHBvdGVudGlhbF9tb3Zlc193aXRoX3Jpc2tzLmFwcGVuZCgoY3VycmVudF9yaXNrX3Njb3JlLCByLCBjKSkKCiAgIyBTZWxlY3QgdGhlIG1vdmUocykgd2l0aCB0aGUgbWluaW11bSByaXNrIHNjb3JlCiAgaWYgcG90ZW50aWFsX21vdmVzX3dpdGhfcmlza3M6CiAgICAgICMgRmluZCB0aGUgbWluaW11bSByaXNrIHNjb3JlIGFtb25nIGFsbCBwb3RlbnRpYWwgbW92ZXMKICAgICAgbWluX3Jpc2tfc2NvcmUgPSBmbG9hdCgnaW5mJykKICAgICAgZm9yIHJpc2ssIF8sIF8gaW4gcG90ZW50aWFsX21vdmVzX3dpdGhfcmlza3M6CiAgICAgICAgICBtaW5fcmlza19zY29yZSA9IG1pbihtaW5fcmlza19zY29yZSwgcmlzaykKCiAgICAgICMgQ29sbGVjdCBhbGwgbW92ZXMgdGhhdCBoYXZlIHRoaXMgbWluaW11bSByaXNrIHNjb3JlCiAgICAgIGJlc3RfbW92ZXMgPSBbKHIsIGMpIGZvciByaXNrLCByLCBjIGluIHBvdGVudGlhbF9tb3Zlc193aXRoX3Jpc2tzIGlmIHJpc2sgPT0gbWluX3Jpc2tfc2NvcmVdCgogICAgICBpZiBiZXN0X21vdmVzOgogICAgICAgICAgIyBSYW5kb21seSBjaG9vc2Ugb25lIG9mIHRoZSBiZXN0IChsb3dlc3QgcmlzaykgbW92ZXMKICAgICAgICAgIGNob3Nlbl9tb3ZlID0gcmFuZG9tLmNob2ljZShiZXN0X21vdmVzKQogICAgICAgICAgcmV0dXJuIGYiW3tjaG9zZW5fbW92ZVswXX0ge2Nob3Nlbl9tb3ZlWzFdfV0iCgogICMgRmluYWwgRmFsbGJhY2s6IElmIG5vIG1vdmVzIHBhc3NlZCB0aGUgZmlsdGVycyAoZS5nLiwgYWxsIHJlbWFpbmluZyBjZWxscyBhcmUgY29uc2lkZXJlZCBtaW5lcywKICAjIG9yIG5vIGxvZ2ljYWxseSBzYWZlL2d1ZXNzYWJsZSBtb3ZlcyB3ZXJlIGZvdW5kIGZyb20gdGhlIGN1cnJlbnQgc3RhdGUpLAogICMgYnV0IHRoZXJlIGFyZSBzdGlsbCB1bnJldmVhbGVkIGNlbGxzLCBwaWNrIG9uZSByYW5kb21seSBmcm9tIHRydWx5IHVua25vd24gY2VsbHMuCiAgdW5yZXZlYWxlZF9jZWxsc19yZW1haW5pbmcgPSBbXQogIGZvciByIGluIHJhbmdlKG51bV9yb3dzKToKICAgICAgZm9yIGMgaW4gcmFuZ2UobnVtX2NvbHMpOgogICAgICAgICAgaWYgZ3JpZFtyXVtjXSA9PSAnLic6CiAgICAgICAgICAgICAgIyBPbmx5IHBpY2sgdHJ1bHkgdW5yZXZlYWxlZCBjZWxscyB0aGF0IGFyZSBub3QgeWV0IG1hcmtlZCBhcyBtaW5lcyAoaXMgTm9uZSkKICAgICAgICAgICAgICBpZiBib2FyZF9taW5lc1tyXVtjXSBpcyBOb25lOgogICAgICAgICAgICAgICAgICB1bnJldmVhbGVkX2NlbGxzX3JlbWFpbmluZy5hcHBlbmQoKHIsYykpCgogIGlmIHVucmV2ZWFsZWRfY2VsbHNfcmVtYWluaW5nOgogICAgICBjaG9zZW5fbW92ZSA9IHJhbmRvbS5jaG9pY2UodW5yZXZlYWxlZF9jZWxsc19yZW1haW5pbmcpCiAgICAgIHJldHVybiBmIlt7Y2hvc2VuX21vdmVbMF19IHtjaG9zZW5fbW92ZVsxXX1dIgoKICByYWlzZSBFeGNlcHRpb24oIk5vIGxlZ2FsIGFjdGlvbnMgY2FuIGJlIHByb3Bvc2VkLiBBbGwgbm9uLW1pbmUgY2VsbHMgbWlnaHQgYmUgcmV2ZWFsZWQgb3Igbm8gc2FmZS9ndWVzc2FibGUgbW92ZXMgZm91bmQuIik=)

def propose_action(board: str) -> str:

"""Propose one of the best legal actions given the game board as text such that the final reward is maximized.

Args:

board (str): Game board as text.

Returns:

str: A string representing one of the best legal actions.

Raises:

Exception: If fail to propose any legal action.

"""

grid = parse_board_to_grid(board)

if not grid:

raise Exception("Failed to parse the board or board is empty, cannot propose an action.")

num_rows, num_cols = get_board_dimensions(grid)

if num_rows == 0 or num_cols == 0:

raise Exception("Board dimensions are zero, cannot propose an action.")

# Check if this is the very first move (all cells are unrevealed)

all_cells_unrevealed = True

for r_check in range(num_rows):

for c_check in range(num_cols):

if grid[r_check][c_check] != ’.’:

all_cells_unrevealed = False

break

if not all_cells_unrevealed:

break

# Strategy 1: First move (if all cells are unrevealed)

# Pick a central cell to maximize the initial revealed area for a safe start.

if all_cells_unrevealed:

# For an 8x8 board, (3,3) is a common safe starting point.

first_move_row = num_rows // 2 - (1 if num_rows % 2 == 0 and num_rows // 2 > 0 else 0)

first_move_col = num_cols // 2 - (1 if num_cols % 2 == 0 and num_cols // 2 > 0 else 0)

return f"[{first_move_row} {first_move_col}]"

# Strategy 2: Logic Deduction for Guaranteed Safe Cells and Mines

# board_mines stores: True for known mine, False for known safe, None for unknown.

board_mines: list[list[bool | None]] = [[None for _ in range(num_cols)] for _ in range(num_rows)]

# Initialize board_mines based on currently revealed cells

for r in range(num_rows):

for c in range(num_cols):

if grid[r][c].isdigit():

# Revealed cells are definitely not mines.

board_mines[r][c] = False

# Unrevealed cells ’.’ are initially None (unknown)

safe_to_reveal: list[tuple[int, int]] = [] # Cells that are deduced to be safe to click

safe_cells_set = set() # Use a set to track already added safe cells to avoid duplicates

# Propagate deductions multiple times until no new deductions are made

max_deduction_iterations = num_rows * num_cols # Safety limit to ensure termination

for _ in range(max_deduction_iterations):

new_deductions_made_this_iteration = False # Track deductions per iteration

# --- Simple Deduction Rules (Rule A & B) ---

for r in range(num_rows):

for c in range(num_cols):

if grid[r][c].isdigit():

N = int(grid[r][c])

unrevealed_unknown_neighbors = [] # Neighbors that are ’.’ and NOT yet marked as mine/safe (None in board_mines)

known_mine_neighbors_count = 0

for dr in [-1, 0, 1]:

for dc in [-1, 0, 1]:

if dr == 0 and dc == 0:

continue

nr, nc = r + dr, c + dc

if 0 <= nr < num_rows and 0 <= nc < num_cols:

if board_mines[nr][nc] is True:

known_mine_neighbors_count += 1

elif grid[nr][nc] == ’.’ and board_mines[nr][nc] is None:

unrevealed_unknown_neighbors.append((nr, nc))

num_unrevealed_and_unknown = len(unrevealed_unknown_neighbors)

mines_to_deduce = N - known_mine_neighbors_count

# Rule A: Deduce Mines

# If (clue N - known_mine_neighbors_count) equals the number of unrevealed and unknown neighbors,

# then all these unrevealed and unknown neighbors must be mines.

if mines_to_deduce > 0 and mines_to_deduce == num_unrevealed_and_unknown:

for (ur, uc) in unrevealed_unknown_neighbors:

if board_mines[ur][uc] is None: # Only mark if not already marked

board_mines[ur][uc] = True

new_deductions_made_this_iteration = True

# Rule B: Deduce Safe Cells

# If clue N equals the number of known mine neighbors,

# then all other unrevealed and unknown neighbors must be safe.

elif mines_to_deduce == 0 and num_unrevealed_and_unknown > 0:

for (ur, uc) in unrevealed_unknown_neighbors:

if board_mines[ur][uc] is None: # Only mark if not already marked

board_mines[ur][uc] = False # Mark as safe

if (ur, uc) not in safe_cells_set: # Add to safe list only if new

safe_to_reveal.append((ur, uc))

safe_cells_set.add((ur, uc))

new_deductions_made_this_iteration = True

# --- Advanced Deduction Rules (Subset Rule) ---

# Collect all clue constraints that have unknown neighbors

clue_constraints = [] # List of (mines_needed, set_of_unknown_neighbors)

for r_clue in range(num_rows):

for c_clue in range(num_cols):

if grid[r_clue][c_clue].isdigit():

N_clue = int(grid[r_clue][c_clue])

unknown_neighbors_set = set()

known_mines_around_clue = 0

for dr_clue in [-1, 0, 1]:

for dc_clue in [-1, 0, 1]:

if dr_clue == 0 and dc_clue == 0:

continue

nr_clue, nc_clue = r_clue + dr_clue, c_clue + dc_clue

if 0 <= nr_clue < num_rows and 0 <= nc_clue < num_cols:

if board_mines[nr_clue][nc_clue] is True:

known_mines_around_clue += 1

elif grid[nr_clue][nc_clue] == ’.’ and board_mines[nr_clue][nc_clue] is None:

unknown_neighbors_set.add((nr_clue, nc_clue))

mines_needed = N_clue - known_mines_around_clue

# Only add valid constraints where mines_needed is positive and there are unknown cells to consider.

# If mines_needed <= 0, Rule B (safe cells) would have already covered it or it means too many mines are already identified.

if mines_needed > 0 and unknown_neighbors_set:

clue_constraints.append((mines_needed, unknown_neighbors_set))

# Apply subset rule to all pairs of clue constraints

for i in range(len(clue_constraints)):

for j in range(len(clue_constraints)):

if i == j: # Don’t compare a constraint with itself

continue

nm1, s1 = clue_constraints[i] # mines_needed_1, set_of_unknown_neighbors_1

nm2, s2 = clue_constraints[j] # mines_needed_2, set_of_unknown_neighbors_2

if s1.issubset(s2) and s1 != s2: # If s1 is a proper subset of s2

s_diff = s2 - s1 # Cells in s2 but not in s1

nm_diff = nm2 - nm1 # Difference in needed mines

if nm_diff == 0 and s_diff: # If difference in mines is 0, then s_diff cells must be safe

for (sr, sc) in s_diff:

if board_mines[sr][sc] is None:

board_mines[sr][sc] = False

if (sr, sc) not in safe_cells_set:

safe_to_reveal.append((sr, sc))

safe_cells_set.add((sr, sc))

new_deductions_made_this_iteration = True

elif nm_diff == len(s_diff) and s_diff: # If difference in mines equals number of cells in s_diff, they are all mines

for (sr, sc) in s_diff:

if board_mines[sr][sc] is None:

board_mines[sr][sc] = True

new_deductions_made_this_iteration = True

if not new_deductions_made_this_iteration:

break # No new deductions this iteration (neither simple nor advanced), stop propagating

# If guaranteed safe cells are found, choose one randomly.

if safe_to_reveal:

chosen_move = random.choice(safe_to_reveal)

return f"[{chosen_move[0]} {chosen_move[1]}]"

# Strategy 3: Probabilistic Heuristic for Best Guess (when no guaranteed safe cells are found)

potential_moves_with_risks = [] # Stores (risk_score, row, col)

total_unrevealed_unknown_dots = 0

identified_mines_count = 0

for r in range(num_rows):

for c in range(num_cols):

if board_mines[r][c] is True:

identified_mines_count += 1

elif grid[r][c] == ’.’ and board_mines[r][c] is None:

total_unrevealed_unknown_dots += 1

# Assuming a standard 8x8 Minesweeper board has 10 mines. This is a common setup.

total_mines_on_board = 10

global_mine_prob = 0.0

if total_unrevealed_unknown_dots > 0:

remaining_mines_to_place = max(0, total_mines_on_board - identified_mines_count)

global_mine_prob = remaining_mines_to_place / total_unrevealed_unknown_dots

# Clamp global probability between 0 and 1

global_mine_prob = max(0.0, min(1.0, global_mine_prob))

# Iterate over all unrevealed cells that are not known mines to calculate risk scores

for r in range(num_rows):

for c in range(num_cols):

# Only consider truly unknown cells (’.’) for guessing that are not marked as mines

if grid[r][c] == ’.’ and board_mines[r][c] is None:

current_cell_risk_sum = 0.0

num_adjacent_clues_influencing = 0

# Analyze neighbors of the candidate cell (r, c)

for dr_adj in [-1, 0, 1]:

for dc_adj in [-1, 0, 1]:

if dr_adj == 0 and dc_adj == 0:

continue

nr_adj, nc_adj = r + dr_adj, c + dc_adj

if 0 <= nr_adj < num_rows and 0 <= nc_adj < num_cols:

if grid[nr_adj][nc_adj].isdigit(): # If adjacent to a revealed clue

num_adjacent_clues_influencing += 1

N_clue = int(grid[nr_adj][nc_adj])

mines_around_clue = 0

unknown_around_clue_for_clue = 0 # Unknown neighbors specifically for THIS clue’s context

for dr_sub in [-1, 0, 1]:

for dc_sub in [-1, 0, 1]:

if dr_sub == 0 and dc_sub == 0:

continue

snr, snc = nr_adj + dr_sub, nc_adj + dc_sub

if 0 <= snr < num_rows and 0 <= snc < num_cols:

if board_mines[snr][snc] is True:

mines_around_clue += 1

elif grid[snr][snc] == ’.’ and board_mines[snr][snc] is None:

unknown_around_clue_for_clue += 1

remaining_mines_for_clue = N_clue - mines_around_clue

if unknown_around_clue_for_clue > 0:

# Probability of an unknown cell being a mine given this clue

prob_from_clue = max(0.0, min(1.0, remaining_mines_for_clue / unknown_around_clue_for_clue))

current_cell_risk_sum += prob_from_clue

if num_adjacent_clues_influencing > 0:

# Average the probabilities from all influencing clues

current_risk_score = current_cell_risk_sum / num_adjacent_clues_influencing

else: # If the candidate cell is isolated from any revealed numbers, use global probability

current_risk_score = global_mine_prob

potential_moves_with_risks.append((current_risk_score, r, c))

# Select the move(s) with the minimum risk score

if potential_moves_with_risks:

# Find the minimum risk score among all potential moves

min_risk_score = float(’inf’)

for risk, _, _ in potential_moves_with_risks:

min_risk_score = min(min_risk_score, risk)

# Collect all moves that have this minimum risk score

best_moves = [(r, c) for risk, r, c in potential_moves_with_risks if risk == min_risk_score]

if best_moves:

# Randomly choose one of the best (lowest risk) moves

chosen_move = random.choice(best_moves)

return f"[{chosen_move[0]} {chosen_move[1]}]"

# Final Fallback: If no moves passed the filters (e.g., all remaining cells are considered mines,

# or no logically safe/guessable moves were found from the current state),

# but there are still unrevealed cells, pick one randomly from truly unknown cells.

unrevealed_cells_remaining = []

for r in range(num_rows):

for c in range(num_cols):

if grid[r][c] == ’.’:

# Only pick truly unrevealed cells that are not yet marked as mines (is None)

if board_mines[r][c] is None:

unrevealed_cells_remaining.append((r,c))

if unrevealed_cells_remaining:

chosen_move = random.choice(unrevealed_cells_remaining)

return f"[{chosen_move[0]} {chosen_move[1]}]"

raise Exception("No legal actions can be proposed. All non-mine cells might be revealed or no safe/guessable moves found.")

### D.2 Chess-v0

Interesting code snippets for Chess-v0 including Universal Chess Interface (UCI) parsing and formatting, piece localizing and attack checking. Note that not the whole code harness is shown here.

[⬇](data:text/plain;base64,ZGVmIF90b191Y2lfY29vcmQocm93OiBpbnQsIGNvbDogaW50KSAtPiBzdHI6CiAgICAiIiJDb252ZXJ0cyAwLWluZGV4ZWQgZ3JpZCBjb29yZGluYXRlcyAocm93LCBjb2wpIHRvIFVDSSBzdHJpbmcgKGUuZy4sICdlMicpLiIiIgogICAgZmlsZV9jaGFyID0gY2hyKG9yZCgnYScpICsgY29sKQogICAgcmFua19jaGFyID0gc3RyKDggLSByb3cpICMgR3JpZCByb3cgMCBpcyByYW5rIDgsIGdyaWQgcm93IDcgaXMgcmFuayAxCiAgICByZXR1cm4gZmlsZV9jaGFyICsgcmFua19jaGFyCgpkZWYgX2Zyb21fdWNpX2Nvb3JkKGNvb3JkX3N0cjogc3RyKSAtPiB0dXBsZVtpbnQsIGludF0gfCBOb25lOgogICAgIiIiQ29udmVydHMgVUNJIHN0cmluZyAoZS5nLiwgJ2UyJykgdG8gMC1pbmRleGVkIGdyaWQgY29vcmRpbmF0ZXMgKHJvdywgY29sKS4gUmV0dXJucyBOb25lIG9uIGludmFsaWQgaW5wdXQuIiIiCiAgICBpZiBub3QgKGxlbihjb29yZF9zdHIpID09IDIgYW5kICdhJyA8PSBjb29yZF9zdHJbMF0gPD0gJ2gnIGFuZCAnMScgPD0gY29vcmRfc3RyWzFdIDw9ICc4Jyk6CiAgICAgICAgcmV0dXJuIE5vbmUKICAgIGNvbCA9IG9yZChjb29yZF9zdHJbMF0pIC0gb3JkKCdhJykKICAgIHJvdyA9IDggLSBpbnQoY29vcmRfc3RyWzFdKSAjIFJhbmsgOCBpcyBncmlkIHJvdyAwLCByYW5rIDEgaXMgZ3JpZCByb3cgNwogICAgcmV0dXJuIHJvdywgY29sCgpkZWYgX2ZpbmRfa2luZyhncmlkOiBsaXN0W2xpc3Rbc3RyXV0sIGtpbmdfY29sb3I6IHN0cikgLT4gdHVwbGVbaW50LCBpbnRdIHwgTm9uZToKICAgICIiIkZpbmRzIHRoZSBjb29yZGluYXRlcyBvZiB0aGUga2luZyBvZiB0aGUgc3BlY2lmaWVkIGNvbG9yLiIiIgogICAgZm9yIHIgaW4gcmFuZ2UoOCk6CiAgICAgICAgZm9yIGMgaW4gcmFuZ2UoOCk6CiAgICAgICAgICAgIHBpZWNlID0gZ3JpZFtyXVtjXQogICAgICAgICAgICBpZiAoa2luZ19jb2xvciA9PSAndycgYW5kIHBpZWNlID09ICdLJykgb3IgXAogICAgICAgICAgICAgICAoa2luZ19jb2xvciA9PSAnYicgYW5kIHBpZWNlID09ICdrJyk6CiAgICAgICAgICAgICAgICByZXR1cm4gciwgYwogICAgcmV0dXJuIE5vbmUgIyBLaW5nIG5vdCBmb3VuZCAoc2hvdWxkIGlkZWFsbHkgbm90IGhhcHBlbiBpbiBhIHZhbGlkIGdhbWUgc3RhdGUpCgpkZWYgX2lzX3NxdWFyZV9hdHRhY2tlZChncmlkOiBsaXN0W2xpc3Rbc3RyXV0sIHI6IGludCwgYzogaW50LCBieV93aGl0ZTogYm9vbCkgLT4gYm9vbDoKICAgICIiIkNoZWNrcyBpZiBzcXVhcmUgKHIsIGMpIGlzIGF0dGFja2VkIGJ5IGFueSBwaWVjZSBvZiB0aGUgY29sb3IgJ2J5X3doaXRlJyAoVHJ1ZSBmb3IgV2hpdGUsIEZhbHNlIGZvciBCbGFjaykuIiIiCgogICAgIyBIZWxwZXIgdG8gY2hlY2sgaWYgYSBwaWVjZSBhdCAocHIsIHBjKSBpcyBvZiB0aGUgYXR0YWNraW5nX2NvbG9yCiAgICBkZWYgaXNfYXR0YWNrZXIocGllY2Vfc3ltOiBzdHIsIGlzX3doaXRlX2F0dGFja2VyOiBib29sKSAtPiBib29sOgogICAgICAgIGlmIHBpZWNlX3N5bSA9PSAnLic6IHJldHVybiBGYWxzZQogICAgICAgIHJldHVybiAoaXNfd2hpdGVfYXR0YWNrZXIgYW5kIHBpZWNlX3N5bS5pc3VwcGVyKCkpIG9yIFwKICAgICAgICAgICAgICAgKG5vdCBpc193aGl0ZV9hdHRhY2tlciBhbmQgcGllY2Vfc3ltLmlzbG93ZXIoKSkKCiAgICAjIDEuIFBhd24gYXR0YWNrcyAoZGlhZ29uYWwgMSBzdGVwKQogICAgIyBJZiBjaGVja2luZyBhdHRhY2sgKmJ5KiBXaGl0ZSwgV2hpdGUgcGF3bnMgYXR0YWNrICJ1cCIgKGRlY3JlYXNpbmcgcm93IGluZGV4KS4gU28gYSB3aGl0ZSBwYXduIGF0dGFja2luZyAocixjKSB3b3VsZCBiZSBhdCAocisxLCBjLTEpIG9yIChyKzEsIGMrMSkuCiAgICAjIElmIGNoZWNraW5nIGF0dGFjayAqYnkqIEJsYWNrLCBCbGFjayBwYXducyBhdHRhY2sgImRvd24iIChpbmNyZWFzaW5nIHJvdyBpbmRleCkuIFNvIGEgYmxhY2sgcGF3biBhdHRhY2tpbmcgKHIsYykgd291bGQgYmUgYXQgKHItMSwgYy0xKSBvciAoci0xLCBjKzEpLgogICAgcGF3bl9hdHRhY2tlcl9kcl9mcm9tX3RhcmdldCA9IDEgaWYgYnlfd2hpdGUgZWxzZSAtMQogICAgZm9yIGRjX3Bhd24gaW4gWy0xLCAxXToKICAgICAgICBwciwgcGMgPSByICsgcGF3bl9hdHRhY2tlcl9kcl9mcm9tX3RhcmdldCwgYyArIGRjX3Bhd24KICAgICAgICBpZiAwIDw9IHByIDwgOCBhbmQgMCA8PSBwYyA8IDggYW5kIGdyaWRbcHJdW3BjXS51cHBlcigpID09ICdQJzoKICAgICAgICAgICAgaWYgaXNfYXR0YWNrZXIoZ3JpZFtwcl1bcGNdLCBieV93aGl0ZSk6CiAgICAgICAgICAgICAgICByZXR1cm4gVHJ1ZQoKICAgICMgMi4gS25pZ2h0IGF0dGFja3MgKEwtc2hhcGUpCiAgICBrbmlnaHRfbW92ZXNfZGVsdGFzID0gWygtMiwgLTEpLCAoLTIsIDEpLCAoLTEsIC0yKSwgKC0xLCAyKSwgKDEsIC0yKSwgKDEsIDIpLCAoMiwgLTEpLCAoMiwgMSldCiAgICBmb3IgZHJfaywgZGNfayBpbiBrbmlnaHRfbW92ZXNfZGVsdGFzOgogICAgICAgIGtyLCBrYyA9IHIgKyBkcl9rLCBjICsgZGNfawogICAgICAgIGlmIDAgPD0ga3IgPCA4IGFuZCAwIDw9IGtjIDwgOCBhbmQgZ3JpZFtrcl1ba2NdLnVwcGVyKCkgPT0gJ04nOgogICAgICAgICAgICBpZiBpc19hdHRhY2tlcihncmlkW2tyXVtrY10sIGJ5X3doaXRlKToKICAgICAgICAgICAgICAgIHJldHVybiBUcnVlCgogICAgIyAzLiBLaW5nIGF0dGFja3MgKDEgc3RlcCBpbiBhbnkgZGlyZWN0aW9uKQogICAgIyBBIGtpbmcgY2Fubm90IG1vdmUgaW50byBhIHNxdWFyZSBhdHRhY2tlZCBieSBhbm90aGVyIGtpbmcsIGJ1dCBmb3Igc2ltcGxpY2l0eSBvZiBjaGVjayBkZXRlY3Rpb24sIHdlIGNvbnNpZGVyIGEga2luZydzIGRpcmVjdCB2aWNpbml0eSBhcyBhdHRhY2tlZCBieSBhbiBvcHBvc2luZyBraW5nLgogICAgZm9yIGRyX2ssIGRjX2sgaW4gWygtMSwgLTEpLCAoLTEsIDApLCAoLTEsIDEpLCAoMCwgLTEpLCAoMCwgMSksICgxLCAtMSksICgxLCAwKSwgKDEsIDEpXToKICAgICAgICBrciwga2MgPSByICsgZHJfaywgYyArIGRjX2sKICAgICAgICBpZiAwIDw9IGtyIDwgOCBhbmQgMCA8PSBrYyA8IDggYW5kIGdyaWRba3JdW2tjXS51cHBlcigpID09ICdLJzoKICAgICAgICAgICAgaWYgaXNfYXR0YWNrZXIoZ3JpZFtrcl1ba2NdLCBieV93aGl0ZSk6CiAgICAgICAgICAgICAgICByZXR1cm4gVHJ1ZQoKICAgICMgNC4gUm9vay9RdWVlbiBhdHRhY2tzIChzdHJhaWdodCBsaW5lcykKICAgIHN0cmFpZ2h0X2RpcmVjdGlvbnMgPSBbKC0xLCAwKSwgKDEsIDApLCAoMCwgLTEpLCAoMCwgMSldICMgVXAsIERvd24sIExlZnQsIFJpZ2h0CiAgICBmb3IgZHJfcywgZGNfcyBpbiBzdHJhaWdodF9kaXJlY3Rpb25zOgogICAgICAgIGZvciBzdGVwIGluIHJhbmdlKDEsIDgpOgogICAgICAgICAgICBzciwgc2MgPSByICsgZHJfcyAqIHN0ZXAsIGMgKyBkY19zICogc3RlcAogICAgICAgICAgICBpZiBub3QgKDAgPD0gc3IgPCA4IGFuZCAwIDw9IHNjIDwgOCk6IGJyZWFrICMgT3V0IG9mIGJvdW5kcwoKICAgICAgICAgICAgcGllY2VfYXRfc3Jfc2MgPSBncmlkW3NyXVtzY10KICAgICAgICAgICAgaWYgcGllY2VfYXRfc3Jfc2MgPT0gJy4nOiBjb250aW51ZSAjIFBhdGggY2xlYXIKCiAgICAgICAgICAgIGlmIGlzX2F0dGFja2VyKHBpZWNlX2F0X3NyX3NjLCBieV93aGl0ZSkgYW5kIFwKICAgICAgICAgICAgICAgKHBpZWNlX2F0X3NyX3NjLnVwcGVyKCkgPT0gJ1InIG9yIHBpZWNlX2F0X3NyX3NjLnVwcGVyKCkgPT0gJ1EnKToKICAgICAgICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBicmVhayAjIEJsb2NraW5nIHBpZWNlIGlzIG5vdCBhbiBhdHRhY2tlciBvciBpcyBvd24gcGllY2UsIG9yIGFub3RoZXIgcGllY2UKCiAgICAjIDUuIEJpc2hvcC9RdWVlbiBhdHRhY2tzIChkaWFnb25hbCBsaW5lcykKICAgIGRpYWdvbmFsX2RpcmVjdGlvbnMgPSBbKC0xLCAtMSksICgtMSwgMSksICgxLCAtMSksICgxLCAxKV0gIyBVcC1MZWZ0LCBVcC1SaWdodCwgRG93bi1MZWZ0LCBEb3duLVJpZ2h0CiAgICBmb3IgZHJfZCwgZGNfZCBpbiBkaWFnb25hbF9kaXJlY3Rpb25zOgogICAgICAgIGZvciBzdGVwIGluIHJhbmdlKDEsIDgpOgogICAgICAgICAgICBzciwgc2MgPSByICsgZHJfZCAqIHN0ZXAsIGMgKyBkY19kICogc3RlcAogICAgICAgICAgICBpZiBub3QgKDAgPD0gc3IgPCA4IGFuZCAwIDw9IHNjIDwgOCk6IGJyZWFrICMgT3V0IG9mIGJvdW5kcwoKICAgICAgICAgICAgcGllY2VfYXRfc3Jfc2MgPSBncmlkW3NyXVtzY10KICAgICAgICAgICAgaWYgcGllY2VfYXRfc3Jfc2MgPT0gJy4nOiBjb250aW51ZSAjIFBhdGggY2xlYXIKCiAgICAgICAgICAgIGlmIGlzX2F0dGFja2VyKHBpZWNlX2F0X3NyX3NjLCBieV93aGl0ZSkgYW5kIFwKICAgICAgICAgICAgICAgKHBpZWNlX2F0X3NyX3NjLnVwcGVyKCkgPT0gJ0InIG9yIHBpZWNlX2F0X3NyX3NjLnVwcGVyKCkgPT0gJ1EnKToKICAgICAgICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBicmVhayAjIEJsb2NraW5nIHBpZWNlIGlzIG5vdCBhbiBhdHRhY2tlciBvciBpcyBvd24gcGllY2UsIG9yIGFub3RoZXIgcGllY2UKICAgIHJldHVybiBGYWxzZQ==)

def _to_uci_coord(row: int, col: int) -> str:

"""Converts 0-indexed grid coordinates (row, col) to UCI string (e.g., ’e2’)."""

file_char = chr(ord(’a’) + col)

rank_char = str(8 - row) # Grid row 0 is rank 8, grid row 7 is rank 1

return file_char + rank_char

def _from_uci_coord(coord_str: str) -> tuple[int, int] | None:

"""Converts UCI string (e.g., ’e2’) to 0-indexed grid coordinates (row, col). Returns None on invalid input."""

if not (len(coord_str) == 2 and ’a’ <= coord_str[0] <= ’h’ and ’1’ <= coord_str[1] <= ’8’):

return None

col = ord(coord_str[0]) - ord(’a’)

row = 8 - int(coord_str[1]) # Rank 8 is grid row 0, rank 1 is grid row 7

return row, col

def _find_king(grid: list[list[str]], king_color: str) -> tuple[int, int] | None:

"""Finds the coordinates of the king of the specified color."""

for r in range(8):

for c in range(8):

piece = grid[r][c]

if (king_color == ’w’ and piece == ’K’) or \

(king_color == ’b’ and piece == ’k’):

return r, c

return None # King not found (should ideally not happen in a valid game state)

def _is_square_attacked(grid: list[list[str]], r: int, c: int, by_white: bool) -> bool:

"""Checks if square (r, c) is attacked by any piece of the color ’by_white’ (True for White, False for Black)."""

# Helper to check if a piece at (pr, pc) is of the attacking_color

def is_attacker(piece_sym: str, is_white_attacker: bool) -> bool:

if piece_sym == ’.’: return False

return (is_white_attacker and piece_sym.isupper()) or \

(not is_white_attacker and piece_sym.islower())

# 1. Pawn attacks (diagonal 1 step)

# If checking attack *by* White, White pawns attack "up" (decreasing row index). So a white pawn attacking (r,c) would be at (r+1, c-1) or (r+1, c+1).

# If checking attack *by* Black, Black pawns attack "down" (increasing row index). So a black pawn attacking (r,c) would be at (r-1, c-1) or (r-1, c+1).

pawn_attacker_dr_from_target = 1 if by_white else -1

for dc_pawn in [-1, 1]:

pr, pc = r + pawn_attacker_dr_from_target, c + dc_pawn

if 0 <= pr < 8 and 0 <= pc < 8 and grid[pr][pc].upper() == ’P’:

if is_attacker(grid[pr][pc], by_white):

return True

# 2. Knight attacks (L-shape)

knight_moves_deltas = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

for dr_k, dc_k in knight_moves_deltas:

kr, kc = r + dr_k, c + dc_k

if 0 <= kr < 8 and 0 <= kc < 8 and grid[kr][kc].upper() == ’N’:

if is_attacker(grid[kr][kc], by_white):

return True

# 3. King attacks (1 step in any direction)

# A king cannot move into a square attacked by another king, but for simplicity of check detection, we consider a king’s direct vicinity as attacked by an opposing king.

for dr_k, dc_k in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:

kr, kc = r + dr_k, c + dc_k

if 0 <= kr < 8 and 0 <= kc < 8 and grid[kr][kc].upper() == ’K’:

if is_attacker(grid[kr][kc], by_white):

return True

# 4. Rook/Queen attacks (straight lines)

straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right

for dr_s, dc_s in straight_directions:

for step in range(1, 8):

sr, sc = r + dr_s * step, c + dc_s * step

if not (0 <= sr < 8 and 0 <= sc < 8): break # Out of bounds

piece_at_sr_sc = grid[sr][sc]

if piece_at_sr_sc == ’.’: continue # Path clear

if is_attacker(piece_at_sr_sc, by_white) and \

(piece_at_sr_sc.upper() == ’R’ or piece_at_sr_sc.upper() == ’Q’):

return True

else:

break # Blocking piece is not an attacker or is own piece, or another piece

# 5. Bishop/Queen attacks (diagonal lines)

diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # Up-Left, Up-Right, Down-Left, Down-Right

for dr_d, dc_d in diagonal_directions:

for step in range(1, 8):

sr, sc = r + dr_d * step, c + dc_d * step

if not (0 <= sr < 8 and 0 <= sc < 8): break # Out of bounds

piece_at_sr_sc = grid[sr][sc]

if piece_at_sr_sc == ’.’: continue # Path clear

if is_attacker(piece_at_sr_sc, by_white) and \

(piece_at_sr_sc.upper() == ’B’ or piece_at_sr_sc.upper() == ’Q’):

return True

else:

break # Blocking piece is not an attacker or is own piece, or another piece

return False
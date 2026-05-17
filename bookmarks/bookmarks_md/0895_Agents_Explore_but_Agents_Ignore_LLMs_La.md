Title: Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity

URL Source: https://arxiv.org/html/2604.17609v1

Published Time: Tue, 21 Apr 2026 01:24:58 GMT

Markdown Content:
Leon Engländer 

Cohere 

leon@cohere.com

&Sophia Althammer 

Cohere 

&Ahmet Üstün 

Cohere 

&Matthias Gallé 

Poolside 

&Tom Sherborne 

Cohere

###### Abstract

LLM-based agents are assumed to integrate environmental observations into their reasoning: discovering highly relevant but unexpected information should naturally lead to a model exploiting its own discoveries. We show that this assumption is false for current LLM-based agents, which struggle to reflect or react to unexpected information. Across three benchmarks (Terminal-Bench, SWE-Bench, AppWorld), we inject complete task solutions into the agent environments to deliberately expose a task’s solution to a model. While agents discover these solutions on Terminal-Bench in 79–81% of runs, they interact, or exploit, them in only 37-50% of cases. This gap is starkest in AppWorld: agents see documentation stating that a command “returns the complete solution to this task” in over 90% of attempts but exploit this in fewer than 7% of trials. We show that agents lack what we call _environmental curiosity_: the capability to recognize and investigate unexpected but relevant observations in response to environmental stimuli. We identify three main factors influencing environmental curiosity: available tools in the agent scaffold, test-time compute, and training data distribution. Our findings identify configurations that maximize curiosity also achieve the best performance on the unmodified benchmarks. Yet even jointly optimized agents still ignore discovered solutions in the majority of trials: current agents use the environment to fetch expected information, but not to revise their strategy or maximally exploit useful stimuli.

## 1 Introduction

Contemporary LLM-based agents have made rapid progress on benchmarks simulating complex real-world tasks. On SWE-Bench Verified (Chowdhury et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib3 "Introducing SWE-bench verified")), resolution rates climbed from 33.2% to 80+% through improved models and agent scaffolds like SWE-Agent (Yang et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib10 "SWE-agent: agent-computer interfaces enable automated software engineering")) and OpenHands (Wang et al., [2025](https://arxiv.org/html/2604.17609v1#bib.bib11 "OpenHands: an open platform for AI software developers as generalist agents")).

Agents begin each task without knowledge of the codebase they act in. To succeed, they must explore the environment to discover relevant information and integrate findings into their reasoning and future steps. During exploration, the agent may encounter unexpected but highly relevant information, such as code that already solves parts of the task. In those situations, an agent would benefit from environmental curiosity, which we define as the capability to recognize and investigate such observations in response to environmental stimuli. We show that current agents lack this useful exploration behavior: while agents regularly discover relevant but unexpected information, they fail to investigate and apply this information to solve the problem at hand, but rather ignore the information.

To evaluate environmental curiosity, we propose _solution injection_: we place the respective solution directly inside the environment, e.g., as a script, and measure (i) whether agents discover the solution and (ii) whether they interact with it, e.g., read the added solution file. Existing benchmarks primarily measure task success (often based on environment state), and thus cannot distinguish agents that adapt their behavior based on observations from those that execute fixed patterns learned during training. Through solution injection, we are able to quantify this distinction.

![Image 1: Refer to caption](https://arxiv.org/html/2604.17609v1/x1.png)

Figure 1: Agents discover but ignore injected solutions. This figure shows a trajectory from AppWorld with injected solution using gpt-oss-120b as the LLM. The agent executes cli --help and observes documentation explicitly stating that calling the solution API would display the solution for the current task. The agent proceeds without calling it. Current LLM-based agents lack environmental curiosity: while gpt-oss-120b discovers the documentation in 97.54% of runs, it calls the solution API in only 0.53% of cases.

We apply solution injection to three agentic benchmarks: Terminal-Bench (Merrill et al., [2026](https://arxiv.org/html/2604.17609v1#bib.bib13 "Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces")), SWE-Bench Verified (Chowdhury et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib3 "Introducing SWE-bench verified")), and AppWorld (Trivedi et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib12 "AppWorld: A controllable world of apps and people for benchmarking interactive coding agents")) that span code and non-code domains, including terminal tasks, software engineering tasks, and everyday digital tasks performed via API calls. Our experiments show that across all three benchmarks, and two distinct agent scaffolds (SWE-agent, Yang et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib10 "SWE-agent: agent-computer interfaces enable automated software engineering"); Terminus, Merrill et al., [2026](https://arxiv.org/html/2604.17609v1#bib.bib13 "Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces")), agents frequently discover injected solutions but rarely interact with them. This discovery-interaction gap is starkest in AppWorld: in 97.54% of attempts, gpt-oss-120b sees documentation explicitly stating that a command “returns the complete solution to this task”, yet calls this tool only 0.53% of the time, as illustrated in Figure[1](https://arxiv.org/html/2604.17609v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity").

We find three critical factors that strongly influence environmental curiosity at inference time: tool availability, reasoning budget, and exploration-oriented prompting. Adding tools beyond a basic bash shell strongly reduces interaction rates, as agents default to learned tool-specific patterns rather than examining their environment. Yet even with all those factors optimized, agents still ignore discovered solutions in the majority of trials, indicating that the deficit is not solely in inference-time configuration. We further investigate the role of training distribution and find that supervised fine-tuning on narrow, in-distribution data reduces environmental curiosity and the diversity of explored solution paths, degrading the benefit of increased performance from additional trials, seen in lower pass@k for higher k.

Crucially, the prompts that most improve interaction rates also achieve the best performance on the original, unmodified benchmarks, and narrow in-distribution fine-tuning degrades pass@k scaling on the original benchmarks as well. Optimizing for environmental curiosity consistently improves performance on the original benchmarks.

Our main contributions are:

*   •
We define Environmental Curiosity and benchmark the (lack of) capacity of modern LLMs to leverage unexpected relevant information. This gap between discovery and interaction is consistent across three benchmarks, multiple LLMs, and agent scaffolds.

*   •
We introduce Solution Injection as a method for adapting agent benchmarks to evaluate environmental curiosity. We propose two new metrics, discovery@k and interaction@k, to separately measure whether agents discover and act on relevant information.

*   •
We investigate test-time factors influencing environmental curiosity. The most consistent effect comes from tool availability: restricting the agent scaffold to bash-only roughly doubles interaction rates. Increased reasoning budget and prompts instructing to explore also improve environmental curiosity. Yet even with all factors optimized, agents still ignore discovered solutions in the majority of runs.

*   •
We find that fine-tuning on narrow in-distribution data reduces environmental curiosity and the diversity of explored solution paths, leading to worse pass@k scaling even on the original benchmarks.

## 2 Method

To evaluate environmental curiosity, i.e., the tendency to investigate relevant observations in response to environmental stimuli, we need to separately measure an agent’s ability to discover relevant information and whether it interacts with what it discovers. To achieve this, we propose injecting the task’s gold solution directly into the environment.

### 2.1 Solution Injection

The central idea is to add the task solution directly to the environment. This is conceptually applicable to any existing agent benchmark where a gold solution exists. The injected solution must be (i) complete so that following it guarantees task success and (ii) discoverable through agent actions.

This offers unexpected but highly relevant information. It is relevant because it contains the complete task solution, and unexpected because it lies outside the agent’s typical workflow. This allows us to measure whether the agent is environmentally curious enough to investigate it. The injected solutions are deliberately obvious. Agents that ignore information explicitly labeled as the solution are unlikely to integrate the subtler information present in real environments. We apply solution injection to Terminal-Bench, SWE-Bench, and AppWorld, injecting solutions as executable files or as documented API endpoints, depending on the benchmark 1 1 1 For example, in Terminal-Bench and SWE-Bench, we add the solution as solution.sh to the agent’s working directory. In AppWorld, we add a solution API endpoint documented in the CLI help output.. To ensure our findings are not artifacts of a specific file name or format, we also experiment with different injection variants (Appendix[B.2](https://arxiv.org/html/2604.17609v1#A2.SS2 "B.2 Effect of file name ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [B.3](https://arxiv.org/html/2604.17609v1#A2.SS3 "B.3 Solution injection difficulty levels ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")).

### 2.2 Metrics

To measure performance and how often the agent discovers and exploits solution injection, we measure three metrics across n attempts per task. We use the pass@k definition from Chen et al. ([2021](https://arxiv.org/html/2604.17609v1#bib.bib9 "Evaluating large language models trained on code")) and introduce two new metrics for discovery and interaction using the same unbiased estimator to compute probabilities across n attempts:

pass@k: The probability that at least one of k attempts successfully completes the task. With c_{\text{pass}} being the number of attempts that pass the task:

\text{pass@}k:=\underset{\text{Tasks}}{\mathbb{E}}\left[1-\dfrac{\binom{n-c_{\text{pass}}}{k}}{\binom{n}{k}}\right](1)

discovery@k: The probability that at least one of k attempts executes a command that surfaces the injected solution in the agent’s context. This metric serves as a sanity check that the injected solution is indeed discoverable through the normal agent’s actions. With c_{\text{disc}} being the number of attempts in which the solution was discovered:

\text{discovery@}k:=\underset{\text{Tasks}}{\mathbb{E}}\left[1-\dfrac{\binom{n-c_{\text{disc}}}{k}}{\binom{n}{k}}\right](2)

interaction@k: The probability that, across k attempts, the agent interacts with the injected solution at least once, such as reading or executing the solution file or querying the solution API.2 2 2 We detect interaction by checking whether any command executed by the agent references the injected solution, e.g. contains “solution.sh” or “cli solution”. This metric measures environmental curiosity: a high interaction rate would mean that the agent investigated the unexpected but highly relevant information it discovered. A low interaction rate would mean that it ignored it. With c_{\text{interact}} being the number of attempts in which the agent interacted with the solution, we define \text{interaction@}k as:

\text{interaction@}k:=\underset{\text{Tasks}}{\mathbb{E}}\left[1-\dfrac{\binom{n-c_{\text{interact}}}{k}}{\binom{n}{k}}\right](3)

## 3 Experiments

We evaluate the environmental curiosity of agents and investigate which factors influence environmental curiosity. We structure our investigation around three hypotheses: (H1) LLM-based agents lack environmental curiosity: they discover relevant information during exploration but systematically fail to act on it. (H2) Test-time design decisions shape environmental curiosity. (H3) Narrow fine-tuning suppresses environmental curiosity.

##### Benchmarks.

We apply solution injection to three benchmarks: Terminal-Bench v1(Merrill et al., [2026](https://arxiv.org/html/2604.17609v1#bib.bib13 "Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces")), SWE-Bench Verified(Chowdhury et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib3 "Introducing SWE-bench verified")), and AppWorld(Trivedi et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib12 "AppWorld: A controllable world of apps and people for benchmarking interactive coding agents")). Terminal-Bench spans a wide variety of terminal-based tasks, including file manipulation, system administration, and data processing. SWE-Bench Verified evaluates agents on resolving real GitHub issues by editing repository code. AppWorld requires agents to complete everyday digital tasks, such as managing emails, notes, and calendars, by interacting with simulated apps via API calls. For Terminal-Bench and SWE-Bench Verified, we inject the solution as an executable solution.sh in the agent’s working directory. For AppWorld, we add a solution API endpoint documented in the “cli --help”, as shown in Figure[1](https://arxiv.org/html/2604.17609v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). We also report on AppWorld’s validation split, rather than test split, as we require gold solutions for solution injection, which only exist for the validation split.

##### Agent implementation.

The agent setup involves three layers: the _harness_, _scaffold_, and _tools_. The _harness_ handles the execution environment, i.e., initializes the Docker execution environment and controls evaluating submitted solutions. The _scaffold_ is the agent loop (i.e., ReACT loop from Yao et al. ([2023](https://arxiv.org/html/2604.17609v1#bib.bib26 "ReAct: synergizing reasoning and acting in language models"))), including prompting, tool-call parsing, and history management. The _tools_ determine how the agent may interact with its environment. We evaluate two scaffolds: Terminus 1(Merrill et al., [2026](https://arxiv.org/html/2604.17609v1#bib.bib13 "Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces")), which is the default Terminal-Bench agent, and SWE-agent(Yang et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib10 "SWE-agent: agent-computer interfaces enable automated software engineering")). We adapt these scaffolds to use native function-calling APIs over raw prompting to remove the potential variable of out-of-distribution function calling interfaces (introduced in proprietary scaffolds) to instead rely on a provider’s native tool-use interface.

We evaluate two tool suites: bash-only, and bash and str_replace_editor. The str_replace_editor is a structured file-editing tool introduced by Anthropic(Anthropic, [2024](https://arxiv.org/html/2604.17609v1#bib.bib25 "Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku"))3 3 3[https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool) that has become the standard editing tool in coding agent scaffolds(Yang et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib10 "SWE-agent: agent-computer interfaces enable automated software engineering"); Wang et al., [2025](https://arxiv.org/html/2604.17609v1#bib.bib11 "OpenHands: an open platform for AI software developers as generalist agents")). This is one of only three tools in SWE-agent’s default configuration, alongside bash and a submit tool.4 4 4 For SWE-agent, “bash-only” refers to bash plus the submit tool, i.e. without str_replace_editor.

##### Evaluation setup.

We evaluate three LLMs: gpt-oss-120b(OpenAI, [2025](https://arxiv.org/html/2604.17609v1#bib.bib23 "Gpt-oss-120b & gpt-oss-20b model card")) with high reasoning, GLM-4.7(GLM, [2025](https://arxiv.org/html/2604.17609v1#bib.bib22 "GLM-4.5: agentic, reasoning, and coding (ARC) foundation models")), and fine-tuned variants of command-a-reasoning(Cohere et al., [2025](https://arxiv.org/html/2604.17609v1#bib.bib7 "Command a: an enterprise-ready large language model"); Cohere, [2025](https://arxiv.org/html/2604.17609v1#bib.bib6 "Command A reasoning: enterprise-grade control for AI agents")) trained on different task distributions, as described in Section[3.3](https://arxiv.org/html/2604.17609v1#S3.SS3 "3.3 Effect of training distribution ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). Unless otherwise specified, we use the Terminal-Bench harness and the Terminus agent with bash as the only tool. We evaluate with n=10 attempts per task and report discovery@k and interaction@k (Equations[2](https://arxiv.org/html/2604.17609v1#S2.E2 "In 2.2 Metrics ‣ 2 Method ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") and [3](https://arxiv.org/html/2604.17609v1#S2.E3 "In 2.2 Metrics ‣ 2 Method ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")) alongside pass@k for all experiments.

![Image 2: Refer to caption](https://arxiv.org/html/2604.17609v1/x2.png)

Figure 2: discovery@1 versus interaction@1 across benchmarks. We evaluate gpt-oss-120b with high reasoning (gpt-oss), GLM-4.7, and Command A Reasoning fine-tuned for Terminal-Bench (cmd-a). Agents consistently discover solutions but rarely interact with them.

### 3.1 Agents lack environmental curiosity

Figure[2](https://arxiv.org/html/2604.17609v1#S3.F2 "Figure 2 ‣ Evaluation setup. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") shows the discovery and interaction rates across all three benchmarks. Across all models and benchmarks, agents consistently discover the injected solutions but rarely interact with them. On Terminal-Bench, discovery@1 ranges from 78.6–81.2% while interaction@1 reaches only 37.1–50.3%. On SWE-Bench, agents discover solutions in 53.4–98.2% of runs but interact in only 5.9–17.4%. The gap is starkest on AppWorld: discovery@1 exceeds 90% for all models, yet interaction@1 never surpasses 6.3%. The bottleneck for current agents is not discovering relevant information but integrating observations into their reasoning. We show an example trajectory in Figure[1](https://arxiv.org/html/2604.17609v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity").

Table 1: Task performance of gpt-oss-120b (high reasoning) on original and solution-injected benchmarks. Improvements correlate with the interaction rate in Figure [2](https://arxiv.org/html/2604.17609v1#S3.F2 "Figure 2 ‣ Evaluation setup. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity").

Table[1](https://arxiv.org/html/2604.17609v1#S3.T1 "Table 1 ‣ 3.1 Agents lack environmental curiosity ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") shows the performance on the original and solution-injected benchmarks for gpt-oss-120b. On the original benchmarks, the model achieves 40-46% pass@1, which confirms that these are challenging tasks. Injecting solutions improves performance, with the largest gain on Terminal-Bench (+11.4) where interaction is highest. On AppWorld, where agents almost never call the solution API, the gain is minimal (+2.6). This observation holds across all models; full results in Appendix[B.1](https://arxiv.org/html/2604.17609v1#A2.SS1 "B.1 Expanded results ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity").

### 3.2 Test-time factors

We next investigate why agents fail to use what they discover. We begin with examining how test-time design decisions shape environmental curiosity (H2) by investigating three factors: agent scaffolding, test-time compute, and prompting.

##### Agent scaffolding.

We compare Terminus and SWE-agent scaffolds to ensure our findings are not artifacts of any specific agent implementation. This comparison additionally investigates how available tools shape environmental curiosity by evaluating two tool configurations: bash-only, and bash with str_replace_editor. We evaluate gpt-oss-120b and a fine-tuned variant of command-a-reasoning trained on bash-only trajectories from SWE-smith (SWE-Bench-SFT; described in Section[3.3](https://arxiv.org/html/2604.17609v1#S3.SS3 "3.3 Effect of training distribution ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")). All experiments are conducted on SWE-Bench Verified; for scaffold implementation details, see Appendix[E](https://arxiv.org/html/2604.17609v1#A5 "Appendix E Agent Implementations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). Figure[3](https://arxiv.org/html/2604.17609v1#S3.F3 "Figure 3 ‣ Agent scaffolding. ‣ 3.2 Test-time factors ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") shows that scaffold choice substantially affects both task performance and environmental curiosity (e.g., SWE-Bench-SFT with bash-only achieves 46.9 pass@1 with Terminus but 25.2 with SWE-agent), but both scaffolds consistently exhibit the discovery-interaction gap.

The available tools substantially affect environmental curiosity. Adding str_replace_editor improves pass@1 across all configurations but reduces interaction, conditional upon discovery, in every case. The same pass@1 improvement appears on the original, unmodified SWE-Bench Verified, confirming that the performance gains from richer toolsets are not artifacts of solution injection. Notably, SWE-Bench-SFT has never encountered str_replace_editor during fine-tuning, yet providing it at test time still relatively reduces interaction given discovery by 13.7% to 48.3%, suggesting that the tool-use patterns that reduce exploration originate from pre-training. Among trajectories where agents do interact with the solution, the median interaction step is similar with (step 18) and without (step 15) the editor. Both medians fall within the first 25% of the trajectory, indicating that the tool does not delay interaction but suppresses it. We conjecture that when a dedicated editing tool is available, agents default to applying it directly rather than first examining their environment; we discuss this further in Section[4](https://arxiv.org/html/2604.17609v1#S4 "4 Discussion ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity").

![Image 3: Refer to caption](https://arxiv.org/html/2604.17609v1/x3.png)

Figure 3: Adding tools improves task performance but reduces environmental curiosity. We evaluate gpt-oss-120b and cmd-a (SWE-Bench SFT) across two scaffolds (Terminus, SWE-agent) on SWE-Bench Verified. Adding str_replace_editor increases pass@1 for the solution injected as well as the original (faint lines) benchmark, but consistently decreases the probability of interacting with discovered solutions. The discovery@1 exceeds 87.9% across all configurations, i.e., the conditional metric is not driven by varying discovery rates.

##### Effect of reasoning effort.

![Image 4: Refer to caption](https://arxiv.org/html/2604.17609v1/x4.png)

Figure 4: gpt-oss-120b with different reasoning budgets on Terminal-Bench.

To additionally measure the effect of reasoning levels, we evaluate gpt-oss-120b with low, medium and high reasoning on all benchmarks. We observe that increased reasoning substantially improves environmental curiosity: Terminal-Bench interaction@1 more than triples from 11% to 37%, as shown in figure[4](https://arxiv.org/html/2604.17609v1#S3.F4 "Figure 4 ‣ Effect of reasoning effort. ‣ 3.2 Test-time factors ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). This is not an artifact of higher discovery rates: The conditional probability of interaction given discovery increases from 17.65% (low) to 36.68% (medium) to 45.69% (high). On SWE-Bench, interaction@1 increases from 0.78% to 17.42% when increasing reasoning. On AppWorld, interaction remains near zero across all reasoning levels, indicating that increased compute alone cannot overcome the gap for all task types.

##### Prompting.

We test whether explicit instructions improve environmental curiosity. Prompting the agent to explore its environment before acting improves task performance across all three benchmarks by on average +2.57% on the original benchmarks and +2.96% on the solution-injected versions, as shown in Appendix[B.4](https://arxiv.org/html/2604.17609v1#A2.SS4 "B.4 Prompt variations ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). On Terminal-Bench, we further evaluate prompts encouraging reflection and adapting to environmental observations (Appendix[B.4.1](https://arxiv.org/html/2604.17609v1#A2.SS4.SSS1 "B.4.1 Prompt variations on Terminal-Bench ‣ B.4 Prompt variations ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")). Less directive prompts to encourage curiosity and step-wise reflection yield diminishing returns. Requiring agents to investigate all discovered files before proceeding achieves the highest interaction and pass rates on the solution injected benchmark. Notably, the best-performing prompt on the solution-injected benchmark is also the best-performing prompt on the original Terminal-Bench, suggesting that improved environmental curiosity benefits general task performance.

##### Summary.

All three test-time factors improve interaction rates as proposed by Hypothesis (H2). Tool availability shapes how agents approach their environment: with fewer tools, agents must examine files to understand the environment; with more tools, they default to learned tool-specific patterns and skip investigation or curiosity. Test-time compute and prompt design support agents to identify and act on unexpected but highly relevant information. Yet even with optimal settings, i.e., bash-only, high reasoning, and explicit instructions to investigate, agents still ignore solutions in the majority of trials. This suggests the limitation is not solely a matter of inference-time configuration, but is inherent to how LLMs are trained. Given this finding, we now examine the influence of training data distribution on how agents exhibit curiosity-driven behavior.

### 3.3 Effect of training distribution

The previous section identified that optimizing test-time factors does not resolve the gap between discovery and interaction, suggesting that the limited environmental curiosity stems from the training phase. To investigate this, we fine-tune command-a-reasoning via rejection sampling(Guo et al., [2025](https://arxiv.org/html/2604.17609v1#bib.bib1 "DeepSeek-r1 incentivizes reasoning in llms through reinforcement learning")) on three task distributions: Terminal-Bench-like tasks from an external vendor (T-Bench-SFT), the AppWorld training split (AppWorld-SFT), and SWE-smith (SWE-Bench-SFT). All models are trained on approximately 20,000 turns; further details are provided in Appendix[C](https://arxiv.org/html/2604.17609v1#A3 "Appendix C SFT Training Data Details ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). We use these models to analyze how training breadth and domain transfer affect environmental curiosity.

##### Narrow in-distribution training reduces solution diversity.

AppWorld’s task distribution is a narrow subset of Terminal-Bench’s distribution (Appendix[D](https://arxiv.org/html/2604.17609v1#A4 "Appendix D AppWorld is a subset of Terminal-Bench ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")), so comparing T-Bench-SFT and AppWorld-SFT isolates the effect of training distribution breadth. Table[2](https://arxiv.org/html/2604.17609v1#S3.T2 "Table 2 ‣ Curiosity does not transfer across domains. ‣ 3.3 Effect of training distribution ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") shows that on AppWorld, AppWorld-SFT achieves higher pass@1 (44.2 vs. 34.5) but is surpassed by T-Bench-SFT at higher k (65.8 vs. 69.0 at pass@10), suggesting that narrow in-domain training compresses the explored solution space. Interaction@10 shows the same gap (29.8 vs. 41.5). On Terminal-Bench, where AppWorld-SFT is out-of-distribution, T-Bench-SFT achieves higher pass and interaction rates. The same patterns appear on the original, unmodified benchmarks (Figure[5](https://arxiv.org/html/2604.17609v1#S3.F5 "Figure 5 ‣ Curiosity does not transfer across domains. ‣ 3.3 Effect of training distribution ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")): T-Bench-SFT surpasses AppWorld-SFT at higher k on AppWorld and achieves consistently higher pass@k on Terminal-Bench, indicating that when the evaluation domain is a subset of a broader training distribution, the broader-trained model has lower pass@1 but better pass@k scaling, i.e., explores a wider solution space.

##### Curiosity does not transfer across domains.

To test whether environmental curiosity generalizes beyond the training distribution, we compare T-Bench-SFT and SWE-Bench-SFT, which cover structurally distinct task types. Table[3](https://arxiv.org/html/2604.17609v1#S3.T3 "Table 3 ‣ Curiosity does not transfer across domains. ‣ 3.3 Effect of training distribution ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") shows that on each benchmark, the respective in-domain model achieves consistently higher pass and interaction rates. Together, these results show that environmental curiosity can benefit from in-domain training data in some scenarios, but a narrow in-domain distribution reduces or degrades this benefit.

![Image 5: Refer to caption](https://arxiv.org/html/2604.17609v1/x5.png)

![Image 6: Refer to caption](https://arxiv.org/html/2604.17609v1/x6.png)

Figure 5: Training distribution affects pass@n scaling on the _original_, i.e. unmodified, benchmarks. Left: On AppWorld, the narrow in-distribution model (AppWorld-SFT) achieves higher pass@1 but is surpassed by the broader-trained model (T-Bench-SFT) at higher k, indicating that narrow training compresses the explored solution space. Right: On Terminal-Bench, the broader-trained model outperforms across all k. Results averaged over 3 fine-tuned models with different seeds.

Table 2: Effect of training distribution on environmental curiosity and task performance. All models are fine-tuned from command-a-reasoning. Narrow in-distribution training (AppWorld-SFT) yields higher pass@1 on AppWorld but lower interaction rates and worse pass@10 scaling. Results averaged over 3 seeds.

Table 3: Cross-domain comparison of T-Bench-SFT and SWE-Bench-SFT, both fine-tuned from command-a-reasoning. On each benchmark, the respective in-domain model achieves higher interaction rates and better pass@10 scaling. Results on SWE-Bench from a single seed.

## 4 Discussion

Our results confirm all three hypotheses: agents consistently discover but fail to act on injected solutions (H1), test-time factors modulate but cannot close this gap (H2), and fine-tuning on narrow in-distribution data further suppresses environmental curiosity (H3).

This raises a key question: do current models already possess environmental curiosity that scaffolding or later-stage alignment fails to elicit, or does training never produce environmental curiosity in the first place?Our evidence suggests that both factors play a role. Optimizing test-time factors improves environmental curiosity (Section [3.2](https://arxiv.org/html/2604.17609v1#S3.SS2 "3.2 Test-time factors ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")), indicating that training does produce latent capability that scaffolding can amplify. However, even with all investigated factors jointly optimized, agents ignore discovered solutions in the majority of runs. LLM-as-a-judge analysis of reasoning traces confirms that in attempts where the solution is discovered but not interacted with, the agent’s reasoning does not mention the discovered solution at all; the agent proceeds as if the observation never occurred (Appendix [A.1](https://arxiv.org/html/2604.17609v1#A1.SS1 "A.1 LLM-as-a-Judge analysis: agents ignore rather than reject discovered solutions ‣ Appendix A Ruling Out Alternative Explanations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")). Yet when the solution is injected directly in the user prompt or the agent’s first reasoning step, agents incorporate it into their plan and solve the task at substantially higher rates (Appendix [A.2](https://arxiv.org/html/2604.17609v1#A1.SS2 "A.2 Case study: agents can use solutions ‣ Appendix A Ruling Out Alternative Explanations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")), which shows that they do have the capability to use the information, but they habitually decide to ignore it.

Currently, the agent loop is:

\text{Action}\rightarrow\text{Observation}\rightarrow\text{Reasoning}\rightarrow\text{Next Action}(4)

Whereas environmental curiosity requires reflecting on whether observations fit the agent’s current model of the environment, i.e., whether anything unexpected is observed:

\text{Action}\rightarrow\text{Observation}\rightarrow\text{Reasoning {and reflecting on observations}}\rightarrow\text{Next Action}(5)

We hypothesize that training agents on specific environments reinforces Equation [4](https://arxiv.org/html/2604.17609v1#S4.E4 "In 4 Discussion ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") because supervised fine-tuning relies on expert on-policy trajectories in which tool outputs consistently align with the agent’s implicit plan, and, in reinforcement learning, those biases regarding tool outputs are increased. The environment never contradicts the expert, so the model learns to seek specific information and act on what it sought, rather than to notice and act on information it was not looking for. We attempted three SFT setups in order to get the agent to use the relevant information: (1) rejection sampling for curious first turns, (2) mid-trajectory file removal and re-addition to simulate dynamic environments, and (3) injecting masked adversarial turns forcing state recovery. None improved interaction rates, demonstrating that training for environmental curiosity is not straightforward. This raises a deeper open question: does post-training suppress the environmental curiosity that pre-training may produce, or does it never emerge? Developing methods to measure environmental curiosity in base models is an open challenge, since base models cannot operate as agents, and environmental curiosity can only be observed through agentic behavior.

Environmental curiosity is a prerequisite for agents that operate in novel, open-ended environments. Agents that succeed only by executing memorized patterns are fundamentally brittle: they will fail whenever the environment deviates from the training distribution in ways that require adaptation. Outcome-driven metrics like pass@k reward agents executing Equation [4](https://arxiv.org/html/2604.17609v1#S4.E4 "In 4 Discussion ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") as effectively as agents executing Equation [5](https://arxiv.org/html/2604.17609v1#S4.E5 "In 4 Discussion ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), as they cannot distinguish adaptive reasoning from rigid plan execution. Process-oriented metrics like interaction@k, which assess whether agents ground their reasoning in what they observe, are a necessary complement to task success. Solution injection and measuring interaction@k are a first step, but richer methods for measuring environmental curiosity are needed.

We see three directions for future work: (i) developing diverse benchmarks and metrics to measure environmental curiosity beyond solution injection, (ii) training paradigms teaching the reflective behavior in Equation [5](https://arxiv.org/html/2604.17609v1#S4.E5 "In 4 Discussion ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), and (iii) scaffold designs to trigger reflection on observations.

## 5 Related work

##### LLM-Based Agents.

LLM-based agents interleave reasoning with action execution in a single trajectory, as proposed by ReAct(Yao et al., [2023](https://arxiv.org/html/2604.17609v1#bib.bib26 "ReAct: synergizing reasoning and acting in language models")). While ReAct parsed structured actions directly from text output, state-of-the-art agents use native function-calling APIs. For tasks in terminal environments, scaffolds vary widely: Terminus(Merrill et al., [2026](https://arxiv.org/html/2604.17609v1#bib.bib13 "Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces")) provides only a bash tool, SWE-agent(Yang et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib10 "SWE-agent: agent-computer interfaces enable automated software engineering")) adds a curated set of file editing and a few optional tools, and OpenHands(Wang et al., [2025](https://arxiv.org/html/2604.17609v1#bib.bib11 "OpenHands: an open platform for AI software developers as generalist agents")) offers a broad toolkit of over fifty tools. LLMs are trained to use these tools through supervised fine-tuning and reinforcement learning (OpenAI, [2025](https://arxiv.org/html/2604.17609v1#bib.bib23 "Gpt-oss-120b & gpt-oss-20b model card"); GLM, [2025](https://arxiv.org/html/2604.17609v1#bib.bib22 "GLM-4.5: agentic, reasoning, and coding (ARC) foundation models")). Augmenting a bash shell with increasingly rich tool sets has been shown to improve task performance. However, tools have not yet been evaluated for how they shape an agent’s _behavior_ with respect to environmental interaction.

##### Benchmarks.

A growing number of benchmarks evaluate LLM-based agents across diverse domains:SWE-Bench Verified(Chowdhury et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib3 "Introducing SWE-bench verified")) and Terminal-Bench(Merrill et al., [2026](https://arxiv.org/html/2604.17609v1#bib.bib13 "Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces")) evaluate software engineering tasks, AppWorld(Trivedi et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib12 "AppWorld: A controllable world of apps and people for benchmarking interactive coding agents")) considers everyday digital tasks, DiscoveryWorld(Jansen et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib5 "DiscoveryWorld: A virtual environment for developing and evaluating automated scientific discovery agents")) targets scientific discovery, and \tau^{2}-bench(Barres et al., [2025](https://arxiv.org/html/2604.17609v1#bib.bib4 "τ2-Bench: evaluating conversational agents in a dual-control environment")) evaluate assistant tasks with user coordination. These benchmarks all measure end-to-end task success, i.e., whether the agent completes the task, but starkly not how an agent arrives at its solution. These benchmarks cannot distinguish agents that adapt to observations from those that execute fixed patterns, which is the gap our solution injection method addresses.

##### Agentic Exploration.

Recent work on agentic exploration in terminal environments relies on agents executing standard shell commands or using supplementary search tools to discover relevant information (Yang et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib10 "SWE-agent: agent-computer interfaces enable automated software engineering"); Wang et al., [2025](https://arxiv.org/html/2604.17609v1#bib.bib11 "OpenHands: an open platform for AI software developers as generalist agents")), or bypasses open-ended exploration entirely via predefined localization pipelines (Xia et al., [2025](https://arxiv.org/html/2604.17609v1#bib.bib8 "Demystifying llm-based software engineering agents")). Curiosity in reinforcement learning(Schmidhuber, [2020](https://arxiv.org/html/2604.17609v1#bib.bib15 "Generative adversarial networks are special cases of artificial curiosity (1990) and also closely related to predictability minimization (1991)"); Pathak et al., [2017](https://arxiv.org/html/2604.17609v1#bib.bib17 "Curiosity-driven exploration by self-supervised prediction")) formalizes intrinsic rewards to drive the discovery of novel states. Both lines of work address the discovery of relevant information, but our findings show that discovery is not the bottleneck: LLM-based agents consistently find relevant unexpected information but ignore it.

## 6 Conclusion

We introduced solution injection to evaluate environmental curiosity in LLM-based agents, revealing a fundamental disconnect between what agents observe and how they act. Across diverse domains, state-of-the-art agents consistently discover unexpected, highly relevant information yet systematically ignore it. Test-time factors such as tool availability, reasoning budget, and prompting modulate this gap, and the configurations that most improve curiosity also yield the best task performance on the original benchmarks. Yet even jointly optimized, these factors cannot close the gap. Narrow in-distribution fine-tuning further reduces environmental curiosity. Current agents operate as open-loop sequence generators: they use the environment to fetch expected information, not to revise their strategy. However, progress requires training models that treat observations as potential reasons to change their plan, rather than as confirmation of it.

## Acknowledgments

We thank Minjie Xu for providing the codebase on which we built our evaluation and fine-tuning experiments, as well as the data used to train the T-Bench-SFT model.

## References

*   Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku. Note: Blog post External Links: [Link](https://www.anthropic.com/news/3-5-models-and-computer-use)Cited by: [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px2.p2.1 "Agent implementation. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   V. Barres, H. Dong, S. Ray, X. Si, and K. Narasimhan (2025)\tau^{2}-Bench: evaluating conversational agents in a dual-control environment. External Links: 2506.07982, [Link](https://arxiv.org/abs/2506.07982)Cited by: [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px2.p1.1 "Benchmarks. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and W. Zaremba (2021)Evaluating large language models trained on code. CoRR abs/2107.03374. External Links: [Link](https://arxiv.org/abs/2107.03374), 2107.03374 Cited by: [§2.2](https://arxiv.org/html/2604.17609v1#S2.SS2.p1.2 "2.2 Metrics ‣ 2 Method ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   N. Chowdhury, J. Aung, C. J. Shern, O. Jaffe, D. Sherburn, G. Starace, E. Mays, R. Dias, M. Aljubeh, M. Glaese, C. E. Jimenez, J. Yang, L. Ho, T. Patwardhan, K. Liu, and A. Madry (2024)Introducing SWE-bench verified. Note: [https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)Accessed: 2025-12-28 Cited by: [§1](https://arxiv.org/html/2604.17609v1#S1.p1.1 "1 Introduction ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§1](https://arxiv.org/html/2604.17609v1#S1.p4.1 "1 Introduction ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px1.p1.1 "Benchmarks. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px2.p1.1 "Benchmarks. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   T. Cohere, A. Ahmadian, M. Ahmed, J. Alammar, M. Alizadeh, Y. Alnumay, S. Althammer, A. Arkhangorodsky, V. Aryabumi, D. Aumiller, et al. (2025)Command a: an enterprise-ready large language model. arXiv preprint arXiv:2504.00698. Cited by: [Appendix C](https://arxiv.org/html/2604.17609v1#A3.p1.1 "Appendix C SFT Training Data Details ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px3.p1.4 "Evaluation setup. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   T. Cohere (2025)Note: Blog post External Links: [Link](https://cohere.com/blog/command-a-reasoning)Cited by: [Appendix C](https://arxiv.org/html/2604.17609v1#A3.p1.1 "Appendix C SFT Training Data Details ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px3.p1.4 "Evaluation setup. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   GLM (2025)GLM-4.5: agentic, reasoning, and coding (ARC) foundation models. CoRR abs/2508.06471. External Links: [Link](https://doi.org/10.48550/arXiv.2508.06471), [Document](https://dx.doi.org/10.48550/ARXIV.2508.06471), 2508.06471 Cited by: [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px3.p1.4 "Evaluation setup. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px1.p1.1 "LLM-Based Agents. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   D. Guo, D. Yang, H. Zhang, J. Song, P. Wang, Q. Zhu, R. Xu, R. Zhang, S. Ma, X. Bi, X. Zhang, X. Yu, Y. Wu, Z. F. Wu, Z. Gou, Z. Shao, Z. Li, Z. Gao, A. Liu, B. Xue, B. Wang, B. Wu, B. Feng, C. Lu, C. Zhao, C. Deng, C. Ruan, D. Dai, D. Chen, D. Ji, E. Li, F. Lin, F. Dai, F. Luo, G. Hao, G. Chen, G. Li, H. Zhang, H. Xu, H. Ding, H. Gao, H. Qu, H. Li, J. Guo, J. Li, J. Chen, J. Yuan, J. Tu, J. Qiu, J. Li, J. L. Cai, J. Ni, J. Liang, J. Chen, K. Dong, K. Hu, K. You, K. Gao, K. Guan, K. Huang, K. Yu, L. Wang, L. Zhang, L. Zhao, L. Wang, L. Zhang, L. Xu, L. Xia, M. Zhang, M. Zhang, M. Tang, M. Zhou, M. Li, M. Wang, M. Li, N. Tian, P. Huang, P. Zhang, Q. Wang, Q. Chen, Q. Du, R. Ge, R. Zhang, R. Pan, R. Wang, R. J. Chen, R. L. Jin, R. Chen, S. Lu, S. Zhou, S. Chen, S. Ye, S. Wang, S. Yu, S. Zhou, S. Pan, S. S. Li, S. Zhou, S. Wu, T. Yun, T. Pei, T. Sun, T. Wang, W. Zeng, W. Liu, W. Liang, W. Gao, W. Yu, W. Zhang, W. L. Xiao, W. An, X. Liu, X. Wang, X. Chen, X. Nie, X. Cheng, X. Liu, X. Xie, X. Liu, X. Yang, X. Li, X. Su, X. Lin, X. Q. Li, X. Jin, X. Shen, X. Chen, X. Sun, X. Wang, X. Song, X. Zhou, X. Wang, X. Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. Zhang, Y. Xu, Y. Li, Y. Zhao, Y. Sun, Y. Wang, Y. Yu, Y. Zhang, Y. Shi, Y. Xiong, Y. He, Y. Piao, Y. Wang, Y. Tan, Y. Ma, Y. Liu, Y. Guo, Y. Ou, Y. Wang, Y. Gong, Y. Zou, Y. He, Y. Xiong, Y. Luo, Y. You, Y. Liu, Y. Zhou, Y. X. Zhu, Y. Huang, Y. Li, Y. Zheng, Y. Zhu, Y. Ma, Y. Tang, Y. Zha, Y. Yan, Z. Z. Ren, Z. Ren, Z. Sha, Z. Fu, Z. Xu, Z. Xie, Z. Zhang, Z. Hao, Z. Ma, Z. Yan, Z. Wu, Z. Gu, Z. Zhu, Z. Liu, Z. Li, Z. Xie, Z. Song, Z. Pan, Z. Huang, Z. Xu, Z. Zhang, and Z. Zhang (2025)DeepSeek-r1 incentivizes reasoning in llms through reinforcement learning. Nat.645 (8081),  pp.633–638. External Links: [Link](https://doi.org/10.1038/s41586-025-09422-z), [Document](https://dx.doi.org/10.1038/S41586-025-09422-Z)Cited by: [§3.3](https://arxiv.org/html/2604.17609v1#S3.SS3.p1.1 "3.3 Effect of training distribution ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   P. A. Jansen, M. Côté, T. Khot, E. Bransom, B. D. Mishra, B. P. Majumder, O. Tafjord, and P. Clark (2024)DiscoveryWorld: A virtual environment for developing and evaluating automated scientific discovery agents. In Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December 10 - 15, 2024, A. Globersons, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and C. Zhang (Eds.), External Links: [Link](http://papers.nips.cc/paper%5C_files/paper/2024/hash/13836f251823945316ae067350a5c366-Abstract-Datasets%5C_and%5C_Benchmarks%5C_Track.html)Cited by: [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px2.p1.1 "Benchmarks. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   M. A. Merrill, A. G. Shaw, N. Carlini, B. Li, H. Raj, I. Bercovich, L. Shi, J. Y. Shin, T. Walshe, E. K. Buchanan, J. Shen, G. Ye, H. Lin, J. Poulos, M. Wang, M. Nezhurina, J. Jitsev, D. Lu, O. M. Mastromichalakis, Z. Xu, Z. Chen, Y. Liu, R. Zhang, L. L. Chen, A. Kashyap, J. Uslu, J. Li, J. Wu, M. Yan, S. Bian, V. Sharma, K. Sun, S. Dillmann, A. Anand, A. Lanpouthakoun, B. Koopah, C. Hu, E. Guha, G. H. S. Dreiman, J. Zhu, K. Krauth, L. Zhong, N. Muennighoff, R. Amanfu, S. Tan, S. Pimpalgaonkar, T. Aggarwal, X. Lin, X. Lan, X. Zhao, Y. Liang, Y. Wang, Z. Wang, C. Zhou, D. Heineman, H. Liu, H. Trivedi, J. Yang, J. Lin, M. Shetty, M. Yang, N. Omi, N. Raoof, S. Li, T. Y. Zhuo, W. Lin, Y. Dai, Y. Wang, W. Chai, S. Zhou, D. Wahdany, Z. She, J. Hu, Z. Dong, Y. Zhu, S. Cui, A. Saiyed, A. Kolbeinsson, J. Hu, C. M. Rytting, R. Marten, Y. Wang, A. Dimakis, A. Konwinski, and L. Schmidt (2026)Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces. External Links: 2601.11868, [Link](https://arxiv.org/abs/2601.11868)Cited by: [Appendix E](https://arxiv.org/html/2604.17609v1#A5.p1.1 "Appendix E Agent Implementations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§1](https://arxiv.org/html/2604.17609v1#S1.p4.1 "1 Introduction ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px1.p1.1 "Benchmarks. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px2.p1.1 "Agent implementation. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px1.p1.1 "LLM-Based Agents. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px2.p1.1 "Benchmarks. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   OpenAI (2025)Gpt-oss-120b & gpt-oss-20b model card. CoRR abs/2508.10925. External Links: [Link](https://doi.org/10.48550/arXiv.2508.10925), [Document](https://dx.doi.org/10.48550/ARXIV.2508.10925), 2508.10925 Cited by: [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px3.p1.4 "Evaluation setup. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px1.p1.1 "LLM-Based Agents. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   D. Pathak, P. Agrawal, A. A. Efros, and T. Darrell (2017)Curiosity-driven exploration by self-supervised prediction. In Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017, D. Precup and Y. W. Teh (Eds.), Proceedings of Machine Learning Research, Vol. 70,  pp.2778–2787. External Links: [Link](http://proceedings.mlr.press/v70/pathak17a.html)Cited by: [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px3.p1.1 "Agentic Exploration. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   J. Schmidhuber (2020)Generative adversarial networks are special cases of artificial curiosity (1990) and also closely related to predictability minimization (1991). Neural Networks 127,  pp.58–66. External Links: [Link](https://doi.org/10.1016/j.neunet.2020.04.008), [Document](https://dx.doi.org/10.1016/J.NEUNET.2020.04.008)Cited by: [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px3.p1.1 "Agentic Exploration. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   H. Trivedi, T. Khot, M. Hartmann, R. Manku, V. Dong, E. Li, S. Gupta, A. Sabharwal, and N. Balasubramanian (2024)AppWorld: A controllable world of apps and people for benchmarking interactive coding agents. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2024, Bangkok, Thailand, August 11-16, 2024, L. Ku, A. Martins, and V. Srikumar (Eds.),  pp.16022–16076. External Links: [Link](https://doi.org/10.18653/v1/2024.acl-long.850), [Document](https://dx.doi.org/10.18653/V1/2024.ACL-LONG.850)Cited by: [§1](https://arxiv.org/html/2604.17609v1#S1.p4.1 "1 Introduction ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px1.p1.1 "Benchmarks. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px2.p1.1 "Benchmarks. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   X. Wang, B. Li, Y. Song, F. F. Xu, X. Tang, M. Zhuge, J. Pan, Y. Song, B. Li, J. Singh, H. H. Tran, F. Li, R. Ma, M. Zheng, B. Qian, Y. Shao, N. Muennighoff, Y. Zhang, B. Hui, J. Lin, and et al. (2025)OpenHands: an open platform for AI software developers as generalist agents. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025, External Links: [Link](https://openreview.net/forum?id=OJd3ayDDoF)Cited by: [§1](https://arxiv.org/html/2604.17609v1#S1.p1.1 "1 Introduction ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px2.p2.1 "Agent implementation. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px1.p1.1 "LLM-Based Agents. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px3.p1.1 "Agentic Exploration. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   C. S. Xia, Y. Deng, S. Dunn, and L. Zhang (2025)Demystifying llm-based software engineering agents. Proc. ACM Softw. Eng.2 (FSE),  pp.801–824. External Links: [Link](https://doi.org/10.1145/3715754), [Document](https://dx.doi.org/10.1145/3715754)Cited by: [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px3.p1.1 "Agentic Exploration. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press (2024)SWE-agent: agent-computer interfaces enable automated software engineering. In Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December 10 - 15, 2024, A. Globersons, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and C. Zhang (Eds.), External Links: [Link](http://papers.nips.cc/paper%5C_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html)Cited by: [§B.4](https://arxiv.org/html/2604.17609v1#A2.SS4.p1.2 "B.4 Prompt variations ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [Figure 12](https://arxiv.org/html/2604.17609v1#A5.F12 "In Appendix E Agent Implementations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [Appendix E](https://arxiv.org/html/2604.17609v1#A5.p1.1 "Appendix E Agent Implementations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§1](https://arxiv.org/html/2604.17609v1#S1.p1.1 "1 Introduction ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§1](https://arxiv.org/html/2604.17609v1#S1.p4.1 "1 Introduction ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px2.p1.1 "Agent implementation. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px2.p2.1 "Agent implementation. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px1.p1.1 "LLM-Based Agents. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px3.p1.1 "Agentic Exploration. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 
*   S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. R. Narasimhan, and Y. Cao (2023)ReAct: synergizing reasoning and acting in language models. In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023, External Links: [Link](https://openreview.net/forum?id=WE%5C_vluYUL-X)Cited by: [§3](https://arxiv.org/html/2604.17609v1#S3.SS0.SSS0.Px2.p1.1 "Agent implementation. ‣ 3 Experiments ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), [§5](https://arxiv.org/html/2604.17609v1#S5.SS0.SSS0.Px1.p1.1 "LLM-Based Agents. ‣ 5 Related work ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"). 

## Appendix A Ruling Out Alternative Explanations

In addition to the hypothesis investigated in the main part of the paper, one could also suspect that the models lack the capability to comprehend the injected solution or suspect it is an adversarial trap. To rule out these hypotheses, we use an LLM-as-a-judge to show that the models do not see the solution as a trap, but instead simply ignore it. Additionally, we conduct an oracle case study on Terminal-Bench to show that the models do have the general capability to use the information; they just lack the innate trigger to investigate it.

### A.1 LLM-as-a-Judge analysis: agents ignore rather than reject discovered solutions

An alternative explanation for low interaction rates could be that agents recognize the injected solution but deliberately avoid it, e.g., because they suspect it is adversarial or a trap. That the interaction rates increase with reasoning budget points against this theory, as deliberate avoidance would not lead to more interaction with more reasoning. To directly test this, we use an LLM-as-a-judge to classify agent behavior in attempts where the solution was discovered but not interacted with.

##### Method.

For each such attempt, we identify all turns in which the solution was discovered, i.e., not only the first occurrence, as agents may re-encounter the solution file or API in later terminal outputs (e.g., by running ls again). For each discovery turn, we add in the prompt in which turn the solution appeared, followed by the agent’s reasoning and actions for the three subsequent turns. This keeps the judge’s input focused on the agent’s immediate reaction to each discovery event while remaining concise enough for reliable classification. The judge classifies each trajectory into exactly one of five categories:

1.   1.
No acknowledgment. The agent’s reasoning never mentions the solution after seeing it. The agent proceeds as if the observation did not occur.

2.   2.
Acknowledgment without investigation. The agent’s reasoning mentions the solution (e.g., the word “solution” appears) but makes no plan to interact with it.

3.   3.
Deliberate rejection (suspicion/trap). The agent explicitly reasons that the solution might be untrustworthy or adversarial and decides to avoid it.

4.   4.
Deliberate rejection (preference for own approach). The agent acknowledges the solution but explicitly states it prefers to solve the task independently.

5.   5.
Interaction planned but not executed. The agent forms an intent to investigate the solution but never follows through.

Categories 1–2 represent passive non-interaction; category 3 is the active rejection that would undermine our environmental curiosity interpretation. We use GLM-4.7 as the judge with a structured tool call containing a classification field and an evidence field for a supporting quote from the trace. We use separate system prompts for Terminal-Bench/SWE-Bench (solution _files_) and AppWorld (solution _API command_) so the judge receives benchmark-appropriate context. We manually verified 50 random classifications and found the extracted evidence to be correct in all cases. The full judge prompts are provided in Figure[6](https://arxiv.org/html/2604.17609v1#A1.F6 "Figure 6 ‣ Results. ‣ A.1 LLM-as-a-Judge analysis: agents ignore rather than reject discovered solutions ‣ Appendix A Ruling Out Alternative Explanations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity").

##### Results.

Table[4](https://arxiv.org/html/2604.17609v1#A1.T4 "Table 4 ‣ Results. ‣ A.1 LLM-as-a-Judge analysis: agents ignore rather than reject discovered solutions ‣ Appendix A Ruling Out Alternative Explanations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") shows the classification results for gpt-oss-120b and GLM-4.7 across all benchmarks. Deliberate rejection due to suspicion (category 3) occurs in _zero_ cases across all models and benchmarks. The overwhelming majority of non-interactions fall into categories 1 and 2: agents either never mention the solution in their reasoning or briefly acknowledge it before continuing with their original plan (Figure[7](https://arxiv.org/html/2604.17609v1#A1.F7 "Figure 7 ‣ Results. ‣ A.1 LLM-as-a-Judge analysis: agents ignore rather than reject discovered solutions ‣ Appendix A Ruling Out Alternative Explanations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")). On SWE-Bench, no-acknowledgment rates exceed 96% for both models, indicating that agents process the terminal output containing the solution without it entering their reasoning at all. Category 5 is rare (\leq 3.1%), suggesting that the deficit is not in forming intent but in noticing relevance in the first place. These results confirm that agents do not perceive the solution as a trap; they simply do not register it as relevant.

Table 4: LLM-as-a-judge classification of agent behavior on attempts where the solution was discovered but not interacted with. Deliberate rejection due to suspicion (category 3) occurs in zero cases across all models and benchmarks.

Figure 6: LLM-as-a-judge prompt setup. The Terminal-Bench/SWE-Bench variant replaces “solution API command” with “solution file” and adjusts the context to describe solution.sh in the working directory.

Figure 7: Example LLM-as-a-judge classification on AppWorld (gpt-oss-120b). The agent enumerates solution among available APIs but proceeds without investigating it.

### A.2 Case study: agents can use solutions

The previous section rules out that agents deliberately reject discovered solutions. A second alternative explanation is that agents lack the _capability_ to use the injected information even if they noticed it. To test this, we compare the standard solution-injected baseline against four oracle interventions that artificially supply the missing trigger at different stages of the agent’s trajectory. All interventions use oracle information not available to the agent in the standard setup.

1.   1.
Baseline: The standard solution-injected setup from the main paper. solution.sh is present in the working directory.

2.   2.
Injected user prompt to reflect at discovery: On first discovery of solution.sh, we inject a user message asking the agent to reflect on whether any of its observations could be relevant to the task. Evaluated on Terminal-Bench w/ solution.

3.   3.
Solution content in first thought: The complete solution is injected directly into the agent’s first internal reasoning step, simulating a scenario where the agent autonomously formulated the perfect plan. Evaluated on unmodified Terminal-Bench (no solution.sh in the environment).

4.   4.
Solution content in task prompt: The complete solution is provided in the user task prompt. Evaluated on unmodified Terminal-Bench (no solution.sh in the environment).

5.   5.
Instructions to execute solution file: The task prompt instructs the agent to look for solution.sh in its working directory and execute it. Evaluated on Terminal-Bench w/ solution.

Table[5](https://arxiv.org/html/2604.17609v1#A1.T5 "Table 5 ‣ A.2 Case study: agents can use solutions ‣ Appendix A Ruling Out Alternative Explanations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") shows the results for gpt-oss-120b with high reasoning. Pass@1 increases monotonically with more explicit instructions, from 55.88 at baseline to 81.67 when the agent is explicitly told to execute the solution file. Simply prompting the agent to reflect at the moment of discovery raises interaction@1 from 37.12 to 53.33 and pass@1 from 55.88 to 60.00, confirming that a generic nudge to attend to observations is sufficient to improve environmental curiosity. When the solution content is provided directly (conditions 3–4), agents successfully incorporate it, reaching 61.67 and 76.25 pass@1 respectively. This demonstrates that the capability to use the information is not the bottleneck: agents can follow injected solutions when prompted, i.e., deviate from the original user instructions, but the spontaneous trigger to investigate relevant observations is absent.

Table 5: Oracle interventions on Terminal-Bench using gpt-oss-120b (high reasoning). Conditions 2–5 use oracle information not available in the standard setup. Pass@1 increases monotonically as the solution is made more explicit, confirming that agents can use injected solutions but lack the spontaneous trigger to investigate them. Interaction is only measurable for conditions where solution.sh is present in the environment (1, 2, 5).

### A.3 Additional factors: reasoning history and temperature

We test two additional factors that could plausibly influence environmental curiosity: whether the agent’s reasoning history is kept across turns, and sampling temperature.

Retaining or discarding reasoning history has no meaningful effect on task performance (pass@1: 56.25\% with history vs. 55.42\% without) but slightly increases interaction@1 (40.41\% without vs. 35.83\% with) for gpt-oss-120b on Terminal-Bench w/ solution.

Sampling temperature also has negligible effect. Figure[8](https://arxiv.org/html/2604.17609v1#A1.F8 "Figure 8 ‣ A.3 Additional factors: reasoning history and temperature ‣ Appendix A Ruling Out Alternative Explanations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") shows interaction@k for gpt-oss-120b (high reasoning) on Terminal-Bench across five temperatures (0, 0.25, 0.5, 0.75, 1.0). Interaction rates remain stable across the full range, indicating that the lack of environmental curiosity is not a consequence of low sampling diversity.

![Image 7: Refer to caption](https://arxiv.org/html/2604.17609v1/x7.png)

Figure 8: Effect of sampling temperature on interaction@k for gpt-oss-120b (high reasoning) on Terminal-Bench w/ solution. Temperature has negligible effect on environmental curiosity.

## Appendix B Solution injection

### B.1 Expanded results

Tables[6](https://arxiv.org/html/2604.17609v1#A2.T6 "Table 6 ‣ B.1 Expanded results ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"),[7](https://arxiv.org/html/2604.17609v1#A2.T7 "Table 7 ‣ B.1 Expanded results ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"), and[8](https://arxiv.org/html/2604.17609v1#A2.T8 "Table 8 ‣ B.1 Expanded results ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") report complete results for all models evaluated on Terminal-Bench, AppWorld (dev split), and SWE-Bench Verified, respectively. These include gpt-oss-120b at three reasoning budgets, GLM-4.5, GLM-4.7, and all command-a-reasoning fine-tuned variants with per-seed breakdowns. Our selected models span a wide range of architectures and scales: gpt-oss-120b is a mixture-of-experts model with 117B total / 5.1B active parameters, GLM-4.5 and GLM-4.7 are mixture-of-experts with 355B total / 32B active parameters, and command-a-reasoning is a 111B dense model. Unless otherwise noted, all evaluations use the Terminus scaffold with bash as the only tool. The discovery-interaction gap reported in the main paper is consistent across all models and configurations.

Table 6: Complete evaluation results on Terminal-Bench. All evaluations are conducted using Terminus as the agent, with a bash as the only tool. Where multiple seeds were run, individual seed results are shown followed by the average across seeds. 

Table 7: Complete evaluation results on AppWorld. All evaluations are conducted using Terminus as the agent, with bash as the only tool. Where multiple seeds were run, individual seed results are shown followed by the average across seeds.

Table 8: Complete evaluation results on SWE-Bench Verified. Unless otherwise specified, all evaluations are conducted using Terminus as the agent with bash only.

### B.2 Effect of file name

A potential confound is that agents avoid the injected solution because of the specific file name. To rule this out, we evaluate solution injection with different file names on both SWE-Bench Verified and Terminal-Bench. Table[9](https://arxiv.org/html/2604.17609v1#A2.T9 "Table 9 ‣ B.2 Effect of file name ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") shows that interaction rates are stable across file names within each benchmark, including highly explicit names such as SOLUTION_TO_THIS_SPECIFIC_TASK_READ_THIS_FIRST.md and familiar names such as README.md that agents routinely open during normal exploration. We see that the discovery-interaction gap is not an artifact of the injection format.

Table 9: Effect of injection file name on discovery and interaction rates. SWE-Bench Verified evaluated with gpt-oss-120b (high reasoning) using SWE-agent with bash + str_replace_editor; Terminal-Bench evaluated with gpt-oss-120b (high reasoning) using Terminus with bash-only. Interaction rates are stable across file names within each benchmark.

### B.3 Solution injection difficulty levels

The solution injection setup used in the main paper places the solution as a single executable file in the agent’s working directory. This is deliberately trivial: if agents cannot leverage a solution at this difficulty, they are unlikely to integrate subtler environmental signals. To provide a framework for measuring environmental curiosity as models improve, we define five difficulty levels with increasing requirements for exploration and multi-step reasoning. These levels apply to benchmarks utilizing the file system, i.e., Terminal-Bench and SWE-Bench.

1.   1.
Level 1: Solution added as an executable solution.sh in the working directory.

2.   2.
Level 2: Solution transformed into a README.md where steps are embedded in function blocks with LLM-generated comments explaining each action.

3.   3.
Level 3: Solution split across two files. The first README.md states that information is missing and is present in another file, but does not link to it. The second file must be discovered at ./notes/README.md.

4.   4.
Level 4:README.md is encrypted. A separate HINT.md provides a decryption tutorial and states that README.md contains the task solution.

5.   5.
Level 5: 50 incorrect solution variants are placed in ./notes/, generated by instructing an LLM to modify one or two instructions to change semantic behavior. HINT.md provides the checksum of the correct file.

Table[10](https://arxiv.org/html/2604.17609v1#A2.T10 "Table 10 ‣ B.3 Solution injection difficulty levels ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") shows results for gpt-oss-120b (high reasoning) on Terminal-Bench. Interaction rates are stable across levels 1–3 (37–38\%), indicating that reformatting the solution does not meaningfully change agent behavior. At levels 4 and 5, where leveraging the solution requires multi-step reasoning (decryption or checksum verification), interaction rates drop further (\sim 20–25%). Since current agents already ignore solutions at level 1, we focus on this trivial case throughout the main paper. The higher difficulty levels provide a framework for evaluating environmental curiosity as models improve.

pass@1 interaction@1
Original Terminal-Bench (no injection)44.50–
Level 1: solution.sh 55.88 37.12
Level 2: README.md with comments 51.67 37.50
Level 3: Split across two files 50.83 38.33
Level 4: Encrypted + hint 37.92 19.59
Level 5: 50 variants + checksum 53.75 24.58

Table 10: Solution injection difficulty levels on Terminal-Bench using gpt-oss-120b (high reasoning) with Terminus (bash-only). Levels 1–3 show stable interaction rates; levels 4–5 add multi-step barriers that further reduce interaction.

### B.4 Prompt variations

We evaluate how prompting affects environmental curiosity and task performance. Table[11](https://arxiv.org/html/2604.17609v1#A2.T11 "Table 11 ‣ B.4.1 Prompt variations on Terminal-Bench ‣ B.4 Prompt variations ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") shows that adding an instruction to explore the environment before acting improves pass@1 on both the original and solution-injected benchmarks across all three benchmarks, with an average improvement of +2.57 on the original and +2.96 on the solution-injected variants. The prompts we used for all evaluations with the Terminus agent are in Figure[10](https://arxiv.org/html/2604.17609v1#A5.F10 "Figure 10 ‣ Appendix E Agent Implementations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") for terminal bench, Figure[11](https://arxiv.org/html/2604.17609v1#A5.F11 "Figure 11 ‣ Appendix E Agent Implementations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") for AppWorld and Figure[12](https://arxiv.org/html/2604.17609v1#A5.F12 "Figure 12 ‣ Appendix E Agent Implementations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")) for SWE-Bench. The SWE-Bench prompt closely follows the SWE-agent prompt from Yang et al. ([2024](https://arxiv.org/html/2604.17609v1#bib.bib10 "SWE-agent: agent-computer interfaces enable automated software engineering")), adapted to our scaffold’s terminal_use interface (see Appendix[E](https://arxiv.org/html/2604.17609v1#A5 "Appendix E Agent Implementations ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity") for scaffold differences).

#### B.4.1 Prompt variations on Terminal-Bench

On Terminal-Bench, we further evaluate prompts with increasingly directive instructions for environmental interaction (Table[12](https://arxiv.org/html/2604.17609v1#A2.T12 "Table 12 ‣ B.4.1 Prompt variations on Terminal-Bench ‣ B.4 Prompt variations ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity"); full prompts in Figure[9](https://arxiv.org/html/2604.17609v1#A2.F9 "Figure 9 ‣ B.4.1 Prompt variations on Terminal-Bench ‣ B.4 Prompt variations ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")). Adding a general curiosity instruction or step-wise reflection yields modest gains over the base exploration prompt. The most effective prompt explicitly instructs the agent to investigate all discovered files before proceeding, achieving the highest pass@1 on both the original (44.50) and solution-injected (55.88) Terminal-Bench as well as the highest interaction rates. Notably, the prompt that maximizes environmental curiosity also achieves the best task performance on the original, unmodified benchmark. We use “base prompt + exploration + investigate all files” as the default prompt for all Terminal-Bench evaluations in the main paper.

Table 11: Pass@1 with and without an exploration instruction across all benchmarks, using gpt-oss-120b (high reasoning). Instructing the agent to explore improves performance on both the original and solution-injected variants. Terminal-Bench and AppWorld evaluated using Terminus; SWE-Bench evaluated using SWE-agent.

Table 12: Effect of increasingly directive prompts on Terminal-Bench using gpt-oss-120b (high reasoning), 10 attempts per task. The prompt that maximises interaction rates also achieves the highest pass@1 on the original benchmark.

Figure 9: Prompt variants evaluated on Terminal-Bench (Table[12](https://arxiv.org/html/2604.17609v1#A2.T12 "Table 12 ‣ B.4.1 Prompt variations on Terminal-Bench ‣ B.4 Prompt variations ‣ Appendix B Solution injection ‣ Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity")). Each variant is a complete prompt; {{base prompt}} denotes the shared base prompt that is identical across all conditions.

## Appendix C SFT Training Data Details

All fine-tuned models are trained from a variant of command-a-reasoning(Cohere et al., [2025](https://arxiv.org/html/2604.17609v1#bib.bib7 "Command a: an enterprise-ready large language model"); Cohere, [2025](https://arxiv.org/html/2604.17609v1#bib.bib6 "Command A reasoning: enterprise-grade control for AI agents")) that has been supervised fine-tuned for improved instruction following.

##### Rejection sampling.

For each training task instance, we generate five agent trajectories using gpt-oss-120b with high reasoning. Each trajectory is a complete multi-turn interaction between the agent and the environment, consisting of alternating reasoning, action, and observation turns. We retain only the shortest successful trajectory per task. This yields training data that is both correct and concise, avoiding unnecessarily long solution paths. We use Terminus 1 as the agent to generate these trajectories.

##### Training details.

We train three models on different task distributions:

*   •
T-Bench-SFT: Trained on Terminal-Bench-like tasks sourced from an external vendor, covering a broad distribution of terminal-based tasks. 14,005 trainable turns 5 5 5 A trainable turn is a single assistant message (comprising reasoning and action) within a trajectory., trained for 2 epochs.

*   •
AppWorld-SFT: Trained on tasks from the AppWorld training split, covering API-based digital tasks. 15,841 trainable turns, trained for 2 epochs.

*   •
SWE-Bench-SFT: Trained on tasks from SWE-smith, covering code editing and software engineering tasks. 21,424 trainable turns, trained for 1.5 epochs.

We chose the number of epochs such that all models are trained on approximately 30k effective task-specific turns (turns \times epochs). To prevent overfitting to the task-specific data, we include a general-purpose tool-use SFT mixture as auxiliary data with a 1:1 mixing ratio in each training run. Training only on the general-purpose SFT mixture achieves 5.12 pass@1 on Terminal-Bench and 0.18 pass@1 on AppWorld. This near-zero baseline confirms that the agentic capability and environmental curiosity observed in our fine-tuned variants is attributable to the task-specific training data.

## Appendix D AppWorld is a subset of Terminal-Bench

AppWorld tasks require an agent to discover, call, and reason over APIs across nine simulated day-to-day applications (e.g., Amazon, Spotify, Venmo) in a multi-turn fashion, spanning 457 endpoints in total. This task type is also present in terminal-bench but accounts for only a small slice of its distribution. Specifically, four of T-Bench v1’s 80 tasks exercise the same core loop of API endpoint discovery, reasoning and interaction:

*   •
simple-sheets-put asks the agent to query a spreadsheet API to extract structured data, and then issue the correct sequence of API calls to create a spreadsheet, add a named sheet, populate cells with tabular data, and compute a derived column.

*   •
simple-web-scraper asks the agent to scrape structured data from a web service, extract fields from HTML, aggregate the results into a CSV, and produce a summary report.

*   •
create-bucket involves configuring an S3 bucket via CLI-based API calls

*   •
security-vulhub-minio requires the agent to interact with a running MinIO service via its API to extract its credentials.

These four tasks, i.e. 5% of T-Bench v1 tasks, share AppWorld’s defining pattern but represent only a narrow slice of terminal-bench’s broader distribution. Per-task complexity is comparable across the two benchmarks: on successful trajectories, gpt-oss (120b) with high reasoning averages 26.2 turns on terminal-bench and 29.6 on AppWorld. For reference, SWE-Bench requires 62.8 turns on average, reflecting substantially different per-task complexity. The combination of terminal-bench containing AppWorld-style tasks and both benchmarks exhibiting similar per-task complexity supports our view of AppWorld as a narrow subset of the T-Bench v1 task distribution.

## Appendix E Agent Implementations

We evaluate Terminus 1(Merrill et al., [2026](https://arxiv.org/html/2604.17609v1#bib.bib13 "Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces")) and SWE-agent(Yang et al., [2024](https://arxiv.org/html/2604.17609v1#bib.bib10 "SWE-agent: agent-computer interfaces enable automated software engineering")). These agents differ in many aspects. The most important factors are prompts, how large outputs are truncated, and how commands are executed with SWE-agent using blocking commands while Terminus allows the model to specify timeouts and interrupt long-running processes. Among the many differences in implementation is also how tool results are formatted, i.e., how the terminal history is presented. We use the default Terminus and SWE-agent implementations but adapt them to use native function-calling APIs over raw prompting to remove the potential variable of out-of-distribution function calling interfaces (introduced in proprietary scaffolds) to instead rely on a provider’s native tool-use interface.

Terminal-Bench System Prompt

Figure 10: The Terminal-Bench system prompt provided to the Terminus agent during evaluation of the Terminal-Bench benchmark.

AppWorld System Prompt

Figure 11: The AppWorld system prompt provided to the Terminus agent during evaluation of the AppWorld benchmark.

SWE-Bench System Prompt

Figure 12: The SWE-Bench system prompt provided to the Terminus agent during evaluation of the SWE-Bench benchmark. This prompt closely follows the SWE-agent prompt from Yang et al. ([2024](https://arxiv.org/html/2604.17609v1#bib.bib10 "SWE-agent: agent-computer interfaces enable automated software engineering")), adapted to our scaffold’s terminal_use interface.

---
url: https://arxiv.org/html/2602.11988v1
title: "Evaluating AGENTS.md:\nAre Repository-Level Context Files Helpful for Coding Agents?"
captured_at: "2026-03-09T03:46:24.545Z"
---

# Evaluating AGENTS.md:
Are Repository-Level Context Files Helpful for Coding Agents?

###### Abstract

A widespread practice in software development is to tailor coding agents to repositories using context files, such as AGENTS.md, by either manually or automatically generating them. Although this practice is strongly encouraged by agent developers, there is currently no rigorous investigation into whether such context files are actually effective for real-world tasks. In this work, we study this question and evaluate coding agents’ task completion performance in two complementary settings: established SWE-bench tasks from popular repositories, with LLM-generated context files following agent-developer recommendations, and a novel collection of issues from repositories containing developer-committed context files.

Across multiple coding agents and LLMs, we find that context files tend to *reduce* task success rates compared to providing no repository context, while also *increasing inference cost* by over 20%. Behaviorally, both LLM-generated and developer-provided context files encourage broader exploration (e.g., more thorough testing and file traversal), and coding agents tend to respect their instructions. Ultimately, we conclude that unnecessary requirements from context files make tasks harder, and human-written context files should describe only minimal requirements.

Machine Learning, ICML

\\colorlet

my-bluemy-full-blue!30 \\colorletmy-orangemy-full-orange!30 \\colorletmy-greenmy-full-green!90 \\colorletmy-redmy-full-red!90 \\colorletmy-purplemy-full-purple!30 \\colorletmyredLightPink1 \\colorletmyblueSteelBlue2 \\colorletmyorangeDarkOrange1 \\algrenewcommand\\alglinenumber\[1\]#1 

## 1 Introduction

Coding agents are being rapidly adopted across the software engineering industry (Sarkar, [2025](https://arxiv.org/html/2602.11988v1#bib.bib28)), and providing context files like AGENTS.md, a README specifically targeting agents, has become common practice. With various industry leaders (AGENTS.md, [2025](https://arxiv.org/html/2602.11988v1#bib.bib1); Anthropic, [2025b](https://arxiv.org/html/2602.11988v1#bib.bib4)) recommending this approach to adapt their agents to specific repositories, context files are now supported by most popular agent frameworks, and included in over 60’000 open-source repositories at the time of writing, as reported by AGENTS.md ([2025](https://arxiv.org/html/2602.11988v1#bib.bib1)).

These context files typically contain a repository overview and information on relevant developer tooling, aiming to help coding agents to navigate a given repository more efficiently, run build and test commands correctly, adhere to style guides and design patterns, and ultimately to solve tasks to the user’s satisfaction more frequently. To date, despite their widespread adoption, the impact of context files on the coding agent’s ability to solve complex software engineering tasks has not been rigorously studied. This is due to two key challenges: i) because of their recent introduction, context files are not available for instances of prior benchmarks, and ii) popular, well-known repositories, typically used to create such benchmarks, are not representative of most codebases. As a result, a rigorous evaluation of the context files used in practice requires a new, complementary benchmark that contains only issues from less popular repositories with developer-committed context files.

![Refer to caption](https://arxiv.org/html/2602.11988v1/x1.png)

Figure 1: Overview of our evaluation pipeline. We begin with real-world repositories and tasks derived from past pull requests. For each repository state, we generate three settings: \\tiny{1}⃝ If a developer-provided context file exists, we include it in the repository. In \\tiny{2}⃝, we omit the context file. \\tiny{3}⃝ We use the coding agent’s recommended settings to generate the context file. Then we pass the repository and context file to the coding agent and instruct it to autonomously resolve the task. We finally analyze the trace for behavioral changes and apply the generated patch to check for task resolution success.

#### This work: Benchmarking context files’ impact on resolving GitHub issues

In this work, we investigate the effect of actively used context files on the resolution of real-world coding tasks. We evaluate agents both in popular and less-known repositories, and, importantly, with context files provided by repository developers. For this purpose, we construct a novel benchmark ([Figure˜1](https://arxiv.org/html/2602.11988v1#S1.F1 "In 1 Introduction ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), left), AGENTbench, comprising Python software engineering tasks, created specifically from real GitHub issues. The benchmark contains 138138 unique instances, covering both bug-fixing and feature addition tasks across 1212 recent and niche repositories, which all feature developer-written context files. AGENTbench complements SWE-bench Lite, which we leverage for the evaluation of automatically generated context files on popular repositories. We evaluate coding agents in three settings ([Figure˜1](https://arxiv.org/html/2602.11988v1#S1.F1 "In 1 Introduction ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), middle): without any context file, with context files automatically generated using agent-developer recommendations, and with the developer-provided context file. Our code to generate AGENTbench instances and evaluate coding agents is available [here](https://github.com/eth-sri/agentbench).

Surprisingly, we observe that *developer-provided files only marginally improve performance* compared to omitting them entirely (an increase of 4% on average), while *LLM-generated context files have a small negative effect* on agent performance (a decrease of 3% on average). These observations are robust across different LLMs and prompts used to generate the context files. In a more detailed analysis ([Figure˜1](https://arxiv.org/html/2602.11988v1#S1.F1 "In 1 Introduction ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), right), we observe that context files lead to increased exploration, testing, and reasoning by coding agents, and, as a result, increase costs by over 20%. We therefore suggest omitting LLM-generated context files for the time being, contrary to agent developers’ recommendations, and including only minimal requirements (e.g., specific tooling to use with this repository). We hope our evaluation framework will aid agent and model developers to improve the helpfulness of LLM-generated context files.

#### Key contributions

Our key contributions are:

1.  1.

    AGENTbench, a new curated benchmark for the impact of actively used context files on agents’ ability to solve real-world software engineering tasks.

2.  2.

    An extensive evaluation of different coding agents and underlying models on AGENTbench and SWE-bench Lite, showing that LLM-generated context files tend to decrease agent performance, across models or prompts used to generate them, while developer-written context files tend to slightly improve it.

3.  3.

    A detailed investigation of agent traces, showing that context files lead to more thorough testing and exploration by coding agents.

## 2 Background and Related Work

#### Coding agents

Coding agents are LLM-based systems designed for autonomous resolution of coding tasks (Yang et al., [2024](https://arxiv.org/html/2602.11988v1#bib.bib37)). Typically, they consist of a harness that allows an LLM to interact with its environment using specialized tools for, e.g., executing bash commands, conducting web searches, or reading, creating, or modifying files (Wang et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib36); Yang et al., [2024](https://arxiv.org/html/2602.11988v1#bib.bib37)).

Their impressive performance on repository-level coding tasks like SWE-bench (Jimenez et al., [2024](https://arxiv.org/html/2602.11988v1#bib.bib15)) led to rapid adoption in the software engineering community (Sarkar, [2025](https://arxiv.org/html/2602.11988v1#bib.bib28)) and the development of new agents by specialized companies (Aider, [2024](https://arxiv.org/html/2602.11988v1#bib.bib2); Wang et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib36)) and model providers (OpenAI, [2025c](https://arxiv.org/html/2602.11988v1#bib.bib25); Google, [2025](https://arxiv.org/html/2602.11988v1#bib.bib13); QwenLM, [2025](https://arxiv.org/html/2602.11988v1#bib.bib27); Anthropic, [2025a](https://arxiv.org/html/2602.11988v1#bib.bib3)). Model providers now train their LLMs to use the tools exposed by their harnesses (QwenLM, [2025](https://arxiv.org/html/2602.11988v1#bib.bib27)), which can substantially improve coding ability relative to simpler harnesses (Lieret et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib19)). Accordingly, in [Section˜4](https://arxiv.org/html/2602.11988v1#S4 "4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), we evaluate each LLM only within its corresponding harness.

#### Context files

As coding agents were more broadly adopted, a common need arose to provide the agent with additional context about novel and little-known codebases (Boyina, [2025](https://arxiv.org/html/2602.11988v1#bib.bib7); Sewell, [2025](https://arxiv.org/html/2602.11988v1#bib.bib30)). To address this issue, model and agent developers recommend including *context files*, such as AGENTS.md or CLAUDE.md, with codebases (OpenAI, [2025a](https://arxiv.org/html/2602.11988v1#bib.bib23); Anthropic, [2025b](https://arxiv.org/html/2602.11988v1#bib.bib4)). Many agent harnesses provide built-in commands to initialize such context files automatically using the coding agent itself, e.g., by providing a dedicated /init command in the agent interface (OpenAI, [2025c](https://arxiv.org/html/2602.11988v1#bib.bib25); QwenLM, [2025](https://arxiv.org/html/2602.11988v1#bib.bib27); Anthropic, [2025a](https://arxiv.org/html/2602.11988v1#bib.bib3)). At the time of writing, AGENTS.md ([2025](https://arxiv.org/html/2602.11988v1#bib.bib1)) report that over 60’000 public GitHub repositories include a context file.

#### Evaluating context files

Prior work collected and categorized the content of context files (Chatlatanagulchai et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib9); Mohsenimofidi et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib20)), deriving mostly descriptive metrics about their content without investigating their effectiveness (Nigh, [2025](https://arxiv.org/html/2602.11988v1#bib.bib22)). While individual developers report anecdotal evidence of better alignment and solution capabilities when providing context files (Sewell, [2025](https://arxiv.org/html/2602.11988v1#bib.bib30); Sawers, [2025](https://arxiv.org/html/2602.11988v1#bib.bib29)), we are the first to investigate the impact of actively used context files on agent behavior and performance at scale.

#### Repository-level evaluation

Spearheaded by Jimenez et al. ([2024](https://arxiv.org/html/2602.11988v1#bib.bib15)), evaluating coding agents on the autonomous resolution of real-world repository-level tasks quickly became the gold standard for assessing their capabilities. While initial work focuses on issue resolution (Jimenez et al., [2024](https://arxiv.org/html/2602.11988v1#bib.bib15)), follow-up work proposed benchmarks on feature addition (Li et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib17); Du et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib12)), unit test generation (Mündler et al., [2024](https://arxiv.org/html/2602.11988v1#bib.bib21)), function generation (Liang et al., [2024](https://arxiv.org/html/2602.11988v1#bib.bib18)), code performance (He et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib14)), and security (Chen et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib10)). Our work evaluates whether autonomous issue resolution and feature addition capabilities improve with actively used context files.

Orthogonally, benchmarks have also been extended by mining more recent and more difficult problems (Badertdinov et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib6); Zhang et al., [2025a](https://arxiv.org/html/2602.11988v1#bib.bib38)), as well as instances focusing on end-user applications (Vergopoulos et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib34)). We follow their approaches to mining novel task instances to obtain a specialized set of tasks in repositories that feature context files.

## 3 AGENTbench

In this Section, we discuss the requirements for AGENTbench, a SWE-Bench\-like benchmark that targets the evaluation of developer-provided context files, its generation process, and its statistics.

### 3.1 Notation and Definitions

We first introduce the notation to describe codebases, their test suites, and changes to these codebases in the form of patches. Following the notation of Mündler et al. ([2024](https://arxiv.org/html/2602.11988v1#bib.bib21)), we denote a codebase, or repository RR after applying patch XX as R∘XR\\circ X. Several patches can be applied sequentially, i.e., R∘X∘YR\\circ X\\circ Y is the codebase RR after applying a first patch XX and then a second one YY.

A *test suite* 𝒯\\mathcal{T} is a collection of tests that is used to validate the functionality of code in the repository. Executing a test suite 𝒯\\mathcal{T} on repository state RR returns execR​(𝒯)∈{pass,fail}\\mathrm{exec}\_{R}(\\mathcal{T})\\in\\{\\textsc{pass},\\textsc{fail}\\} either indicating that all tests in the suite passed or that at least one test failed. An *issue* II is a task for autonomous completion by the coding agent, such as resolving a bug or implementing a requested feature. We denote quadruples of (I,R,𝒯,X∗)(I,R,\\mathcal{T},X^{\*}) as *instances*, where the coding agent is tasked with predicting a patch X^\\hat{X} given issue II and repository state RR such that execR∘X^​(𝒯)\=pass\\mathrm{exec}\_{R\\circ\\hat{X}}(\\mathcal{T})=\\textsc{pass}, and X∗X^{\*} is the golden patch for that instance. We define the *success rate* 𝒮\\mathcal{S} as the percentage of predicted patches X^i\\hat{X}\_{i} for instances (Ii,Ri,𝒯i,Xi∗)(I\_{i},R\_{i},\\mathcal{T}\_{i},X^{\*}\_{i}) where execRi∘X^i​(𝒯i)\=pass\\mathrm{exec}\_{R\_{i}\\circ\\hat{X}\_{i}}(\\mathcal{T}\_{i})=\\textsc{pass}.

### 3.2 Generation of AGENTbench Instances

To construct AGENTbench, we use a five-stage construction process summarized below. We defer all the prompts used for this process to [Appendix˜B](https://arxiv.org/html/2602.11988v1#A2 "Appendix B Prompts ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?").

#### Requirements

We aim to evaluate the impact of both automatically generated context files and developer-written context files on the success rate of coding agents on real-world tasks and codebases. The primary source for real-world codebases is open-source projects and their publicly tracked and documented changes, so-called pull requests (PRs). In order to obtain developer-written context files, we need to source PRs from projects that adopted context files. This is challenging, because context files have only been formalized in August 2025, and have not been frequently used before. Further, the adoption of context file is not uniform across the industry: even at the time of writing, many repositories do not include context files.

#### Finding repositories

We first use GitHub search to build a list of potential candidate repositories to extract instances from. Specifically, we select codebases that contain a context file such as AGENTS.md or CLAUDE.md at the root directory. Next, we filter down to those using Python as the main language and featuring a test suite. Finally, we filter for projects with many publicly documented changes, requiring at least 400400 PRs. This criterion allows us to select codebases from which we can extract at least 1010 instances after our rigorous post-processing.

#### Filtering pull requests

Given a repository, we filter PRs to retain those that are most likely to generate higher-quality instances using a combination of rule-based checks and an LLM agent. We only keep PRs that satisfy the following two criteria: they should reference at least one issue, and they should modify at least one Python file. Further, we filter for PRs that are assessed by the agent to introduce deterministic, testable behaviors that are suitable for SWE-bench Lite\-like regression tests. We notice that, because the use of context files is a recently emerging trend, most repositories containing context files are niche. These niche repositories have less strict rules regarding pull requests, and thus most PRs may not include specific tests. To enable building instances from these more niche repositories, we therefore do not require PRs to edit unit tests that validate the code changes, in contrast to SWE-bench Lite, which focused on large and popular repositories and requires PRs to contain unit tests.

#### Environment Set-Up

For every PR and corresponding repository state, we set up an execution environment such that its test suite can be run, using a coding agent. Specifically, we ask the agent to produce a small script that i) sets up the execution environment, ii) runs the test suite and iii) stores the results as a machine-readable dictionary at the root of the repository. We only keep PRs where the resulting dictionary contains at least one passing test, which corresponds to 87%87\\% of the filtered instances.

#### Task Descriptions

Many of the smaller repositories we used to source AGENTbench do not enforce strict requirements on the quality of PR and issue descriptions. As a result, many issues are too imprecise and underspecified to solve the task in a testable manner (e.g., in some cases, the PR body is empty). Further, some PRs implement new features, which would require detailed descriptions about expected behavior and interfaces. We therefore use a third LLM agent to produce a standardized and detailed task description II based on the PR description, associated issues if available, and the original patch X∗X^{\*}. This standardized task description is divided into 6 sections: description, steps to reproduce, expected behavior, observed behavior, specification, and additional information. Importantly, we ask the agent not to leak the solution in the generated task description, and to provide precise specifications. We randomly sampled and inspected 10% of the generated instances, and found that none of them leaked the solution.

#### Generating Unit Tests

As most collected PRs do not modify or add unit tests that we could use to check the correctness of any given implementation, we use an LLM agent to generate such unit tests. We provide the agent with the standardized task description II, the test files modified by the PR, if available, the original code changes X∗X^{\*} made by the PR, and the base state of the repository RR. We then ask it to generate tests that pass for any implementation that resolves the described task. We verify that the added tests fail on RR and pass on R∘X∗R\\circ X^{\*}. Finally, we manually improve tests that are over-specified (i.e., tests that check for implementation details not specified in the task description), resulting in newly generated tests 𝒯iX\\mathcal{T}\_{i}^{X}. We further determine all tests of the repository test suite 𝒯iR\\mathcal{T}\_{i}^{R} that pass on the patched code, i.e., the maximal set 𝒯iR⁣∗⊆𝒯iR\\mathcal{T}\_{i}^{R\*}\\subseteq\\mathcal{T}\_{i}^{R}, such that execRi∘Xi∗​(𝒯iR⁣∗)\=pass\\mathrm{exec}\_{R\_{i}\\circ X\_{i}^{\*}}(\\mathcal{T}\_{i}^{R\*})=\\textsc{pass}, and obtain the final test set 𝒯i\=𝒯iX⊎𝒯iR⁣∗\\mathcal{T}\_{i}=\\mathcal{T}^{X}\_{i}\\uplus\\mathcal{T}^{R\*}\_{i}. The resulting tests achieve an average coverage of 75% of the modified code (see [Table˜1](https://arxiv.org/html/2602.11988v1#S3.T1 "In Evaluation ‣ 3.2 Generation of AGENTbench Instances ‣ 3 AGENTbench ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?")).

#### Evaluation

We thus obtain AGENTbench instances ii, each consisting of a task description IiI\_{i}, a codebase RiR\_{i}, golden patch Xi∗X^{\*}\_{i}, and a set of tests 𝒯i\\mathcal{T}\_{i}. During evaluation, we first set up the environment before prompting the coding agent with the task description IiI\_{i}, retrieving the predicted patch X^i\\hat{X}\_{i}, and measuring execRi∘X^i​(𝒯i)\\mathrm{exec}\_{R\_{i}\\circ\\hat{X}\_{i}}(\\mathcal{T}\_{i}).

![Refer to caption](https://arxiv.org/html/2602.11988v1/x2.png)

Figure 2: Distribution of AGENTbench instances across 12 open-source GitHub repositories, each containing context files.

Table 1: Average, minimum, and maximum of key statistics of AGENTbench across the 138 instances. For context files, a section is the content between Markdown headers.

<table id="S3.T1.1.1"><tbody><tr id="S3.T1.1.1.2"><td id="S3.T1.1.1.2.1"></td><td id="S3.T1.1.1.2.2"></td><td id="S3.T1.1.1.2.3">Mean</td><td id="S3.T1.1.1.2.4">Min</td><td id="S3.T1.1.1.2.5">Max</td></tr><tr id="S3.T1.1.1.3"><td id="S3.T1.1.1.3.1"><span id="S3.T1.1.1.3.1.1">PR body</span></td><td id="S3.T1.1.1.3.2"># words</td><td id="S3.T1.1.1.3.3">415.3</td><td id="S3.T1.1.1.3.4">5</td><td id="S3.T1.1.1.3.5">4961</td></tr><tr id="S3.T1.1.1.1"><td id="S3.T1.1.1.1.1"><span id="S3.T1.1.1.1.1.1">Issue <math id="S3.T1.1.1.1.1.1.m1" alttext="I" display="inline" intent=":literal"><semantics><mi>I</mi><annotation encoding="application/x-tex">I</annotation></semantics></math></span></td><td id="S3.T1.1.1.1.2"># words</td><td id="S3.T1.1.1.1.3">211.6</td><td id="S3.T1.1.1.1.4">96</td><td id="S3.T1.1.1.1.5">500</td></tr><tr id="S3.T1.1.1.4"><td id="S3.T1.1.1.4.1"><span id="S3.T1.1.1.4.1.1">Codebase</span></td><td id="S3.T1.1.1.4.2"># files</td><td id="S3.T1.1.1.4.3">3337</td><td id="S3.T1.1.1.4.4">151</td><td id="S3.T1.1.1.4.5">26602</td></tr><tr id="S3.T1.1.1.5"><td id="S3.T1.1.1.5.1" rowspan="2"><span id="S3.T1.1.1.5.1.1">PR patch</span></td><td id="S3.T1.1.1.5.2"># lines edited</td><td id="S3.T1.1.1.5.3">118.9</td><td id="S3.T1.1.1.5.4">12</td><td id="S3.T1.1.1.5.5">1973</td></tr><tr id="S3.T1.1.1.6"><td id="S3.T1.1.1.6.1"># files edited</td><td id="S3.T1.1.1.6.2">2.5</td><td id="S3.T1.1.1.6.3">1</td><td id="S3.T1.1.1.6.4">23</td></tr><tr id="S3.T1.1.1.7"><td id="S3.T1.1.1.7.1"><span id="S3.T1.1.1.7.1.1">Test</span></td><td id="S3.T1.1.1.7.2">Coverage</td><td id="S3.T1.1.1.7.3">75%</td><td id="S3.T1.1.1.7.4">2.5%</td><td id="S3.T1.1.1.7.5">100%</td></tr><tr id="S3.T1.1.1.8"><td id="S3.T1.1.1.8.1" rowspan="2"><span id="S3.T1.1.1.8.1.1">Context file</span></td><td id="S3.T1.1.1.8.2"># words</td><td id="S3.T1.1.1.8.3">641.0</td><td id="S3.T1.1.1.8.4">24</td><td id="S3.T1.1.1.8.5">2003</td></tr><tr id="S3.T1.1.1.9"><td id="S3.T1.1.1.9.1"># sections</td><td id="S3.T1.1.1.9.2">9.7</td><td id="S3.T1.1.1.9.3">1</td><td id="S3.T1.1.1.9.4">29</td></tr></tbody></table>

#### Overview of AGENTbench

Using this process, we obtained 138 instances from a total of 5694 PRs from 12 repositories that meet our criteria, using GPT-5.2 with Codex as the agent. We visualize the distribution over repositories in [Figure˜2](https://arxiv.org/html/2602.11988v1#S3.F2 "In Evaluation ‣ 3.2 Generation of AGENTbench Instances ‣ 3 AGENTbench ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?") and show key statistics of AGENTbench in [Table˜1](https://arxiv.org/html/2602.11988v1#S3.T1 "In Evaluation ‣ 3.2 Generation of AGENTbench Instances ‣ 3 AGENTbench ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"). In comparison to SWE-bench Lite, our dataset is both more evenly distributed over repositories and has otherwise similar statistics.

## 4 Experimental Evaluation

In this Section, we investigate what effect context files have on the behavior of coding agents and how strong this effect is. To this end, we conduct an extensive evaluation of various coding agents on SWE-bench Lite and AGENTbench, considering both automatically generated and developer-provided context files.

![Refer to caption](https://arxiv.org/html/2602.11988v1/x3.png)

![Refer to caption](https://arxiv.org/html/2602.11988v1/x4.png)

Figure 3: Resolution rate for 4 different models, without context files, with LLM-generated context files, and with developer-written context files, on SWE-bench Lite (left) and AGENTbench (right).

### 4.1 Experimental Setup

We describe the experimental setup below, deferring further details to [Section˜A.1](https://arxiv.org/html/2602.11988v1#A1.SS1 "A.1 Additional Experimental Details ‣ Appendix A Experimental Details ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?").

#### Coding Agents

We consider four coding agents, paired with suitable models: Claude Code (Anthropic, [2025a](https://arxiv.org/html/2602.11988v1#bib.bib3)) with Sonnet-4.5 (Anthropic, [2025](https://arxiv.org/html/2602.11988v1#bib.bib5)), Codex (OpenAI, [2025c](https://arxiv.org/html/2602.11988v1#bib.bib25)) with GPT-5.2 and GPT-5.1 mini (Singh et al., [2026](https://arxiv.org/html/2602.11988v1#bib.bib31)), and Qwen Code (QwenLM, [2025](https://arxiv.org/html/2602.11988v1#bib.bib27)) with Qwen3-30b-coder (Team, [2025](https://arxiv.org/html/2602.11988v1#bib.bib33)). For Claude Code, we use the default settings and set the temperature of Sonnet-4.5 to 0. Similarly, for Codex, we also use the default settings and set the temperature of GPT-5.2 and GPT-5.1 mini to 0. For Qwen Code, we enable chat compression upon reaching 6060% of the total context limit (set to 256256K tokens), restrict shell outputs to 20002000 tokens, and set the temperature of Qwen3-30b-coder to 0.70.7 with top-pp sampling at 0.80.8. We deploy Qwen3-30b-coder locally using vLLM (Kwon et al., [2023](https://arxiv.org/html/2602.11988v1#bib.bib16)). We sample completions for each agent once. For all agents, the context file is fed into their context, either by writing it to AGENTS.md for Codex and Qwen Code, or to CLAUDE.md for Claude Code.

#### Datasets

We use SWE-bench Lite (Jimenez et al., [2024](https://arxiv.org/html/2602.11988v1#bib.bib15)), which consists of 300 tasks sourced from GitHub issues across 11 popular Python repositories, none containing developer-written context files, and our novel AGENTbench, consisting of 138 instances from 12 repositories, all containing developer-provided context files (see [Section˜3](https://arxiv.org/html/2602.11988v1#S3 "3 AGENTbench ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?")).

#### Settings

We consider three context file settings:

1.  None: No context files are available, i.e., we remove developer-provided files for AGENTbench.

2.  LLM: An LLM-generated context file is available. We use the recommended initialization command and model for each agent individually to generate the context file using the pre-patch repository state RR.

3.  Human: A developer-provided context file is available. We use the context file of the pre-patch repository state RR. Only available for AGENTbench.

#### Metrics

The main metric for agent performance is success rate ([Section˜3.1](https://arxiv.org/html/2602.11988v1#S3.SS1 "3.1 Notation and Definitions ‣ 3 AGENTbench ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?")), i.e., the portion of instances for which the agent produces a patch that leads to all tests passing. We additionally consider the number of *steps* the agent requires to complete a task. Each step is one interaction with the environment, e.g., calling a shell tool or modifying a file. Finally, we report the total *cost* of LLM inference required to complete a task. For Qwen3-30b-coder, we estimate the cost from the average OpenRouter API price.

### 4.2 Main Results

![Refer to caption](https://arxiv.org/html/2602.11988v1/x5.png)

![Refer to caption](https://arxiv.org/html/2602.11988v1/x6.png)

Figure 4: Number of steps before the first interaction between the agent and a file included in the PR patch (lower is better) is generally lower without context files than with LLM-generated context files or with developer-written context files (Human) on SWE-bench Lite (left) and AGENTbench (right).

Table 2: The average number of steps (lower is better) and execution cost (in USD — lower is better) per SWE-bench Lite and AGENTbench instance without context files (None), with LLM-generated context files (LLM), and with developer-written context files (Hum). We bold the best setting.

<table id="S4.T2.9.1"><tbody><tr id="S4.T2.9.1.1"><td id="S4.T2.9.1.1.1"></td><td id="S4.T2.9.1.1.2" rowspan="2"><span id="S4.T2.9.1.1.2.1">Type</span></td><td id="S4.T2.9.1.1.3" colspan="2"><span id="S4.T2.9.1.1.3.1">Sonnet-4.5</span></td><td id="S4.T2.9.1.1.4" colspan="2"><span id="S4.T2.9.1.1.4.1">GPT-5.2</span></td><td id="S4.T2.9.1.1.5" colspan="2"><span id="S4.T2.9.1.1.5.1">GPT-5.1 M.</span></td><td id="S4.T2.9.1.1.6" colspan="2"><span id="S4.T2.9.1.1.6.1">Qwen3-30B</span></td></tr><tr id="S4.T2.9.1.2"><td id="S4.T2.9.1.2.1"></td><td id="S4.T2.9.1.2.2">Steps</td><td id="S4.T2.9.1.2.3">Cost</td><td id="S4.T2.9.1.2.4">Steps</td><td id="S4.T2.9.1.2.5">Cost</td><td id="S4.T2.9.1.2.6">Steps</td><td id="S4.T2.9.1.2.7">Cost</td><td id="S4.T2.9.1.2.8">Steps</td><td id="S4.T2.9.1.2.9">Cost</td></tr><tr id="S4.T2.9.1.3"><td id="S4.T2.9.1.3.1" rowspan="2"><span id="S4.T2.9.1.3.1.1"><span id="S4.T2.9.1.3.1.1.1"><span id="S4.T2.9.1.3.1.1.1.1"><span id="S4.T2.9.1.3.1.1.1.1.1">SWE-</span></span> <span id="S4.T2.9.1.3.1.1.1.2"><span id="S4.T2.9.1.3.1.1.1.2.1">Bench</span></span> <span id="S4.T2.9.1.3.1.1.1.3"><span id="S4.T2.9.1.3.1.1.1.3.1">Lite</span></span></span></span></td><td id="S4.T2.9.1.3.2"><span id="S4.T2.9.1.3.2.1">None</span></td><td id="S4.T2.9.1.3.3"><span id="S4.T2.9.1.3.3.1">54.4</span></td><td id="S4.T2.9.1.3.4"><span id="S4.T2.9.1.3.4.1">1.30</span></td><td id="S4.T2.9.1.3.5"><span id="S4.T2.9.1.3.5.1">12.5</span></td><td id="S4.T2.9.1.3.6"><span id="S4.T2.9.1.3.6.1">0.32</span></td><td id="S4.T2.9.1.3.7"><span id="S4.T2.9.1.3.7.1">40.9</span></td><td id="S4.T2.9.1.3.8"><span id="S4.T2.9.1.3.8.1">0.18</span></td><td id="S4.T2.9.1.3.9"><span id="S4.T2.9.1.3.9.1">29.7</span></td><td id="S4.T2.9.1.3.10"><span id="S4.T2.9.1.3.10.1">0.12</span></td></tr><tr id="S4.T2.9.1.4"><td id="S4.T2.9.1.4.1">LLM</td><td id="S4.T2.9.1.4.2">57.2</td><td id="S4.T2.9.1.4.3">1.51</td><td id="S4.T2.9.1.4.4">12.7</td><td id="S4.T2.9.1.4.5">0.43</td><td id="S4.T2.9.1.4.6">45.2</td><td id="S4.T2.9.1.4.7">0.22</td><td id="S4.T2.9.1.4.8">32.2</td><td id="S4.T2.9.1.4.9">0.13</td></tr><tr id="S4.T2.9.1.5"><td id="S4.T2.9.1.5.1" rowspan="4"><span id="S4.T2.9.1.5.1.1"><span id="S4.T2.9.1.5.1.1.1"><span id="S4.T2.9.1.5.1.1.1.1"><span id="S4.T2.9.1.5.1.1.1.1.1">Agent-</span></span> <span id="S4.T2.9.1.5.1.1.1.2"><span id="S4.T2.9.1.5.1.1.1.2.1">bench</span></span></span></span></td><td id="S4.T2.9.1.5.2"><span id="S4.T2.9.1.5.2.1">None</span></td><td id="S4.T2.9.1.5.3"><span id="S4.T2.9.1.5.3.1">40.7</span></td><td id="S4.T2.9.1.5.4"><span id="S4.T2.9.1.5.4.1">1.15</span></td><td id="S4.T2.9.1.5.5"><span id="S4.T2.9.1.5.5.1">12.1</span></td><td id="S4.T2.9.1.5.6"><span id="S4.T2.9.1.5.6.1">0.38</span></td><td id="S4.T2.9.1.5.7"><span id="S4.T2.9.1.5.7.1">40.6</span></td><td id="S4.T2.9.1.5.8"><span id="S4.T2.9.1.5.8.1">0.18</span></td><td id="S4.T2.9.1.5.9"><span id="S4.T2.9.1.5.9.1">31.5</span></td><td id="S4.T2.9.1.5.10"><span id="S4.T2.9.1.5.10.1">0.13</span></td></tr><tr id="S4.T2.9.1.6"><td id="S4.T2.9.1.6.1">LLM</td><td id="S4.T2.9.1.6.2">46.5</td><td id="S4.T2.9.1.6.3">1.33</td><td id="S4.T2.9.1.6.4">13.1</td><td id="S4.T2.9.1.6.5">0.57</td><td id="S4.T2.9.1.6.6">46.9</td><td id="S4.T2.9.1.6.7">0.20</td><td id="S4.T2.9.1.6.8">34.2</td><td id="S4.T2.9.1.6.9">0.15</td></tr><tr id="S4.T2.9.1.7"><td id="S4.T2.9.1.7.1"><span id="S4.T2.9.1.7.1.1">Hum.</span></td><td id="S4.T2.9.1.7.2">45.3</td><td id="S4.T2.9.1.7.3">1.30</td><td id="S4.T2.9.1.7.4">13.6</td><td id="S4.T2.9.1.7.5">0.54</td><td id="S4.T2.9.1.7.6">46.6</td><td id="S4.T2.9.1.7.7">0.19</td><td id="S4.T2.9.1.7.8">32.8</td><td id="S4.T2.9.1.7.9">0.15</td></tr></tbody></table>

#### LLM-generated context files increase cost and reduce performance

LLM-generated context files cause performance drops in 5 out of 8 settings across SWE-bench Lite and AGENTbench (see [Figure˜3](https://arxiv.org/html/2602.11988v1#S4.F3 "In 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?")). In more detail, the average resolution rate is reduced by 0.5%0.5\\% and 2%2\\% on average on SWE-bench Lite and AGENTbench, respectively. Meanwhile, the context files increase the # steps in every setting on average by 2.452.45 and 3.923.92 steps, respectively, which leads to a cost increase of 20% and 23% on average, respectively (see [Table˜2](https://arxiv.org/html/2602.11988v1#S4.T2 "In 4.2 Main Results ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?")).

#### Human context files increase cost and performance

We observe that the developer-provided context files outperform the LLM-generated ones for all four agents, despite not being agent-specific, and improve the performance compared to no context files for all agents but Claude Code (see [Figure˜3](https://arxiv.org/html/2602.11988v1#S4.F3 "In 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?") right). However, developer-provided context files also increase the average number of steps and costs required to solve the task, on average by 3.343.34 steps and at most 19%, respectively.

#### Context files do not provide effective overviews

One recommendation for context files is to include a codebase overview (AGENTS.md, [2025](https://arxiv.org/html/2602.11988v1#bib.bib1)). Across the 12 developer-provided context files in AGENTbench, 8 include a dedicated codebase overview, with 4 explicitly enumerating and describing the directories and subdirectories in the repository. Similarly, both the Codex and Qwen Code context file generation prompts explicitly instruct the agent to include an overview section, while the Claude Code prompt advocates for a high-level overview only and warns against listing components that are easily discoverable. We use GPT-OSS-120b to assess which of the LLM-generated context files contain codebase overviews. Surprisingly, 100%100\\% of Sonnet-4.5\-generated context files are flagged for overviews, and 95%95\\% and 99%99\\% for Qwen3-30b-coder and GPT-5.2 respectively. Only GPT-5.1 mini has significantly fewer overviews (36%36\\%).

![Refer to caption](https://arxiv.org/html/2602.11988v1/x7.png)

Figure 5: When removing all documentation-related files from the codebase, LLM-generated context files tend to outperform developer-provided (Human) ones on AGENTbench.

![Refer to caption](https://arxiv.org/html/2602.11988v1/x8.png)

Figure 6: Increase in average tool use when including LLM-generated (bright green) or developer-provided (dark green) context files, compared to the average tool use without context files. For tool names, we map Codex and Qwen Code tools to the Claude Code equivalents (we detail the mapping in [Appendix˜A](https://arxiv.org/html/2602.11988v1#A1 "Appendix A Experimental Details ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?")).

To assess the usefulness of these overviews, we measure how quickly agents discover files relevant to the described issue II. Concretely, we measure the average number of steps before the coding agent interacts with any file modified in the original PR patch X∗X^{\*}. We exclude the 3%3\\% of instances in which the agent never interacts with any file modified in X∗X^{\*}. Both on SWE-bench Lite and AGENTbench the presence of context files does not meaningfully reduce this metric, as shown in [Figure˜4](https://arxiv.org/html/2602.11988v1#S4.F4 "In 4.2 Main Results ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?").

While context files appear to increase the number of required steps significantly for GPT-5.1 mini, we observe in manual trace inspection that this increase is due to it (i) issuing multiple commands to find the context files and (ii) reading them (multiple times) despite them being already included in the agent’s context. Interestingly, we only observed this behavior if context files were present at all. We conclude that context files, even developer-provided ones, are not effective at providing a repository overview.

#### Context files are redundant documentation

Our hypothesis is that LLM-generated context files are highly redundant with existing documentation, while developer-provided context files add additional information. To confirm this, we manually remove all documentation (files ending with .md, example code, and the folder docs/) after generating the context file, and before evaluating the coding agents. We show the results in [Figure˜5](https://arxiv.org/html/2602.11988v1#S4.F5 "In Context files do not provide effective overviews ‣ 4.2 Main Results ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), excluding Claude Code due to its hight cost. In this setting, where context files are the only source of documentation available, LLM-generated context files not only consistently improve performance by 2.72.7% on average, but also outperform developer-written documentation. This may explain anecdotal evidence reporting that coding agents perform better after adding context files (Sewell, [2025](https://arxiv.org/html/2602.11988v1#bib.bib30)), since many less popular repositories contain little to no documentation.

### 4.3 Trace analysis

We now analyze the impact of context files on agent behavior in more detail by analysing the frequency of agent tool calls and length of reasoning traces. We describe our setup in more detail in [Section˜B.2](https://arxiv.org/html/2602.11988v1#A2.SS2 "B.2 Analyzing Traces of Coding Agents ‣ Appendix B Prompts ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?").

#### Context files lead to more testing and exploration

In [Figure˜6](https://arxiv.org/html/2602.11988v1#S4.F6 "In Context files do not provide effective overviews ‣ 4.2 Main Results ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), we show the increase in average tool use when including LLM-generated (bright green) or developer-provided (dark green) context files. Negative values imply a decrease in tool use. We find that, across all models, when context files are present, the coding agents run more tests. They also tend to navigate the repository more: they search more files (grep), read more files, and write more files. Lastly, adding context files causes agents to use more repository-specific tooling (e.g., uv and repo\_tool). In [Figure˜10](https://arxiv.org/html/2602.11988v1#A1.F10 "In Refining the tool names ‣ A.2 Trace Analysis ‣ Appendix A Experimental Details ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?") ([Appendix˜A](https://arxiv.org/html/2602.11988v1#A1 "Appendix A Experimental Details ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?")), we perform a similar analysis using the intent of the tool call, leading to the same conclusion.

#### Instructions in context files are typically followed

We find that agents generally follow instructions present in the context files. For instance, uv is used 1.6 times per instance on average when mentioned in the context files, compared to fewer than 0.01 times when it is not mentioned, and repository-specific tools are used 2.5 times per instance on average when mentioned, compared to fewer than 0.05 times when they are not mentioned. This effect is observable across almost all measured tools displayed in [Figure˜6](https://arxiv.org/html/2602.11988v1#S4.F6 "In Context files do not provide effective overviews ‣ 4.2 Main Results ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), as we show in a more in-depth analysis in [Appendix˜A](https://arxiv.org/html/2602.11988v1#A1 "Appendix A Experimental Details ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"). In particular, this result implies that the absence of improvements with context files is not due to a lack of instruction-following.

![Refer to caption](https://arxiv.org/html/2602.11988v1/x9.png)

Figure 7: Number of reasoning tokens spent on average by GPT-5.2 and GPT-5.1 mini, without context files, with LLM-generated context files, and with developer-written context files, on SWE-bench Lite (left) and AGENTbench (right).

#### Following context files requires more thinking

We hypothesize that these additional instructions make the task harder. To confirm this, we analyze the average number of reasoning tokens used by GPT-5.2 and GPT-5.1 mini, as their adaptive reasoning (OpenAI, [2025b](https://arxiv.org/html/2602.11988v1#bib.bib24)) allows them to use more reasoning tokens for tasks that they deem harder. In [Figure˜7](https://arxiv.org/html/2602.11988v1#S4.F7 "In Instructions in context files are typically followed ‣ 4.3 Trace analysis ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), we show that LLM-generated context files indeed increase the average number of reasoning tokens by 22% for GPT-5.2 and 14% for GPT-5.1 mini on SWE-bench Lite (respectively 14% and 10% on AGENTbench), and that developer-written context files increase the number of reasoning tokens by 20% and 2% for GPT-5.2 and GPT-5.1 mini, respectively.

### 4.4 Ablations

In this Section we analyze differences between the context files generated by different models, and the impact of the prompt used to create the context files.

![Refer to caption](https://arxiv.org/html/2602.11988v1/x10.png)

Figure 8: On SWE-bench Lite, performance is improved with context files generated by GPT-5.2 compared to using the model underlying the agent, while on AGENTbench performance is degraded.

#### Stronger models don’t generate better context files

We compare context files generated with GPT-5.2 + Codex to those created by our standard agents in [Figure˜8](https://arxiv.org/html/2602.11988v1#S4.F8 "In 4.4 Ablations ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"). This improves performance on SWE-bench Lite across all models (2% on average), but degrades performance on AGENTbench across all models (3% on average). We thus conclude that stronger models do not necessarily generate superior context files.

![Refer to caption](https://arxiv.org/html/2602.11988v1/x11.png)

Figure 9: When generating context files using the prompt from Codex or from Claude Code on SWE-bench Lite and AGENTbench, there is no consistent impact on success rate.

#### No difference between the specific prompts

We compare context files generated using the prompt of Codex and Claude Code across all agents and models in [Figure˜9](https://arxiv.org/html/2602.11988v1#S4.F9 "In Stronger models don’t generate better context files ‣ 4.4 Ablations ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"). Surprisingly, Claude Code performs better with context files generated using the Codex prompt, while both GPT-5.2 and GPT-5.1 mini perform better on SWE-bench Lite with the Codex prompt but worse on AGENTbench. Overall, neither the prompt matching the underlying model and agent, nor a specific prompt performs consistently best, indicating that sensitivity to different (good) prompts is generally small.

## 5 Limitations and Future Work

While our work addresses important shortcomings in the literature, exciting opportunities for future research remain.

#### Niche programming languages

The current evaluation is focused heavily on Python. Since this is a language that is widely represented in the training data, much detailed knowledge about tooling, dependencies, and other repository specifics might be present in the models’ parametric knowledge, nullifying the effect of context files. Future work may investigate the effect of context files on more niche programming languages and toolchains that are less represented in the training data, and known to be more difficult for LLMs (Cassano et al., [2022](https://arxiv.org/html/2602.11988v1#bib.bib8); Orlanski et al., [2023](https://arxiv.org/html/2602.11988v1#bib.bib26)).

#### Context files beyond task resolution

In this work, we evaluate the impact of context files on task resolution rate. However, there are many other relevant aspects of coding agents, such as code efficiency (He et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib14)) and security (Chen et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib10)), that we believe could be explored in future work. Specifically, for security, prior work found that prompting LLMs to generate secure code significantly improves the security of generated code (Vero et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib35)).

#### Improving context file generation

Another interesting avenue opened by this work is how to improve the automatic generation of *useful* context files. Here, human developers appear to dominate per our evaluation. Several related works in the direction of planning and continuous learning from prior tasks may be applicable for this task (Suzgun et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib32); Zhang et al., [2025b](https://arxiv.org/html/2602.11988v1#bib.bib39); Cheng et al., [2025](https://arxiv.org/html/2602.11988v1#bib.bib11)). By tackling this challenge, future agents could gain a long-term capability at meaningful self-improvement.

## 6 Conclusion

We present an extensive evaluation of the impact of context files on coding agent performance for four common coding agents on SWE-bench Lite and AGENTbench. The latter is a new benchmark we built from recent GitHub issues and less popular repositories containing developer-written context files. We find that all context files consistently increase the number of steps required to complete tasks. LLM-generated context files have a marginal negative effect on task success rates, while developer-written ones provide a marginal performance gain.

Our trace analyses show that instructions in context files are generally followed and lead to more testing and a broader exploration, however they do not function as effective repository overviews. Overall, our results suggest that context files have only marginal effect on agent behavior, and are likely only desirable when manually written. This highlights a concrete gap between current agent-developer recommendations and observed outcomes, and motivates future work on principled ways to automatically generate concise, task-relevant guidance for coding agents.

## References

-   AGENTS.md (2025) AGENTS.md. AGENTS.md - A simple, open format for guiding coding agents, 2025. URL [https://agents.md/](https://agents.md/).
-   Aider (2024) Aider. AI pair programming in your terminal, 2024. URL [https://aider.chat](https://aider.chat/).
-   Anthropic (2025a) Anthropic. Claude Code overview, 2025a. URL [https://code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview).
-   Anthropic (2025b) Anthropic. Using CLAUDE.md files: Customizing Claude Code for your codebase, 2025b. URL [https://claude.com/blog/using-claude-md-files](https://claude.com/blog/using-claude-md-files).
-   Anthropic (2025) Anthropic. Claude Sonnet 4.5, 2025. URL [https://www.anthropic.com/news/claude-sonnet-4-5](https://www.anthropic.com/news/claude-sonnet-4-5).
-   Badertdinov et al. (2025) Badertdinov, I., Golubev, A., Nekrashevich, M., Shevtsov, A., Karasik, S., Andriushchenko, A., Trofimova, M., Litvintseva, D., and Yangel, B. SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents. *arXiv preprint*, 2025. URL [https://arxiv.org/abs/2505.20411](https://arxiv.org/abs/2505.20411).
-   Boyina (2025) Boyina, G. Why I Created AGENTS.md: A Simple Solution to a Growing Problem, 2025. URL [https://thegowtham.medium.com/why-i-created-agents-md-a-simple-solution-to-a-growing-problem-3afc1f6211f7](https://thegowtham.medium.com/why-i-created-agents-md-a-simple-solution-to-a-growing-problem-3afc1f6211f7).
-   Cassano et al. (2022) Cassano, F., Gouwar, J., Nguyen, D., Nguyen, S., Phipps-Costin, L., Pinckney, D., Yee, M.-H., Zi, Y., Anderson, C. J., Feldman, M. Q., et al. MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation. *arXiv preprint*, 2022. URL [https://arxiv.org/abs/2208.08227](https://arxiv.org/abs/2208.08227).
-   Chatlatanagulchai et al. (2025) Chatlatanagulchai, W., Li, H., Kashiwa, Y., Reid, B., Thonglek, K., Leelaprute, P., Rungsawang, A., Manaskasemsak, B., Adams, B., Hassan, A. E., et al. Agent READMEs: An Empirical Study of Context Files for Agentic Coding. *arXiv preprint*, 2025. URL [https://arxiv.org/abs/2511.12884](https://arxiv.org/abs/2511.12884).
-   Chen et al. (2025) Chen, J., Huang, H., Lyu, Y., An, J., Shi, J., Yang, C., Zhang, T., Tian, H., Li, Y., Li, Z., et al. SecureAgentBench: Benchmarking Secure Code Generation under Realistic Vulnerability Scenarios. *arXiv preprint*, 2025. URL [https://arxiv.org/abs/2509.22097](https://arxiv.org/abs/2509.22097).
-   Cheng et al. (2025) Cheng, Y., Wang, Z., Ma, W., Zhu, W., Deng, Y., and Zhao, J. EvoCurr: Self-evolving Curriculum with Behavior Code Generation for Complex Decision-making. *arXiv preprint*, 2025. URL [https://arxiv.org/abs/2508.09586](https://arxiv.org/abs/2508.09586).
-   Du et al. (2025) Du, Y., Cai, Y., Zhou, Y., Wang, C., Qian, Y., Pang, X., Liu, Q., Hu, Y., and Chen, S. SWE-Dev: Evaluating and Training Autonomous Feature-Driven Software Development. *arXiv preprint*, 2025. URL [https://arxiv.org/abs/2505.16975](https://arxiv.org/abs/2505.16975).
-   Google (2025) Google. google-gemini/gemini-cli: An open-source AI agent that brings the power of Gemini directly into your terminal, 2025. URL [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli).
-   He et al. (2025) He, X., Liu, Q., Du, M., Yan, L., Fan, Z., Huang, Y., Yuan, Z., and Ma, Z. SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositories? *arXiv preprint*, 2025. URL [https://arxiv.org/abs/2507.12415](https://arxiv.org/abs/2507.12415).
-   Jimenez et al. (2024) Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., and Narasimhan, K. R. SWE-bench: Can Language Models Resolve Real-world Github Issues? In *ICLR*, 2024. URL [https://openreview.net/forum?id=VTF8yNQM66](https://openreview.net/forum?id=VTF8yNQM66).
-   Kwon et al. (2023) Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu, C. H., Gonzalez, J. E., Zhang, H., and Stoica, I. Efficient Memory Management for Large Language Model Serving with PagedAttention. In *Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles*, 2023.
-   Li et al. (2025) Li, W., Zhang, X., Guo, Z., Mao, S., Luo, W., Peng, G., Huang, Y., Wang, H., and Li, S. FEA-Bench: A Benchmark for Evaluating Repository-Level Code Generation for Feature Implementation. In *ACL*, 2025. URL [https://aclanthology.org/2025.acl-long.839/](https://aclanthology.org/2025.acl-long.839/).
-   Liang et al. (2024) Liang, S., Hu, Y., Jiang, N., and Tan, L. Can Language Models Replace Programmers for Coding? REPOCOD Says ’Not Yet’. *arXiv preprint*, 2024. URL [https://arxiv.org/abs/2410.21647](https://arxiv.org/abs/2410.21647).
-   Lieret et al. (2025) Lieret, K., Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., and Narasimhan, K. R. SWE-bench Bash Only, 2025. URL [https://www.swebench.com/bash-only.html](https://www.swebench.com/bash-only.html).
-   Mohsenimofidi et al. (2025) Mohsenimofidi, S., Galster, M., Treude, C., and Baltes, S. Context Engineering for AI Agents in Open-Source Software. *arXiv preprint*, 2025. URL [https://arxiv.org/abs/2510.21413](https://arxiv.org/abs/2510.21413).
-   Mündler et al. (2024) Mündler, N., Müller, M. N., He, J., and Vechev, M. T. SWT-Bench: Testing and Validating Real-World Bug-Fixes with Code Agents. In *NeurIPS*, 2024. URL [http://papers.nips.cc/paper\_files/paper/2024/hash/94f093b41fc2666376fb1f667fe282f3-Abstract-Conference.html](http://papers.nips.cc/paper_files/paper/2024/hash/94f093b41fc2666376fb1f667fe282f3-Abstract-Conference.html).
-   Nigh (2025) Nigh, M. How to write a great agents.md: Lessons from over 2,500 repositories, 2025. URL [https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/).
-   OpenAI (2025a) OpenAI. OpenAI co-founds the Agentic AI Foundation under the Linux Foundation, 2025a. URL [https://openai.com/index/agentic-ai-foundation/](https://openai.com/index/agentic-ai-foundation/).
-   OpenAI (2025b) OpenAI. GPT-5.1: A smarter, more conversational ChatGPT, 2025b. URL [https://openai.com/index/gpt-5-1/](https://openai.com/index/gpt-5-1/).
-   OpenAI (2025c) OpenAI. openai/codex: Lightweight coding agent that runs in your terminal, 2025c. URL [https://github.com/openai/codex](https://github.com/openai/codex).
-   Orlanski et al. (2023) Orlanski, G., Xiao, K., Garcia, X., Hui, J., Howland, J., Malmaud, J., Austin, J., Singh, R., and Catasta, M. Measuring the Impact of Programming Language Distribution. In *ICML*, 2023. URL [https://proceedings.mlr.press/v202/orlanski23a.html](https://proceedings.mlr.press/v202/orlanski23a.html).
-   QwenLM (2025) QwenLM. QwenLM/Qwen3-Coder: Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team, Alibaba Cloud, 2025. URL [https://github.com/QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder).
-   Sarkar (2025) Sarkar, S. K. Ai agents, productivity, and higher-order thinking: Early evidence from software development. *Available at SSRN 5713646*, 2025.
-   Sawers (2025) Sawers, P. The Rise of Agents.md, an Open Standard and Single Source of Truth for AI Coding Agents, 2025. URL [https://tessl.io/blog/the-rise-of-agents-md-an-open-standard-and-single-source-of-truth-for-ai-coding-agents/](https://tessl.io/blog/the-rise-of-agents-md-an-open-standard-and-single-source-of-truth-for-ai-coding-agents/).
-   Sewell (2025) Sewell, S. Improve your AI code output with AGENTS.md (+ my best tips), 2025. URL [https://www.builder.io/blog/agents-md](https://www.builder.io/blog/agents-md).
-   Singh et al. (2026) Singh, A., Fry, A., Perelman, A., Tart, A., Ganesh, A., El-Kishky, A., McLaughlin, A., Low, A., Ostrow, A., Ananthram, A., et al. OpenAI GPT-5 System Card. *arXiv preprint*, 2026. URL [https://arxiv.org/abs/2601.03267](https://arxiv.org/abs/2601.03267).
-   Suzgun et al. (2025) Suzgun, M., Yuksekgonul, M., Bianchi, F., Jurafsky, D., and Zou, J. Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory. *arXiv preprint*, 2025. URL [https://arxiv.org/abs/2504.07952](https://arxiv.org/abs/2504.07952).
-   Team (2025) Team, Q. Qwen3 Technical Report. *arXiv preprint*, 2025. URL [https://arxiv.org/abs/2505.09388](https://arxiv.org/abs/2505.09388).
-   Vergopoulos et al. (2025) Vergopoulos, K., Müller, M. N., and Vechev, M. Automated Benchmark Generation for Repository-Level Coding Tasks. *arXiv preprint*, 2025. URL [https://arxiv.org/abs/2503.07701](https://arxiv.org/abs/2503.07701).
-   Vero et al. (2025) Vero, M., Mündler, N., Chibotaru, V., Raychev, V., Baader, M., Jovanovic, N., He, J., and Vechev, M. T. BaxBench: Can LLMs Generate Correct and Secure Backends? In *ICML*, 2025.
-   Wang et al. (2025) Wang, X., Li, B., Song, Y., Xu, F. F., Tang, X., Zhuge, M., Pan, J., Song, Y., Li, B., Singh, J., et al. OpenHands: An Open Platform for AI Software Developers as Generalist Agents. In *ICLR*, 2025. URL [https://openreview.net/forum?id=OJd3ayDDoF](https://openreview.net/forum?id=OJd3ayDDoF).
-   Yang et al. (2024) Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., and Press, O. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. In *NeurIPS*, 2024. URL [http://papers.nips.cc/paper\_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html](http://papers.nips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html).
-   Zhang et al. (2025a) Zhang, L., He, S., Zhang, C., Kang, Y., Li, B., Xie, C., Wang, J., Wang, M., Huang, Y., Fu, S., et al. SWE-bench Goes Live! *arXiv preprint*, 2025a. URL [https://arxiv.org/abs/2505.23419](https://arxiv.org/abs/2505.23419).
-   Zhang et al. (2025b) Zhang, Q., Hu, C., Upasani, S., Ma, B., Hong, F., Kamanuru, V., Rainton, J., Wu, C., Ji, M., Li, H., et al. Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models. *arXiv preprint*, 2025b. URL [https://arxiv.org/abs/2510.04618](https://arxiv.org/abs/2510.04618).

## Appendix A Experimental Details

In this section, we provide additional details about our experiments from [Section˜4](https://arxiv.org/html/2602.11988v1#S4 "4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?").

### A.1 Additional Experimental Details

We now describe the remaining experimental details for the experiments in [Section˜4.2](https://arxiv.org/html/2602.11988v1#S4.SS2 "4.2 Main Results ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?").

#### Coding environment

For AGENTbench instances, we run the coding agent in a Docker container with basic tooling (python, apt-get, uv, …) and Internet access. Importantly, we remove the git commit history and all remotes. For SWE-bench Lite, we use the Docker images provided by Jimenez et al. ([2024](https://arxiv.org/html/2602.11988v1#bib.bib15)). We let the coding agents access the web (either via dedicated tools or through the command line) and manually checked that the agents do not cheat (e.g., looking at the PR corresponding to the instance description). We find no such case of cheating, and web access represents a minority of the tool calls (less than 1%). For Claude Code, we keep the Task tool enabled: it allows Sonnet-4.5 to invoke sub-agents, using Haiku-4.5, to solve sub-tasks. For instance, a sub-task can be exploring the repository to find specific files.

### A.2 Trace Analysis

Here, we detail the experiments from [Section˜4.3](https://arxiv.org/html/2602.11988v1#S4.SS3 "4.3 Trace analysis ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"). In particular, we give the mapping used to aggregate tool names across coding agents, analyze the correlation between the number of tool uses and whether the tool is mentioned in the context files, and expand the trace analysis to the intent behind tool calls.

#### Experimental setup

We recall the experimental setup from [Section˜4.3](https://arxiv.org/html/2602.11988v1#S4.SS3 "4.3 Trace analysis ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"). Given a list of tool calls from an agent, we analyze the frequency of each tool call. For tools included in the agentic framework (e.g., Read, Write, or TodoWrite), we record the name of the tool being called. For shell commands, we use an LLM to extract (from the command and its output) the concrete command that was executed (e.g., uv, pytest, cat) and to categorize the intent of the tool call (e.g., install dependencies, run tests, read files). We build the categories iteratively. We start with an empty set of categories, and for each shell command, we ask the LLM to assign it to an existing category if possible and otherwise create a new category. As the LLM, we use GPT-OSS-120b, and the prompt is given in [Section˜B.2](https://arxiv.org/html/2602.11988v1#A2.SS2 "B.2 Analyzing Traces of Coding Agents ‣ Appendix B Prompts ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"). Finally, we manually merge duplicate and closely adjacent categories.

Table 3: Equivalence classes used to group the different tool calls.

<table id="A1.T3.4.1"><tbody><tr id="A1.T3.4.1.1"><td id="A1.T3.4.1.1.1"><span id="A1.T3.4.1.1.1.1">Claude Code</span> tool</td><td id="A1.T3.4.1.1.2"><span id="A1.T3.4.1.1.2.1">Codex</span></td><td id="A1.T3.4.1.1.3"><span id="A1.T3.4.1.1.3.1">Qwen Code</span></td></tr><tr id="A1.T3.4.1.2"><td id="A1.T3.4.1.2.1">Edit</td><td id="A1.T3.4.1.2.2"><span id="A1.T3.4.1.2.2.1">sed</span></td><td id="A1.T3.4.1.2.3"><span id="A1.T3.4.1.2.3.1">sed</span>, <span id="A1.T3.4.1.2.3.2">edit</span></td></tr><tr id="A1.T3.4.1.3"><td id="A1.T3.4.1.3.1">Write</td><td id="A1.T3.4.1.3.2"><span id="A1.T3.4.1.3.2.1">apply_patch</span></td><td id="A1.T3.4.1.3.3"><span id="A1.T3.4.1.3.3.1">write_file</span></td></tr><tr id="A1.T3.4.1.4"><td id="A1.T3.4.1.4.1">Grep</td><td id="A1.T3.4.1.4.2"><span id="A1.T3.4.1.4.2.1">grep</span>, <span id="A1.T3.4.1.4.2.2">rg</span></td><td id="A1.T3.4.1.4.3"><span id="A1.T3.4.1.4.3.1">grep</span></td></tr><tr id="A1.T3.4.1.5"><td id="A1.T3.4.1.5.1">Read</td><td id="A1.T3.4.1.5.2"><span id="A1.T3.4.1.5.2.1">cat</span></td><td id="A1.T3.4.1.5.3"><span id="A1.T3.4.1.5.3.1">cat</span>, <span id="A1.T3.4.1.5.3.2">read_file</span>, <span id="A1.T3.4.1.5.3.3">search_file_content</span></td></tr><tr id="A1.T3.4.1.6"><td id="A1.T3.4.1.6.1">TodoWrite</td><td id="A1.T3.4.1.6.2"><span id="A1.T3.4.1.6.2.1">update_plan</span></td><td id="A1.T3.4.1.6.3"><span id="A1.T3.4.1.6.3.1">todo_write</span></td></tr></tbody></table>

#### Refining the tool names

For [Figure˜6](https://arxiv.org/html/2602.11988v1#S4.F6 "In Context files do not provide effective overviews ‣ 4.2 Main Results ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), we further manually refined the tool names for readability. In particular, in [Table˜3](https://arxiv.org/html/2602.11988v1#A1.T3 "In Experimental setup ‣ A.2 Trace Analysis ‣ Appendix A Experimental Details ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), we map tool names from other agents, namely Codex and Qwen Code, as well as some CLI tools, to Claude Code tooling. Lastly, for repository-specific tooling (e.g., pdm, ansible, or opshin), we grouped them into the repo\_tool category.

![Refer to caption](https://arxiv.org/html/2602.11988v1/x12.png)

Figure 10: Increase in the average tool use (grouped into high-level categories) when including LLM-generated (bright green) or developer-provided (dark green) context files, compared to the average tool use without context files. For the high-level categories, we use an LLM to categorize the various tool calls.

![Refer to caption](https://arxiv.org/html/2602.11988v1/x13.png)

Figure 11: Average number of tool calls depending on whether the tool name is mentioned in the context files. For tool names, we use the equivalence classes from [Table˜3](https://arxiv.org/html/2602.11988v1#A1.T3 "In Experimental setup ‣ A.2 Trace Analysis ‣ Appendix A Experimental Details ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), and consider a tool to be mentioned in the context file if any tool from the corresponding equivalence class is mentioned in the context file.

![Refer to caption](https://arxiv.org/html/2602.11988v1/x14.png)

![Refer to caption](https://arxiv.org/html/2602.11988v1/x15.png)

Figure 12: Resolution rate grouped by repository for four different models: without context files, with LLM-generated context files, and with developer-written context files on SWE-bench Lite (top) and AGENTbench (bottom). For SWE-bench Lite in particular, the majority of instances come from the same repository (django), making per-repository estimates of the success rate noisy.

#### Correlation between the number of tool calls and context files

In [Figure˜11](https://arxiv.org/html/2602.11988v1#A1.F11 "In Refining the tool names ‣ A.2 Trace Analysis ‣ Appendix A Experimental Details ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), we show the average number of tool calls depending on whether the tool name is mentioned in the context file. We find that, if a tool name is mentioned in the context files, this increases its usage by the coding agents. For instance, uv, pytest, or repository-specific tools (repo\_tool) are used almost exclusively if they are mentioned in the context file. This means that instructions in the context files are followed, and that a lack of instruction-following capabilities does not explain why we observe, in [Section˜4.2](https://arxiv.org/html/2602.11988v1#S4.SS2 "4.2 Main Results ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), no gain in accuracy when using context files.

#### Analyzing intents of tool calls

For the tool intents extracted by the LLM (334334 different categories in total), we further aggregate them into the following 10 categories:

-   •

    git: Repository and version-control operations (e.g., commits, branches, diffs, checkout, stash, status).

-   •

    model: Model lifecycle tasks such as downloading or loading models, inspecting configurations or parameters, and running inference.

-   •

    env\_deps: Python environment and dependency management (virtualenv or venv, installations, versions, lockfiles).

-   •

    build: Building, compiling, or packaging code and producing artifacts or distribution packages.

-   •

    quality: Code quality and correctness checks (linting, formatting, type checking, validation or verification, schema checks).

-   •

    testing: Running and reviewing tests (unit, integration, regression, sanity, pytest) and test results.

-   •

    run\_exec: Executing workflows and scripts or commands (Python, shell, Django), including reproduction and debugging runs.

-   •

    search: Discovery and inspection actions (search, find, grep, glob, list, view, show, display, inspect, parse).

-   •

    file\_ops: Direct file and filesystem operations (read, write, edit, copy, move, delete, create, permissions, paths).

-   •

    system: System and miscellaneous utilities (processes, disk usage, environment variables, HTTP checks, checksums, tool or device information, help).

In [Figure˜10](https://arxiv.org/html/2602.11988v1#A1.F10 "In Refining the tool names ‣ A.2 Trace Analysis ‣ Appendix A Experimental Details ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), we show the difference in frequency of these categories with and without context files. The conclusion is similar to that of [Section˜4.3](https://arxiv.org/html/2602.11988v1#S4.SS3 "4.3 Trace analysis ‣ 4 Experimental Evaluation ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"): the presence of context files significantly increases the number of tests run by coding agents, as well as the extent of codebase exploration and code quality checks.

### A.3 Per-repository Success Rate

In [Figure˜12](https://arxiv.org/html/2602.11988v1#A1.F12 "In Refining the tool names ‣ A.2 Trace Analysis ‣ Appendix A Experimental Details ‣ Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"), we show the success rate of the different scenarios (None, LLM, and Human) grouped by repository. For both SWE-bench Lite and AGENTbench, there is no single repository where the presence of context files has a significant impact. Nonetheless, for AGENTbench in particular, we see that the difficulty across instances is relatively balanced, validating our approach to building the instances.

## Appendix B Prompts

In this section, we detail all prompts used throughout this work.

### B.1 AGENTbench instances generation

We detail below the prompts used for filtering pull requests, setting up the instances, describing the instances, and generating the test cases.

### B.2 Analyzing Traces of Coding Agents

To analyze the tool calls made by the coding agents, we use GPT-OSS-120bwith the prompt below.
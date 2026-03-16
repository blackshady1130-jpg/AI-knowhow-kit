---
url: https://arxiv.org/html/2602.13964v3
title: "HLE-Verified: A Systematic Verification and Structured \nRevision of Humanity’s Last Exam"
captured_at: "2026-03-09T03:47:07.259Z"
---

# HLE-Verified: A Systematic Verification and Structured 
Revision of Humanity’s Last Exam

Weiqi Zhai1∗, Zhihai Wang2∗, Jinghang Wang1, Boyu Yang1, Xiaogang Li1, Xander Xu1, Bohan Wang2, Peng Wang2, Xingzhe Wu2, Anfeng Li2, Qiyuan Feng1, Yuhao Zhou1, Shoulin Han1, Wenjie Luo1, Yiyuan Li1, Yaxuan Wang1, Ruixian Luo1, Guojie Lin1, Peiyao Xiao1, Chengliang Xu1, Ben Wang1, Zeyu Wang1, Zichao Chen1, Jianan Ye1, Yijie Hu1, Jialong Chen1, Zongwen Shen1, Yuliang Xu1, An Yang2, Bowen Yu2, Dayiheng Liu2, Junyang Lin2, Hu Wei1, Que Shen2†, Bing Zhao1†
1Alibaba Group
2Qwen Team, Alibaba Group
\* Equal Contribution
†\\dagger Corresponding Authors: shenque.sq@alibaba-inc.com, xiongdao@alibaba-inc.com

###### Abstract

Humanity’s Last Exam (HLE) has become a widely used benchmark for evaluating frontier large language models on challenging, multi-domain questions. However, subsequent community-led analyses have raised concerns that HLE contains a non-trivial number of noisy items (e.g., ambiguous statements, incorrect answers, or mismatched rationales), which can systematically bias evaluation results and distort cross-model comparisons. To address this challenge, we introduce HLE-Verified, a verified and revised version of HLE accompanied by a transparent, component-wise verification protocol and fine-grained error taxonomy. Our construction follows a two-stage validation-and-repair workflow resulting in a unified certified benchmark. In Stage I, each item is subjected to binary validation on the *problem* and *final answer* dimensions (with rationale used as an auxiliary consistency signal), combining domain-expert review and model-based cross-checks. This stage yields 668 items verified as correct. In Stage II, items identified as flawed but fixable are systematically revised under strict constraints that preserve the original evaluation intent, through dual independent expert repairs, model-assisted consistency auditing, and final expert adjudication, resulting in 1,143 revised-and-certified items. The remaining 689 items are released as a documented *uncertain* set with explicit uncertainty sources and required expertise tags for future community refinement. We compare the performance of eight state-of-the-art language models on HLE and HLE-Verified, observing an average absolute accuracy gain of 7–10 percentage points on HLE-Verified. The improvement is particularly pronounced on items where the original HLE problem statement and/or reference answer is erroneous: on this subset, the models achieve an average accuracy increase of 30–40 percentage points. Moreover, our analyses indicate a strong association between model confidence and the presence of errors in the problem statement or reference answer, providing evidence for the effectiveness of our revisions. Overall, HLE-Verified improves HLE-style evaluations by reducing annotation noise and enabling more faithful measurements of model capabilities. Data is available at: https://huggingface.co/datasets/skylenage/HLE-Verified.

## 1 Introduction

As frontier language models (LMs) continue to advance rapidly, there is increasing demand for evaluation benchmarks that are simultaneously difficult, broad in disciplinary coverage, and resistant to saturation. High-difficulty benchmarks play a central role in tracking progress, validating capability claims, and shaping scientific discourse about model reasoning abilities. Against this backdrop, the Humanity’s Last Exam (HLE) has emerged as a widely adopted benchmark for evaluating model performance on challenging questions across mathematics, science, engineering, and the humanities(Center for AI Safety et al., [2026](https://arxiv.org/html/2602.13964v3#bib.bib53 "A benchmark of expert-level academic questions to assess AI capabilities")). Results on HLE have been cited to support claims regarding reasoning depth, generalization capacity, and reliability of state-of-the-art models.

However, as benchmark difficulty increases, so does the importance of annotation integrity. When many items lie near a model’s decision boundary, even minor inconsistencies in problem statements or reference answers can disproportionately influence aggregate metrics. Recent independent audits and community-led reviews have highlighted substantial noise in the HLE dataset, including ambiguous or poorly defined question statements, erroneous reference answers, and inconsistencies between rationales and final answers ([A. White (2025)](https://arxiv.org/html/2602.13964v3#bib.bib2 "About 30% of humanity’s last exam chemistry/biology answers are likely wrong"); [lhl (2026)](https://arxiv.org/html/2602.13964v3#bib.bib3 "Hle-gpqa-error-claims"); [17](https://arxiv.org/html/2602.13964v3#bib.bib4 "Research: i forensically audited humanity’s last exam")). These analyses suggest that a portion of measured model performance on HLE may reflect annotation artifacts rather than genuine capability differences.

This issue highlights a broader methodological question: how should high-difficulty benchmarks be systematically verified and maintained after deployment? While benchmark construction traditionally emphasizes task design and data collection, comparatively less attention has been devoted to post-release verification, structured auditing, and transparent revision protocols. For benchmarks that inform scientific claims and cross-model comparisons, the absence of systematic validation can undermine interpretability, reproducibility, and measurement reliability.

To address this reliability challenge, we developed HLE-Verified—a rigorously validated and partially revised version of HLE built under a structured two-stage validation and revision protocol. This approach employs a component-level verification framework, treating *problem statements* and *final answers* as primary targets for correctness assessment while utilizing *rationale* as secondary signals to detect internal contradictions or underdefined specifications. Under this protocol, HLE-Verified is organized into three disjoint subsets: verified gold items, revised items corrected under preserved evaluation objectives, and uncertain items whose validity cannot be conclusively determined.

We position HLE-Verified as dataset infrastructure: not a new benchmark task, but a methodological reliability enhancement that enables more rigorous, interpretable, and reproducible model comparisons. Furthermore, we provide an empirical evaluation of how verification and revision affect downstream model measurements, and we release structured metadata that supports continued community-driven refinement.

##### Contributions.

-   •

    We release HLE-Verified, a verified and revised version of HLE constructed via a transparent component-wise verification protocol and fine-grained error taxonomy, comprising 668 verified items, 1,143 revised-and-verified items, and a 689\-item documented *uncertain* set for structured community refinement.

-   •

    We introduce a systematic two-stage verification-and-revision framework for post-release benchmark auditing.

-   •

    We benchmark eight state-of-the-art LLMs on HLE vs. HLE-Verified, demonstrating that verification materially alters measured performance (an average +7–10 accuracy points overall and +30–40 points on items with erroneous problems/answers), and we analyze the relationship between model confidence and problem/answer errors.

## 2 Background

### 2.1 Why benchmark errors matter

Benchmarks serve as the primary measurement interface between model development and scientific claims about capability. Let a benchmark contain a fraction ρ\\rho of flawed items. Even for small ρ\\rho, aggregate metrics such as accuracy or pass@k can be meaningfully distorted, particularly when flawed items are not randomly distributed. If such items are concentrated in specific domains, reasoning patterns, or difficulty strata, they may introduce systematic measurement bias (Liang et al., [2022](https://arxiv.org/html/2602.13964v3#bib.bib46 "Holistic evaluation of language models"); Gema et al., [2025](https://arxiv.org/html/2602.13964v3#bib.bib47 "Are we done with mmlu?")), favoring certain model families while penalizing others due to differences in training exposure, reasoning style, or calibration behavior.

Beyond aggregate accuracy, benchmark flaws pose a deeper challenge to interpretability. Many analyses assume a well-defined correspondence between correctness and model confidence, particularly in calibration- or uncertainty-aware evaluations (Guo et al., [2017](https://arxiv.org/html/2602.13964v3#bib.bib48 "On calibration of modern neural networks"); Kadavath et al., [2022](https://arxiv.org/html/2602.13964v3#bib.bib49 "Language models (mostly) know what they know")). When items are ill-posed, contain incorrect answer keys, or admit multiple valid interpretations, this correspondence becomes ill-defined: models may be penalized for producing valid but unanticipated answers, or rewarded for matching erroneous supervision. In such cases, apparent calibration error or ranking instability may reflect properties of benchmark noise rather than intrinsic model behavior (Chao et al., [2024](https://arxiv.org/html/2602.13964v3#bib.bib50 "Make large language model a better ranker")).

In practice, benchmark flaws commonly manifest in several recurring forms: (1) underspecified or ambiguous problem statements Min et al. ([2020](https://arxiv.org/html/2602.13964v3#bib.bib51 "AmbigQA: answering ambiguous open-domain questions")); (2) incorrect or mismatched answer keys (e.g., unit or format inconsistencies); (3) internal inconsistencies between the provided rationale and the final answer; and (4) reliance on contested facts, implicit conventions, or unstated assumptions. Notably, these failure modes often arise in different components of an evaluation item—the problem statement, the final answer, and the accompanying rationale—suggesting that item validity is multi-dimensional rather than binary.

### 2.2 HLE as an evaluation substrate

Humanity’s Last Exam (HLE) has emerged as a widely used benchmark for evaluating frontier language models on challenging, multi-domain questions. In practice, HLE is often reduced to a single scalar performance metric, typically accuracy, occasionally augmented with rationale- or chain-of-thought-based prompting. Implicit in this usage is the assumption that annotation noise is sufficiently small and uniformly distributed such that aggregate comparisons remain meaningful.

However, prior work has demonstrated that large-scale benchmarks may contain systematic annotation errors or unstable evaluation artifacts that meaningfully affect model rankings (Gema et al., [2025](https://arxiv.org/html/2602.13964v3#bib.bib47 "Are we done with mmlu?"); Prathifkumar et al., [2025](https://arxiv.org/html/2602.13964v3#bib.bib52 "Does swe-bench-verified test agent ability or model memory?")). To date, such concerns have not been systematically quantified for HLE, nor has their impact on evaluation outcomes been rigorously characterized. Consequently, it remains unclear to what extent observed performance differences on HLE reflect genuine capability gaps versus sensitivity to benchmark defects.

This gap motivates a principled re-examination of HLE as an evaluation substrate. Rather than treating benchmark errors as unstructured noise, our work explicitly characterizes item validity, distinguishes different sources of error and uncertainty, and assesses how these factors affect evaluation results. HLE-Verified operationalizes this perspective by making correctness, revision status, and epistemic uncertainty explicit at the dataset level, thereby enabling more reliable and interpretable model comparisons.

## 3 Dataset Verification Process and Methods

This section describes the construction protocol of HLE-Verified, including (i) the end-to-end item pipeline, (ii) the operational definitions of *verified* (gold), *revised*, and *uncertain* items, and (iii) the structured annotation schema used to record error types, revision actions, and item-level epistemic status. The protocol is designed to make benchmark validity explicit, auditable, and component-wise traceable, while preserving the original evaluation intent of HLE wherever possible.

![Refer to caption](https://arxiv.org/html/2602.13964v3/aidata_figs/hle_verified_pie_modern.png)

Figure 1: Structural composition of HLE-Verified.

### 3.1 Overview of the pipeline

Starting from the original HLE collection (2,500 items), we construct a single consolidated benchmark release, HLE-Verified, through a structured two-stage process. Stage I performs component-wise binary verification and produces a high-confidence gold subset. Stage II conducts systematic repair for items judged flawed but repairable, followed by re-verification. Items that remain indeterminate after these procedures are retained as an explicitly documented uncertain subset rather than discarded.

Each item is decomposed into three annotatable components: (i) the problem (statement plus image, if present), (ii) the final answer, and (iii) the rationale (reference solution, when available).

The problem and final answer are primary objects of correctness assessment, defining the evaluand and grading target, while the rationale serves as diagnostic support for detecting inconsistencies, missing assumptions, or explanation defects.

The resulting release comprises three disjoint subsets (Fig [1](https://arxiv.org/html/2602.13964v3#S3.F1 "Figure 1 ‣ 3 Dataset Verification Process and Methods ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam")):

1.  1.

    Gold subset (668 items): validated without modification.

2.  2.

    Revision subset (1,143 items): corrected and re-verified under preserved evaluation objectives.

3.  3.

    Uncertain subset (689 items): items whose validity remains indeterminate under available expertise and evidence.

Across both stages, we record structured item-level metadata including component-wise validity labels, error-type annotations, revision traces, adjudication notes, and uncertainty descriptors. These fields enable transparent accounting and downstream analyses stratified by defect type and epistemic status.

### 3.2 Stage I: component-wise verification

![Refer to caption](https://arxiv.org/html/2602.13964v3/aidata_figs/stage1.png)

Figure 2: HLE Revision Stage I. High-Difficulty Problem Validity Verification & Golden Subset Construction

##### Goal.

Stage I aims to determine whether an item is usable *as originally released*, without performing substantive content edits. The outcome of Stage I is a component-wise binary validity record and a high-confidence gold subset.

##### Operational definition of validity.

For each item component, validity is defined as follows:

-   •

    Problem validity: the statement (and image, if present) is well-posed, self-consistent, and sufficiently specified for a unique or properly qualified solution; assumptions and conventions needed for solving are either explicit or standard within the domain.

-   •

    Answer validity: the provided final answer is correct with respect to the problem specification, including units, format, and acceptable equivalence classes.

-   •

    Rationale validity: the reference solution is mathematically/logically sound, internally consistent, and compatible with the final answer (when the rationale is intended as an authoritative reference).

##### Multi-source verification and adjudication.

Stage I integrates three sources of evidence in a serial–hybrid workflow:

1.  1.

    External domain-expert screening. Independent subject-matter reviewers assess problem, answer, and rationale, providing component-wise binary judgments and concise notes.

2.  2.

    Model-assisted replication checks (pass@8). We invoke multiple frontier multimodal solvers under pass@8 sampling to generate independent solution attempts. Extracted final answers are normalized and compared against the reference answer under a fixed equivalence protocol (numeric tolerance, format normalization, semantic equivalence where applicable). This step provides reproducibility evidence and highlights items exhibiting extreme human–model disagreement.

3.  3.

    Internal expert adjudication. Internal reviewers synthesize supplier judgments and model-assisted evidence to make conservative inclusion decisions. Items enter the gold subset only when both problem and answer are judged unproblematic and no high-risk ambiguity is identified.

##### Stage I outcome.

Stage I yields the gold (verified) subset of 668 items that are retained without modification. All remaining items are carried forward either to Stage II for repair (if flawed but repairable) or to the uncertain pool (if indeterminate or high-risk).

### 3.3 Stage II: systematic revision and re-verification

![Refer to caption](https://arxiv.org/html/2602.13964v3/aidata_figs/stage2.png)

Figure 3: HLE Revision Stage II. Systematic Revision of Challenging Questions

##### Goal.

Stage II targets items that are judged flawed but *repairable* under the constraint that the original evaluation objective and reasoning target must be preserved. In other words, revisions are corrective rather than creative: they aim to restore well-posedness and correctness without altering what the item is intended to test.

##### Scope and boundary.

To ensure that revision results are objectively reviewable, Stage II focuses on domains where correctness can be reliably adjudicated and independently reproduced (mathematics, physics, chemistry, biomedicine, and computer science in our current release). Items in domains with weak verification boundaries or subjective conventions are handled conservatively (routed to the uncertain subset).

##### Revision workflow.

For each candidate item, Stage II generates independent repair proposals followed by expert convergence:

1.  1.

    Independent supplier repairs (two-track). Two independent expert teams propose corrective edits following a standardized sequence: *Problem Fix* →\\rightarrow *Solution Fix* →\\rightarrow *Answer Fix*, each accompanied by change notes. Items requiring substantive alteration of evaluation intent are marked non-repairable.

2.  2.

    Model-assisted auxiliary proposals. Multi-model sampling may generate additional repair candidates and stability checks. Model outputs serve as auxiliary evidence and do not replace expert adjudication.

3.  3.

    Final expert adjudication. Internal experts select or synthesize a canonical repaired version under the principles of objective preservation, correctness, and minimal necessary edits. Items remaining ambiguous or unverifiable are routed to the uncertain subset.

##### Stage II outcome.

Stage II yields the revision subset of 1,143 items that are corrected and re-verified as suitable for evaluation. Each revised item includes structured revision metadata, including which components were changed, what error types were addressed, and brief adjudication notes sufficient for auditing.

### 3.4 Uncertain subset: epistemic status and documentation

After verification and revision, 689 items remain uncertain. Rather than discarding them, we retain these items as an explicit epistemic category, reflecting cases where validity cannot be established with sufficient confidence. An item is assigned to the uncertain subset when resolution would require non-standard assumptions, authoritative external references, unresolved expert disagreement, or domain knowledge beyond the current verification scope.

Each uncertain item includes structured documentation:

-   •

    an uncertainty source label,

-   •

    and a required expertise tag indicating the type of specialist input needed for resolution.

This design separates capability limits from benchmark indeterminacy and enables principled community refinement.

### 3.5 Component-wise annotation framework and defect taxonomy

All HLE-Verified items are annotated at the component level to enable localized defect attribution, structured revision tracking, and reproducible auditing. Each item is decomposed into three semantically distinct components: the *problem statement* (Problem), the *reference rationale/solution* (Rationale), and the *final answer* (Answer). Defect labels and revision records are assigned to the specific component in which the issue originates, rather than treating item validity as a monolithic binary property.

Each defect category corresponds to a violation of component-level validity constraints, reflecting that item validity is structured and multi-dimensional. We define a taxonomy comprising 19 categories in total, organized as 5 problem-level errors, 10 rationale-level errors, and 4 answer-level errors. The taxonomy serves as the unified basis for (i) statistical reporting of defect prevalence, (ii) analysis of repair patterns in the revised subset, and (iii) public release of structured item-level metadata.

![Refer to caption](https://arxiv.org/html/2602.13964v3/aidata_figs/error_adjust.png)

Figure 4: HLE Component-wise Defect Taxonomy

##### Problem-level defects.

Problem-level defects arise from flaws in task specification that compromise interpretability, solvability, or semantic faithfulness.

-   •

    (Q1) Semantic Error. The statement is ambiguous, contradictory, or underspecified, admitting multiple interpretations.

-   •

    (Q2) Knowledge Error. The statement contains incorrect factual premises or misuse of established domain knowledge.

-   •

    (Q3) Missing Information. Essential constraints or assumptions required for solvability or uniqueness are omitted.

-   •

    (Q4) Theoretical Invalidity. The statement is invalid under accepted theory, supported by explicit corrective evidence.

-   •

    (Q5) Format Semantic Error (Problem). Notation, LaTeX, or terminology defects that distort or obscure intended meaning.

##### Rationale-level defects.

Rationale-level defects characterize failures in the *reference reasoning chain* provided by the benchmark. These categories apply to the authoritative solution text rather than to model-generated reasoning.

-   •

    (S1) Non-Redundancy Violation. Redundant reasoning steps that reduce minimality or auditability.

-   •

    (S2) Circular Reasoning. The conclusion depends on itself directly or indirectly.

-   •

    (S3) Empirical Soundness Violation. Steps contradict established facts or accepted knowledge.

-   •

    (S4) Step Inconsistency. Logical conflicts among intermediate steps.

-   •

    (S5) Domain Misapplication. Misuse of rules or theorems outside their valid scope.

-   •

    (S6) Overconfidence Bias. Incorrect content stated with unjustified certainty.

-   •

    (S7) Missing Prerequisite. Critical assumptions or conditions omitted while proceeding with derivation.

-   •

    (S8) Deceptive Similarity. Superficially plausible reasoning containing subtle structural corruption.

-   •

    (S9) Multi-Solution Inconsistency. Inconsistency across legitimate solution paths or case analyses.

-   •

    (S10) Format Semantic Error (Rationale). Symbol, LaTeX, unit, or terminology issues impairing verifiability or semantic alignment.

##### Answer-level defects.

Answer-level defects concern correctness, completeness, and verifiability of the final output.

-   •

    (A1) Incorrect Answer. The final answer is inconsistent with the correct solution (e.g., sign/value/boolean inversion).

-   •

    (A2) Incomplete Answer. Required cases, qualifiers, or multi-part conclusions are missing.

-   •

    (A3) Ambiguous / Ill-defined Answer. The answer is non-verifiable due to vagueness or mismatch with required output form.

-   •

    (A4) Format Semantic Error (Answer). Expression-level defects (e.g., LaTeX errors, incorrect symbols, unit inconsistencies) that impair interpretability without necessarily altering conceptual content.

##### Revision and epistemic annotations.

For items in the revised subset, we record component-level modification indicators (problem\_fix, solution\_fix, answer\_fix) together with concise change notes. Revisions are performed under the constraint that the *original evaluation objective and reasoning target* are preserved; corrections restore validity and internal consistency without redefining the underlying capability being assessed.

Each item additionally includes an epistemic status label (*verified*, *revised*, or *uncertain*) and structured uncertainty descriptors where applicable. These fields make correction history, defect attribution, and indeterminacy explicit at the dataset level, enabling transparent auditing and stratified evaluation analyses.

![Refer to caption](https://arxiv.org/html/2602.13964v3/x1.png)

Figure 5: Overall annotation outcomes on the problematic data of HLE. We report the counts of three labels—valid (1), invalid (0), and uncertain—for each annotatable component: *Problem*, *Answer*, and *Rationale*. The results show clear component-wise differences, with substantially more invalid/uncertain cases in *Answer* and especially *Rationale* than in *Problem*.

![Refer to caption](https://arxiv.org/html/2602.13964v3/x2.png)

Figure 6: Annotation outcome distribution across subject categories. For each subject category, we visualize the percentage of valid (1), invalid (0), and uncertain labels for the *Problem*, *Answer*, and *Rationale* components. The label composition varies by domain, while the *Rationale* component consistently exhibits the lowest validity and the highest uncertainty/invalidity across categories.

## 4 Dataset Statistical Analysis

We report a statistical analysis of the *problematic subset* of HLE-Verified, defined as items that did not enter the gold subset in Stage I. Our analysis focuses on (i) component-wise annotation outcomes (Problem, Answer, Rationale), and (ii) cross-domain variation in defect patterns. We further summarize recurring failure modes to contextualize the distributional findings.

### 4.1 Component-wise annotation outcomes

Each HLE instance is decomposed into three annotatable components—Problem, Answer, and Rationale—with labels valid (1), invalid (0), or uncertain. Figure [5](https://arxiv.org/html/2602.13964v3#S3.F5 "Figure 5 ‣ Revision and epistemic annotations. ‣ 3.5 Component-wise annotation framework and defect taxonomy ‣ 3 Dataset Verification Process and Methods ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam") presents the aggregate distribution across the problematic subset.

Across components, the Problem field exhibits the highest reliability. The majority of problem statements are structurally valid, and explicit structural errors constitute only a small fraction of cases. This indicates that most instances are well-posed at the task-description level. In contrast, reliability decreases at the Answer level. Only about half of the answers are fully valid, with a substantial portion either incorrect or difficult to verify. This suggests that correctness mismatches and solution inconsistencies are a major source of dataset noise. The most pronounced degradation appears in the Rationale component. Invalid rationales outnumber valid ones, indicating that reasoning chains frequently contain logical gaps, unsupported inferences, or incorrect derivations—even when the corresponding problem statement appears acceptable.

Importantly, the uncertain label constitutes a non-trivial fraction across all components. These cases typically arise from underspecified assumptions, ambiguous notation, incomplete derivations, or dependence on implicit conventions. The prevalence of uncertainty underscores that problematicness in HLE is not limited to outright incorrectness but often involves epistemic indeterminacy.

### 4.2 Cross-domain variation

Figure [6](https://arxiv.org/html/2602.13964v3#S3.F6 "Figure 6 ‣ Revision and epistemic annotations. ‣ 3.5 Component-wise annotation framework and defect taxonomy ‣ 3 Dataset Verification Process and Methods ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam") further disaggregates component-wise validity by subject category, revealing pronounced cross-domain differences.

For the Problem component, formal scientific domains exhibit markedly higher structural reliability. Math and Biology/Medicine both exceed 92% validity, while Chemistry remains comparatively strong at 73.3%. In contrast, Physics shows only 30.0% valid problem statements, and Engineering, Humanities/Social Science, and Other fall further to the 22–27% range. Notably, in these lower-validity domains, the majority of remaining cases are labeled uncertain (roughly 67–77%), rather than explicitly invalid, indicating verification ambiguity rather than structural error.

At the Answer level, domain gaps persist. Computer Science/AI (65.1%) and Chemistry (67.3%) achieve the highest answer validity rates. Math (59.6%) and Biology/Medicine (58.6%) remain above 50%, but both exhibit substantial invalid proportions (36.8% and 38.2%, respectively), suggesting that answer correctness in these domains is typically decidable and frequently incorrect rather than ambiguous. By contrast, Physics, Engineering, Humanities/Social Science, and Other remain below 30% valid, with uncertainty again dominating (approximately two-thirds to three-quarters of cases).

The divergence becomes most pronounced for the Rationale component. In Math and Biology/Medicine, invalid rationales dominate (65.9% and 66.4%, respectively), and Chemistry reaches an even higher invalid rate of 70.3%. These domains therefore display explicit logical or derivational errors even when problems are well-formed. In contrast, Engineering, Humanities/Social Science, and Other show extremely high uncertainty rates (approximately 73–77%) with virtually no explicit invalidation, reflecting verification difficulty rather than clear logical contradiction. Physics occupies an intermediate position, with high uncertainty (67.0%) but a non-trivial invalid share (10.9%).

Overall, these findings reinforce two structural observations. First, problematicness in HLE is rarely concentrated in problem statements alone; answer- and rationale-level defects account for the majority of reliability degradation. Second, domains differ not only in defect prevalence but in defect type: some disciplines exhibit predominantly incorrect content, while others exhibit epistemic indeterminacy due to verification complexity. These patterns justify a component-wise and epistemically explicit verification framework, as aggregate item-level labeling would obscure substantial heterogeneity in defect structure.

### 4.3 Component-wise Defect Distribution Across Subjects

We next analyze the distribution of defect categories within the revised subset of HLE-Verified using the 19-category component-wise taxonomy. Rather than reporting raw counts alone, we examine the *relative proportions* of defect types within each component, both globally and across subjects (Figure [S1](https://arxiv.org/html/2602.13964v3#A1.F1 "Figure S1 ‣ A.4 Component-wise Defect Distribution Across Subjects ‣ Appendix A Appendix ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam")).

##### Global component-level proportions.

When aggregating across subjects, three structural patterns emerge.

Answer-level defects. Across all five domains, *Incorrect Answer* (type 1) is consistently the dominant answer-level defect. Its within-component proportion ranges from 69.4% (Chemistry) to 97.2% (Biology/Medicine), with all subjects exceeding 70%. This indicates that answer-level failures are primarily deterministic correctness violations rather than ambiguity, partial specification, or formatting issues.

Rationale-level defects. Rationale defects are more heterogeneous across subjects. In Mathematics (40.1%) and Biology/Medicine (45.0%), type 3 defects (structural incompleteness) dominate, whereas Chemistry (40.0%) and Computer Science (63.3%) are led by type 10 defects (format-induced semantic errors). Physics shows a flatter distribution, with type 3 accounting for 25.0% of rationale defects. Overall, rationale instability arises primarily from missing intermediate structure and representation misalignment rather than classical logical contradictions.

Problem-level defects. Problem-level defect patterns are domain-sensitive. Mathematics (40.0%), Chemistry (56.5%), and Computer Science (94.6%) are dominated by type 5 defects (format semantic errors), whereas Physics is led by type 1 (57.1%) and Biology/Medicine by type 2 (33.3%). The near absence of dominant theoretical-invalidity categories suggests that most flawed items originate from specification or representation-level imprecision rather than fundamentally incorrect task concepts.

Taken together, these proportions indicate that reliability degradation in HLE is primarily driven by answer-key instability and representation-level specification errors, with pronounced disciplinary heterogeneity in defect structure.

##### Structural implications.

Across domains, several robust regularities emerge:

1.  1.

    Incorrect final answers dominate answer-level instability. Deterministic answer-key errors constitute the principal failure mode across all subjects.

2.  2.

    Rationale instability is primarily structural or representational. Missing intermediate steps and format-level semantic misalignment outweigh classical logical contradictions.

3.  3.

    Representation sensitivity is discipline-dependent. Format semantic errors play a particularly large role in Chemistry and Computer Science.

4.  4.

    Conceptual invalidity is not the dominant driver. Most defects arise from specification or answer-key instability rather than from fundamentally incorrect task concepts.

These findings suggest that defect patterns in HLE exhibit systematic structure rather than uniform random noise. Reliability risks are component-specific and discipline-sensitive, with answer correctness and rationale completeness constituting the dominant bottlenecks. This empirical structure justifies a component-wise verification protocol and cautions against treating benchmark noise as uniform or negligible.

Table 1: Dominant defect type (Top-1) by subject and component. Percentages denote within-component ratios.

Table [1](https://arxiv.org/html/2602.13964v3#S4.T1 "Table 1 ‣ Structural implications. ‣ 4.3 Component-wise Defect Distribution Across Subjects ‣ 4 Dataset Statistical Analysis ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam") summarizes the dominant defect type (Top-1) for each subject and component. The table highlights a consistent asymmetry: answer-level defects are overwhelmingly dominated by *Incorrect Answer* across all subjects, whereas problem- and rationale-level dominant defects vary by discipline. In particular, format-induced semantic errors dominate Computer Science, while structural incompleteness is most prevalent in Mathematics and Physics. These patterns reinforce the component-specific and domain-sensitive nature of reliability degradation in HLE.

### 4.4 Case Studies

To complement the quantitative findings, we present representative case studies illustrating structural defect patterns identified in HLE-Verified. These examples demonstrate that benchmark failures are not isolated anomalies but manifestations of systematic component-level weaknesses. We focus on three recurring families aligned with our component-wise analysis:

(1) Answer-level errors (incorrect conclusions, unit/format mismatches, inconsistency with the problem specification), (2) Rationale-level defects (missing prerequisites, circular reasoning, empirical violations, internally inconsistent derivations), and (3) Uncertainty-inducing ambiguity (underspecified assumptions or multiple valid interpretations).

These illustrate why component-wise auditing is essential: an item may present a well-formed problem statement yet remain unsuitable for evaluation due to an incorrect answer key or a structurally non-verifiable rationale. Below we present representative canonical cases selected by domain experts; the complete revision artifacts and detailed correction records are available in the open-sourced HLE-Verified benchmark.

Across domains, failures cluster in recurring structural patterns: theoretical–implementation confusion, constraint omission, numerical incoherence, sign inconsistency, invariant violation, and conceptual mislocalization. These are structural validity failures rather than cosmetic defects. Stage II revisions therefore restore logical soundness, theoretical alignment, and domain consistency, reinforcing that benchmark reliability depends on component-level integrity rather than superficial correctness.

## 5 Experimental Results

### 5.1 Experimental Setup

##### Models.

We evaluate the following frontier models: GPT-5.2-Thinking (OpenAI, [2025](https://arxiv.org/html/2602.13964v3#bib.bib5 "Introducing gpt-5.2")), Gemini3-Pro-Preview (Google DeepMind, [2025](https://arxiv.org/html/2602.13964v3#bib.bib6 "Gemini Pro")), Claude-Opus4.5 (Anthropic, [2025](https://arxiv.org/html/2602.13964v3#bib.bib8 "Claude opus 4.5")), Claude-Opus4.6 (Anthropic, [2026](https://arxiv.org/html/2602.13964v3#bib.bib9 "Claude opus 4.6")), Grok-4.1 (fast-reasoning) (xAI, [2025](https://arxiv.org/html/2602.13964v3#bib.bib7 "Grok 4.1 fast")), DeepSeek-V3.2-Thinking (Liu et al., [2025](https://arxiv.org/html/2602.13964v3#bib.bib10 "Deepseek-v3. 2: pushing the frontier of open large language models")), Qwen3-Max-Thinking (Qwen, [2026a](https://arxiv.org/html/2602.13964v3#bib.bib11 "Pushing qwen3-max-thinking beyond its limits")), Qwen3.5-Plus (Qwen, [2026b](https://arxiv.org/html/2602.13964v3#bib.bib12 "Qwen3.5: accelerating productivity with native multimodal agents")). All models were evaluated using the same system prompt recommended by the HLE official guidelines, along with each model’s own default recommended decoding configuration. To reduce variance from stochastic decoding, we run five independent rollouts per item and report avg5 accuracy, i.e., the average correctness across the five sampled completions (without additional post-hoc selection unless otherwise stated).

##### Metrics.

We report (i) Accuracy (Acc) and (ii) Calibration Error (Cali Err). Calibration error is computed from the model’s self-reported confidence and the binary correctness label: we parse each response-level confidence into c∈\[0,1\]c\\in\[0,1\] and compute

<table id="S5.Ex5"><tbody><tr><td></td><td><math id="S5.Ex5.m1" alttext="\text{Cali Err}=100\times\mathrm{calib\_err}(c,y;\,p=2,\beta=100)," display="block" intent=":literal"><semantics><mrow><mtext>Cali Err</mtext><mo>=</mo><mn>100</mn><mo lspace="0.222em" rspace="0.222em">×</mo><mi>calib</mi><mi mathvariant="normal">_</mi><mi>err</mi><mrow><mo stretchy="false">(</mo><mi>c</mi><mo>,</mo><mi>y</mi><mo rspace="0.337em">;</mo><mi>p</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>β</mi><mo>=</mo><mn>100</mn><mo stretchy="false">)</mo></mrow><mo>,</mo></mrow><annotation encoding="application/x-tex">\text{Cali Err}=100\times\mathrm{calib\_err}(c,y;\,p=2,\beta=100),</annotation></semantics></math></td><td></td></tr></tbody></table>

where y∈{0,1}y\\in\\{0,1\\} indicates whether the item is answered correctly, and calib​\_​err\\mathrm{calib\\\_err} is a smoothed L2L\_{2} miscalibration estimator with smoothing parameter β\\beta. Note that this calib​\_​err\\mathrm{calib\\\_err} estimator follows the official HLE evaluation code.

##### Evaluation Datasets.

We report results on (i) the Full Set (Raw HLE Full vs. Revised HLE-Verified Full) to quantify the end-to-end impact on the benchmark, and (ii) a Revised Subset comparison (Raw HLE Subset vs. Revised HLE-Verified Subset) limited to items that were edited/flagged during our verification process, which isolates the effect of flawed items and their corrections. Note that, to ensure comprehensive revisions, we also corrected the original rationales and released them to the open-source community. However, under the standard HLE benchmark evaluation, items with errors only in the rationale do not affect the final scores, since mainstream evaluation uses only the problem and answer. Therefore, the Revised Subset in this experimental section includes only items for which at least one of the problem/answer fields was revised. Unless otherwise specified, all evaluation sets used in this section are the text-only subset of HLE.

### 5.2 Main Evaluation: HLE vs. HLE-Verified

Table [2](https://arxiv.org/html/2602.13964v3#S5.T2 "Table 2 ‣ Full-set results. ‣ 5.2 Main Evaluation: HLE vs. HLE-Verified ‣ 5 Experimental Results ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam") summarizes performance on the original benchmark and on HLE-Verified. We focus on the accuracy shift

<table id="S5.Ex6"><tbody><tr><td></td><td><math id="S5.Ex6.m1" alttext="\Delta\text{Acc}=\mathrm{Acc}(\text{HLE-Verified})-\mathrm{Acc}(\text{HLE})," display="block" intent=":literal"><semantics><mrow><mrow><mrow><mi mathvariant="normal">Δ</mi><mo lspace="0em" rspace="0em">​</mo><mtext>Acc</mtext></mrow><mo>=</mo><mrow><mrow><mi>Acc</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mtext>HLE-Verified</mtext><mo stretchy="false">)</mo></mrow></mrow><mo>−</mo><mrow><mi>Acc</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mtext>HLE</mtext><mo stretchy="false">)</mo></mrow></mrow></mrow></mrow><mo>,</mo></mrow><annotation encoding="application/x-tex">\Delta\text{Acc}=\mathrm{Acc}(\text{HLE-Verified})-\mathrm{Acc}(\text{HLE}),</annotation></semantics></math></td><td></td></tr></tbody></table>

computed either on the Full Set or on the Revised Subset.

##### Large accuracy gains on revised items.

On the Revised Subset, all models exhibit substantial positive shifts, indicating that flawed items in the original benchmark systematically suppress measured performance. Specifically, accuracy increases by: Gemini-3-pro (+29.94), GPT-5.2 (+38.04), Claude-Opus4.5 (+32.94), Grok-4.1 fast-reasoning (+34.82), Claude-Opus4.6 (+30.13), and DeepSeek-V3.2 (+39.58) percentage points. The magnitude of these shifts implies that a non-trivial fraction of “errors” on raw HLE are attributable to benchmark issues rather than model capability.

##### Calibration improves after verification.

Calibration error decreases consistently after revision on the same subset (e.g., GPT-5.2: 63→\\rightarrow28; DeepSeek-V3.2: 70→\\rightarrow28; Grok-4.1: 83→\\rightarrow47), suggesting that flawed items can also distort confidence-based evaluation by inducing confidently incorrect (or otherwise miscalibrated) responses. In contrast, HLE-Verified yields a more faithful estimate of the confidence–correctness relationship.

##### Full-set results.

On the Full Set, we also observe consistent gains after verification, though smaller in magnitude than on the Revised Subset, as expected since most items are unchanged. Specifically, accuracy increases by: Gemini-3-pro (+7.58), GPT-5.2 (+9.95), Claude-Opus4.5 (+8.68), Grok-4.1 fast-reasoning (+9.26), Claude-Opus4.6 (+7.75), DeepSeek-V3.2 (+10.79), and Qwen3-Max-Thinking (+8.92) percentage points. Calibration error likewise decreases across models (e.g., GPT-5.2: 45→\\rightarrow36; DeepSeek-V3.2: 56→\\rightarrow46; Grok-4.1: 73→\\rightarrow63), indicating that HLE-Verified not only raises measured accuracy but also yields more reliable confidence estimates at benchmark scale.

Table 2: Results on Full Set and Revised Subset.

![Refer to caption](https://arxiv.org/html/2602.13964v3/x3.png)

![Refer to caption](https://arxiv.org/html/2602.13964v3/x4.png)

Figure 7: HLE Raw LeaderBoard vs HLE-Verified LeaderBoard

![Refer to caption](https://arxiv.org/html/2602.13964v3/x5.png)

Figure 8: HLE Raw vs HLE-Verified on Revised Set

![Refer to caption](https://arxiv.org/html/2602.13964v3/x6.png)

![Refer to caption](https://arxiv.org/html/2602.13964v3/x7.png)

![Refer to caption](https://arxiv.org/html/2602.13964v3/x8.png)

![Refer to caption](https://arxiv.org/html/2602.13964v3/x9.png)

![Refer to caption](https://arxiv.org/html/2602.13964v3/x10.png)

![Refer to caption](https://arxiv.org/html/2602.13964v3/x11.png)

Figure 9: HLE Raw vs HLE-Verified on Revised Set across Subject Categories.

![Refer to caption](https://arxiv.org/html/2602.13964v3/figs/Main_Evaluation/confidence_analysis.png)

Figure 10: Impact of item repair on model confidence. Mean confidence shift Δ​Conf\=𝔼​\[cVerified−cRaw\]\\Delta\\text{Conf}=\\mathbb{E}\[c\_{\\text{Verified}}-c\_{\\text{Raw}}\] computed on the Full Set (blue) and on the Problem-Error Subset containing items with statement-level errors (red). Confidence increases consistently after repair on the error subset, while shifts on the full set are near zero due to dilution by unchanged items.

### 5.3 Comparison on Revised Subset across Subject Categories

##### Category-level gains are uneven but consistently positive.

Figure [9](https://arxiv.org/html/2602.13964v3#S5.F9 "Figure 9 ‣ Full-set results. ‣ 5.2 Main Evaluation: HLE vs. HLE-Verified ‣ 5 Experimental Results ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam") further breaks down the Revised Subset by subject category for several representative models. Across *all* categories, we observe a consistent Raw→\\rightarrowVerified accuracy increase, confirming that the benefits of verification are not confined to a single domain. However, the magnitude of improvement varies substantially by subject: the largest jumps appear in Physics and Biology/Medicine, where raw accuracies are particularly low but rise sharply after correction, suggesting that benchmark flaws in these categories more frequently affect the problem/answer fields and thus the final pass/fail outcome. In contrast, Chemistry and Computer Science/AI show smaller yet still clear gains, indicating fewer or less severe scoring-impacting issues among the revised items. Overall, this category-wise analysis highlights that raw HLE introduces *non-uniform* measurement noise across subjects, and HLE-Verified mitigates this distortion, yielding a more faithful cross-domain comparison of model capability.

### 5.4 Confidence as a Diagnostic for Noisy Items

A natural question is whether models’ self-reported confidence is sensitive to noise in the benchmark itself. If noisy items systematically elicit lower confidence, confidence (and related calibration signals) may serve as a practical diagnostic for item flaws; conversely, if models remain highly confident on flawed items, confidence-based analyses may be unreliable. We therefore study the relationship between model confidence and item quality by comparing confidence statistics before and after verification and repair. To align with this goal, we focus on items whose *problem statements* are flagged as erroneous, and we compare each model’s confidence on the original version versus the repaired version of the *same* item. Intuitively, if an item is flawed, we expect models to express lower confidence on the raw statement due to missing conditions, ambiguities, or contradictions; after repair, the clarified statement should reduce uncertainty and lead to higher confidence.

Accordingly, for each model we compute the mean confidence shift

<table id="S5.Ex7"><tbody><tr><td></td><td><math id="S5.Ex7.m1" alttext="\Delta\text{Conf}\;=\;\mathbb{E}\!\left[c_{\text{Verified}}-c_{\text{Raw}}\right]," display="block" intent=":literal"><semantics><mrow><mrow><mrow><mi mathvariant="normal">Δ</mi><mo lspace="0em" rspace="0em">​</mo><mtext>Conf</mtext></mrow><mo lspace="0.558em" rspace="0.558em">=</mo><mrow><mpadded width="0.497em"><mi>𝔼</mi></mpadded><mo lspace="0em" rspace="0em">​</mo><mrow><mo>[</mo><mrow><msub><mi>c</mi><mtext>Verified</mtext></msub><mo>−</mo><msub><mi>c</mi><mtext>Raw</mtext></msub></mrow><mo>]</mo></mrow></mrow></mrow><mo>,</mo></mrow><annotation encoding="application/x-tex">\Delta\text{Conf}\;=\;\mathbb{E}\!\left[c_{\text{Verified}}-c_{\text{Raw}}\right],</annotation></semantics></math></td><td></td></tr></tbody></table>

reported both on the Full Set and on a Problem-Error Subset consisting only of items with statement-level errors. Figure [10](https://arxiv.org/html/2602.13964v3#S5.F10 "Figure 10 ‣ Full-set results. ‣ 5.2 Main Evaluation: HLE vs. HLE-Verified ‣ 5 Experimental Results ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam") shows that confidence increases consistently after repair on the Problem-Error Subset across all evaluated models, with gains ranging from roughly +1.83 to +11.08 confidence points (absolute). In contrast, the Full-Set shifts are near zero (and can even be slightly negative), which is expected because the majority of items are unchanged and thus dilute the effect.

These results suggest that statement-level noise in raw HLE may not only depress accuracy but also *reduce model confidence* in a systematic way. As a result, confidence (and related calibration signals) could be a useful diagnostic for flagging potentially noisy or ambiguous items, and HLE-Verified appears to mitigate one source of uncertainty that might otherwise distort confidence-based evaluation.

## 6 Conclusion

We introduced HLE-Verified, a verified and revised benchmark intended to strengthen the scientific reliability of HLE-based evaluations. Our work makes benchmark flaws measurable, provides a transparent correction pipeline, and quantifies how such flaws bias reported accuracy and calibration.

Beyond this release, the disputed set provides a roadmap for community-driven improvements. We expect that a continuously maintained verification process, with structured metadata and clear contribution guidelines, can make exam-style benchmarks more robust and more informative for tracking real progress in language model reasoning.

## References

-   Claude opus 4.5. Note: [https://www.anthropic.com/news/claude-opus-4-5](https://www.anthropic.com/news/claude-opus-4-5) Cited by: [§5.1](https://arxiv.org/html/2602.13964v3#S5.SS1.SSS0.Px1.p1.1 "Models. ‣ 5.1 Experimental Setup ‣ 5 Experimental Results ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   Anthropic (2026) Claude opus 4.6. Note: [https://www.anthropic.com/news/claude-opus-4-6](https://www.anthropic.com/news/claude-opus-4-6) Cited by: [§5.1](https://arxiv.org/html/2602.13964v3#S5.SS1.SSS0.Px1.p1.1 "Models. ‣ 5.1 Experimental Setup ‣ 5 Experimental Results ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   Center for AI Safety, Scale AI, and HLE Contributors Consortium (2026) A benchmark of expert-level academic questions to assess AI capabilities. Nature 649, pp. 1139–1146. External Links: [Document](https://dx.doi.org/10.1038/s41586-025-09962-4) Cited by: [§1](https://arxiv.org/html/2602.13964v3#S1.p1.1 "1 Introduction ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   W. Chao, Z. Zheng, H. Zhu, and H. Liu (2024) Make large language model a better ranker. arXiv preprint arXiv:2403.19181. Cited by: [§2.1](https://arxiv.org/html/2602.13964v3#S2.SS1.p2.1 "2.1 Why benchmark errors matter ‣ 2 Background ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   A. P. Gema, J. O. J. Leang, G. Hong, A. Devoto, A. C. M. Mancino, R. Saxena, X. He, Y. Zhao, X. Du, M. R. G. Madani, et al. (2025) Are we done with mmlu?. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pp. 5069–5096. Cited by: [§2.1](https://arxiv.org/html/2602.13964v3#S2.SS1.p1.2 "2.1 Why benchmark errors matter ‣ 2 Background ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam"), [§2.2](https://arxiv.org/html/2602.13964v3#S2.SS2.p2.1 "2.2 HLE as an evaluation substrate ‣ 2 Background ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   Google DeepMind (2025) Gemini Pro. Note: [https://deepmind.google/models/gemini/pro/](https://deepmind.google/models/gemini/pro/) Cited by: [§5.1](https://arxiv.org/html/2602.13964v3#S5.SS1.SSS0.Px1.p1.1 "Models. ‣ 5.1 Experimental Setup ‣ 5 Experimental Results ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger (2017) On calibration of modern neural networks. In International conference on machine learning, pp. 1321–1330. Cited by: [§2.1](https://arxiv.org/html/2602.13964v3#S2.SS1.p2.1 "2.1 Why benchmark errors matter ‣ 2 Background ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   S. Kadavath, T. Conerly, A. Askell, T. Henighan, D. Drain, E. Perez, N. Schiefer, Z. Hatfield-Dodds, N. DasSarma, E. Tran-Johnson, et al. (2022) Language models (mostly) know what they know. arXiv preprint arXiv:2207.05221. Cited by: [§2.1](https://arxiv.org/html/2602.13964v3#S2.SS1.p2.1 "2.1 Why benchmark errors matter ‣ 2 Background ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   lhl (2026) Hle-gpqa-error-claims. Note: [https://github.com/lhl/hle-gpqa-error-claims](https://github.com/lhl/hle-gpqa-error-claims)GitHub repository. Cited by: [§1](https://arxiv.org/html/2602.13964v3#S1.p2.1 "1 Introduction ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   P. Liang, R. Bommasani, T. Lee, D. Tsipras, D. Soylu, M. Yasunaga, Y. Zhang, D. Narayanan, Y. Wu, A. Kumar, et al. (2022) Holistic evaluation of language models. arXiv preprint arXiv:2211.09110. Cited by: [§2.1](https://arxiv.org/html/2602.13964v3#S2.SS1.p1.2 "2.1 Why benchmark errors matter ‣ 2 Background ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   A. Liu, A. Mei, B. Lin, B. Xue, B. Wang, B. Xu, B. Wu, B. Zhang, C. Lin, C. Dong, et al. (2025) Deepseek-v3. 2: pushing the frontier of open large language models. arXiv preprint arXiv:2512.02556. Cited by: [§5.1](https://arxiv.org/html/2602.13964v3#S5.SS1.SSS0.Px1.p1.1 "Models. ‣ 5.1 Experimental Setup ‣ 5 Experimental Results ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   S. Min, J. Michael, H. Hajishirzi, and L. Zettlemoyer (2020) AmbigQA: answering ambiguous open-domain questions. arXiv preprint arXiv:2004.10645. Cited by: [§2.1](https://arxiv.org/html/2602.13964v3#S2.SS1.p3.1 "2.1 Why benchmark errors matter ‣ 2 Background ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   OpenAI (2025) Introducing gpt-5.2. Note: [https://openai.com/zh-Hans-CN/index/introducing-gpt-5-2/](https://openai.com/zh-Hans-CN/index/introducing-gpt-5-2/) Cited by: [§5.1](https://arxiv.org/html/2602.13964v3#S5.SS1.SSS0.Px1.p1.1 "Models. ‣ 5.1 Experimental Setup ‣ 5 Experimental Results ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   T. Prathifkumar, N. S. Mathews, and M. Nagappan (2025) Does swe-bench-verified test agent ability or model memory?. arXiv preprint arXiv:2512.10218. Cited by: [§2.2](https://arxiv.org/html/2602.13964v3#S2.SS2.p2.1 "2.2 HLE as an evaluation substrate ‣ 2 Background ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   T. Qwen (2026a) Pushing qwen3-max-thinking beyond its limits. External Links: [Link](https://qwen.ai/blog?id=qwen3-max-thinking) Cited by: [§5.1](https://arxiv.org/html/2602.13964v3#S5.SS1.SSS0.Px1.p1.1 "Models. ‣ 5.1 Experimental Setup ‣ 5 Experimental Results ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   T. Qwen (2026b) Qwen3.5: accelerating productivity with native multimodal agents. External Links: [Link](https://qwen.ai/blog?id=qwen3.5) Cited by: [§5.1](https://arxiv.org/html/2602.13964v3#S5.SS1.SSS0.Px1.p1.1 "Models. ‣ 5.1 Experimental Setup ‣ 5 Experimental Results ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   \[17\] (2025) Research: i forensically audited humanity’s last exam. Note: [https://www.reddit.com/r/LocalLLaMA/comments/1qhz9e2/research\_i\_forensicaudited\_humanitys\_last\_exam/](https://www.reddit.com/r/LocalLLaMA/comments/1qhz9e2/research_i_forensicaudited_humanitys_last_exam/)Reddit thread on r/LocalLLaMA. Cited by: [§1](https://arxiv.org/html/2602.13964v3#S1.p2.1 "1 Introduction ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   A. White (2025) About 30% of humanity’s last exam chemistry/biology answers are likely wrong. Note: [https://www.futurehouse.org/research-announcements/hle-exam](https://www.futurehouse.org/research-announcements/hle-exam)FutureHouse research announcement. Cited by: [§1](https://arxiv.org/html/2602.13964v3#S1.p2.1 "1 Introduction ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").
-   xAI (2025) Grok 4.1 fast. Note: [https://x.ai/news/grok-4-1-fast](https://x.ai/news/grok-4-1-fast) Cited by: [§5.1](https://arxiv.org/html/2602.13964v3#S5.SS1.SSS0.Px1.p1.1 "Models. ‣ 5.1 Experimental Setup ‣ 5 Experimental Results ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam").

## Appendix A Appendix

### A.1 LLM Judge Prompt

#### A.1.1 LLM Judge Prompt in Stage I

#### A.1.2 LLM Judge Prompt in Stage II

### A.2 Quality control and decision principles

We adopt conservative decision principles throughout both stages, reflecting the asymmetric risk inherent in benchmark release. Including a flawed item can introduce systematic evaluation bias and distort cross-model comparisons, whereas excluding a potentially valid item primarily reduces coverage without inducing measurement error. Consequently, our protocol prioritizes minimizing false inclusion over maximizing dataset size.

##### Conservative inclusion.

Inclusion into the gold or revision subsets requires positive evidence of component-wise validity. Items are admitted only when the problem and final answer are judged well-posed, correct, and stable under expert scrutiny. The absence of detected defects is not considered sufficient; rather, validity must be affirmatively supported. Rationale-level defects alone do not automatically disqualify an item, since evaluation is typically answer-based. However, when a rationale defect signals deeper ambiguity, hidden assumptions, or incompatibility with the final answer, the item is escalated for re-audit or routed to revision.

##### Model-assisted checks as auxiliary evidence.

Model-based replication outcomes (e.g., pass@8 success rates) are treated as diagnostic signals rather than adjudicative authority. Extreme patterns—such as systematic failure across multiple strong solvers—may trigger expert re-audit for underspecification, hidden conventions, or answer-key errors. Conversely, high solver agreement is not regarded as proof of correctness. Models serve as stochastic probes that expose potential instability, but final correctness judgments remain grounded in expert evaluation.

##### Expert recruitment and profile.

The verification and revision process was conducted by domain experts recruited through two independent supplier teams and supported by internal adjudication specialists. The participating experts are predominantly Master’s- and Ph.D.-level researchers from research-intensive universities and institutes, with formal academic training in mathematics, physics, chemistry, biomedicine, and computer science. Their academic backgrounds align directly with the disciplinary scope of HLE-Verified, enabling subject-matter–grounded validation and revision across all covered domains. Independent acceptance reviewers with doctoral-level expertise further examined complex or contentious cases.

### A.3 Case Study

### A.4 Component-wise Defect Distribution Across Subjects

![Refer to caption](https://arxiv.org/html/2602.13964v3/aidata_figs/error_dist_grid_subjects.png)

Figure S1: HLE Error Type Distribution by Subject

### A.5 Cross-subject proportional differences.

Figure [S1](https://arxiv.org/html/2602.13964v3#A1.F1 "Figure S1 ‣ A.4 Component-wise Defect Distribution Across Subjects ‣ Appendix A Appendix ‣ HLE-Verified: A Systematic Verification and Structured Revision of Humanity’s Last Exam") reveals substantial domain-level variation.

Mathematics. Answer-level defects are overwhelmingly dominated by *Incorrect Answer* (89.4%). At the rationale level, type 3 (40.1%) is the leading defect, reflecting structural incompleteness in derivations. Problem-level defects are more moderate in scale, with type 5 (40.0%) most frequent. This pattern suggests that mathematical items are generally conceptually stable but vulnerable to answer-key inaccuracies and incomplete reasoning articulation.

Physics. Physics exhibits relatively small defect counts overall. Answer-level errors remain dominated by type 1 (80.0%). Problem-level defects are led by type 1 (57.1%), while rationale defects show a flatter distribution with type 3 accounting for 25.0%. Compared to other domains, physics demonstrates comparatively less concentration in a single rationale category.

Chemistry. Chemistry shows a more balanced defect structure. Although incorrect answers (71.4%) remain the leading answer-level issue, both problem- (56.5%) and rationale-level (40.0%) defects are dominated by format semantic errors. This reflects the domain’s sensitivity to symbolic precision and representational alignment.

Biology/Medicine. Biology/Medicine displays the highest dominance of incorrect answers (97.2%). Rationale-level defects are primarily type 3 (45.0%), indicating incomplete explanatory structure. Problem-level defects are more evenly distributed, with type 2 (33.3%) emerging as the most frequent category.

Computer Science. Computer Science exhibits the most pronounced representation sensitivity. Format semantic errors (type 5) dominate problem-level defects (94.6%), while type 10 dominates rationale-level defects (63.3%). Answer-level incorrectness (78.1%) remains substantial but less extreme than in mathematics or biomedicine.
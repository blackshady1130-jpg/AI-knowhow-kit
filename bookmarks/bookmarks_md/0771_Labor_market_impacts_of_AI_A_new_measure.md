# Labor market impacts of AI: A new measure and early evidence

Mar 5, 2026 · Anthropic Economic Research

Written by Maxim Massenkoff and Peter McCrory.

[Read in PDF](https://cdn.sanity.io/files/4zrzovbb/website/2b5bbaf2c1eb81dbf6e6fb813c1a24e35a64d376.pdf)

## Key findings

- No systematic increase in unemployment for highly exposed workers since late 2022, though suggestive evidence that hiring of younger workers has slowed in exposed occupations
- Workers in the most exposed professions are more likely to be older, female, more educated, and higher-paid
- Occupations with higher observed exposure are projected by the BLS to grow less through 2034
- AI is far from reaching its theoretical capability: actual coverage remains a fraction of what's feasible
- A new measure of AI displacement risk — observed exposure — combines theoretical LLM capability and real-world usage data

## Introduction

The rapid diffusion of AI is generating a wave of research measuring and forecasting its impacts on labor markets. But the track record of past approaches gives reason for humility. A prominent attempt to measure job offshorability identified roughly a quarter of US jobs as vulnerable, but a decade on, most of those jobs maintained healthy employment growth.

In this paper, we present a new framework for understanding AI's labor market impacts, and test it against early data, finding limited evidence that AI has affected employment to date.

## Measuring exposure

Our approach combines data from three sources:

1. Task-level exposure estimates from Eloundou et al. (2023) — whether it is theoretically possible for an LLM to make a task at least twice as fast
2. Anthropic's own usage data (as measured in the Anthropic Economic Index)
3. The O*NET database, which enumerates tasks associated with around 800 unique occupations in the US

### A new measure of occupational exposure

Our new measure, **observed exposure**, quantifies: of those tasks that LLMs could theoretically speed up, which are actually seeing automated usage in professional settings? A job's exposure is higher if:

- Its AI-impacted tasks make up a larger share of the overall role
- It has a relatively higher share of automated use patterns or API implementation
- Its tasks are performed in work-related contexts
- Its tasks see significant usage in the Anthropic Economic Index
- Its tasks are theoretically possible with AI

### Most exposed occupations

Computer Programmers are at the top with 75% coverage, followed by Customer Service Representatives, and Data Entry Keyers at 67% coverage. At the bottom end, 30% of workers have zero coverage (Cooks, Motorcycle Mechanics, Lifeguards, Bartenders, etc.).

## How exposure tracks with projected job growth

For every 10 percentage point increase in coverage, the BLS's growth projection drops by 0.6 percentage points. Workers in the top quartile of exposure are 16 percentage points more likely to be female, 11 percentage points more likely to be white, earn 47% more, and have higher levels of education.

## Initial results

We study trends in unemployment using the Current Population Survey. The average change in the gap since the release of ChatGPT is small and insignificant, suggesting that the unemployment rate of the more exposed group has increased slightly but the effect is indistinguishable from zero.

### Young workers

Entry into the most exposed jobs decreases by about half a percentage point. The averaged estimate in the post-ChatGPT era is a 14% drop in the job finding rate in exposed occupations for workers aged 22-25, though this is just barely statistically significant. There is no such decrease for workers older than 25.

## Discussion

We find no impact on unemployment rates for workers in the most exposed occupations, although there's tentative evidence that hiring into those professions has slowed slightly for workers aged 22-25. Our work is a first step toward cataloging the impact of AI on the labor market.

---
Source: https://www.anthropic.com/research/labor-market-impacts

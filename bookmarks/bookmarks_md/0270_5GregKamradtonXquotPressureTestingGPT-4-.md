---
url: https://twitter.com/GregKamradt/status/1722386725635580292
title: "X 上的 Greg Kamradt：“Pressure Testing GPT-4-128K With Long Context Recall\n\n128K tokens of context is awesome - but what's performance like?\n\nI wanted to find out so I did a “needle in a haystack” analysis\n\nSome expected (and unexpected) results\n\nHere's what I found:\n\nFindings:\n* GPT-4’s recall https://t.co/nHMokmfhW5” / X"
published: "2023-11-08T22:52:50.000Z"
captured_at: "2026-03-08T11:09:24.717Z"
---

# X 上的 Greg Kamradt：“Pressure Testing GPT-4-128K With Long Context Recall

128K tokens of context is awesome - but what's performance like?

I wanted to find out so I did a “needle in a haystack” analysis

Some expected (and unexpected) results

Here's what I found:

Findings:
* GPT-4’s recall https://t.co/nHMokmfhW5” / X

Pressure Testing GPT-4-128K With Long Context Recall 128K tokens of context is awesome - but what's performance like? I wanted to find out so I did a “needle in a haystack” analysis Some expected (and unexpected) results Here's what I found: Findings: \* GPT-4’s recall performance started to degrade above 73K tokens \* Low recall performance was correlated when the fact to be recalled was placed between at 7%-50% document depth \* If the fact was at the beginning of the document, it was recalled regardless of context length So what: \* No Guarantees - Your facts are not guaranteed to be retrieved. Don’t bake the assumption they will into your applications \* Less context = more accuracy - This is well know, but when possible reduce the amount of context you send to GPT-4 to increase its ability to recall \* Position matters - Also well know, but facts placed at the very beginning and 2nd half of the document seem to be recalled better Overview of the process: \* Use Paul Graham essays as ‘background’ tokens. With 218 essays it’s easy to get up to 128K tokens \* Place a random statement within the document at various depths. Fact used: “The best thing to do in San Francisco is eat a sandwich and sit in Dolores Park on a sunny day.” \* Ask GPT-4 to answer this question only using the context provided \* Evaluate GPT-4s answer with another model (gpt-4 again) using

evals \* Rinse and repeat for 15x document depths between 0% (top of document) and 100% (bottom of document) and 15x context lengths (1K Tokens > 128K Tokens) Next Steps To Take This Further: \* Iterations of this analysis were evenly distributed, it’s been suggested that doing a sigmoid distribution would be better (it would tease out more nuanced at the start and end of the document) \* For rigor, one should do a key:value retrieval step. However for relatability I did a San Francisco line within PGs essays. Notes: \* While I think this will be directionally correct, more testing is needed to get a firmer grip on GPT4s abilities \* Switching up prompt with vary results \* 2x tests were run at large context lengths to tease out more performance \* This test cost ~$200 for API calls (a single call at 128K input tokens costs $1.28) \* Thank you to

for being a sounding board and providing great next steps
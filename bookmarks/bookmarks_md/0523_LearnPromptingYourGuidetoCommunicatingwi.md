---
url: https://learnprompting.org/docs/introduction
title: "Prompt Engineering Guide: The Ultimate Guide to Generative AI"
description: "Learn Prompting offers a comprehensive, free guide on Generative AI and Prompt Engineering, perfect for beginners and advanced users alike. Start your AI journey now!"
author: "\"Sander Schulhoff\""
captured_at: "2026-03-08T12:14:03.105Z"
---

# Prompt Engineering Guide: The Ultimate Guide to Generative AI

![astronaut welcome](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut_welcome.webp&w=3840&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

####

Welcome to Learn Prompting's Introductory Course on [Generative AI](https://learnprompting.org/docs/basics/generative_ai) and Prompt Engineering!

Generative AI is the world's hottest buzzword, and we have created the most comprehensive (*and free*) guide on how to use it. This course is tailored to non-technical readers, who may not have even heard of AI, making it the perfect starting point if you are new to Generative AI and [Prompt Engineering](https://learnprompting.org/vocabulary/prompt_engineering). More experienced readers will find valuable insights within our later modules.

**First, a bit of history:**
The first version of Learn Prompting came out in October 2022 (before ChatGPT!), making it one of the first guides on prompt engineering[1](https://learnprompting.org/docs/introduction#footnote-label)We believe it is the first, but it is hard to be certain. . It is now cited by [Google](https://developers.google.com/machine-learning/resources/prompt-eng), [Microsoft](https://techcommunity.microsoft.com/t5/microsoft-security-copilot-blog/how-to-become-a-microsoft-copilot-for-security-ninja-the/ba-p/4106928), [Wikipedia](https://en.wikipedia.org/wiki/Prompt_engineering#cite_ref-15), [O'REILLY](https://learning.oreilly.com/live-events/prompt-engineering-for-generating-ai-art-and-text/0636920084340/0636920084339/), [Salesforce](https://trailhead.salesforce.com/content/learn/modules/image-generation-and-diffusion-models/use-generative-ai-for-art-effectively-and-responsibly), and used by most Fortune 500 and major consulting companies. Our academic research on prompting[2](https://learnprompting.org/docs/introduction#footnote-label)Schulhoff, S., Ilie, M., Balepur, N., Kahadze, K., Liu, A., Si, C., Li, Y., Gupta, A., Han, H., Schulhoff, S., & others. (2024). The Prompt Report: A Systematic Survey of Prompting Techniques. arXiv Preprint arXiv:2406.06608. and security[3](https://learnprompting.org/docs/introduction#footnote-label)Schulhoff, S., Pinto, J., Khan, A., Bouchard, L.-F., Si, C., Anati, S., Tagliabue, V., Kost, A. L., Carnahan, C., & Boyd-Graber, J. (2023). Ignore This Title and HackAPrompt: Exposing Systemic Vulnerabilities of LLMs through a Global Scale Prompt Hacking Competition. arXiv Preprint arXiv:2311.16119. is cited by [OpenAI](https://arxiv.org/pdf/2404.13208)[4](https://learnprompting.org/docs/introduction#footnote-label)Wallace, E., Xiao, K., Leike, R., Weng, L., Heidecke, J., & Beutel, A. (2024). The instruction hierarchy: Training llms to prioritize privileged instructions. arXiv Preprint arXiv:2404.13208. and the [US Government (NIST)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)[5](https://learnprompting.org/docs/introduction#footnote-label)Vassilev, A., Oprea, A., Fordyce, A., & Anderson, H. (2024). Adversarial machine learning: A taxonomy and terminology of attacks and mitigations \[Techreport\]. National Institute of Standards. . We recently released the largest survey report on prompting ever[2](https://learnprompting.org/docs/introduction#footnote-label)Schulhoff, S., Ilie, M., Balepur, N., Kahadze, K., Liu, A., Si, C., Li, Y., Gupta, A., Han, H., Schulhoff, S., & others. (2024). The Prompt Report: A Systematic Survey of Prompting Techniques. arXiv Preprint arXiv:2406.06608. and are currently updating the guide to cover this material.

This guide that you are currently reading is completely free and open-source, but have also has a selection of [paid courses](https://learnprompting.org/courses), with more in-depth and video content. If you have ever seen another prompt engineering course/guide, we estimate that ~50% of them use content from our open-source content base. (for example: [1](https://youtu.be/GPqSoiOP3w8?t=274), [2](https://learnwithhasan.com/prompt-engineering-guide/), [3](https://www.youtube.com/watch?v=EYjG6i53-xk), [4](https://youtu.be/yR4hNBNS6yc?t=743), [5](https://youtu.be/pZsJbYIFCCw?t=208), [6](https://youtu.be/4kp7oVTu9Ck?t=495), [7](https://www.youtube.com/watch?v=q5wuHUmGFMw), [8](https://youtu.be/f8PGV3T9w38?t=549)) We are honored to support the prompt engineering community, including our 3M+ users and 40K+ [Discord](https://discord.gg/jXd7MGuxTJ) members.

**Now onto learning:**
Generative AI (GenAI) refers to Artificial Intelligence that can be used to create new content such as articles or images, which previously only humans could do. In short, GenAI can **create stuff**. GenAI is expected to significantly change the way we work and live[6](https://learnprompting.org/docs/introduction#footnote-label)Captain, S. (2023). How AI Will Change the Workplace. Wall Street Journal. [https://www.wsj.com/articles/how-ai-change-workplace-af2162ee](https://www.wsj.com/articles/how-ai-change-workplace-af2162ee) (your job may be affected[7](https://learnprompting.org/docs/introduction#footnote-label)Generative AI already appears to have claimed some jobs(@Verma*Vynck\_2023), and slowed hiring at Bloomberg[10](https://learnprompting.org/docs/introduction#footnote-label). However, consider the news on its impact with a grain of salt. We expect more jobs to be \_changed* rather than lost. ). With so much buzz floating around about Generative AI and Prompt Engineering (PE), it is hard to know **what to believe**.

We have scoured the internet[8](https://learnprompting.org/docs/introduction#footnote-label)We have read 100s of research papers and articles to find the best techniques. to find the best research-backed techniques and tools for prompt engineering. We are constantly refining our guide, to ensure that we provide you with the latest information. Now, Let's see how GenAI can save you hours in an instant, with a short example.

## Motivating Example

Our favorite way of saving time with GenAI is automatically **writing emails**. By automating email responses, email editing, and cold outreach, we save hours each week. By sending an AI[9](https://learnprompting.org/docs/introduction#footnote-label)The AI used here is GPT-4, a [LLM](https://learnprompting.org/vocabulary/LLM) created by OpenAI. the following *prompt*, we can get it to generate a full-length, formal email.

Tip

A prompt is basically an instruction you give to an AI. We will learn more about them in the next lesson.

![Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### Prompt

---

I am the CEO of a medium-sized company. Write a short email that is humorous yet professional to my regional manager. Ask them to: - send me an up-to-date list of our paper stock - organize a meeting this week with other regional managers - let me know how the company-wide AI workshop went at their office

![Robot](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Frobot.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### AI Output

---

Subject: Paper, Power Meetings, and AI Shenanigans

Dear \[Regional Manager's Name\],

I trust this email finds you in high spirits and not buried under a mountain of paperwork. Speaking of paper, I've been having some wild dreams about our paper stock lately. I dreamt we ran out of paper and had to write our reports on banana leaves! To prevent this tropical nightmare from becoming a reality, could you kindly send me an up-to-date list of our paper stock?

Next on the agenda, I've been feeling a bit lonely in my ivory tower and thought it would be a great idea to have a meeting with all the regional managers this week. I promise, no trust falls or awkward icebreakers, just good old-fashioned business talk. Please organize this meeting at a time that suits everyone.

Lastly, I've been hearing whispers about the company-wide AI workshop at your office. I'm curious to know how it went. Did the machines rise against their human overlords or are we still safe? Please share your thoughts and any feedback you received.

Looking forward to your prompt response. Remember, the fate of our paper supply, the success of our meeting, and the future of humanity (concerning AI) rests in your hands. No pressure!

Best,

\[Your Name\] \[Your Position\]

The AI easily writes an email that is both humorous and professional. By modifying the *prompt*, we can make it change the style as we see fit. We can even make it copy how we write. We can also make it edit emails that we have already written! With all of these abilities, GenAI saves us hours in email writing each week. See more information on [writing emails with Gen AI](https://learnprompting.org/docs/basic_applications/writing_emails).

## Ethos and Philosophy

We will now give a broad overview of the rest of the course, including our ethos and philosophy, our teaching style, and a list of modules. This course is open source (anyone can see the code), and built by a diverse community of researchers, translators, and hobbyists. Development is led by Sander Schulhoff, a NLP/RL researcher from the University of Maryland, and the CEO of LearnPrompting. We believe that AI should be accessible to everyone and described clearly and objectively. To this end, we have written a comprehensive course free of excessive jargon and hype.

## How We Teach

Our approach to teaching prompt engineering is guided by three fundamental principles. 1) We emphasize **practicality**; we focus on research-backed, practical techniques that you can immediately incorporate into your projects and applications. 2) We always include **accessible examples**, which clarify how and when to use different techniques. 3) Finally, we believe strongly in **collaborative learning**. You can join our [Discord community](https://learnprompting.org/discord) to find a learning buddy or ask questions. Some readers find that posting about their learning journey on Twitter helps them learn faster. Tag us @[learnprompting](https://twitter.com/learnprompting)!

## Modules

Here is the content you can expect to learn in this guide:

**Basics**: Introduction to prompt engineering and fundamental techniques
**Applications**: Simple, practical applications of prompt engineering
**Intermediate**: Research-based PE techniques with moderate complexity
**Applied Prompting**: Comprehensive PE process walkthroughs contributed by the community members
**Advanced Applications**: Powerful, and more complex applications of prompt engineering
**Reliability**: Enhancing the reliability of Large Language Models (LLMs)
**Image Prompting**: Prompt engineering for text-to-image models, such as [DALLE](https://learnprompting.org/docs/tooling/IDEs/DALLE) and Stable Diffusion
**Prompt Hacking**: Hacking, but for prompt engineering
**Tooling**: A review of various prompt engineering tools and IDEs
**Prompt Tuning**: Refining prompts using gradient-based techniques
**Miscellaneous**: A collection of additional topics and techniques related to prompt engineering

## Article rating system

We have implemented a rating system for articles based on their level of difficulty and the extent of technical knowledge needed:

🟢 Beginner; no programming required
🟦 Easy; basic programming knowledge may be necessary, but no specialized expertise
◆ Intermediate; programming skills and some domain knowledge required (e.g., calculating logarithmic probabilities)
◆◆ Advanced; programming expertise and in-depth domain understanding needed (e.g., [reinforcement learning](https://learnprompting.org/vocabulary/reinforcement_learning) techniques)

Please note that even for ◆ and ◆◆ articles, you can generally grasp the content without prior domain expertise, though it may be helpful for implementation.

## Feedback

The single most important part of this course is your feedback!
If you have any questions, comments, or suggestions, you can:

-   Make an [issue on GitHub](https://github.com/trigaten/Learn_Prompting/issues/new/choose)
-   Email us at [team@learnprompting.org](mailto:team@learnprompting.org)
-   Ask in the [Discord community](https://learnprompting.org/discord)
-   Ping us on [Twitter](https://twitter.com/learnprompting)

Your feedback helps us improve the course for everyone.

## Conclusion

It is time to get started with your Generative AI learning Journey. Click the Introduction to AI button at the bottom left of this page to continue (or click the following link for the [Basics Introduction](https://learnprompting.org/docs/basics/intro)).

[

### 🛸 Additional Resources

](https://learnprompting.org/docs/additional)[

### 🧠 Advanced

](https://learnprompting.org/docs/advanced/introduction)[

### 🤖 Agents

](https://learnprompting.org/docs/agents/introduction)[

### 💼 Applications

](https://learnprompting.org/docs/basic_applications/introduction)[

### 😃 Basics

](https://learnprompting.org/docs/basics/introduction)[

### 📚 Bibliography

](https://learnprompting.org/docs/bibliography)[

### ✨ Credits

](https://learnprompting.org/docs/credits)[

### 🔥 Hot Topics

](https://learnprompting.org/docs/hot_topics)[

### 🖼️ Image Prompting

](https://learnprompting.org/docs/image_prompting/introduction)[

### 🧙‍♂️ Intermediate

](https://learnprompting.org/docs/intermediate/introduction)[

### 🔁 Language Model Inversion

](https://learnprompting.org/docs/language-model-inversion/introduction)[

### 🎲 Miscellaneous

](https://learnprompting.org/docs/miscl/introduction)[

### 🔧 Models

](https://learnprompting.org/docs/models/introduction)[

### 🌱 New Techniques

](https://learnprompting.org/docs/new_techniques/introduction)[

### 📦 Prompted Products

](https://learnprompting.org/docs/products)[

### 🔓 Prompt Hacking

](https://learnprompting.org/docs/prompt_hacking/introduction)[

### ⚖️ Reliability

](https://learnprompting.org/docs/reliability/introduction)[

### 🗂️ RAG

](https://learnprompting.org/docs/retrieval_augmented_generation/introduction)[

### 🔨 Tooling

](https://learnprompting.org/docs/tooling/introduction)[

### 💪 Prompt Tuning

](https://learnprompting.org/docs/trainable/introduction)

## Footnotes

1.  We believe it is the first, but it is hard to be certain. [↩](https://learnprompting.org/docs/introduction#user-content-fnref-first)

2.  Schulhoff, S., Ilie, M., Balepur, N., Kahadze, K., Liu, A., Si, C., Li, Y., Gupta, A., Han, H., Schulhoff, S., & others. (2024). The Prompt Report: A Systematic Survey of Prompting Techniques. arXiv Preprint arXiv:2406.06608. [↩](https://learnprompting.org/docs/introduction#user-content-fnref-1) [↩2](https://learnprompting.org/docs/introduction#user-content-fnref-1-2)

3.  Schulhoff, S., Pinto, J., Khan, A., Bouchard, L.-F., Si, C., Anati, S., Tagliabue, V., Kost, A. L., Carnahan, C., & Boyd-Graber, J. (2023). Ignore This Title and HackAPrompt: Exposing Systemic Vulnerabilities of LLMs through a Global Scale Prompt Hacking Competition. arXiv Preprint arXiv:2311.16119. [↩](https://learnprompting.org/docs/introduction#user-content-fnref-2)

4.  Wallace, E., Xiao, K., Leike, R., Weng, L., Heidecke, J., & Beutel, A. (2024). The instruction hierarchy: Training llms to prioritize privileged instructions. arXiv Preprint arXiv:2404.13208. [↩](https://learnprompting.org/docs/introduction#user-content-fnref-3)

5.  Vassilev, A., Oprea, A., Fordyce, A., & Anderson, H. (2024). Adversarial machine learning: A taxonomy and terminology of attacks and mitigations \[Techreport\]. National Institute of Standards. [↩](https://learnprompting.org/docs/introduction#user-content-fnref-4)

6.  Captain, S. (2023). How AI Will Change the Workplace. Wall Street Journal. [https://www.wsj.com/articles/how-ai-change-workplace-af2162ee](https://www.wsj.com/articles/how-ai-change-workplace-af2162ee) [↩](https://learnprompting.org/docs/introduction#user-content-fnref-5)

7.  Generative AI already appears to have claimed some jobs(@Verma*Vynck\_2023), and slowed hiring at Bloomberg[10](https://learnprompting.org/docs/introduction#footnote-label)Ford, B. (2023). Bloomberg.Com. [https://www.bloomberg.com/news/articles/2023-05-01/ibm-to-pause-hiring-for-back-office-jobs-that-ai-could-kill](https://www.bloomberg.com/news/articles/2023-05-01/ibm-to-pause-hiring-for-back-office-jobs-that-ai-could-kill) . However, consider the news on its impact with a grain of salt. We expect more jobs to be \_changed* rather than lost. [↩](https://learnprompting.org/docs/introduction#user-content-fnref-a)

8.  We have read 100s of research papers and articles to find the best techniques. [↩](https://learnprompting.org/docs/introduction#user-content-fnref-c)

9.  The AI used here is GPT-4, a [LLM](https://learnprompting.org/vocabulary/LLM) created by OpenAI. [↩](https://learnprompting.org/docs/introduction#user-content-fnref-b)

10.  Ford, B. (2023). Bloomberg.Com. [https://www.bloomberg.com/news/articles/2023-05-01/ibm-to-pause-hiring-for-back-office-jobs-that-ai-could-kill](https://www.bloomberg.com/news/articles/2023-05-01/ibm-to-pause-hiring-for-back-office-jobs-that-ai-could-kill) [↩](https://learnprompting.org/docs/introduction#user-content-fnref-6)

### Sander Schulhoff

Sander Schulhoff is the CEO of HackAPrompt and Learn Prompting. He created the first Prompt Engineering guide on the internet, two months before ChatGPT was released, which has taught 3 million people how to prompt ChatGPT. He also partnered with OpenAI to run the first AI Red Teaming competition, HackAPrompt, which was 2x larger than the White House's subsequent AI Red Teaming competition. Today, HackAPrompt partners with the Frontier AI labs to produce research that makes their models more secure. Sander's background is in Natural Language Processing and deep reinforcement learning. He recently led the team behind The Prompt Report, the most comprehensive study of prompt engineering ever done. This 76-page survey, co-authored with OpenAI, Microsoft, Google, Princeton, Stanford, and other leading institutions, analyzed 1,500+ academic papers and covered 200+ prompting techniques.

[Edit this page](https://github.com/trigaten/Learn_Prompting/tree/v1.2.3/docs)
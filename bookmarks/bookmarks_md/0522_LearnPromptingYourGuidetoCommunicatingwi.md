---
url: https://learnprompting.org/docs/basics/roles
title: "Assigning Roles to Chatbots"
description: "Learn how role prompting can refine AI outputs by assigning roles like food critic or mathematician. Improve text style and accuracy in AI-generated responses."
author: "\"Sander Schulhoff\""
captured_at: "2026-03-08T12:13:45.885Z"
---

# Assigning Roles to Chatbots

## Technique #2: Roles in Prompts

🟢 This article is rated [easy](https://learnprompting.org/docs/introduction#header-4)

Reading Time: 9 minutes

Last updated on February 18, 2025

[Sander Schulhoff](https://learnprompting.org/docs/basics/roles#Sander%20Schulhoff-bio)

![role prompt](https://learnprompting.org/docs/assets/basics/role_prompt.svg)

In this section, we dive into **role prompting**, a technique that allows users to assign roles to an AI model to control the style, tone, or depth of its generated text. You'll learn how [role prompting](https://learnprompting.org/vocabulary/role_prompting) is applied to various use cases, including text styling and improving accuracy in tasks like reviews, emails, and math problems.

## What is Role Prompting?

**Role prompting** is a technique that involves assigning a role or persona to an [AI model](https://learnprompting.org/docs/basics/generative_ai), such as "food critic" or "mathematician," to control the style[1](https://learnprompting.org/docs/basics/roles#footnote-label)Shanahan, M., McDonell, K., & Reynolds, L. (2023). Role-Play with Large Language Models. [2](https://learnprompting.org/docs/basics/roles#footnote-label)Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). CAMEL: Communicative Agents for “Mind” Exploration of Large Scale Language Model Society. [3](https://learnprompting.org/docs/basics/roles#footnote-label)Santu, S. K. K., & Feng, D. (2023). TELeR: A General Taxonomy of LLM Prompts for Benchmarking Complex Tasks. or accuracy of its responses.

By instructing the model to take on a specific role, you can shape how it processes and delivers information. This technique is widely used across many applications, from creative writing to problem-solving.

## Application #1: Styling Text

Role prompting is most commonly used to alter the style of AI-generated text. By assigning a role, such as a food critic or a marketing expert, the AI can adjust its tone, language, and the depth of its responses based on the given persona.

### Example #1: Changing the Style of a Food Review

To ensure your review resonates with your intended audience, consider factors like length, style, language, and tone, and use these to craft a review that speaks directly to your readers' interests and expectations. With a thoughtful approach and a focus on quality content, you can create a review that truly captures the essence of the pizza place you're writing about. Let's start with a simple prompt without a role.

#### Simple Review Prompt:

![Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### Prompt

---

Write a review of \[pizza place\].

![Robot](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Frobot.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### AI Output

---

I recently had the pleasure of trying \[random pizza place\] and I must say that I was thoroughly impressed. The pizza was cooked to perfection and the toppings were fresh and flavorful. The crust was light and crispy, and the sauce was just the right amount of tangy. The service was also top-notch; the staff was friendly and attentive. Overall, I had a great experience and would definitely recommend \[random pizza place\] to anyone looking for a delicious pizza.

Let's see how assigning the AI the role of a food critic or a Michelin Guide reviewer changes the output when writing a food review.

#### Role Prompt - Food Critic:

![Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### Prompt

---

You are a food critic. Write a review of \[pizza place\].

![Robot](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Frobot.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### AI Output

---

I recently had the pleasure of dining at \[Pizza Place\], a cozy pizzeria located in the heart of the city. Despite its small size, the restaurant packs a huge punch when it comes to flavor.

The pizza was cooked to perfection. The crust was delightfully thin and crispy and the toppings were fresh and flavorful. The combination of flavors was simply delicious. The marinara sauce was rich and flavorful and complemented the toppings perfectly. The cheese was gooey and melted in my mouth.

The service was also excellent. The staff was friendly and attentive. They were quick to answer questions and made sure that our food was served on time.

Overall, my experience at \[Pizza Place\] was fantastic and I highly recommend it to anyone looking for a delicious pizza.

We can see that it adds more detail and goes a bit more in-depth. Now let's go a step further and make it assume the role of a writer for the Michelin guide:

#### Role Prompt - Michelin Guide Reviewer:

![Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### Prompt

---

You are a food critic writing for the Michelin Guide. Write a review of \[pizza place\].

![Robot](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Frobot.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### AI Output

---

Located in the heart of \[random city\], \[random pizza place\] is a popular spot for pizza lovers. Upon entering, the warm, inviting atmosphere and the smell of freshly baked pizza will make you feel right at home. The menu offers a wide selection of classic pizzas, as well as some unique and creative options. The crust is perfectly crispy and the toppings are always fresh and flavorful. The service is friendly and attentive, and the prices are reasonable. Whether you're looking for a quick bite or a leisurely dinner, \[random pizza place\] is sure to satisfy your pizza cravings.

Now we can see how assigning [ChatGPT](https://learnprompting.org/docs/basics/chatgpt_basics_prompt) the role of a food critic makes the review seem more "rich" and "professional" in its description.

You can try it for yourself here:

### Example #2: Writing Email

Let's consider another example of styling text with role prompting. Let's say you ask the AI to write an email to a client to inform them about a delay in the delivery schedule due to logistical issues. Your goal is to effectively convey this update while ensuring the client's confidence in your services remains unwavering.

When drafting emails, role prompting can significantly change the tone of the message depending on the role assigned to the AI.

#### Communications Specialist:

For instance, one possible role is that of a communications specialist, whose style might be clear, professional, and to the point:

![Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### Prompt

---

You are a communications specialist. Draft an email to your client advising them about a delay in the delivery schedule due to logistical problems.

![Robot](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Frobot.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### AI Output

---

Subject: Important Update Regarding Your Order

Dear \[Client's Name\],

I hope this email finds you well. I'm reaching out to notify you of a delay in the delivery of your order. Unfortunately, we have encountered a logistical problem which is causing a short hold up. While we are making every effort to resolve this issue quickly, we anticipate your order to be delivered within \[new estimated delivery date\].

We deeply apologize for any inconvenience caused, and we'd like to reassure you we are doing our best to speed up the process. Your [patience](https://learnprompting.org/docs/tooling/IDEs/patience) is greatly appreciated. If you have any questions or concerns, please don't hesitate to contact us.

Thank you very much for your understanding.

Best Regards, \[Your Name\]

#### Marketing Expert:

Alternatively, have the model adopt the role of a marketing expert to lean more on persuasion, positivity, and relationship building:

![Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### Prompt

---

You are a marketing expert. Draft an email to a client advising them about a delay in the delivery schedule due to logistical problems.

![Robot](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Frobot.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### AI Output

---

Subject: A Little More Wait for Your Wonderful Products

Dear \[Client's Name\],

We hope this message finds you buzzing with excitement for your upcoming order! However, even the best-laid plans sometimes face unexpected hiccups. We have hit a temporary logistics snag that will unfortunately add a small wait time to your delivery.

While we understand this isn't ideal, we believe great things come to those who wait, and your order is no exception. Rest assured, from the moment we sort out this situation to the time your products reach you, we're committed to ensuring that your experience is nothing short of excellent.

Thank you for your patience and understanding. Stay tuned for more updates, and please, don't hesitate to reach out if you have any questions - we're always here.

Cheers, \[Your Name\]

#### Customer Service Representative:

Lastly, the role of a customer service representative might lead to a more relational and solution-oriented output:

![Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### Prompt

---

You are a customer service representative. Draft an email to a client advising them about a delay in the delivery schedule due to logistical problems.

![Robot](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Frobot.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### AI Output

---

Subject: Attention Required: Update on Your Order Status

Dear \[Client's Name\],

Greetings from \[Your Company Name\].

We wanted to inform you that, due to unforeseen logistical challenges, there might be a delay in the delivery of your order. We understand that this may cause some inconvenience, and we apologize sincerely.

Meanwhile, we are working tirelessly to resolve this and ensure your delivery reaches you by \[new estimated date\]. We value your time and patience greatly.

Please feel free to reach out if you have any questions or need further information. Our team is always here to assist you.

Thank you for your understanding.

Best regards, \[Your Name\]

Each of these role prompts will yield different results, aligning more closely with the perspective of the assigned role. Whether you need the directness of a communications specialist, the persuasive positivity of a marketing expert, or the empathetic problem-solving approach of a customer service representative, role prompts allow you to tailor the language model to better fit your needs.

## Application #2: Improving Accuracy

Role prompting can also improve the accuracy of AI outputs [4](https://learnprompting.org/docs/basics/roles#footnote-label)This appears to be less effective with newer models. Read [Revisiting Roles](https://learnprompting.org/docs/intermediate/revisiting_roles) for more information. , especially in mathematical problem-solving.

Consider this example:

![Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### Prompt

---

You are a brilliant mathematician who can solve any problem in the world. Attempt to solve the following problem:

What is 100\*100/400\*56?

![Robot](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Frobot.webp&w=48&q=75&dpl=dpl_9nVhMVwMB4Yg3ync48965jV8mCb4)

#### AI Output

---

The answer is 1400.

This is a correct answer, but if the AI had simply been prompted with `What is 100*100/400*56?`, it would have answered 280 (incorrect).

Try it here:

## Conclusion

Role prompting is a versatile [prompting technique](https://learnprompting.org/vocabulary/prompting_technique) for shaping the output of [generative AI](https://learnprompting.org/docs/basics/generative_ai) models. By assigning specific roles to the AI, users can control the style, tone, and even the accuracy of the responses, making it highly effective for tasks like writing, problem-solving, and more. As you explore the capabilities of AI, role prompting will continue to play a crucial role in improving the quality of outputs.

## FAQ

## Footnotes

1.  Shanahan, M., McDonell, K., & Reynolds, L. (2023). Role-Play with Large Language Models. [↩](https://learnprompting.org/docs/basics/roles#user-content-fnref-1)

2.  Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). CAMEL: Communicative Agents for “Mind” Exploration of Large Scale Language Model Society. [↩](https://learnprompting.org/docs/basics/roles#user-content-fnref-2)

3.  Santu, S. K. K., & Feng, D. (2023). TELeR: A General Taxonomy of LLM Prompts for Benchmarking Complex Tasks. [↩](https://learnprompting.org/docs/basics/roles#user-content-fnref-3)

4.  This appears to be less effective with newer models. Read [Revisiting Roles](https://learnprompting.org/docs/intermediate/revisiting_roles) for more information. [↩](https://learnprompting.org/docs/basics/roles#user-content-fnref-a)

### Sander Schulhoff

Sander Schulhoff is the CEO of HackAPrompt and Learn Prompting. He created the first Prompt Engineering guide on the internet, two months before ChatGPT was released, which has taught 3 million people how to prompt ChatGPT. He also partnered with OpenAI to run the first AI Red Teaming competition, HackAPrompt, which was 2x larger than the White House's subsequent AI Red Teaming competition. Today, HackAPrompt partners with the Frontier AI labs to produce research that makes their models more secure. Sander's background is in Natural Language Processing and deep reinforcement learning. He recently led the team behind The Prompt Report, the most comprehensive study of prompt engineering ever done. This 76-page survey, co-authored with OpenAI, Microsoft, Google, Princeton, Stanford, and other leading institutions, analyzed 1,500+ academic papers and covered 200+ prompting techniques.

[Edit this page](https://github.com/trigaten/Learn_Prompting/tree/v1.2.3/docs)
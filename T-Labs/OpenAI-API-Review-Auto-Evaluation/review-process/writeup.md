## Question 1

What is the most common sentiment observed in your sample of 50 reviews according to your OpenAI labeled data?

According to the labeled data, negative sentiment was the most commonly observed across the 50 reviews. This suggests a high level of dissatisfaction among customers, particularly around product taste and packaging — themes that appeared frequently in the reviews.

## Question 2

How reliable do you believe these labels are? Look at the respective labels OpenAI has generated for specific reviews, does it seem like the large language model accurately described the user's review? What risk do model hallucinations introduce into this analysis?

Model Reliability & Hallucination Risks
During testing, I noticed fluctuations in the number of sentiment labels returned by GPT-4o-mini — at times exceeding the number of input reviews. I noticed that HTML tags, escape characters, and special formatting (e.g., <br />, \", etc.) may be caused the model to misinterpret single reviews as multiple inputs.

To resolve this, I investigated the application of regex-based preprocessing to clean and standardize the review data and used a truncation safeguard to ensure the number of sentiments and reviews matched: sentiments = sentiments[:len(reviews)]

This greatly reduced hallucinations and stabilized model output. That said, some hallucinations still persist, which can introduce noise into downstream analysis (eg., plots, etc.) — potentially leading to inaccurate insights or missed opportunities.

With continued refinement — through better preprocessing, prompt engineering, or even fine-tuning — GPT-4o-mini can perform quite reliably. But for production use, particularly in customer-facing products that automate sentiment labeling, I’d recommend also testing more robust models like GPT-4 or GPT-4 Turbo for improved consistency, lowering the risk of hallucination, and better alignment with high-stakes decision-making workflows.

## Question 3

Using the most common sentiment, what would you recommend to this Coconut Water producer to improve customer satisfaction? Should they continue to pursue current market/product outcomes, or does there exist an opportunity for this business to improve its product?

Based on the overwhelming negative feedback, the company has a clear opportunity for improvement. A more granular analysis of these reviews reveals a recurring theme — specifically around taste. Common issues/concerns include added sugar or unnatural sweetness, an 'old' or stale flavor, and a plastic-like aftertaste.

That said, many customers expressed enthusiasm for the newer mango flavor, highlighting it as a standout option. I would recommend the company revisit its formula, packaging materials, and sourcing strategy to address these recurring issues — while continuing to offer the flavors that are resonating well with customers. This balanced approach can help rebuild trust and enhance brand loyalty.
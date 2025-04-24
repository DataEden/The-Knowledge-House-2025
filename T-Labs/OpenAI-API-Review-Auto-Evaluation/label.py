from openai import OpenAI # Importing the OpenAI class from the openai module 
import re # the re module for regular expression operations.

def get_sentiment(text: list) -> list:

    """
    Classifies each review in a list using gpt-4o-mini and returns a list of
    sentiment labels: positive, neutral, negative, or irrelevant.

    Args:
        text (list): A list of review strings.

    Returns:
        list: A list of sentiment labels.
    """
    # Check if input is a list of strings
    if not isinstance(text, list) or not all(isinstance(item, str) for item in text):
        return "Wrong input. text must be list array of strings."
    
    # Check if input is empty or contains non-string elements
    if not text:
        return "Wrong input. text must be an array of strings."
    
    # Inline cleaning: remove <br>, <br/>, and <br /> tags (case-insensitive)
    # and replace newlines with spaces.
    cleaned_text = [re.sub(r'<[^>]+>', ' ', review, flags=re.IGNORECASE).replace("\n", " ").strip()  for review in text]   
    
    # Remove extra spaces and newlines
    joined_reviews = "\n".join(cleaned_text)

    #print(" Cleaned input reviews being sent to gpt-4o-mini:\n")
    #print(joined_reviews)
   
    client = OpenAI() # Create a object of the OpenAI class.

    # Define the system and user prompts.
    # The system prompt sets the context for the model, and the user prompt provides the input data.
    system_prompt = (
        "You are an expert sentiment classifier. For each review:\n"
        "- Classify each review with one of these labels: positive, neutral, negative, or irrelevant.\n"
        "- Return only one label per line.\n"
        "- Never Split the review into multiple lines.\n"
        "- Do NOT include numbering, punctuation, brackets, or extra formatting.\n"
        "- Be sensitive to emotional tone, sarcasm, irony, or context.\n"
        "- Watch for transitions like 'but', 'however', or 'overall', as these may indicate a negative sentiment.\n"
        "- Always base your label on the full review, not just a portion.\n"
    )

    user_prompt = (
        "Hi! It is May. Please label each review below as either positive, neutral, negative, or irrelevant. \
            And Please return only 50 responses per the amount of reviews: \n\n"
        f"{joined_reviews}"
    )
    # Send the request to OpenAI API
    # The chat completion method is used to generate a response based on provided message(s).
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
      ]
    )
    # Get response from the API
    # The expected response is in the format of a chat message.
    raw_output = response.choices[0].message.content

    # Split the response into lines and strips whitespaces
    # Response is processed to ensure each label is in lowercase and stripped of leading/trailing whitespaces.
    sentiments = [line.strip().lower() for line in raw_output.splitlines() if line.strip()]

    # Check if the number of sentiments matches number of reviews
    # If API returned more sentiments than reviews, truncate list to match number of reviews.
    if len(sentiments) > len(text):
        sentiments = sentiments[:len(text)]
    elif len(sentiments) < len(text):
        missing_response = len(text) - len(sentiments)
        sentiments += ["irrelevant"] * missing_response
     
    # Print the number of reviews and sentiments returned
    # Useful for debugging and sanity checking, ensuring the function works as expected.
    print(f"🧾 Number of reviews: {len(text)}")
    print(f"📋 Number of sentiments returned: {len(sentiments)}")

    return sentiments
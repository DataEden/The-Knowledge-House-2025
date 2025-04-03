from openai import OpenAI

def get_sentiment(text: list) -> list:
    """
    
    """
    # Check if the input is a list of strings
    if not isinstance(text, list) or not all(isinstance(item, str) for item in text):
        return "Wrong input. text must be an array of strings."
    # Check if the list is empty
    if not text:
        return "Wrong input. text must be an array of strings."
    
    client = OpenAI()

    system_prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
        """
    user_prompt = "Here are the product reviews:\n" + "\n".join(text)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
            {"role": "developer", "content": system_prompt},
            {"role": "user", "content": user_prompt},
            
        ]
        
    )
    text_response = completion.choices[0].message.content

    return text_response(text) #[line.strip().lower() for line in text_response.splitlines()]




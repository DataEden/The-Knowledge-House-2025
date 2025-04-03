from openai import OpenAI

def get_sentiment(text: list) -> list:
    
    """
    Classifies each review in a list using gpt-4o-mini and returns a list of
    labels: positive, neutral, negative, or irrelevant. Handles edge cases for
    empty lists or wrong input types.

    """

    # Check if the input is a list of strings
    if not isinstance(text, list) or not all(isinstance(item, str) for item in text):
        return "Wrong input. text must be an array of strings."
    
    # Check if the list is empty
    if not text:
        return "Wrong input. text must be an array of strings."
    
    client = OpenAI()

    system_prompt = f"""
    "You are an expert sentiment classifier. "
    "Classify each review as one of the following: positive, neutral, negative, or irrelevant. "
    Return only a single word per line, in the same order as the input. "
    "Do not include punctuation, numbering, brackets, or any additional formatting. "
    "The result should be plain text only, one label per line."
    """
    user_prompt =  "Hey Quantum! I've got some reviews for you to classify. Please label each line as" \
    " one of the following: positive, neutral, negative, or irrelevant.\n\n" + "\n".join(text)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
            
        ]
        
    )
    text_response = completion.choices[0].message.content

    return [line.strip().lower() for line in text_response.splitlines()]




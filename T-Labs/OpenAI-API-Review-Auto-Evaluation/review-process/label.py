from openai import OpenAI

def get_sentiment(text: list) -> list:
    
    """
    This function classifies each review in a list using gpt-4o-mini and returns a list of
    labels: positive, neutral, negative, or irrelevant. Handles edge cases for
    empty lists or wrong input types.

    args:
        text (list): A list of strings representing reviews.

    returns:
        list: A list of sentiment labels for each review.
    """

    # Check if the input is a list of strings
    if not isinstance(text, list) or not all(isinstance(item, str) for item in text):
        return "Wrong input. text must be an array of strings."
    
    # Check if the list is empty
    if not text:
        return "Wrong input. text must be an array of strings."
    
    client = OpenAI() # Create a object of the OpenAI class.

    # Define the system and user prompts
    # The system prompt sets the context for the model, and the user prompt provides the input data.
    system_prompt = f"""
    "You are an expert sentiment classifier. "
    "Classify each review as one of the following: positive, neutral, negative, or irrelevant. "
    "Return only a single word per line, in the same order as the input. "
    "Do not include punctuation, numbering, brackets, or any additional formatting. "
    "The result should be plain text only, one label per line."
    """
    user_prompt =  "It's May. I've got some reviews for you to classify. Please label each line as" \
    " one of the following: positive, neutral, negative, or irrelevant.\n\n" + "\n".join(text)

    # Send the request to the OpenAI API
    # The chat completion method is used to generate a response based on the provided messages.
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
            
        ]
        
    )
    # Get the response from the API
    # The response is expected to be in the format of a chat message.
    text_response = completion.choices[0].message.content

    # Split the response into lines and strips whitespaces
    # The response is processed to ensure each label is in lowercase and stripped of leading/trailing whitespaces.
    return [line.strip().lower() for line in text_response.splitlines()]
                                                    
from openai import OpenAI


def get_sentiment(text: list) -> list:
    """
    INSERT DOCSTRING HERE
    """
    system_prompt = """
    ...
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """
    pass

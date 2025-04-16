import matplotlib.pyplot as plt
from collections import Counter
import os


def make_plot(sentiments: list) -> None:
    """
    This function visualizes the sentiment distribution of a list of sentiments.

    It counts the occurrences of each sentiment label and creates a bar chart.
     
      Args:
        sentiments (list): A list of sentiment labels (e.g., "positive", "neutral", "negative", "irrelevant").
    
      returns:
        None: The function saves a bar chart of sentiment distribution to a file.
    """
    # Initialize counts
    #counts = {
    #    "positive": 0,
    #    "neutral": 0,
    #    "negative": 0,
    #    "irrelevant": 0
    #}

    # Count manually
    #for sentiment in sentiments:
    #    sentiment = sentiment.strip().lower()
    #    if sentiment in counts:
    #        counts[sentiment] += 1
    
    # Use Counter to count occurrences of each sentiment label
    valid_labels = {"positive", "neutral", "negative", "irrelevant"}
    # Normalize the sentiments to lowercase and strip whitespace
    normalized_sentiments = [s.strip().lower() for s in sentiments if s.strip().lower() in valid_labels]

    #normalized_sentiments = [s.strip().lower() for s in sentiments]

    counts = Counter(normalized_sentiments)

    # Ensure all sentiment labels are present in the counts dictionary
    for sentiment_labels in ["positive", "neutral", "negative", "irrelevant"]:
        if sentiment_labels not in counts: 
            counts[sentiment_labels] = 0

    # Enforce the order of labels due to matplotlib's bar chart behavior (reordering alphabetically)
    # This ensures the bars are plotted in the order I've chosen.
    sentiment_order = ["positive", "neutral", "negative", "irrelevant"]
    values = [counts.get(label, 0) for label in sentiment_order]

    # Prepare data for plotting
    #labels = list(counts.keys())
    #values = list(counts.values())

    # Plot bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(sentiment_order, values, color="#1f77b4", alpha=0.8)
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.tight_layout()

    # If folder doesn't exist create and save
    # os.makedirs("images", exist_ok=True)
    plt.savefig("images/sentiment_plot.png")
    plt.close()

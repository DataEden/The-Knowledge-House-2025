import matplotlib.pyplot as plt


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
    counts = {
        "positive": 0,
        "neutral": 0,
        "negative": 0,
        "irrelevant": 0
    }

    # Count manually
    for sentiment in sentiments:
        sentiment = sentiment.strip().lower()
        if sentiment in counts:
            counts[sentiment] += 1

    # Prepare data for plotting
    labels = list(counts.keys())
    values = list(counts.values())

    # Plot bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=["green", "yellow", "red", "gray"])
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.tight_layout()

    # Ensure the folder exists and save
    #import os
    #os.makedirs("images", exist_ok=True)
    plt.savefig("images/sentiment_plot.png")
    plt.close()

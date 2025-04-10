from label import get_sentiment # Import the get_sentiment function from label.py
from visualize import make_plot # Import the make_plot function from visualize.py

import json # Import the json module to handle JSON files

def run(filepath: str):
    """
    This function reads a JSON file containing reviews, extracts the reviews, and uses the get_sentiment function
    to classify each review's sentiment.
    It handles edge cases such as empty reviews and incorrect input types using the get_sentiment funciton.
    
    The function also prints the review-sentiment pairs in a clean format.
    Additionally, it visualizes the sentiment distribution using the make_plot function.

    args:
        filepath (str): The path to the JSON file containing reviews.

    returns:
        list: A list of sentiment labels for each review.
    """
    # open the json object
    with open(filepath, "r") as file:
       data_file = json.load(file)

    # check if the reviews are empty    
    #if not reviews:
        #return []

    # extract reviews from the json file
    reviews = data_file.get("results", [])
   
    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(reviews)

    # Pair each review with its sentiment
    paired_output = list(zip(reviews, sentiments))

    # Print them cleanly
    print("\n Review + Sentiment Pairs:\n")
    for i, (review, sentiment) in enumerate(paired_output, 1):
        print(f"{i:02d}. [{sentiment.upper()}] {review[0:]}{'...' if len(review) > 200 else ''}")
    
    # plot a visualization expressing sentiment ratio
    make_plot(sentiments)

    # return sentiments
    return sentiments

# Main function to run the script. 
# This function is called when the script is run directly. 
if __name__ == "__main__":
    print(run("data/raw/reviews.json"))

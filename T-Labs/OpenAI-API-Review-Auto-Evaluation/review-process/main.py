from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    INSERT DOCSTRING HERE
    """
    # open the json object
    ...

    # extract the reviews from the json file
    ...

    # get a list of sentiments for each line using get_sentiment
    ...

    # plot a visualization expressing sentiment ratio
    ...

    # return sentiments
    ...


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))

import re

import praw

from utils import retrieve_credentials_from_json

def create_reddit_object() -> praw.Reddit:
    """
    Retrieves credential information and creates Reddit object.

    Params
    ------
        None

    Returns
    -------
        praw.Reddit
            An object that represents the Reddit api itself.
    """
    credentials: dict = retrieve_credentials_from_json()

    return praw.Reddit(
        client_id=credentials['client-id'],
        client_secret=credentials['client-secret'],
        password=credentials['password'],
        user_agent=credentials['user-agent'],
        username=credentials['user']
    )

def extract_data(topics: list) -> tuple:
    """
    Given a list of topics extracts data from Reddit, returning both the data and the topic related.

    Params
    ------
        topics: list
            A list of n topics about to be retrieved from Reddit.
    
    Returns
    -------
        tuple
            A tuple containing the discussion (data) and the topic (label, class) related.
    """
    reddit: praw.Reddit = create_reddit_object()

    # Function to count characters from post
    char_count = lambda post: len(
        re.sub(
            "\W|\d",
            "",
            post.selftext
        )
    )

    # Function that will allow posts only with up to 99 characters
    up_to_99_chars = lambda post: char_count(post) >= 100

    # Lists to store retrieved data
    data, labels = [], []

    for idx_topic, topic in enumerate(topics):
        
        # Retrieving data from subreddit r/<topic>
        posts_from_subreddit: praw.models.ListingGenerator = reddit.subreddit(topic).new(limit=1000)

        # Filtering posts up to 99 chars
        filtered_posts: list = [post.selftext for post in filter(up_to_99_chars, posts_from_subreddit)]

        # Adding captured data (labels stored as int)
        data.extend(filtered_posts)
        labels.extend(len(filtered_posts) * [idx_topic])

    return data, labels
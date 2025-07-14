

import os
import praw
from dotenv import load_dotenv
import logging

# Logging configure karo shuru mein hi (sirf is module ke liye, main app handle karega global logging)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_reddit_praw_instance():
    """
    Reddit API credentials ko .env file se load karke PRAW Reddit object return karta hai.
    """
    load_dotenv() # Ensure .env is loaded

    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT")

    if not all([client_id, client_secret, user_agent]):
        logging.error("Reddit API keys (REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT) .env file mein set nahi hain.")
        raise ValueError("Reddit API credentials missing. Please check your .env file.")

    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        logging.info("PRAW Reddit object successfully created.")
        return reddit
    except Exception as e:
        logging.error(f"PRAW ko initialize karne mein error: {e}")
        raise

def get_username_from_url(url: str) -> str:
    """
    Reddit user profile URL se username extract karta hai.
    Example: https://www.reddit.com/user/kojied/ -> kojied
    """
    parts = url.strip('/').split('/')
    if len(parts) >= 2 and parts[-2] == 'user':
        return parts[-1]
    raise ValueError(f"Invalid Reddit user profile URL: {url}")

def scrape_user_data(reddit_instance: praw.Reddit, username: str):
    """
    Ek specific Reddit user ke comments aur posts ko scrape karta hai.
    """
    user_data = {
        "username": username,
        "comments": [],
        "posts": []
    }
    logging.info(f"Scraping data for user: /u/{username}")

    try:
        redditor = reddit_instance.redditor(username)
        
        logging.info(f"Fetching comments for /u/{username}...")
        for comment in redditor.comments.new(limit=200): # Limit  LLM context 
            user_data["comments"].append({
                "id": comment.id,
                "created_utc": comment.created_utc,
                "subreddit": comment.subreddit.display_name,
                "body": comment.body,
                "permalink": f"https://www.reddit.com{comment.permalink}",
                "score": comment.score
            })
        logging.info(f"Total comments scraped for /u/{username}: {len(user_data['comments'])}")

        logging.info(f"Fetching posts for /u/{username}...")
        for submission in redditor.submissions.new(limit=50): # Limit  LLM context 
            user_data["posts"].append({
                "id": submission.id,
                "created_utc": submission.created_utc,
                "subreddit": submission.subreddit.display_name,
                "title": submission.title,
                "selftext": submission.selftext if submission.is_self else "",
                "url": submission.url if not submission.is_self else "",
                "permalink": f"https://www.reddit.com{submission.permalink}",
                "score": submission.score
            })
        logging.info(f"Total posts scraped for /u/{username}: {len(user_data['posts'])}")

    except Exception as e:
        logging.error(f"Error scraping data for /u/{username}: {e}", exc_info=True)
        if "404" in str(e):
            raise ValueError(f"User /u/{username} found nahi hua Reddit par.") from e
        raise # Re-raise for general errors

    return user_data

if __name__ == "__main__":
    
    reddit = setup_reddit_praw_instance()
    # Example usage:
    # user_data = scrape_user_data(reddit, "kojied")
    # print(user_data)
    pass
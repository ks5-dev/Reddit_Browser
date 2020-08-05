import praw

def browse_subreddit(sub):
    reddit = praw.Reddit(client_id='7nNFTKsHEzX_ZA', 
                     client_secret='eeHFhV-5VrCAXdHf6U1y1_zOoQk', 
                     user_agent='Reddit_Browser', 
                     username='kien5S5', 
                     password='ltkcraft555')
    subreddit = reddit.subreddit(sub)
    submissions = subreddit.hot(limit=5)
    submission_data = {"title":[],"url":[],"score":[],"body":[]}
    for submission in submissions:
        submission_data["title"].append(submission.title)
        submission_data["url"].append(submission.url)
        submission_data["score"].append(submission.score)
        submission_data["body"].append(submission.selftext)
    return submission_data

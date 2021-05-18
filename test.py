import praw
import time

reddit = praw.Reddit(client_id="**********",
                     client_secret="**********",
                     user_agent="**********",
                     username="**********",
                     password="**********")

subreddit = reddit.subreddit("nepal")

keyphrase = "test"
quote = "test bot"

for submission in subreddit.new(limit=10):
    for comment in subreddit.stream.comments():
        if keyphrase in comment.body.lower():
            print("********")
            print(comment.body)





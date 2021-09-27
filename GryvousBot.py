import praw
import re
import os
import time
from dotenv import load_dotenv
load_dotenv()

reddit = praw.Reddit(    
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    username=os.getenv('BOT_USERNAME'),
    password=os.getenv('BOT_PASSWORD'),
    user_agent="GryvousBot:v0.3 (by /u/Kapt_Roodbaard)")
subreddit = reddit.subreddit('pythonforengineers')

# Have we run this code before? If not, create an empty list
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

# Get the latest 20 upvotes posts from our subreddit
for submission in subreddit.hot(limit=20):
    # For every comment in the post
    for comment in submission.comments:
        # If we haven't replied to this post before
        if comment.id not in comments_replied_to:

            # Do a case insensitive search
            if re.search("hello there", comment.body, re.IGNORECASE):
                # Reply to the post
                print("Bot replying to : ", comment.id)
                comment.reply("General Kenobi, you are a bold one.")                

                # Store the current id into our list
                comments_replied_to.append(comment.id)
            
# Write our updated list back to the file
with open("comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
        f.write(comment_id + "\n")

print("Sleeping for 10 sec...")
time.sleep(10)

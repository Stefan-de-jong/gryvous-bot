import variables
import praw
import re
import os
import random

reddit = praw.Reddit('GryvousBot', client_id=variables._client_id, client_secret=variables._client_secret, username=variables._username, password=variables._password)
subreddit = reddit.subreddit('pythonforengineers')

# Define some quotes to reply with
gryvous_quotes = \
[
"How does it feel to die?",
"Your lightsabers will make a fine addition to my collection!",
"I’m no errand boy. I am not in this war for Dooku’s politics. I am the leader of the most powerful droid army the galaxy has ever seen.",
"Anakin Skywalker, I expected someone with your reputation to be a little… older.",
"General Kenobi, you are a bold one.",
"I will deal with this Jedi slime myself."
]

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
                comment.reply("General Kenobi, you are a bold one.")
                print("Bot replying to : ", comment.id)
                # Store the current id into our list
                comments_replied_to.append(comment.id)

            if re.search("!Gryvous", comment.body, re.IGNORECASE):
                # Reply with a random quote
                comment.reply(random.choice(gryvous_quotes))
                print("Bot quoting to : ", comment.id)
                # Store the current id into our list
                comments_replied_to.append(comment.id)

# Write our updated list back to the file
with open("comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
        f.write(comment_id + "\n")

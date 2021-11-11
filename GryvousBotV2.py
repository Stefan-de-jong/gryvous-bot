import praw
import re
import os
import random
import time
from dotenv import load_dotenv
load_dotenv()

def bot_login():
    r = praw.Reddit(
                    client_id=os.getenv('CLIENT_ID'),
                    client_secret=os.getenv('CLIENT_SECRET'),
                    username=os.getenv('BOT_USERNAME'),
                    password=os.getenv('BOT_PASSWORD'),
                    user_agent="GryvousBot:v0.5 (by /u/Kapt_Roodbaard)"
                    )
    return r

hello = ['hello there']
grievous = ['Grievous', 'grievous','Gryvous', 'gryvous', 'General Grievous', 'General Gryvous']
shorter = ['shorter', 'short']
hangar = ['jedi have landed', 'hangar bay', 'main hanger bay']
negotiator = ['offer', 'negotiate', 'negotiations', 'half price']
lightsaber = ['job to do', 'try not to upset him']
murderer = ['reputation', 'murderer']
move = ['your move']
future = ['what have you to show','all your power', 'what have you to gain']

def run_bot(r, comments_replied_to):
    for comment in r.subreddit('PrequelMemes').comments(limit=25):
        for keyword in hello:
            if re.search(r"\b(" + "|".join(hello) + r")\b",comment.body,re.IGNORECASE) and comment.id not in comments_replied_to and not comment.author == r.user.me:
                print("salutations")
                comment.reply("General Kenobi!")
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
        for keyword in move:
            if re.search(r"\b(" + "|".join(move) + r")\b", comment.body,re.IGNORECASE) and comment.id not in comments_replied_to and not comment.author == r.user.me:
                print("move")
                comment.reply("You fool! I've been trained in your Jedi arts by Count Dooku!")
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
        for keyword in negotiator:
            if re.search(r"\b(" + "|".join(negotiator) + r")\b", comment.body,re.IGNORECASE) and comment.id not in comments_replied_to and not comment.author == r.user.me:
                print("negotiator")
                comment.reply("Ah yes, the negotiator.")
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
        for keyword in hangar:
            if re.search(r"\b(" + "|".join(hangar) + r")\b", comment.body,re.IGNORECASE) and comment.id not in comments_replied_to and not comment.author == r.user.me:
                print("jedi in the hangar!")
                comment.reply("Just as Count Dooku predicted!")
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
        for keyword in lightsaber:
            if re.search(r"\b(" + "|".join(lightsaber) + r")\b", comment.body,re.IGNORECASE) and comment.id not in comments_replied_to and not comment.author == r.user.me:
                print("collection")
                comment.reply("Your lightsabers will make a fine addition to my collection.")
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
        for keyword in future:
            if re.search(r"\b(" + "|".join(future) + r")\b", comment.body,re.IGNORECASE) and comment.id not in comments_replied_to and not comment.author == r.user.me:
                print("move")
                comment.reply("The future. A future where there are no Jedi.")
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")

        for keyword in grievous:
            if re.search(r"\b(" + "|".join(grievous) + r")\b", comment.body,re.IGNORECASE) and comment.id not in comments_replied_to and not comment.author == r.user.me:
                for keyword in shorter:
                    if re.search(r"\b(" + "|".join(shorter) + r")\b",comment.body,re.IGNORECASE) and comment.id not in comments_replied_to and not comment.author == r.user.me:
                        print("shorter than expected")
                        comment.reply("Jedi scum!")
                        comments_replied_to.append(comment.id)
                        with open("comments_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")                
                for keyword in murderer:
                    if re.search(r"\b(" + "|".join(murderer) + r")\b", comment.body,re.IGNORECASE) and comment.id not in comments_replied_to and not comment.author == r.user.me:
                        print("rid the galaxy")
                        comment.reply("Murderer? Is it murder to rid the galaxy of you Jedi filth?")
                        comments_replied_to.append(comment.id)
                        with open("comments_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                
        if re.search(r"\b(" + "|".join(grievous) + r")\b", comment.body,re.IGNORECASE) and comment.id not in comments_replied_to and comment.author not in comments_replied_to and comment.author != r.user.me():
                print("just random")
                quotes = [                
                    "What's the situation, captain?",
                    "*Coughing*",
                    "Just as Count Dooku predicted.",
                    "Time to abandon ship.",
                    "That wasn't much of a rescue.",
                    comment.author.name + ", I was expecting someone with your reputation to be a little... older.",
                    "Army or not, you must realize, you.. are.. doomed!",
                    "Kill him!",
                    "I will deal with this Jedi slime myself",
                    "How does it feel to die?",
                    "I am the leader of the most powerfull droid army the galaxy has ever seen!",
                    comment.author.name + ", did you really think I would leave the hyperdrive unguarded?",
                    "Your comment will make a fine addition to my collection.",
                    "Your screams are like music to my audio receptors.",
                    "The Kaleesh are not known for their mercy.",
                    "Make peace with the Force now, for this is your final outing.",
                    "You lose, General " + comment.author.name + "!",
                    "Be thankful, " + comment.author.name  + ", that you have not found yourself in my grip. Your ship is waiting.",
                    "I have always been greater than you. Enough of this. Do you think you can defeat me? You’re nothing.",
                    "You have no idea of the power that is in my grasp."
                ]
                random_item = random.choice(quotes)
                comment.reply(random_item)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")

    print("sleeping")
    time.sleep(15)
def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
while True:
    try:
        run_bot(r, comments_replied_to)
    except Exception as e:
        print(e)
        time.sleep(60)
    
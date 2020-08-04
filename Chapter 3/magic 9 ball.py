# the goal of this program is to create a magic 9 ball
# Ask a question and the 9 ball will answer with 1 of 9 possible responses at random

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy, try again later"
    elif answerNumber == 5:
        return "Askagain later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook is not good"
    elif answerNumber == 9:
        return "Very doubtful"

r = random.randint(1, 9)
fortune = getAnswer(r)

print(fortune)

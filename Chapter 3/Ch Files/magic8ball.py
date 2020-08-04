import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "Outcome likely"
    elif answerNumber == 3:
        return "It is fortold"
    elif answerNumber == 4:
        return "Outcome uncertain"
    elif answerNumber == 5:
        return "Outcome hazy, ask again later"
    elif answerNumber == 6:
        return "Note sure of Outcome"
    elif answerNumber == 7:
        return "It is unlikely"
    elif answerNumber == 8:
        return "Outcome not good"
    elif answerNumber == 9:
        return "Sorry bro, but no"

r = random.randint(1, 9)
fortune = getAnswer(r)

print(fortune)

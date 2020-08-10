import random

answers = ['It is certain',
    'it is decidedly so',
    'it shall be',
    'outcome uncertain',
    'uncertain answer',
    'try again later',
    'it shall not be',
    'outcome unlikely',
    'not happening']

print(answers[random.randint(0, len(answers) - 1)])

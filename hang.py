array = ['panda', 'joker', 'finish']

import random

answer = list(random.choice(array))
k=0
m=0
riddle=[]
already_guessed = []
for i in range(len(answer)):
    riddle.append('*')
while k<5 and m < len(answer):
    print('Guess a letter')
    letter = input()
    if letter in already_guessed:
        print('You have already guessed this one!\n')
    elif letter in answer:
        print('Nice!\n')
        already_guessed.append(letter)
        for i, elem in enumerate(answer):
            if elem == letter:
                riddle[i] = letter
                m += 1
    else:
        k += 1
        print('Wrong! {} mistakes out of 5\n'.format(k))
    print('The word: ', end = '')
    for elem in riddle:
        print(elem, end = '')
    print('\n')

if k>=5:
    print('Sorry! You lost!')
else:
    print('Congratulations! You won!')
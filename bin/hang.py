import random


ARRAY_CAPS = ['panda', 'joker', 'finish']


def check_already_guessed(letter, array1):
    return letter in array1


ANSWER_SMTH = list(random.choice(ARRAY_CAPS))


def game():
    k = 0
    counter = 0
    riddle = []
    already_guessed = []
    for i in range(len(ANSWER_SMTH)):
        riddle.append('*')
    while k < 5 and counter < len(ANSWER_SMTH):
        print('Guess a letter')
        letter = input()
        if letter in ANSWER_SMTH and not check_already_guessed(letter, already_guessed):
            print('Nice!\n')
            already_guessed.append(letter)
            for i, elem in enumerate(ANSWER_SMTH):
                if elem == letter:
                    riddle[i] = letter
                    counter += 1
        elif check_already_guessed(letter, already_guessed):
            print('You have already guessed this one!\n')
        else:
            k += 1
            already_guessed.append(letter)
            print('Wrong! {} mistakes out of 5\n'.format(k))
        print('The word: ', end='')
        for elem in riddle:
            print(elem, end='')
        print('\n')

    if k >= 5:
        print('Sorry! You lost!')
    else:
        print('Congratulations! You won!')


if __name__ == '__main__':
    game()

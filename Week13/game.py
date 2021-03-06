from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()
        
        guessedChar = input('Select a letter: ')
        ## 입력이 영어 인경우만 처리 하기 위해
        if guessedChar.isalpha() != 1:
            print('Enter alphabet')
            continue
        if len(guessedChar) != 1:
            ## 만약 사용자가 문자대신 단어를 입력해서 맞으면 success
            if guessedChar == guess.secretWord:
                print('genius godgod smart!')
                finished = True
                break
            else:
                print('One character at a time!')
                continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        finished = guess.guess(guessedChar)
        if finished == True:
            break
    if finished == True:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()

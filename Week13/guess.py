class Guess:

    def __init__(self, word):
        ## 단어를 secretword에, 
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = '_' * len(self.secretWord)

    def display(self):
        print('Current : ' + self.currentStatus)
        print('Tries : ' + str(self.numTries))


    def guess(self, character):
        ## 문자를 이미 입력했었던 경우
        if character in self.guessedChars:
            pass
        ## 문자를 새로 입력하는 경우
        else:
            ## 문자가 단어에 있는경우
            if self.secretWord.find(character) != -1:
                self.guessedChars.append(character)
                ## 문자가 있는 부분의 인덱스만 따로 초기화
                for i in range(len(self.secretWord)):
                    if character == self.secretWord[i]:
                        self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]
                if self.currentStatus == self.secretWord:
                    print('Answer is ' + self.secretWord)
                    return True
            ##문자가 단어에 없는 경우
            else:
                self.guessedChars.append(character)
                self.numTries += 1


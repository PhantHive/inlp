class Stemming:
    def __init__(self, all_words):
        self.words = all_words

        self.deleting_x()
        self.deleting_else()

    def deleting_x(self):

        for word in self.words:
            i = self.words.index(word)

            if word[-1:] == "x":
                if  word[-3:] == "aux":
                    self.words[i] = word[:-3]+"al"
                else:
                    self.words[i] = word[:-1]

    def deleting_else(self):

        for word in self.words:
            i = self.words.index(word)

            if word[-1:] == "s":
                self.words[i] = word[:-1]

            if word[-1:] == "r":
                self.words[i] = word[:-1]

            if word[-1:] == "e":
                self.words[i] = word[:-1]

            if word[-1:] == "é":
                self.words[i] = word[:-1]

            if word[-1:] == word[-2:-1]:
                self.words[i] = word[:-1]

            if word[-4:] == "ement" or word[-4:] == "ament":
                self.words[i] = word[:-4]
    
    def show_words(self):
        return self.words

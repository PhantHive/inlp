class Stemmer:
    '''
    Porter Stemmer algorithm inspiration
    '''

    def __init__(self, all_words):
        self.all_words = all_words
        self.stem_words = []
        self.new_word = ""
        self.stemmer()

    def stemmer(self):
        for word in self.all_words:
            if len(word) >= 5:
                if word.endswith("x"):
                    if word.endswith("aux"):
                        self.new_word = word.replace("aux", "al")
                    else:
                        self.new_word = word.replace("x", "")

                    self.stem_words.append(self.new_word)

                else:
                    blacklist = ["s", "r", "é", "e"]
                    end = -1
                    verif = False

                    for let in blacklist:
                        if word.endswith(let):
                            word = list(word)
                            word[-1] = ""
                            self.new_word = "".join(word)
                            word = "".join(word)

                    while not verif:
                        if word[end] == word[end - 1]:
                            word = list(word)
                            word[end] = ""
                            word = "".join(word)
                        else:
                            self.new_word = "".join(word)
                            verif = True

                    self.stem_words.append(self.new_word)
            else:
                self.new_word = word
                self.stem_words.append(self.new_word)

        return self.stem_words

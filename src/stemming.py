class IrisStemmer:
    '''
    Snowball Stemmer algorithm inspiration
    '''

    def __init__(self):

        self.stem_words = []
        self.new_word = ""

    def stem(self, word):
        if len(word) >= 5:
            if word.endswith("x"):
                if word.endswith("aux") and not (word.endswith("eaux")):
                    self.new_word = word.replace("aux", "al")
                else:
                    self.new_word = word.replace("x", "")

                self.stem_words.append(self.new_word)

            else:
                blacklist = ["issement", "ablement", "ation", "ment", "é", "e", "es"]
                end = -1
                verif = False

                for w in blacklist:
                    if word.endswith(w):
                        for i in range(len(w)):
                            word = list(word)
                            word[-1] = ""
                            self.new_word = "".join(word)
                            word = "".join(word)

                if word.endswith("c"):
                    word = list(word)
                    word[end] = "qu"
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

    def stemmer(self, w):

        if isinstance(w, list):
            for word in w:
                self.stem(word)
            return self.stem_words
        else:
            self.stem(w)
            return self.new_word
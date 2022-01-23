class Stemmer:
    '''
    Porter Stemmer algorithm inspiration
    '''

    def __init__(self, all_words):
        self.all_words = all_words
        self.stem_words = []
        self.new_word = ""

    def stemmer(self):
        for word in self.all_words:
            if len(word) >= 5:
                if word.endswith("x"):
                    if word.endswith("aux") and not(word.endswith("eaux")):
                        self.new_word = word.replace("aux", "al")
                    else:
                        self.new_word = word.replace("x", "")

                    self.stem_words.append(self.new_word)

                else:
                    blacklist = ["é", "e"]
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


if __name__ == '__main__':


    words = ['belle', "gosse", "teste", "oiseaux", "abyssaux", "laisse", "bouygues", "fait", "amour", "souvent", "anale"]
    IrisStemmer = Stemmer(words)
    newList = IrisStemmer.stemmer()
    for w in range(len(newList)):
        print(words[w], ":", newList[w])
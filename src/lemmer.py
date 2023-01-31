import os.path

class IrisLemmer:

    def __init__(self):

        self.base_word = ""
        self.word = ""
        self.lem_words = []
        self.lemmer_path = os.path.abspath('../assets/dict/lemmatization-fr.txt')
        self.lemmer_path_2 = os.path.abspath('../assets/dict/lemmatization-fr-2.txt')

    def lemm(self, word):

        self.lemmer_file = open(self.lemmer_path, "r", encoding="utf8")
        self.lemmer_file_2 = open(self.lemmer_path_2, "r", encoding="utf8")

        self.word = word

        for row in self.lemmer_file:

            lem_word = row.split()[1]
            if self.word == lem_word:
                self.base_word = row.split()[0]
                self.lem_words.append(self.base_word)
                return self.base_word

        for row in self.lemmer_file_2:
            # print("mot 2:", self.word)
            lem_word = row.split()[1]
            # print("lem_word:", lem_word, "mot:", w)
            if self.word == lem_word:
                self.base_word = row.split()[0]
                self.lem_words.append(self.base_word)
                return self.base_word

        self.lem_words.append(self.word)
        return self.word



    def lemmer(self, w):

        if isinstance(w, list):
            for word in w:
                self.lemm(word)
            return self.lem_words

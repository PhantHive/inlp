import os.path

class IrisLemmer:

    def __init__(self):


        self.lem_words = []
        self.lemmer_path = os.path.abspath('assets/dict/lemmatization-fr.txt')
        self.lemmer_path_2 = os.path.abspath('assets/dict/lemmatization-fr-2.txt')

        self.lemmer_file = open(self.lemmer_path, "r", encoding="utf8")
        self.lemmer_file_2 = open(self.lemmer_path_2, "r", encoding="utf8")

    def lemm(self, w):
        

        for row in self.lemmer_file:

            lem_word = row.split()[1]

            if w == lem_word:
                base_word = row.split()[0]
                return base_word

        for row in self.lemmer_file_2:

            lem_word = row.split()[1]

            if w == lem_word:
                base_word = row.split()[0]
                return base_word



    def lemmer(self, w):

        if isinstance(w, list):
            for word in w:
                base_word = self.lemm(word)
                self.lem_words.append(base_word)
            return self.lem_words
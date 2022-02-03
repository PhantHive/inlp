import unidecode


class Lemmer:

    def __init__(self, w):

        self.w = w
        print(self.w)

        self.lemmer_path = '../assets/dict/lemmatization-fr.txt'
        self.lemmer_path_2 = '../assets/dict/lemmatization-fr-2.txt'

        self.lemmer_file = open(self.lemmer_path, "r", encoding="utf8")
        self.lemmer_file_2 = open(self.lemmer_path_2, "r", encoding="utf8")

    def lemm(self):

        for row in self.lemmer_file:

            lem_word = row.split()[1]

            if self.w == lem_word:
                base_word = row.split()[0]
                return base_word

        for row in self.lemmer_file_2:

            lem_word = row.split()[1]

            if self.w == lem_word:
                base_word = row.split()[0]
                return base_word


if __name__ == '__main__':
    
    lemmer = Lemmer("éjaculât")

    bw = lemmer.lemm()

    print(bw)  # print base word :)

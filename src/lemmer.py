import os

class Lemmer:


    def __init__(self, w):

        self.w = w

        self.lemmer_path = os.path.dirname('../assets/dict/lemmatization-fr.txt')
        #assert os.path.isfile(self.lemmer_path)
        self.lemmer_file = open(self.lemmer_path, "r").read()


    def lemm(self):

        for row in self.lemmer_file:

            base_word = row.split(" ")[0]
            print(base_word)
            print(self.w)
            if self.w == base_word:
                print("match")
                return



if __name__ == '__main__':

    test = Lemmer("yeux")

    test.lemm()


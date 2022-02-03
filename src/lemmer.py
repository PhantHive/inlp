import os

class Lemmer:


    def __init__(self, w):

        self.w = w

        self.lemmer_path = '../assets/dict/lemmatization-fr.txt'
        self.lemmer_path_2 = '../assets/dict/lemmatization-fr-2.txt'

        self.lemmer_file = open(self.lemmer_path, "r")
        self.lemmer_file_2 = open(self.lemmer_path_2, "r")


    def lemm(self):

        for row in self.lemmer_file:

            base_word = row.split()[0]

            if self.w == base_word:
                print(base_word)
                print(self.w)
                print("match")
                return


        for row in self.lemmer_file_2:


            base_word = row.split()[0]

            if self.w == base_word:
                print(base_word)
                print(self.w)
                print("match")
                return



if __name__ == '__main__':

    test = Lemmer("yeux")

    test.lemm()


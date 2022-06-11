import numpy as np
from src.indexing import Indexing
from src.ngrams import Ngram

class Word2Vec:

    def __init__(self, words):

        self.i_dict = {}
        self.X = []
        self.Y = []
        self.Z = []
        self.n = None  # number of unique words
        self.words = words
        self.word_dict = {}

    def Word2Vec(self):


        i_encode = Indexing(self.words)
        self.word_dict = i_encode.encode()

        self.words = list(self.word_dict.keys())

        ngram = Ngram(self.words, 3)  # N-gram with 2 words context
        data_points = ngram.context()



        self.n = len(self.word_dict)

        for j, data_point in enumerate(data_points[1]):
            focus_word = self.word_dict.get(data_point[0])
            context_word = self.word_dict.get(data_point[1])
            context_word2 = self.word_dict.get(data_point[2])

            X_row = np.zeros(self.n)
            Y_row = np.zeros(self.n)
            Z_row = np.zeros(self.n)

            X_row[focus_word] = 1
            Y_row[context_word] = 1
            Z_row[context_word2] = 1

            self.X.append(X_row)
            self.Y.append(Y_row)
            self.Z.append(Z_row)

        self.X = np.asarray(self.X)
        self.Y = np.asarray(self.Y)
        self.Z = np.asarray(self.Z)


    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_Z(self):
        return self.Z

    def get_word_dict(self):
        return self.word_dict
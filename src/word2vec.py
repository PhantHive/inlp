import numpy as np
from src.ngrams import Ngram


class Word2Vec:

    def __init__(self, one_hot_matrix, words):

        self.one_hot_matrix = one_hot_matrix
        self.X = []
        self.Y = []
        self.n = len(words)  # number of unique words
        self.words = words
        self.word_dict = {}

    def Word2Vec(self):

        ngram = Ngram(self.words, 2)  # N-gram with 2 words context
        data_points = ngram.context()

        for i, word in enumerate(self.words):
            self.word_dict[word] = i

        for j, data_point in enumerate(data_points):
            focus_word = self.word_dict.get(data_point[0])
            context_word = self.word_dict.get(data_point[1])

            X_row = np.zeros(self.n)
            Y_row = np.zeros(self.n)

            X_row[focus_word] = 1
            Y_row[context_word] = 1

            self.X.append(X_row)
            self.Y.append(Y_row)

        self.X = np.asarray(self.X)
        self.Y = np.asarray(self.Y)


    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_word_dict(self):
        return self.word_dict
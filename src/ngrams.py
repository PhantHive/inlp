class Ngram:

    def __init__(self, words, n):
        self.words = words
        self.ctx = []
        self.n = n
        self.data_points = []

    def context(self):

        for i in range(len(self.words)):
            for j in range(self.n):
                if i - j - 1 >= 0:
                    self.data_points.append((self.words[i], self.words[i - j - 1]))

                if i + j + 1 < len(self.words):
                    self.data_points.append((self.words[i], self.words[i + j + 1]))

        return self.data_points


if __name__ == '__main__':

    wrds = ["The", "future", "king", "is", "the", "prince"]
    ngram = Ngram(wrds, 2)

    tples = ngram.context()

    for wrd in tples:
        print(wrd)

    print(len(tples))

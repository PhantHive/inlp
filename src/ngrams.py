class Ngram:

    def __init__(self, words, n):
        self.words = words
        self.ctx = []
        self.n = n
        self.data_points = []

    def context(self):

        for i in range(len(self.words) - self.n + 1):
            for j in range(self.n):
                self.data_points.append(self.words[i + j])
            self.ctx.append(tuple(self.data_points))
            self.data_points = []

        return self.ctx


if __name__ == '__main__':

    wrds = ["Je", "mange", "beaucoup", "de", "pommes", "de", "terres"]
    ngram = Ngram(wrds, 2)

    tples = ngram.context()

    for wrd in tples:
        print(wrd)



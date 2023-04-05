class Ngram:

    def __init__(self, words, n):
        self.words = words
        self.ctx = []
        self.n = n
        self.data_points = []

    def context(self):

        for i in range(len(self.words)):
            base_tpl = (self.words[i],)
            base_tpl2 = (self.words[i],)
            for j in range(self.n - 1):
                if i - j - 1 >= 0:
                    base_tpl += (self.words[i - j - 1],)

                if i + j + 1 < len(self.words):
                    base_tpl2 += (self.words[i + j + 1],)

            if (len(base_tpl) == self.n):
                self.data_points.append(base_tpl)
            if (len(base_tpl2) == self.n):
                self.data_points.append(base_tpl2)



        return self.data_points

    def get_context_words(self, index):
        context_words = []
        for tpl in self.data_points:
            if tpl[0] == self.words[index]:
                for i in range(1, len(tpl)):
                    if tpl[i] not in context_words:
                        context_words.append(tpl[i])
        return context_words





if __name__ == '__main__':

    wrds = ["The", "future", "king", "is", "the", "prince"]
    ngram = Ngram(wrds, 3)

    tples = ngram.context()

    for wrd in tples:
        print(wrd)

    print(len(tples))

    print(ngram.get_context_words(2))

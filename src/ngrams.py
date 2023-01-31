class Ngram:

    def __init__(self, words, n):
        self.words = words
        self.ctx = []
        self.n = n
        self.data_points = []

    def context(self):

        backward_dp = []
        forward_dp = []

        for i in range(len(self.words)):
            base_tpl = (self.words[i],) # backward context (index(focus_word) = -1)
            base_tpl2 = (self.words[i],) # forward context (index(focus_word) = 1)
            for j in range(self.n - 1):
                if i - j - 1 >= 0:
                    base_tpl += (self.words[i - j - 1],)

                if i + j + 1 < len(self.words):
                    base_tpl2 += (self.words[i + j + 1],)

            if (len(base_tpl) == self.n):
                #self.data_points.append(base_tpl)
                backward_dp.append(base_tpl)
            if (len(base_tpl2) == self.n):
                #self.data_points.append(base_tpl2)
                forward_dp.append(base_tpl2)

        self.data_points.append(backward_dp)
        self.data_points.append(forward_dp)

        return self.data_points


if __name__ == '__main__':

    wrds = ["L'association", "IRIS", "est", "la", "meilleure"]
    ngram = Ngram(wrds, 3)

    tples = ngram.context()


    print("3-Grams")
    for wrd in tples:
        for tpl in wrd:
            print(tpl)

    #print(len(tples))

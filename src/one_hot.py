class OneHot:

    def __init__(self, all_sentences, all_words):

        self.tokenize_matrix = []
        self.all_sentences = all_sentences
        self.all_words = all_words

    def encode(self):

        words_occ = {}

        for sentence in self.all_sentences:
            # print(sentence)
            for i, word in enumerate(self.all_words):
                if word in sentence:
                    if word not in words_occ:
                        words_occ[i] = i
                else:
                    words_occ[i] = 0

            occurences = list(words_occ.values())
            self.tokenize_matrix.append(occurences)
            words_occ.clear()

        return self.tokenize_matrix
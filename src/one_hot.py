class OneHot:

    def __init__(self, all_words):
        '''
        all_sentences: list of lists of words
        all_words: list of words
        '''

        self.onehot_dict = None
        self.onehot_matrix = []
        self.all_words = all_words

    def encode(self):

        word_dict = {}
        for word in self.all_words:
            if word not in word_dict:
                word_dict[word] = 1

        for word in self.all_words:
            onehot_word = []
            for key in word_dict:
                if key == word:
                    onehot_word.append(1)
                else:
                    onehot_word.append(0)
            self.onehot_matrix.append(onehot_word)

        self.onehot_dict = {}
        for i in range(len(self.onehot_matrix)):
            self.onehot_dict[self.all_words[i]] = self.onehot_matrix[i]

        return self.onehot_matrix, self.onehot_dict




if __name__ == '__main__':

    all_words = ['the', 'cat', 'sat', 'on', 'the', 'mat']

    one_hot = OneHot(all_words)
    one_hot.encode()
    print(one_hot.onehot_matrix)
    print(one_hot.onehot_dict)

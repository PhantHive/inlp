class Indexing:

    def __init__(self, all_words):

        self.tokenize_matrix = []
        self.all_words = all_words
        self.i_dict = {}

    def encode(self):

        # deleting occurrences
        temp_list = []
        for word in self.all_words:
            if word not in temp_list:
                temp_list.append(word)

        self.all_words = temp_list.copy()

        for i, word in enumerate(self.all_words):
            if word not in self.i_dict:
                self.i_dict[word] = i
            else:
                i -= 1

        print(self.i_dict)

        return self.i_dict

class TOKENIZE:

    def __init__(self, text):
        self.text = text
        self.all_sentences = []
        self.sentence = ""
        self.new_text = ""
        self.all_words = []
        self.tokenize_matrix = []
        self.text_to_sentences()

    def text_to_sentences(self):
        end_sentence = ['!', '?', '.', ':']

        for let in self.text:
            if let in end_sentence:
                self.sentence = self.text.split(let, 1)[0]
                self.new_text = self.text.split(let, 1)[1]
                self.all_sentences.append(self.sentence)
                self.text = self.new_text

        self.tokenize()

    def tokenize(self):

        words_occ = {}

        for sentence in self.all_sentences:
            words = sentence.strip(" ").split(" ")
            self.all_words += words

        for sentence in self.all_sentences:
            for e in self.all_words:
                if e in sentence:
                    if e in words_occ:
                        words_occ[e] += 1
                    else:
                        words_occ[e] = 1
                else:
                    words_occ[e] = 0

            occurences = list(words_occ.values())
            self.tokenize_matrix.append(occurences)



    def show_sentences(self):
        return self.all_sentences, self.tokenize_matrix, self.all_words



# tries ===============================

texte = 'I like to eat noodles. But I prefer girls with big boobies! ' \
        'This is a stupid text. Isn\'t it? They slither while they pass, they slip away across the universe.'

test = TOKENIZE(texte)
res, res2, res3 = test.show_sentences()

print(res3)
for lst in res2:
    print(lst)
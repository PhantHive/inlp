import json
from src.stemming import Stemmer


class TOKENIZE:

    def __init__(self, text):
        self.text = text
        self.all_sentences = []
        self.sentence = ""
        self.new_text = ""
        self.all_words = []
        self.tokenize_matrix = []

        stopwords = open('assets/stopwords/stop_words_french.json', 'r')
        self.stopwords = json.load(stopwords)

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

    def remove_stopwords(self):
        temp_list = [word for word in self.all_words if word.lower() not in self.stopwords]
        return temp_list

    def tokenize(self):

        words_occ = {}

        for sentence in self.all_sentences:
            words = sentence.strip(" ").split(" ")
            self.all_words += words

        self.all_words = self.remove_stopwords()

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

texte = "Yo les gens salut tous tous tous à tous mes frères et bienvenue sur ma chaîne donc aujourd'hui les gars on " \
        "se retrouve pour une nouvelle vidéo. "

test = TOKENIZE(texte)
res, res2, res3 = test.show_sentences()

print(res3)
for lst in res2:
    print(lst)

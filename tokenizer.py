import json


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

texte = 'En mon cœur n\'est point escrite'\
'La rose ny autre fleur,'\
'C\'est toy, blanche Marguerite,'\
'Par qui j\'ay cette couleur.'\
'N\'es-tu celle dont les yeux'\
'Ont surpris'\
'Par un regard gracieux'\
'Mes esprits ?'\
'Puis que ta sœur de haut pris,'\
'Ta sœur, pucelle d\'élite,'\
'N\'est cause de ma douleur,'\
'C\'est donc par toy, Marguerite'\
'Que j\'ay pris ceste couleur.'\
'Ma couleur palle nasquit,'\
'Quand mon cœur'\
'Pour maistresse te requit ;'\
'Mais rigueur'\
'D\'une amoureuse langueur'\
'Soudain paya mon mérite,'\
'Me donnant ceste pâleur'\
'Pour t\'aimer trop, Marguerite,'\
'Et ta vermeille couleur.'\
'Quel charme pourroit casser'\
'Mon ennuy'\
'Et ma couleur effacer'\
'Avec luy ?'\
'De l\'amour que tant je suy'\
'La jouissance subite'\
'Seule osteroit le malheur'\
'Que me donna Marguerite,'\
'Par qui j\'ay cette couleur.'\

test = TOKENIZE(texte)
res, res2, res3 = test.show_sentences()

print(res3)
for lst in res2:
    print(lst)

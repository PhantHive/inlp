import json


class TOKENIZE:
    def __init__(self, text):
        self.text = text
        self.all_sentences = []
        self.sentence = ""
        self.new_text = ""
        self.all_words = []
        self.tokenize_matrix = []

        stopwords = open("assets/stopwords/stop_words_french.json", "r")
        self.stopwords = json.load(stopwords)
        self.text_to_sentences()

    def text_to_sentences(self):
        end_sentence = ["!", "?", ".", ":", ";"]

        for let in self.text:
            if let in end_sentence:
                self.sentence = (self.text.split(let, 1)[0]).split()

                for word in self.sentence:
                    if "," in word and word.index(",") > 0:
                        z = self.sentence.index(word)
                        self.sentence[z] = "".join(word.split((",", 1)[0]))
                    if word == "":
                        self.sentence.remove(word)
                for word in self.sentence:
                    for i in word:
                        if i.isupper() and word.index(i) > 0:
                            z = self.sentence.index(word)
                            self.sentence[z] = word.split(i, 1)[0]
                            self.sentence.insert(z + 1, i + word.split(i, )[1])
                for word in self.sentence:
                    if "'" in word and word.index("'") > 0:
                        z = self.sentence.index(word)
                        self.sentence[z] = word.split("'", 1)[0]
                        self.sentence.insert(z + 1, word.split("'", )[1])
                    if word == "":
                        self.sentence.remove(word)

                      
                            self.sentence.insert(
                                z + 1,
                                i + word.split(i, )[1],
                            )

  

                self.new_text = self.text.split(let, 1)[1]
                self.all_sentences.append(self.sentence)
                self.text = self.new_text

        self.tokenize()

    def tokenize(self):

        words_occ = {}

        for word in self.all_sentences:
            if word not in self.stopwords:
                self.all_words += word

        self.all_words = [
            word for word in self.all_words
            if word.lower() not in self.stopwords
        ]

        for sentence in self.all_sentences:
            print(sentence)
            for i in self.all_words:
                print(i)
                if i in sentence:
                    if i in words_occ:
                        words_occ[i] += 1
                    else:
                        words_occ[i] = 1
                else:
                    words_occ[i] = 0

            occurences = list(words_occ.values())
            self.tokenize_matrix.append(occurences)

    def show_sentences(self):
        return self.all_sentences, self.tokenize_matrix, self.all_words


# tries ===============================

texte = ("En mon cœur n'est point escrite"
         "La rose ny autre fleur,"
         "C'est toy, blanche Marguerite,"
         "Par qui j'ay cette couleur."
         "N'es-tu celle dont les yeux"
         "Ont surpris"
         "Par un regard gracieux"
         "Mes esprits ?"
         "Puis que ta sœur de haut pris,"
         "Ta sœur, pucelle d'élite,"
         "N'est cause de ma douleur,"
         "C'est donc par toy, Marguerite"
         "Que j'ay pris ceste couleur."
         "Ma couleur palle nasquit,"
         "Quand mon cœur"
         "Pour maistresse te requit ;"
         "Mais rigueur"
         "D'une amoureuse langueur"
         "Soudain paya mon mérite,"
         "Me donnant ceste pâleur"
         "Pour t'aimer trop, Marguerite,"
         "Et ta vermeille couleur."
         "Quel charme pourroit casser"
         "Mon ennuy"
         "Et ma couleur effacer"
         "Avec luy ?"
         "De l'amour que tant je suy"
         "La jouissance subite"
         "Seule osteroit le malheur"
         "Que me donna Marguerite,"
         "Par qui j'ay cette couleur.")
test = TOKENIZE(texte)
res, res2, res3 = test.show_sentences()

print(res)
for lst in res2:
    print(lst)
print(res3)

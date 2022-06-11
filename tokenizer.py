import json
import re

from src.stemming import IrisStemmer
from src.lemmer import IrisLemmer
import os.path
from src.indexing import Indexing


class TOKENIZE:

    def __init__(self, text):
        self.text = text
        self.all_sentences = []
        self.sentence = ""
        self.new_text = ""
        self.all_words = []
        self.tokenize_matrix = []
        # self.stemmer = IrisStemmer()

        stopwords = open(os.path.abspath("assets/stopwords/stop_words_french.json"), "r", encoding="utf8")
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
                            self.sentence.insert(
                                z + 1,
                                i + word.split(i, )[1],
                            )

                for word in self.sentence:

                    if "'" in word and word.index("'") > 0:
                        z = self.sentence.index(word)
                        self.sentence[z] = word.split("'", 1)[0]
                        self.sentence.insert(
                            z + 1,
                            word.split("'", )[1],
                        )

                    if word == " ":
                        self.sentence.remove(word)
                        z = self.sentence.index(word)
                        self.sentence.insert(
                            z + 1,
                            word.split(" ", )[1],
                        )

                self.new_text = self.text.split(let, 1)[1]
                if self.sentence:
                    self.all_sentences.append(self.sentence)
                self.text = self.new_text

        self.tokenize()

    def preprocess_words(self):

        for word in self.all_sentences:
            if word not in self.all_words:
                self.all_words += word

        remove_chars = ['(', ')', '@', '<', '>', '\\']
        pattern = '[' + '\\'.join(remove_chars) + ']'

        # deleting chars
        self.all_words = [
            re.sub(pattern, '', word) for word in self.all_words
        ]

        # deleting words
        self.all_words = [
            word for word in self.all_words
            if word.lower() not in self.stopwords
        ]



    def tokenize(self):

        # pre-process words by deleting unexpected characters or words.
        self.preprocess_words()

        lemmer = IrisLemmer()  # Lemmatize all words using the IRIS lemmer.
        self.all_words = lemmer.lemmer(self.all_words)

        self.all_words.sort()

    def show_sentences(self):
        return self.all_sentences, self.all_words


# tries ===============================


if __name__ == '__main__':

    '''text = ("En mon cœur n'est point escrite"
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
    
    '''

    '''text = ("Avec l'exemple des (pièces) de Corneille, Molière et Racine, on montre quelques-uns des nombreux " \
           "usages possibles des bases de données textuelles normalisées et lemmatisées. Elles sont d'une " \
           "consultation aisée. Elles fournissent de nombreux renseignements sur le vocabulaire, le style, le sens " \
           "des mots... Pour cela, il faut réduire les graphies multiples et rattacher chaque mot à son entrée de " \
           "dictionnaire.")'''

    '''text = ("C'est l'histoire d'un fainéant qui n'aimait pas faire les choses dans les temps."
            "Romain ne fait jamais les choses dans les temps."
            "Toujours fainéant, Romain ne fait rien."
            "Chaque jour, il se réveille et oublie de faire les choses dans les temps ce jeune Romain."
            "Ce serait bien que Romain fasse quelque chose car la il ne fait rien. Ce"
            "Romain est un gros fainéant, stop Romain être un fainéant. T'es un gros fainéant Romain. Tu devrais faire les choses dans les temps Romain."
            "Romain est un putain de fainéant, ce gros fainéant de Romain!!! c'est énervant d'être aussi fainéant et de rien faire."
            "Romain fait rien, Romain ne fait jamais rien, Romain est fainéant. fainéant ce Romain."
            )'''

    text = ("Je fais à manger.")

    test = TOKENIZE(text)
    res, res3 = test.show_sentences()

    # stemmer = IrisStemmer()
    # res3 = stemmer.stemmer(res3)

    lemmer = IrisLemmer()
    res3 = lemmer.lemmer(res3)

    print(res3) # word list with preprocessing applied


    for sent in res:
        print(sent)

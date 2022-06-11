import numpy as np

from tokenizer import TOKENIZE
from src.word2vec import Word2Vec
from big_brain.bb_graph import BBGraph
from big_brain.bb_test import BB_test as TEST

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
         "Par qui j'ay cette couleur.")'''


'''text = ("C'est l'histoire d'un fainéant qui n'aimait pas faire les choses dans les temps."
        "Romain ne fait jamais les choses dans les temps."
        "Toujours fainéant, Romain ne fait rien."
        "Chaque jour, il se réveille et oublie de faire les choses dans les temps ce jeune Romain."
        "Ce serait bien que Romain fasse quelque chose car la il ne fait rien. Ce"
        "Romain est un gros fainéant, stop Romain être un fainéant. T'es un gros fainéant Romain. Tu devrais faire les choses dans les temps Romain."
        "Romain est un putain de fainéant, ce gros fainéant de Romain!!! c'est énervant d'être aussi fainéant et de rien faire."
        "Romain fait rien, Romain ne fait jamais rien, Romain est fainéant. fainéant ce Romain."
        )'''

text = ("L'intelligence artificielle IA est « l'ensemble des théories et des techniques mises en œuvre en vue de réaliser des machines capables de simuler "
        "l'intelligence humaine »."
        "notant le peu de précision de la définition de L'intelligence artificielle, l'ont présentée comme « le grand mythe de notre temps »3. "
        "Souvent classée dans le groupe des mathématiques et des sciences cognitives, "
        "elle fait appel à la neurobiologie computationnelle particulièrement aux réseaux neuronaux "
        "et à la logique mathématique partie des mathématiques et de la philosophie. "
        "Elle utilise des méthodes de résolution de problèmes à forte complexité logique ou algorithmique. "
        "Par extension, elle comprend, dans le langage courant, les dispositifs imitant ou remplaçant l'homme dans certaines mises en œuvre de ses fonctions cognitives4. "
        "Ses finalités et enjeux ainsi que son développement suscitent, depuis l'apparition du concept, "
        "de nombreuses interprétations, fantasmes ou inquiétudes s'exprimant tant dans les récits ou films de science-fiction que dans les essais philosophiques5. "
        "Si des outils relevant d'intelligences artificielles spécialisées ont fait leurs preuves, "
        "la réalité semble encore tenir l'intelligence artificielle généraliste loin des performances du vivant ; "
        "ainsi, L'intelligence artificielle reste encore bien inférieure au chat dans toutes ses aptitudes naturelles.")

print("\n\n==========PROGRAMME PRINCIPAL========")

test = TOKENIZE(text)
res, res3 = test.show_sentences()

IrisVec = Word2Vec(res3)
IrisVec.Word2Vec()

X = IrisVec.get_X()
Y = IrisVec.get_Y()
Z = IrisVec.get_Z()
word_dict = IrisVec.get_word_dict()

print("\nX:\n", X)
print("\nY:\n", Y)
print("\nZ:\n", Z)



BB = BBGraph(X, Y, Z, word_dict, res3)
BB.show_graph()


'''
BB_test = TEST(X, Y, Z, word_dict, res3)
model = BB_test.init_network()
result = BB_test.forward(model, X[3])
print(word_dict)
print(X[3])

def id_to_word(id):

    temp_keys= list(word_dict.keys())
    temp = list(word_dict.values())
    pos = temp.index(id)
    return temp_keys[pos]


for word in (id_to_word(id) for id in np.argsort(result)[::-1]):
    print(word)
'''

print("\n\n==========FIN DU PROGRAMME========")






print(res3)

print(res)

import json
from tokenizer import TOKENIZE
from src.stemming import IrisStemmer

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


text1 = "Le trésorier s'est barré avec la caisse il est donc un mauvais trésorier cordialement."
test = TOKENIZE(text1)
res, res2, res3 = test.show_sentences()

"""print(res)
for lst in res2:
    print(lst)"""
print("all_words : ")
print(res3)


stem_test = IrisStemmer()
stemmed_words = stem_test.stemmer(res3)
print("stemmed_words : ")
print(stemmed_words)

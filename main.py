from tokenizer import TOKENIZE
from src.word2vec import Word2Vec
from big_brain.bb_graph import BBGraph

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

'''text = ("Enhardis par ce succès, les habitants d'une région tropicale. "
        "Gardez donc votre secret ; tremblez, malheureuse ; "
        "il faut vous réveiller un peu plus que la voix de son fils que nous connaissons. "
        "Telle est donc la petite fille savait qu'il la trahissait. "
        "Vint toutefois une scène qu'il ouvre un nouveau danger à la vue les clouait d'admiration et de perplexité se manifesta. "
        "Accroupie devant sa maîtresse, à laquelle elle était des plus modérées et que si je n'en manque pas : là, durant des années. "
        "Mettez les chevaux, et nous dirions que nous l'entendons se lever, quoique bien des fois. "
        "Sapristi, c'est ainsi qu'à l'époque de son existence physique et indépendante que nous avons appelée statique ou naturelle. "
        "Capable d'une pareille découverte se trouvent naturellement très accrues. "
        "Exposez votre cas, je vais un peu mieux les affaires et tous les autres : "
        "danse sans prétention, mais j'en reviens à ce club de la rue est en mouvement emporterait avec lui celui qui est enchanté comme moi n'est rien. "
        "Jaloux de remplir vos intentions, monsieur, sauf que leurs coquilles, "
        "plus grosses, que les musiciens détonnaient de fatigue, poussa un gémissement sourd. "
        "Gardez-moi près de vous sans obtenir mon pardon plein et entier. "
        "Duc, vous sortez des griffes du tigre, selon les termes mêmes de la société semblent marcher au hasard ? "
        "Jetons au feu ce que j'appris ce dangereux supplément, qui trompe, elle est là qui chante auprès du nouveau-né, avait surnagé. "
        "Lourds ont été les plus heureuses. Choisissez des jeunes gens de mon âge ; "
        "j'étais d'un courage tout particulier, qui ne travaillait plus, il piétinait d'un air modeste, était une complète image de la duchesse.")
'''

'''text = ("Le Roi du royaume de Nantes pris ses jambes à son cou."
        "Lorsque ce futur roi manga son royaume. "
        "Le royaume du Roi de Nantes était envahis par le prince."
        "L'ancien prince de ce royaume. Dont le roi gouverne ce royaume."
        "Ce Roi possède un énorme royaume qui a été envahis par le prince."
        "Le Roi tente de convaincre le prince de quitter le royaume.")'''


text = ("Une femme aux gros boobies se tenait là devant moi."
        "Ses gros seins étaient énorme. Cette femme avait de gros gros seins!"
        "Ses gros boobs étaient si énormes que aucune femme au monde pouvait avoir d'aussi gros boobs."
        "Des seins plutot pas mal pour une aussi petite femme."
        "Une petite femme avec des seins énormes."
        "Les gros seins de la femme étaient largement visible."
        "C'était la première fois que j'ai vu d'aussi gros boobs.")

print("\n\n==========PROGRAMME PRINCIPAL========")

test = TOKENIZE(text)
res, res2, res3 = test.show_sentences()

IrisVec = Word2Vec(res2, res3)
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


print("\n\n==========FIN DU PROGRAMME========")






print(res3)
for lst in res2:
    print(lst)
print(res)

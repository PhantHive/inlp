from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize

ps = SnowballStemmer(language="french")

# choose some words to be stemmed
words = ['belle', "gosse", "teste", "oiseaux", "abyssaux", "laisse", "bouygues", "fait", "amour", "souvent", "anale"]

for w in words:
    print(w, " : ", ps.stem(w))

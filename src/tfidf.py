import math
import os
from collections import defaultdict
from src.tokenizer import TOKENIZE
import numpy as np
import time

class TFIDF:

    def __init__(self, corpus_path):
        self.corpus_path = corpus_path
        self.documents = []

        self.unique_words = defaultdict(lambda: defaultdict(float)) # {word: {doc: freq}}

        self.words_tfidf = defaultdict(lambda: defaultdict(float)) # {word: {doc: tfidf}}
        self.idf_matrix = defaultdict(float) # {doc: idf}
        self.tf_matrix = defaultdict(float) # {doc: tf}

        self.tokenized_doc = defaultdict()

    def tfidf(self):
        self.tf()
        self.idf()

        # numpy array of tf matrix * idf matrix
        tfidf_m = np.array(self.tf_matrix) * np.array(self.idf_matrix)

        return tfidf_m

    def tf(self):

        with os.scandir(self.corpus_path) as files:
            for file in files:
                if file.is_file() and file.name.endswith(".txt"):
                    self.documents.append(file.path)

        print("---------------------------")
        print("All documents tokenized")
        print("---------------------------")

        for doc in self.documents:
            with open(doc, "r", encoding="utf8") as f:
                tokenize = TOKENIZE(f.read())
                _, filtred_doc = tokenize.show_sentences()
                print(filtred_doc)
                self.tokenized_doc[doc] = filtred_doc
                for word in filtred_doc:
                    self.unique_words[word][doc] += 1

        for word, doc in self.unique_words.items():
            for d in doc:
                # get lenght of document thanks to the tokenized doc
                len_doc = len(self.tokenized_doc[d])
                self.unique_words[word][d] = self.unique_words[word][d] / len_doc

        print("---------------------------")
        print(self.unique_words.keys())

        # ---------------------------
        # TF MATRIX
        # ---------------------------
        # ROWS: WORDS
        # COLUMNS: DOCUMENTS
        # ---------------------------

        print("---------------------------")
        print("Processing TF matrix..")
        print("---------------------------")

        self.tf_matrix = []
        for i in range(len(self.documents)):
            tf = []
            for j in range(len(self.unique_words.keys())):
                # check if word at position j is in document
                if list(self.unique_words.keys())[j] in self.unique_words:
                    # check if document at position i is in word
                    if self.documents[i] in self.unique_words[list(self.unique_words.keys())[j]]:
                        tf.append(self.unique_words[list(self.unique_words.keys())[j]][self.documents[i]])
                    else:
                        tf.append(0)
            self.tf_matrix.append(tf)

        # convert to numpy array tf matrix

        self.tf_matrix = np.array(self.tf_matrix)
        print(self.tf_matrix)

        return self.tf_matrix

    def idf(self):

        # ---------------------------
        # IDF MATRIX
        # ---------------------------
        # ROWS: WORDS
        # COLUMNS: DOCUMENTS
        # ---------------------------

        print("---------------------------")
        print("Processing IDF matrix....")
        print("---------------------------")

        self.idf_matrix = []

        for doc in self.documents:
            all_idf = []
            for word in self.unique_words.keys():
                w_appears = 0
                for _ in self.unique_words[word]:
                    w_appears += 1

                if w_appears > 0 and doc in self.unique_words[word]:
                    all_idf.append(abs(math.log(len(self.documents) / (1 + w_appears))))
                else:
                    all_idf.append(0)

            self.idf_matrix.append(all_idf)


        # convert to numpy array idf matrix
        self.idf_matrix = np.array(self.idf_matrix)
        print(self.idf_matrix)
        return self.idf_matrix



if __name__ == '__main__':
    '''
    Corpus is all documents in a specific folder path.
    You should pass a path to a folder containing txt
    '''
    # select abs path to folder assets/corpus
    corpus = os.path.abspath("../assets/corpus")

    # ---------------------------
    # TF-IDF ALGORITHM BY IRIS ROBOTICS
    # ---------------------------

    # calculate execution time

    start_time = time.time()

    tfidf = TFIDF(corpus)
    tfidf_matrix = tfidf.tfidf()
    print("---------------------------")
    print("Processing TF-IDF matrix...")
    print("---------------------------")
    print(tfidf_matrix)

    print("\nExecution time: %s seconds" % (time.time() - start_time))
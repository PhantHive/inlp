import numpy as np


class BB_test:

    def __init__(self, X, Y, Z, word_dict, words):

        self.X = X
        self.Y = Y
        self.Z = Z
        self.word_dict = word_dict
        self.size = len(self.word_dict)
        self.embed_size = 10
        self.words = words

    def softmax(self, X):
        res = []
        for x in X:
            exp = np.exp(x)
            res.append(exp / exp.sum())
        return res

    def init_network(self):

        model = {
            "w1": np.random.randn(self.size, self.embed_size),
            "w2": np.random.randn(self.embed_size, self.size)
        }
        return model

    def forward(self, model, X, return_cache=True):
        cache = {}

        cache["a1"] = X @ model["w1"]
        cache["a2"] = cache["a1"] @ model["w2"]
        cache["z"] = self.softmax(cache["a2"])

        if not return_cache:
            return cache["z"]
        return cache
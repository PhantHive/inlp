from keras.models import Input, Model
from keras.layers import Dense
import matplotlib.pyplot as plt

class BBGraph:

    def __init__(self, X, Y, word_dict, words):

        self.X = X
        self.Y = Y

        self.embed_size = 2 # 3 dimensionnal graph
        self.embedding_dict = {}
        self.word_dict = word_dict
        self.words = words

        self.neural_network()

    def neural_network(self):

        inp = Input(shape=(self.X.shape[1],))

        x = Dense(units=self.embed_size, activation='linear')(inp)
        x = Dense(units=self.Y.shape[1], activation='softmax')(x)

        ai_model = Model(inputs=inp, outputs=x)
        ai_model.compile(loss='categorical_crossentropy', optimizer='adam')

        ai_model.fit(
            x=self.X,
            y=self.Y,
            batch_size=256,
            epochs=1000
        )


        weights = ai_model.get_weights()[0]
        bias = ai_model.get_weights()[1]

        print("\n\nWeights: \n", weights,
              "\n\nBiais: \n", bias)

        for word in self.words:

            self.embedding_dict.update({
                word: weights[self.word_dict.get(word)]
            })

    def show_graph(self):

        plt.figure(figsize=(20, 20))

        for word in list(self.word_dict.keys()):
            coord = self.embedding_dict.get(word)
            plt.scatter(coord[0], coord[1])
            plt.annotate(word, (coord[0], coord[1]))

        plt.show()
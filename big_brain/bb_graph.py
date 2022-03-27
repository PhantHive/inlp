from keras.models import Input, Model
from keras.layers import Dense
import matplotlib.pyplot as plt


class BBGraph:

    def __init__(self, X, Y, Z, word_dict, words):

        self.X = X
        self.Y = Y
        self.Z = Z

        self.embed_size = 3  # 3 dimensionnal graph
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
            y=self.Y,  # target matrix
            batch_size=256,
            epochs=2500
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

        fig = plt.figure(figsize=(10, 10))

        ax = fig.add_subplot(projection='3d')

        for word in list(self.word_dict.keys()):
            coord = self.embedding_dict.get(word)
            ax.scatter(coord[0], coord[1], coord[2])
            ax.text(coord[0], coord[1], coord[2], word)

        plt.show()

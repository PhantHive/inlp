import numpy as np

from src.tokenizer import TOKENIZE
from src.one_hot import OneHot
from src.ngrams import Ngram

class SkipGram:

    def __init__(self, window_size, embedding_size, alpha, corpus_path):
        '''
        :param window_size: the size of the window
        :param tokenize_matrix: the tokenize matrix of the text
        :param corpus_size: the size of the corpus
        :param embdding_size: the size of the embedding
        :param alpha: the learning rate
        '''

        self.hidden_weights = None
        self.hidden_biases = None
        self.window_size = window_size
        self.embedding_size = embedding_size
        self.alpha = alpha

        with open(corpus_path, "r", encoding="utf8") as f:
            self.corpus = f.read()

        self.tokenize = TOKENIZE(self.corpus)
        self.tokenize_matrix, self.filtred_corpus = self.tokenize.show_sentences()

        # remove the duplicates
        self.filtred_corpus = list(dict.fromkeys(self.filtred_corpus))

        self.corpus_size = len(self.filtred_corpus)
        print(f"Corpus size: {self.corpus_size}")

        print("Encoding the corpus...")
        one_hot = OneHot(self.filtred_corpus)
        encoded_words, self.onehot_dict = one_hot.encode()


        # random initialization of the weights
        self.output = np.zeros((self.corpus_size, self.embedding_size))
        # initialize the input and hidden layer weights and biases
        input_size = len(self.onehot_dict)
        self.hidden_size = self.embedding_size  # adjust this parameter as needed

        self.input_weights = np.random.rand(input_size, self.embedding_size)
        self.input_biases = np.zeros(self.hidden_size)

        self.hidden_weights = np.random.rand(self.hidden_size, self.embedding_size)
        self.hidden_biases = np.zeros(self.embedding_size)


    def train(self, epochs):
        '''
        :param epochs: the number of epochs
        This code will train the model for the number of epochs specified
        and will print the loss after each epoch.
        '''

        for epoch in range(epochs):
            print("==================================================")
            print(f"IRIS NLP Training {epoch + 1}/{epochs} epochs")
            print("==================================================")
            self.forward_propagation()



    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0)

    def crossentropy_loss(self, predicted, target, hidden_output):
        '''
        Computes the cross-entropy loss for the predicted and target vectors
        predicted: the predicted output of the model (softmax output)
        target: the one-hot encoded target vector
        hidden_output: the output of the hidden layer
        '''

        # calculate the error (difference between predicted and target)
        error = predicted - target

        # calculate the gradient of the output layer weights
        grad_weights_output = np.dot(error, hidden_output.T)

        # calculate the gradient of the output layer biases
        grad_biases_output = np.mean(error, axis=1)

        # calculate the gradient of the hidden layer weights
        grad_hidden = np.dot(self.input_weights.T, error) * (hidden_output > 0)
        grad_weights_hidden = np.dot(grad_hidden, hidden_output.T)
        grad_biases_hidden = np.mean(grad_hidden, axis=1)

        # calculate the total loss (cross-entropy loss)
        loss = -np.sum(target * np.log(predicted + 1e-8))

        return loss, [grad_weights_hidden, grad_biases_hidden, grad_weights_output, grad_biases_output]

    def forward_propagation(self):
        '''
        This code will compute the forward propagation of the model
        It uses the Ngram class to get the context words for each target word
        and then computes the forward propagation for each target word.
        '''

        ngram = Ngram(self.filtred_corpus, self.window_size)
        ngram.context()

        # for each target word in the corpus
        for i, target_word in enumerate(self.filtred_corpus):
            # skip the target word if it doesn't have any context
            if len(self.onehot_dict[target_word]) == 0:
                continue

            context_words = ngram.get_context_words(i)
            # print(f"Target word: {target_word} | Context words: {context_words}")
            # iterate over the context words for the target word
            for context_word in context_words:
                # encode the context word
                encoded_word = np.array(self.onehot_dict[context_word])
                encoded_word = encoded_word.reshape(encoded_word.shape[0], 1)

                # compute the input layer output
                input_output = np.dot(self.input_weights.T, encoded_word) + self.input_biases
                input_output = np.maximum(input_output, 0)  # apply ReLU activation

                # compute the hidden layer output
                hidden_output = np.dot(input_output, self.hidden_weights) + self.hidden_biases
                hidden_output = np.maximum(hidden_output, 0)  # apply ReLU activation

                # print("Hidden output: ", hidden_output)
                # print(self.hidden_weights)

                # compute the output
                self.output = np.dot(self.input_weights, hidden_output) + self.input_weights
                # compute the softmax
                softmax_output = self.softmax(self.output)

                # print("Softmax output: ", softmax_output)
                # print("Encoded word: ", encoded_word)

                # print("Softmax output: ", softmax_output.shape)
                # print("Encoded word: ", encoded_word.shape)

                loss, softmax_grad = self.crossentropy_loss(softmax_output, encoded_word, hidden_output)
                print(f"Loss: {loss}")

    def predict(self, word, k=3):
        '''
        :param word: the word to find similar words for
        :param k: the number of similar words to return
        This code will find the k most similar words to the input word
        based on the learned embeddings using cosine similarity.
        '''

        # get the one-hot encoding for the input word
        if word not in self.onehot_dict:
            return []

        encoded_word = np.array(self.onehot_dict[word])
        encoded_word = encoded_word.reshape(encoded_word.shape[0], 1)

        # compute the cosine similarity between the output vectors and the input vector
        similarities = np.dot(self.input_weights.T, encoded_word)
        similarities = similarities.reshape(similarities.shape[0])

        # get the indices of the k most similar words
        indices = similarities.argsort()[-k - 1:-1][::-1]
        print(f"Indices: {indices}")

        # get the words corresponding to the indices
        similar_words = [self.filtred_corpus[i] for i in indices]

        return similar_words

    def get_tokenized_matrix(self):
        return self.tokenize_matrix

    def get_filtred_corpus(self):
        return self.filtred_corpus

    def get_weights(self):
        return self.input_weights

    def get_biases(self):
        return self.input_biases



if __name__ == '__main__':

    skipgram = SkipGram(window_size=5, embedding_size=50, alpha=0.005, corpus_path="../assets/corpus/asian/asian.txt")

    # print(skipgram.get_tokenized_matrix())
    print(skipgram.get_filtred_corpus())
    # print(skipgram.get_weights())
    # print(skipgram.get_biases())

    skipgram.train(epochs=10)
    # print(skipgram.get_weights())
    # print(skipgram.get_biases())
    to_predict = "femme"
    similar_words = skipgram.predict(to_predict)
    print(f"Similar words to {to_predict}: {similar_words}")




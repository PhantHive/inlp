
<h1 align="center">IRIS NLP SYSTEM (INS or "inlp")</h1>

![Thumbnail of Hacker](assets/images/thumbnail.png)


Everything about NLP at IRIS-ROBOTICS (IPSA PARIS)  

# ♥ What is NLP? ♥

> NLP stands for Natural Language Processing. The main goal of NLP is to 
> use algorithm to encode/decode our natural language (french for example).
> NLP models are used in many fields such as:
> * Chatbots
> * Speech recognition
> * Sentiment analysis
> * Machine translation
> * Text summarization

## GOAL:
> The goal of this project is to create a chatbot on discord that will help students by understanding their request and giving them the correct ressources to work and succeed.

<br><br><br>
# ♥ Encoder Models ♥
> ***Here is a list of different encoding types for NLP (they are examples)
please remember that all of them can be used together depending on the purpose of the task to create a better model:***
![Thumbnail of Hacker](assets/images/course_1.png)
<br>*Please note: Frequency can also be used in neural networks, TD-IDF is built on top of it for example.* 


The image describe the field of use of each models.<br>
For example, we have:
- the **Frequency encoder** is used to create a **Matrix** of words occurences (the normalized frequency of each word in a document). <br><br>
- the **TF-IDF encoder** is used to create a **Matrix** of words occurences with a **weight**. The weight represents the importance of a word in a document. <br><br>
- **One-hot encoder** is used to create a **matrix** representing the presence of each word in a sentence. Where the presence corresponds to the index of the word in the vocabulary list. <br><br>
- **Word Embedding** is used to create a **matrix** representing the vectorial representation of each word. Each word is mapped to a high-dimensional vector, where the vector represents the semantic meaning of the word 
based on its context in the corpus.

As of today, INLP contains both **One-hot encoder**, **TF-IDF encoder** and a partially working **Word Embedding**.

<br><br>
# ♥ Tokenizer ♥

> The Tokenizer as its name suggest, tokenize all words in a text.
> Those words will be part of our **Matrix** output. But, they need to go through different process 
> before this.

<br><br>
## Pre-Process
During **Pre-processing**, text must be splitted into sentences. Those sentences will be again splitted into
a list of words. 

After this, the **Tokenizer** program removes **Stopwords**, and use **Stemming** or **Lemming** to keep only **root words**.
The use of **Stemming** or **Lemming** depends on the purpose of the task.

<br><br>
## Stemmer

The IrisStemmer follows basic rules in french to stem all words given.

Examples:
* Removing X
* Replacing words ending with AUX with AL

  | Before Stem       | After Stem         
  |:-------------|:------------------
  | Chevaux      | Cheval
  | Belle        | Bel
  | Bouygues     | Bouygu      
  | Assouplissement  | Assoupl

<br><br>
## Lemmer

The IrisLemmer uses a **Lexicon** to find the root form of a given word.

Examples:
* Using a Lexicon
* Replacing words with their corresponding root forms according to a lexicon.

  | Before Lem      | After Lem        
  |:----------------|:------------------
  | Chevaux         | Cheval
  | Belle           | Bel
  | Bouygues        | Bouygues      
  | Assouplissement | Assoupli

<br><br>
# ♥ Encoder ♥
> We will describe here the encoder used in the project Big Brain.

<br><br>
## One-hot Encoder

This encoder is a first step to create a Word Embedding encoder. It is used to create a matrix representing the presence of 
each word in a sentence. For example if there is 3 words in the vocabulary list, the matrix will be 3x3.
And the corresponding vectors for each word will be:
word1 = [1,0,0]
word2 = [0,1,0]
word3 = [0,0,1]

Example given a random set of words:

![one-hot.png](assets%2Fimages%2Fone-hot.png)

*Please note: The One-hot encoder doesn't give any information about the context and/or relation between the words.*

<br><br>
## N-grams

The N-grams algorithm is a first step into considering the context of the words.
The N-grams will give us a list of tuples of words. The size of the tuple depends on the choosen **N**.
Each tuple will be composed of a **focus word** (target word) and a **context word**. Where there might be
multiple context words, there can be only one focus word within one tuple.

Example given a random set of words:
![course_2.png](assets%2Fimages%2Fcourse_2.png)

<br><br>
# ♥ AI models used in the project ♥
> We will describe here the AI models used in the project Big Brain.
> We have 2 models: SkipGram and Transformer.

<br><br>
## SkipGram

> The SkipGram model is a neural network model that is used to create a Word Embedding encoder.
The goal of this model is to predict the context words given a focus word.
But behind this goal, in reality, for our final task we will use the "process" of the model: the weights matrices.
Those matrices will be used to create our Word Embedding encoder.

In fact, it is incredible to see how the model is able to represent the words in a vectorial space without actually be
created in this purpose. By "faking" the goal of the model to find the context words given a focus word, the model will
update the weights matrices in a way that the words that are close to each other in the vectorial space will have a high 
similarity score.

Process of the SkipGram:
- The SkipGram model takes in input a focus word represented as a one-hot encoded vector. <br><br>
- The model multiplies the input vector by a weights matrix of size (V x D), where V is the size of the vocabulary and D is the dimension of the embedding space.<br><br>
- The result of the multiplication is a vector of size (1 x D), which represents the embedding of the focus word in the D-dimensional space.<br><br>
- The model applies a softmax function to the result of the multiplication, which gives a probability distribution over the entire vocabulary. The probabilities represent the likelihood of each word being a context word of the focus word.<br><br>
- The model compares the probability distribution with the actual context words, which are also represented as one-hot encoded vectors.<br><br>
- The model updates the weights matrix using backpropagation and stochastic gradient descent, in order to minimize the difference between the predicted probability distribution and the actual context words.<br><br>
- The model repeats the process for each focus word in the corpus, updating the weights matrix at each step. The final result is a weights matrix that can be used as a word embedding encoder, where each row corresponds to the embedding of a word in the vocabulary.<br><br>

<br><br>
# End note
> the Big Brain project is complex and can seem overwhelming at first. 
> But, it is a great project to learn about NLP and AI. It is also a great way to improve yourself
> into programming and data science.
> 
> I hope this documentation will help you to understand the project and to be able to contribute to it.
> Don't be afraid to jump in and ask questions. We are all here to help each other.

> I will complete this documentation as I go along the project. I might be wrong on some points, so feel free to correct me.

<br><br>
# Author
**[Zakaria Chaouki](https://github.com/PhantHive)** 
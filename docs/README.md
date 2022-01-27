# IRIS-NLP (INLP DOC)

[![.github/workflows/ci.yaml](https://github.com/pages-themes/hacker/actions/workflows/ci.yaml/badge.svg)](https://github.com/pages-themes/hacker/actions/workflows/ci.yaml) [![Gem Version](https://badge.fury.io/rb/jekyll-theme-hacker.svg)](https://badge.fury.io/rb/jekyll-theme-hacker)

![Thumbnail of Hacker](assets/images/thumbnail.png)

## Global Usage



1. Fork this repository and clone it to your local device:

2. Call Tokenizer instance Tokenizer

    ```yml
    tokenizer = TOKENIZE(text) # Call tokenizer instance
    tokenizer.show_sentences() # Return 3 results:
    # 1. all words before tokenization
    # 2. NxM One-hot encoded Matrix
    # 3. all words after tokenization
    ```

## Stemming only

### Usage

1. Call IrisStemmer instance

   ```yml
   iris_stemmer = IrisStemmer() # Call Iris Stemmer instance
   iris_stemmer.stemmer(words) # Stem a list of words or a single string. 
   ```

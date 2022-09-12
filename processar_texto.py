from lib2to3.pgen2 import token
from nltk import word_tokenize, corpus
from nltk.corpus import floresta 

LINGUAGEM = "portuguese"

def get_palavras_de_parada():
    palavras_de_parada = set(corpus.stopwords.words(LINGUAGEM))

    return palavras_de_parada

def remover_palaras_de_parada(tokens):
    tokens_filtrados= []
    palavras_de_parada = get_palavras_de_parada:
    tokens_filtrados.

    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados


def obter_tokens(texto):
    tokens = word_tokenize(texto, LINGUAGEM)

    return tokens

def get_classificar_gramaticalmente():
      classificacoes = []

for (palavras, classificacao) in floresta.tagged_words():
 if "+" in classificacao:
      classificacao = classificacao[classificacao.index("+")+1:]
      
    return classificacoes

def classificar_gramaticalmente(tokens):
    pass 


def imprimir_tokens(tokens):
    for token in tokens:
        print(f"token: {token} ")


if __name__ == "__main__":
    texto = "a verdadeira generosidade para com o futuro consiste em dar tudo ao presente"

tokens = obter_tokens(texto)
imprimir_tokens(tokens)


remover_palaras_de_parada()
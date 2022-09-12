from lib2to3.pgen2 import token
from nltk import word_tokenize, corpus
from nltk.corpus import floresta
from nltk.stem import RSLPStemmer

LINGUAGEM = "portuguese"


def get_palavras_de_parada():
    palavras_de_parada = set(corpus.stopwords.words(LINGUAGEM))

    return palavras_de_parada


def remover_palaras_de_parada(tokens):
    tokens_filtrados = []
    palavras_de_parada = get_palavras_de_parada()

    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados


def obter_tokens(texto):
    tokens = word_tokenize(texto, LINGUAGEM)

    return tokens


def get_classificacoes_gramaticais():
    classificacoes = {}  # coleção

    for (palavras, classificacao) in floresta.tagged_words():
        if "+" in classificacao:
            classificacao = classificacao[classificacao.index("+") + 1]

        classificacoes[palavras.lower()]= classificacao

    return classificacoes

def estemizar(tokens):
    estemizador = RSLPStemmer()

    for token in tokens:
        print(f"A raiz da paravra {token} é {estemizador.stem(token)}")





def classificar_gramaticalmente(tokens):
    classificacoes = get_classificacoes_gramaticais()

    for token in tokens:
       classificacao = classificacoes[token]
        
       print(f"a palavra {token} e uma {classificacao}")


def imprimir_tokens(tokens):
    for token in tokens:
        print(f"token: {token} ")


if __name__ == "__main__":
    texto = "a verdadeira generosidade para com o futuro consiste em dar tudo ao presente"

    tokens = obter_tokens(texto)
# # imprimir_tokens(tokens)


# # remover_palaras_de_parada()
#     classificar_gramaticalmente(tokens)
    estemizar(tokens)
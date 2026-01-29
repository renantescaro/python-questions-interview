"""
Escreva uma função que determina se uma string termina com 'A' e começa com 'B'.
"""

@staticmethod
def check_str_characters(word: str) -> bool:
    """verifica se uma string termina com 'A' e começa com 'B'"""

    if not word:
        raise Exception("'Word' não pode ser vazia")

    word = word.lower()

    if word[0] == "b" and word[-1] == "a":
        return True

    return False


# print(check_str_characters("Bola"))

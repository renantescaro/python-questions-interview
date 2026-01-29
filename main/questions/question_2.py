"""
Considerando a sequência numérica a seguir (11, 18, 25, 32, 39... )
Faça uma função que recebe como entrada uma posição e devolve qual o valor do número naquela posição,
Considerando a sequência numérica apresentada, para todos os efeitos, a sequência começa da posição 1.

print_valor(x=1) retornará 11;
print_valor(x=2) retornará 18;
print_valor(x=200) retornará 1404;
print_valor(x=254) retornará 1.782;
print_valor(x=3.542.158) retornará 24.795.110;
"""

@staticmethod
def get_value_from_numerical_sequence(index: int):
    """
    Recebe como entrada uma posição e retorna o valor do número daquela posição
    """

    if not index:
        raise Exception("'index' não pode ser vazio")

    if index <= 0:
        raise Exception("'index' não pode ser negativo ou igual a zero")

    start = 11
    step = 7
    index_start = 1
    final = start + ((index - index_start) * step)

    return final


# print(get_value_from_numerical_sequence(1))
# print(get_value_from_numerical_sequence(2))
# print(get_value_from_numerical_sequence(18))
# print(get_value_from_numerical_sequence(200))
# print(get_value_from_numerical_sequence(254))
# print(get_value_from_numerical_sequence(3542158))

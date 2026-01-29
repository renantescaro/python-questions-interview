import math

"""
Um jogo com tabuleiro unidirecional comporta dois jogadores. Vence quem chegar primeiro a última casa do tabuleiro com menos turnos.
Para caminhar com as peças, os jogadores utilizam uma roleta que sorteia se devem andar 1, 2 ou 3 casas.
Caso tire um número maior na roleta, que casas faltantes, o jogador deve iniciar novamente o percurso (como um looping), por exemplo, se faltam apenas duas casas para eu ganhar, e tiro 3 na roleta, devo caminhar as duas faltantes mais uma até a primeira casa do tabuleiro, reiniciando todo o percurso.
Regra: O tamanho mínimo do tabuleiro deve ser 3 casas sem um máximo.

Crie uma função que recebe o número de casas do tabuleiro e devolve:
1 - Quantidade mínimo de turnos para se chegar ao destino (caminho ótimo);
2 - Probabilidade de um usuário conseguir executar o caminho ótimo;
3 - Quantas combinações de movimentos diferentes um jogador conseguiria executar sem efetuar nenhum looping no tabuleiro.
"""


@staticmethod
def calculate_board_game_stats(board_size: int) -> tuple:
    # tabuleiro não pode ter menos que 3 casas
    if board_size < 3:
        raise Exception("Tabuleiro não pode ter menos que 3 casas")

    # maior número sorteado da roleta
    max_step = 3

    # quantidade min de turnos, arredonda o número pra cima
    min_turns = math.ceil(board_size / max_step)

    # probabilidade da roleta sortear o numero 3
    probability_number_3 = 1 / max_step

    # potencia da probabilidade do número 3 elevado a quantidade min de turnos
    success_probability = probability_number_3**min_turns

    total_valid_combinations = _count_total_combinations(board_size, max_step)

    return min_turns, success_probability, total_valid_combinations


@staticmethod
def _count_total_combinations(board_size: int, max_step: int):
    path_combinations = [0] * (board_size + 1)
    path_combinations[0] = 1

    for current_square in range(1, board_size + 1):
        for step in range(1, max_step + 1):
            previous_square = current_square - step

            if previous_square >= 0:
                ways_to_reach_previous = path_combinations[previous_square]
                path_combinations[current_square] += ways_to_reach_previous

    return path_combinations[board_size]


# print(calculate_board_game_stats(10))

"""
Escreva uma função que calcula o quanto um funcionário tem a receber de dois benefícios:
Férias e Décimo Terceiro Salário ao pedir demissão.
Simplificando o cenário, as férias zeram a cada aniversário de emprego (ou seja, ele sempre tirou as férias corretamente)
e o décimo terceiro zera a cada virada de ano (não fica nenhum valor residual de um ano para outro).
"""


def calculate_resignation_benefits(salary, admission_date, resignation_date):
    start_month_13th = admission_date.month

    # ano de saida maior que ano de admissao
    if resignation_date.year > admission_date.year:
        start_month_13th = 1

    # meses de trabalho pra receber 13º
    months_13th = resignation_date.month - start_month_13th
    if resignation_date.day >= 15:
        months_13th += 1

    if months_13th < 0:
        months_13th = 0

    # calculo valor do 13º
    thirteenth_salary = (salary / 12) * months_13th

    # calculo meses de férias
    months_vacation = (
        (resignation_date.year - admission_date.year) * 12
        + resignation_date.month
        - admission_date.month
    )

    if resignation_date.day < admission_date.day:
        months_vacation -= 1

    months_vacation %= 12

    vacation_base = (salary / 12) * months_vacation
    total_vacation = vacation_base * (4 / 3)
    total_to_receive = thirteenth_salary + total_vacation

    return thirteenth_salary, total_vacation, total_to_receive


# from datetime import date
# print(
#     calculate_resignation_benefits(
#         salary=3000.00,
#         admission_date=date(2023, 1, 10),
#         resignation_date=date(2023, 12, 20),
#     )
# )

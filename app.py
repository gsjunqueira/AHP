"""
Exemplo
"""
# coding=UTF-8

import matplotlib.pyplot as plt
from multicriterio.multicriterio import AHP


# https://en.wikipedia.org/wiki/Analytic_hierarchy_process_%E2%80%93_car_example
escolher_melhor_carro = AHP(
    metodo='',
    precisao=3,
    alternativas=['Accord Sedan', 'Accord Hybrid', 'Pilot', 'CR-V', 'Element', 'Odyssey'],
    criterios=['cost', 'safety', 'style', 'capacity'],
    sub_criterios={
        'cost': ['Purchase Price', 'Fuel Costs', 'Maintenance Costs', 'Resale Value'],
        'capacity': ['Cargo Capacity', 'Passenger Capacity']
    },
    matrizes_preferencias={
        'criterios': [
            [1, 3, 7, 3],
            [1 / 3, 1, 9, 1],
            [1 / 7, 1 / 9, 1, 1 / 7],
            [1 / 3, 1, 7, 1]
        ],
        'cost': [
            [1, 2, 5, 3],
            [1 / 2, 1, 2, 2],
            [1 / 5, 1 / 2, 1, 1 / 2],
            [1 / 3, 1 / 2, 2, 1]
        ],
        'Purchase Price': [
            [1, 9, 9, 1, 1 / 2, 5],
            [1 / 9, 1, 1, 1 / 9, 1 / 9, 1 / 7],
            [1 / 9, 1, 1, 1 / 9, 1 / 9, 1 / 7],
            [1, 9, 9, 1, 1 / 2, 5],
            [2, 9, 9, 2, 1, 6],
            [1 / 5, 7, 7, 1 / 5, 1 / 6, 1]
        ],
        'Fuel Costs': [
            [1, 1 / 1.13, 1.41, 1.15, 1.24, 1.19],
            [1.13, 1, 1.59, 1.3, 1.4, 1.35],
            [1 / 1.41, 1 / 1.59, 1, 1 / 1.23, 1 / 1.14, 1 / 1.18],
            [1 / 1.15, 1 / 1.3, 1.23, 1, 1.08, 1.04],
            [1 / 1.24, 1 / 4, 1.14, 1 / 1.08, 1, 1 / 1.04],
            [1 / 1.19, 1 / 1.35, 1.18, 1 / 1.04, 1.04, 1]
        ],
        'Maintenance Costs': [
            [1, 1.5, 4, 4, 4, 5],
            [1 / 1.5, 1, 4, 4, 4, 5],
            [1 / 4, 1 / 4, 1, 1, 1.2, 1],
            [1 / 4, 1 / 4, 1, 1, 1, 3],
            [1 / 4, 1 / 4, 1 / 1.2, 1, 1, 2],
            [1 / 5, 1 / 5, 1, 1 / 3, 1 / 2, 1]
        ],
        'Resale Value': [
            [1, 3, 4, 1 / 2, 2, 2],
            [1 / 3, 1, 2, 1 / 5, 1, 1],
            [1 / 4, 1 / 2, 1, 1 / 6, 1 / 2, 1 / 2],
            [2, 5, 6, 1, 4, 4],
            [1 / 2, 1, 2, 1 / 4, 1, 1],
            [1 / 2, 1, 2, 1 / 4, 1, 1]
        ],
        'safety': [
            [1, 1, 5, 7, 9, 1 / 3],
            [1, 1, 5, 7, 9, 1 / 3],
            [1 / 5, 1 / 5, 1, 2, 9, 1 / 8],
            [1 / 7, 1 / 7, 1 / 2, 1, 2, 1 / 8],
            [1 / 9, 1 / 9, 1 / 9, 1 / 2, 1, 1 / 9],
            [3, 3, 8, 8, 9, 1]
        ],
        'style': [
            [1, 1, 7, 5, 9, 6],
            [1, 1, 7, 5, 9, 6],
            [1 / 7, 1 / 7, 1, 1 / 6, 3, 1 / 3],
            [1 / 5, 1 / 5, 6, 1, 7, 5],
            [1 / 9, 1 / 9, 1 / 3, 1 / 7, 1, 1 / 5],
            [1 / 6, 1 / 6, 3, 1 / 5, 5, 1]
        ],
        'capacity': [
            [1, 1 / 5],
            [5, 1]
        ],
        'Cargo Capacity': [
            [1, 1, 1 / 2, 1 / 2, 1 / 2, 1 / 3],
            [1, 1, 1 / 2, 1 / 2, 1 / 2, 1 / 3],
            [2, 2, 1, 1, 1, 1 / 2],
            [2, 2, 1, 1, 1, 1 / 2],
            [2, 2, 1, 1, 1, 1 / 2],
            [3, 3, 2, 2, 2, 1]
        ],
        'Passenger Capacity': [
            [1, 1, 1 / 2, 1, 3, 1 / 2],
            [1, 1, 1 / 2, 1, 3, 1 / 2],
            [2, 2, 1, 2, 6, 1],
            [1, 1, 1 / 2, 1, 3, 1 / 2],
            [1 / 3, 1 / 3, 1 / 6, 1 / 3, 1, 1 / 6],
            [2, 2, 1, 2, 6, 1]
        ]
    },
    log=True
)
resultado = escolher_melhor_carro.resultado()
print(resultado)

plt.bar(resultado.keys(), resultado.values())
plt.ylabel("Prioridade")
plt.show()

# Projeto Multicritério - AHP

Este projeto implementa a metodologia de cálculo **AHP (Analytic Hierarchy Process)**, uma técnica de apoio à decisão multicritério. O AHP é utilizado para modelar decisões complexas e comparações pareadas, auxiliando na escolha da melhor alternativa com base em múltiplos critérios.

## Estrutura do Projeto

- `multicriterio.py`: Contém a implementação da classe `AHP`, responsável pelos cálculos e estruturação do modelo AHP.
- `app.py`: Script principal onde o AHP é aplicado, utilizando a classe `AHP` para resolver problemas de decisão multicritério.

## Metodologia AHP

O **AHP** é uma metodologia desenvolvida por Thomas L. Saaty na década de 1970 e é amplamente utilizada para tomada de decisões complexas. Ela se baseia em:

1. **Decomposição do problema**: Dividindo o problema em uma hierarquia de objetivos, critérios, subcritérios e alternativas.

2. **Comparações pareadas**: Avaliando os elementos em pares, utilizando uma escala de importância para determinar qual elemento é preferido e em que grau.

3. **Cálculo de pesos**: Utilizando os resultados das comparações para calcular pesos para cada critério e alternativa.

4. **Síntese**: Combinando os pesos para determinar a pontuação global das alternativas e, assim, identificar a melhor escolha.

## Uso da Classe AHP

A classe `AHP` possui métodos que facilitam a criação e a resolução de problemas de decisão seguindo a metodologia AHP.

### Exemplo Básico de Uso

```python
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
```

## Instalação

Certifique-se de ter o Python instalado em sua máquina. Clone o repositório e utilize os arquivos multicriterio.py e app.py conforme necessário`

```git clone https://github.com/gsjunqueira/AHP.git
```

## Requisitos

- Python 3.x

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests para melhorias.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo <p style="color:blue">LICENSE</p> para mais detalhes.

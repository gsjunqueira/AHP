'''
O Método Analytic Hierarchy Process "AHP" é uma técnica de apoio à tomada de decisão, sendo
utilizada para resolver problemas complexos de decisão, onde múltiplos critérios e alternativas
precisam ser avaliados. Este método foi desenvolvido pelo matemático Thomas Saaty na década de 1970.

__author__ Giovani Santiago Junqueira
'''
# coding=UTF-8

import numpy as np
from numpy.linalg import matrix_power, eigvals


class AHP():
    """ 
    A classe AHP (Analytic Hierarchy Process) implementa o método AHP para a tomada de decisão
    baseada em múltiplos critérios.

    O AHP permite decompor um problema de decisão em uma hierarquia de objetivos, critérios e
    alternativas. Com base em comparações par-a-par, a classe calcula pesos para cada critério e
    alternativa, e os utiliza para determinar a melhor escolha entre as alternativas disponíveis.
    
    """


    def __init__(self, metodo, precisao, alternativas, criterios, sub_criterios,
                 matrizes_preferencias, log=False):
        self.metodo = metodo
        self.precisao = precisao
        self.alternativas = alternativas
        self.criterios = criterios
        self.sub_criterios = sub_criterios
        self.matrizes_preferencias = matrizes_preferencias
        self.log = log

        self.prioridades_globais = []


    @staticmethod
    def aproximado(matriz, precisao):
        """ Este méodo calcula a média das linhas de uma matriz normalizada e arredonda o resultado
        para a precisão especificada.
        
        Args:
            matriz (np.ndarray): A matriz de entrada, onde cada elemento representa um valor
            numérico.
            precisao (int): O número de casas decimais para o qual as médias das linhas devem
            ser arredondadas.
            
        Returns:
            np.ndarray: Um array unidimensional contendo as médias das linhas da matriz normalizada,
            arredondadas para a precisão especificada.
        """
        soma_colunas = matriz.sum(axis=0)
        matriz_norm = np.divide(matriz, soma_colunas)
        media_linhas = matriz_norm.mean(axis=1)

        return media_linhas.round(precisao)


    @staticmethod
    def geometrico(matriz, precisao):
        """ Este méodo calcula a média geométrica de cada linha de uma matriz e normaliza os
        resultados, arredondo-os para a precisão especificada.
        
        Args:
            matriz (np.ndarray): A matriz de entrada, onde cada elemento representa um valor
            numérico.
            precisao (int): O número de casas decimais para o qual as médias das linhas devem
            ser arredondadas.
            
        Returns:
            np.ndarray: Um array unidimensional contendo as médias geométricas normalizadas das
            de cada linha, arredondadas para a precisão especificada.
        """
        media_geometrica = [np.prod(linha) ** (1 / len(linha)) for linha in matriz]
        media_geometrica_norm = media_geometrica / sum(media_geometrica)

        return media_geometrica_norm.round(precisao)


    @staticmethod
    def autovalor(matriz, precisao, interacao=100, autovetor_anterior=None):
        """ Este método calcula o autovetor principal de uma matriz utilizando o método de iteração
        de potências, com uma precisão e um número máximo de iterações especificados.
        
        Args:
            matriz (np.ndarray): A matriz quadrada de entrada, onde cada elemento representa um
            valor numérico.
            precisao (int): O número de casas decimais para o qual o autovetor deve ser arredondado.
            interacao (int, opcional): O número máximo de iterações para o cálculo do autovetor. O
            padrão é 100.
            autovetor_anterior (np.ndarray, opcional): O autovetor calculado na iteração anterior.
            Se não fornecido, será iniciado com um vetor de zeros.

        Returns:
            np.ndarray: O autovetor principal arredondado para a precisão especificada.
        """
        matriz_quadrada = matrix_power(matriz, 2)
        soma_linhas = np.sum(matriz_quadrada, axis=1)
        soma_coluna = np.sum(soma_linhas, axis=0)
        autovetor_atual = np.divide(soma_linhas, soma_coluna)

        if autovetor_anterior is None:
            autovetor_anterior = np.zeros(matriz.shape[0])

        diferenca = np.subtract(autovetor_atual, autovetor_anterior).round(precisao)
        if not np.any(diferenca):
            return autovetor_atual.round(precisao)

        interacao -= 1

        return AHP.autovalor(matriz_quadrada, precisao, interacao, autovetor_atual
                             ) if interacao > 0 else autovetor_atual.round(precisao)


    @staticmethod
    def consistencia(matriz):
        """ Este método calcula o índice de consistência (IC) e a razão de consistência (RC) de uma
        matriz de comparação, aplicando o teorema de Perron-Frobenius para avaliar se a matriz
        mantém consistência lógica.
        
        Args:
            matriz (np.ndarray): A matriz de comparação, onde cada elemento representa um valor
            numérico.

        Returns:
            tuple: Uma tupla contendo:
                - `lambda_max` (float): O maior autovalor da matriz.
                - `IC` (float): O índice de consistência da matriz.
                - `RC` (float): A razão de consistência da matriz.

        """
        if matriz.shape[0] and matriz.shape[1] > 2:
            # Teorema de Perron-Frobenius
            lambda_max = np.real(eigvals(matriz).max())
            consist_index = (lambda_max - len(matriz)) / (len(matriz) - 1)
            randon_consist_index = {3: 0.52, 4: 0.89, 5: 1.11, 6: 1.25, 7: 1.35, 8: 1.40, 9: 1.45,
                  10: 1.49, 11: 1.52, 12: 1.54, 13: 1.56, 14: 1.58, 15: 1.59}
            consist_ratio = consist_index / randon_consist_index[len(matriz)]
        else:
            lambda_max = 0
            consist_index= 0
            consist_ratio = 0

        return lambda_max, consist_index, consist_ratio


    def local_priority_vector(self):
        """ Este método calcula o vetor de prioridades locais para cada critério com base nas
        matrizes de preferências armazenadas.
        
        Returns:
            dict: Um dicionário onde as chaves são os critérios e os valores são os vetores de
            prioridades locais calculados para cada critério.
        """
        vetor_prioridades_locais = {}
        for criterio in self.matrizes_preferencias:
            matriz = np.array(self.matrizes_preferencias[criterio])
            if self.metodo == 'aproximado':
                prioridades_locais = self.aproximado(matriz, self.precisao)
            elif self.metodo == 'geometrico':
                prioridades_locais = self.geometrico(matriz, self.precisao)
            else:
                if matriz.shape[0] and matriz.shape[1] >= 2:
                    prioridades_locais = self.autovalor(matriz, self.precisao)
                else:
                    prioridades_locais = self.aproximado(matriz, self.precisao)

            vetor_prioridades_locais[criterio] = prioridades_locais

            lambda_max, c_index, c_ratio = self.consistencia(matriz)

            if self.log:
                print('\nPrioridades locais do criterio ' + criterio + ':\n', prioridades_locais)
                print('Soma: ', np.round(np.sum(prioridades_locais), self.precisao))
                print('Lambda_max = ', lambda_max)
                print('Indice de Consistencia ' + criterio + ' = ', round(c_index, self.precisao))
                print('Razão de Concistência ' + criterio + ' = ', round(c_ratio, 2))

        return vetor_prioridades_locais


    def global_priority_vector(self, prioridades, pesos, criterios):
        """ Calcula o vetor de prioridades globais combinando as prioridades locais com os pesos dos
        critérios, e, em seguida, acumula as prioridades globais para os critérios ou subcritérios
        correspondentes.
        
        Args:
            prioridades (dict): Um dicionário onde as chaves são os critérios e os valores são os
            vetores de prioridades locais.
            pesos (list): Uma lista de pesos associados a cada critério.
            criterios (list): Uma lista de critérios para os quais as prioridades globais serão
            calculadas.

        Returns:
            None
        """
        for criterio in criterios:
            peso = pesos[criterios.index(criterio)]
            prioridades_locais = prioridades[criterio]
            prioridade_global = np.round(peso * prioridades_locais, self.precisao)

            if criterio in self.sub_criterios:
                self.global_priority_vector(prioridades, prioridade_global,
                                             self.sub_criterios[criterio])
            else:
                self.prioridades_globais.append(prioridade_global)

                if self.log:
                    print('\nPrioridades globais do criterio ' + criterio + '\n', prioridade_global)
                    print('Soma: ', sum(prioridade_global).round(self.precisao))


    def resultado(self):
        """ Este método calcula o vetor de prioridades globais para as alternativas e retorna o
        resultado como um dicionário.

        Returns:
            dict: Um dicionário onde as chaves são as alternativas e os valores são as prioridades
            globais calculadas para cada alternativa.
        """
        prioridades = self.local_priority_vector()
        self.global_priority_vector(prioridades, prioridades['criterios'], self.criterios)
        prioridades = np.array(self.prioridades_globais)
        prioridades = prioridades.sum(axis=0).round(self.precisao)

        return dict(zip(self.alternativas, prioridades))

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:31:20 2021

@author: tarfa
"""

from flask import Flask, request
import graphene
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS-HEADERS'] = 'Content-Type'


def max_apples2(A,K,L):
    SUBC_K = len(A) - (K-1) #indica quantos subconjuntos de K árvores seguidas posso formar
    SUBC_L = len(A) - (L-1)
    MAX_APPLES = -1 #INDICA O NÚMERO MAX DE MAÇÃS COLHIDAS POR AMBOS. INDICAMOS UM NUMERO BAIXO INICIAL
    INIT_K = -1
    INIT_L = -1
    for i in range(0,SUBC_K):
        for j in range(0,SUBC_L):
            if (j >= (i+K) or i > (j+L)):
                accumulator = 0
                #somando a sequencia de pés de maçã de Marcelo
                for x in range(i, i+K):
                    accumulator += A[x]
                #somando a sequencia de pés de maçã de Carla
                for x in range(j, j+L):
                    accumulator += A[x]
                if MAX_APPLES < accumulator :
                    INIT_K = i
                    INIT_L = j
                    MAX_APPLES = accumulator
    return [MAX_APPLES, INIT_K, INIT_L]
'''
OBJETIVO: ENCONTRAR A MELHOR COMBINAÇÃO SEQUENCIAL DE PÉS DE MAÇÃS QUE POSSUI A MAIOR SOMA
PARÂMETROS: 
    * A = UM ARRAY QUE INDICA O NUMERO DE MAÇÃS EM CADA ÁRVORE CONSECUTIVA
    * N_TREE = O NUMERO DE ÁRVORES QUE SERÃO COLHIDAS POR CARLA OU MARCELO
    * LAST_INIT_COUNT = REPRESENTA O INÍCIO DA COLETA DA ÚLTIMA PESSOA 
                        AVALIADA (CARLA OU MARCELO), POIS NAO PODEM COLETAR MAÇÃS 
                        DE UMA MESMA ÁRVORE. CASO NINGUEM FOI AVALIADO ANTERIORMENTE
                        O VALOR INICIAL É 0
    * LAST_N_TREE = REPRESENTA O NÚMERO DE ARVORES ANALISADAS ANTERIORMENTE, CASO
                    NENHUMA FOI LIDA, O VALOR É 0
RETORNO: UMA LISTA CONTENDO DOIS NÚMEROS: 
        1 - O NÚMERO MÁXIMO DE MAÇÃS COLHIDAS PELA PESSOA ENVIDA,
        2 - E O INÍCIO DA COLETA, SE COMEÇARÁ PELO PÉ 0,1,2,3...
'''
def max_apples_un(A, N_TREE, LAST_INIT_COUNT = 0, LAST_N_TREE = 0):
    '''INICIALMENTE O NUMERO MAXIMO DE MAÇÃS A SEREM COLETADAS É -1, JÁ O 
    INICIO DA CONTAGEM É A PARTIR DA POSIÇÃO INICIAL, 0'''
    MAX_APPLES = -1
    INIT_COUNT = 0
    INIT_COUNT_PERSON = -1 #assumimos que o inicio da coleta da pessoa atual é inválido
    if(LAST_INIT_COUNT == 0):#SIGNIFICA QUE TODAS AS ARVORES PODEM SER AVALIADAS
        while(INIT_COUNT+N_TREE <= len(A)):
            acumulador = 0
            for i in range(INIT_COUNT, INIT_COUNT+N_TREE):
                acumulador += A[i]
            if(MAX_APPLES < acumulador):
                MAX_APPLES = acumulador
                INIT_COUNT_PERSON = INIT_COUNT
            INIT_COUNT += 1
    else: #SE NAO, SIGNIFICA QUE ESTAMO ANALISANDO A SEGUNDA COLHEITA
        '''ENQUANTO HOUVER A POSSIBILIDADE DE ANALISAR O CONJUNTO DE ÁRVORES QUE SOBRARAM, 
           ANTES DE ALCANÇAR O INÍCIO DAS ÁRVORES ESCOLHIDAS PARA A PESSOA ANTERIOR, VAMOS ANALISA-LAS'''
        while(INIT_COUNT+N_TREE <= LAST_INIT_COUNT):
            acumulador = 0
            for i in range(INIT_COUNT, INIT_COUNT+N_TREE):
                acumulador += A[i]
            if(MAX_APPLES < acumulador):
                MAX_APPLES = acumulador
                INIT_COUNT_PERSON = INIT_COUNT
            INIT_COUNT += 1
        #INICIAMOS AGORA O SUBCONJUNTO APÓS O SUBCONJUNTO DA PESSOA ANTERIOR
        INIT_COUNT = LAST_INIT_COUNT + LAST_N_TREE
        #caso haja possibilidade de analisar árvores após as árvores escolhidas para a pessoa anterior
        while(INIT_COUNT+N_TREE <= len(A)):
            acumulador = 0
            for i in range(INIT_COUNT, INIT_COUNT+N_TREE):
                acumulador += A[i]
            if(MAX_APPLES < acumulador):
                MAX_APPLES = acumulador
                INIT_COUNT_PERSON = INIT_COUNT
            INIT_COUNT += 1
    return [MAX_APPLES, INIT_COUNT_PERSON]

'''
OBJETIVO: ENCONTRAR O NÚMERO MÁXIMO DE MAÇÃS COLHIDAS POR MARCELO E CARLA
PARÂMETROS: 
    * A -> UMA LISTA CONTENDO A QUANTIDADE DE MAÇÃS DE CADA PÉ, RESPECTIVAMENTE.
    * K -> NÚMERO DE PÉS QUE SERÃO ESCOLHIDOS PARA O MARCELO
    * L -> NÚMERO DE PÉS QUE SERÃO COLHIDOS POR CARLA
RETORNO: UMA LISTA COM 3 VALORES QUE REPRESENTAM
        1 - A MAIOR QUANTIDADE DE MAÇÃS QUE AMBOS PODERÃO COLHER
        2 - O PRIMEIRO PÉ DE MAÇÃ QUE O MARCELO IRÁ COLHER
        3 - O PRIMEIRO PÉ DE MAÇÃ QUE CARLA IRÁ COLHER
'''
def get_max_apples(A,K,L):
    if(len(A) < (K+L)): #COLHEITA INVÁLIDA!
        return [-1, -1, -1]
    '''
    caso a soma da quantidade de pés de maçã que marcelo(K) e carla(L) escolheram for igual,
    ao total em A, como todos os pés vão ser utilizadas, assumimos que marcelo iniciará
    da árvore 0, até a quantidade dele, e carla ficará com os demais pés de maçã, pois não irá interferir
    no resultado, caso um fique com uma parte e o outro com a outra, o importante é escolher todos os pés.
    '''
    print(len(A) == (K+L)) 
    if(len(A) == (K + L)):
        count = 0
        for n in A:
            count += n
        return [count, 0, K]
    if(L >= K):
            [N_APPLES_C,INIT_TREE_C]=max_apples_un(A, L)
            [N_APPLES_M,INIT_TREE_M]=max_apples_un(A, K, INIT_TREE_C, L)
    else:
        [N_APPLES_M,INIT_TREE_M]=max_apples_un(A, K)
        [N_APPLES_C,INIT_TREE_C]=max_apples_un(A, L, INIT_TREE_M, K)
    return [N_APPLES_M + N_APPLES_C, INIT_TREE_M, INIT_TREE_C]

class Query(graphene.ObjectType):
    max_apples = graphene.String(
            trees=graphene.String(required=True),
            n_marcelo=graphene.Int(required=True),
            n_carla=graphene.Int(required=True)
    )
    
    def resolve_max_apples(self, info, trees, n_marcelo, n_carla):
        list_str_tree = trees.split(",") #separo os números enviados por vigula, pois estará no formato "1,2,3,4"
        list_int_tree = list(map(int, list_str_tree)) #transformo a lista de string, em uma lista de int
        data_apples = max_apples2(list_int_tree, n_marcelo, n_carla)
        return (data_apples)

'''def main():
    result = schema.execute('{ maxApples(trees: "3,4,1,7,8,5", nMarcelo: 3, nCarla: 2) }' )
    print(result)'''

schema = graphene.Schema(query=Query)

@app.route("/graphql", methods=['POST'])
@cross_origin()
def apple_harvest():
    data = json.loads(request.data)
    print(data['query']);
    return json.dumps(schema.execute(data['query']).data)
                

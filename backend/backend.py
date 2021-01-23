# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:31:20 2021

@author: Ronaldo Tafarel
"""

from flask import Flask, request
import graphene
import json
from flask_cors import CORS, cross_origin
import re #para utilizar regex

app = Flask(__name__)

cors = CORS(app)
app.config['CORS-HEADERS'] = 'Content-Type'

'''
OBJETIVO: ENCONTRAR A MELHOR COMBINAÇÃO SEQUENCIAL DE PÉS DE MAÇÃS QUE POSSUI A MAIOR SOMA
PARÂMETROS: 
    * A = UM ARRAY QUE INDICA O NUMERO DE MAÇÃS EM CADA ÁRVORE CONSECUTIVA
    * K = O NUMERO DE ÁRVORES QUE SERÃO COLHIDAS POR MARCELO
    * L = O NUMERO DE ÁRVORES QUE SERÃO COLHIDAS POR CARLA 
RETORNO: UMA STRING COM 3 NÚMEROS, SEPARADOS POR VIRUGLAS ONDE:
        1º - INDICA O NÚMERO MÁXIMO DE MAÇÃS QUE PODEM SER COLHIDAS POR AMBOS
        2º - O INÍCIO DA COLHEITA DE MARCELO
        3º - O INÍCIO DA COLHEITA DE CARLA
'''
def get_max_apples(A,K,L):
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
    return "{},{},{}".format(MAX_APPLES, INIT_K, INIT_L)

class Query(graphene.ObjectType):
    max_apples = graphene.String(
            trees=graphene.String(required=True),
            n_marcelo=graphene.Int(required=True),
            n_carla=graphene.Int(required=True)
    )
    
    def resolve_max_apples(self, info, trees, n_marcelo, n_carla):
        regex_tree = re.compile("(\d(,\d)*)$")
        if regex_tree.match(trees) and n_carla > 0 and n_marcelo > 0:
            list_str_tree = trees.split(",") #separo os números enviados por vigula, pois estará no formato "1,2,3,4"
            list_int_tree = list(map(int, list_str_tree)) #transformo a lista de string, em uma lista de int
            data_apples = get_max_apples(list_int_tree, n_marcelo, n_carla)
            return (data_apples)
        else:
            return "Ops o atributo *trees* deve ser uma string do tipo: 1,5,3,4 os atributos *nMarcelo* e *nCarla* devem ser maior que 0"

schema = graphene.Schema(query=Query)

@app.route("/graphql", methods=['POST'])
@cross_origin()
def apple_harvest():
    data = json.loads(request.data)
    print(data['query']);
    return json.dumps(schema.execute(data['query']).data)
                

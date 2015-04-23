#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 26/10/2014

@author: Vagner Clementino
@summary: Classe que gerencia o lançamento de exceção para todo o software
@version: 0.9

'''
from control_asfbugscaper.LogManager import LogManager


class ASFBugScraperError(Exception):
    '''
            Classe para gerenciar a exibição de erro para o usuário
            Atributos:
               mensagem: a mensagem a se exibida ao usuário 
    '''


    def __init__(self, mensagem):
        try:
            self.__mensagem = mensagem
            self.__logFile = LogManager()
            self.__logFile.writeToLog("ERROR: {0}".format(self.__mensagem))
        except Exception as e:
            print (e.message)        
    def show_error(self):
        print(self.__mensagem)
        
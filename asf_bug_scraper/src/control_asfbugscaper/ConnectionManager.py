#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 22/04/2015

@author: vagner
'''
import psycopg2
from control_asfbugscaper.ASFBugScraperError import ASFBugScraperError


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class ConnetionManager(object):
    '''
    classdocs
    '''
    __DATABASE="projetosqm"
    __USER="sqm"
    __PASSWORD="sqm20151"
    __HOST="127.0.0.1"
    __PORT=5432

    def __init__(self):
        '''
        Constructor
        '''
        try:
            __dbConnection = None
            
        except Exception as e:
            raise ASFBugScraperError("Erro no construtor da classe. Detalhes: {0}".format(e.message))
    def connect(self):
        
        try:
            self.__dbConnection = psycopg2.connect(database=self.__DATABASE, user=self.__USER, password=self.__PASSWORD, host=self.__HOST, port=self.__PORT)
            
        except psycopg2.Error as e:
            raise ASFBugScraperError("Erro ao conectar o banco de dados: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))
        except Exception as ex:
            raise ASFBugScraperError("Erro desconhecido. Destalhes: {0}".format(ex.message))
    def close_connection(self):
        
        if self.__dbConnection == None:
            raise ASFBugScraperError("Erro ao fechar a conexão. Conexão não estabelecida")
        try:
            self.__dbConnection.close()
        except psycopg2.Error as e:
            raise ASFBugScraperError("Erro ao fechar a conexão com o banco de dados: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))
        except Exception as ex:
            raise ASFBugScraperError("Erro desconhecido. Destalhes: {0}".format(ex.message))
    def commit_transation(self):
        try:
            self.__dbConnection.commit()
            
        except psycopg2.Error as e:
            raise ASFBugScraperError("Erro ao realizar o commit da transição: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))
        except Exception as ex:
            raise ASFBugScraperError("Erro desconhecido. Destalhes: {0}".format(ex.message))
    def rollback_transation(self):
        try:
            self.__dbConnection.rollback()
             
        except psycopg2.Error as e:
            raise ASFBugScraperError("Erro ao realizar o rollback da transição: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror)) 
        except Exception as ex:
            raise ASFBugScraperError("Erro desconhecido. Destalhes: {0}".format(ex.message))
    def get_cursor(self):
        try:
            return_cursor = self.__dbConnection.cursor()
        except psycopg2.Error as e:
            raise ASFBugScraperError("Erro ao obter um cursor do banco: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))
        except Exception as ex:
            raise ASFBugScraperError("Erro desconhecido. Destalhes: {0}".format(ex.message))
        return return_cursor
    
    def close_cursor(self, a_cursor):
        try:
            a_cursor.close()
        except psycopg2.Error as e:
            raise ASFBugScraperError("Erro ao fechar um cursor do banco: Error code {0}. Descrição do erro: {1}".format(e.pgcode, e.pgerror))   
        except Exception as ex:
            raise ASFBugScraperError("Erro desconhecido. Destalhes: {0}".format(ex.message))
                
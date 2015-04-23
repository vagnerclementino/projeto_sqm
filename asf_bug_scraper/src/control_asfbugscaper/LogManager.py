#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 21/04/2015

@author: Vagner Clementino
'''


from datetime import datetime
import logging
from model_asfbugscaper.File import File


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class LogManager(object):
    '''
    classdocs
    '''
    
    #__singleInstance = None
    __logFile = None
    __LOGFILENAME="asf_bug_scraper"
   
    def __getLogFileName(self):
        
        try:
            #log_file_name = self.__LOGFILENAME + (datetime.now()).strftime('%d_%m_%Y_%H_%M_%S') + '.log'
            log_file_name = self.__LOGFILENAME + ".log"
            return log_file_name
        except Exception as e:
            logging.error("Erro ao definir o nome do arquivo de log. Detalhes: {0}".format(e.message))


    def __init__(self, logFileName=None, logFileLocalization=None):
        '''
        Constructor
        '''
        try:
            #if LogManager.__singleInstance:
            #    raise LogManager.__singleInstance
            #LogManager.__singleInstance = self
        
            self.__logFile = File(self.__getLogFileName(), ".", 'a')
                
        except Exception as e:
            logging.error("Erro ao criar o singleton. Detalhes: {0}".format(e.message))
        
    def __getFormatedTime(self):
        
            formatedString = "[{0}]".format(datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
            
            return (formatedString)
        
    def writeToLog(self, output_message):
            
            if self.__logFile != None:
                
                try:
                
                    self.__logFile.writeToFile("{0} {1}".format(self.__getFormatedTime(),output_message))
                    
                except Exception as e:
                    logging.error("Erro ao escrever no arquivo de log. Detalhes {0}".format(e.message))
            else:
                logging.error("O arquivo de log não está definido")               

#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 21/04/2015

@author: Vagner Clementino
'''
import os


class File(object):
    '''
    classdocs
    '''
   

    def __init__(self, name="asfbugscaper.log", localization=".", mode="A"):
        
        '''
        Constructor
        '''
        self.__filePointer = None
         
        self.__name = name
        
        if localization == ".":
            
            self.__localization = os.getcwd()
            
        self.__mode = mode.lower()
        
        #Abrindo o arquivo
        self.openFile(self.__mode)
        
    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return (self.__name)
    
    def setLocalization(self, localization):
        self.__localization = localization
        
    def getLocalization(self):
        return (self.__localization)
    
    def setMode(self, mode):
        self.__mode = mode
        
    def getMode(self):
        return(self.__mode)
    
    def openFile(self, mode="A"):
        
    
        self.__mode = mode.lower()
        
        if self.__mode == None:
            
            output_message = 'O modo de abertura não foi definido'
            
            raise Exception(output_message)
        
        if self.__name == None:
            
            output_message = 'O nome do arquivo não foi definido'
            
            raise Exception(output_message)
        
        
        if self.__filePointer == None:
            
            try:
                full_path = self.__localization + "/" + self.__name
                self.__filePointer = open(full_path, self.__mode)
                
            except (OSError, IOError) as e:
                
                output_message = "Erro em abrir o arquivo {0} localizado em {1}. Detalhes: {2}".format(self.__name, self.__localization, e.strerror)
                
                raise Exception(output_message)      
            
        else:
            output_message = "O arquivo {0} localizado em {1} já está aberto.".format(self.__name, self.__localization)
            raise Exception(output_message)

    def closeFile(self):
        
        if not self.__filePointer.closed:
            
            self.__filePointer.close()
            
        else:
            
            raise Exception('Não é possível fechar o arquivo. Ele não está aberto.')
        
    def writeToFile(self, output_message):
        
        if self.__filePointer != None and not self.__filePointer.closed:
            
            self.__filePointer.write(output_message)
            self.__filePointer.write("\n")
        
        else:
            
            raise Exception('Não foi possível escrever no arquivo {0}'.format(self.__name))
                  
     
        
        
        

#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 23/04/2015

@author: vagner
'''
from model_asfbugscaper.BugListModel import BugListModel
from control_asfbugscaper.ASFBugScraperError import ASFBugScraperError

class BugList(object):
    '''
        Classe para representar uma lista dos IDS dos bugs.
        A partir destes ID's será possível recuperar as informações dos Bugs
    '''
    __isEmpty = True
    __numberOfItems = 0
    __nextItem = 0
    __buglist = []
    #__bugListModel = None
    
    def __init__(self):
        '''
        Constructor
        '''
        try:
            __bugListModel = BugListModel()
            
            
        except Exception as e:
            raise ASFBugScraperError("Erro ao criar o objeto BugList. Detalhes: {0}".format(e.message))
        
    def retrieveAllBugs(self):
        '''
            Retorna a lista completa de bugs
        '''
        try:
            self.__bugListModel = BugListModel()
            self.__buglist = self.__bugListModel.retrieveAllIDS()
            self.__numberOfItems = len(self.__buglist)
            if(self.__numberOfItems > 0):
                self.__isEmpty = False
            #endIf
        except Exception as e:
            print(e.message)
            #raise ASFBugScraperError(e.message)
    #endDef   
    def length(self):
        '''
            Retorna o tamanho da lista de bugs ID
        '''
        return self.__numberOfItems
    #endDef
    def isEmpty(self):
        '''
            Retorna o TRUE se a lista estiver vazio, FALSE caso contrário
        '''
        return self.__isEmpty
    #endDef  

    def getNextBugID(self):
        '''
            Retorna o proximo ID de bug  da lista
        '''
        if (not self.__isEmpty):
            
            nextVal =  self.__buglist[self.__nextItem]
            self.__nextItem = self.__nextItem + 1
            return nextVal
        
        else:
                
            raise ASFBugScraperError("Erro: a lista está vazia")
        
        #endIf         
    #endDef
    
    def hasMore(self):
        '''
            Returna TRUE se existe mais algum item da lista para ser recuperado
            ou FALSE caso contrário
        '''
        hasMore = False
        if(self.isEmpty()):
            hasMore = False
        elif(0 <= self.__nextItem and  self.__nextItem < self.length() ):
            hasMore = True
        else:
            hasMore = False
            
        #endIf
        return hasMore        
    #EndDef          
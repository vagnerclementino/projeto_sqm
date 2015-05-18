'''
Created on 23/04/2015

@author: vagner
'''
from control_asfbugscaper.ASFBugScraperError import ASFBugScraperError

class BugList(object):
    '''
        Classe para representar uma lista dos IDS dos bugs.
        A partir destes ID's será possível recuperar as informações dos Bugs
    '''


    def __init__(self, ):
        '''
        Constructor
        '''
        try:
            __buglist = []
            __isEmpty = True
            __numberOfItems = 0
            __bugListModel = None
            __nextItem = 0
        except Exception as e:
            raise ASFBugScraperError("Erro ao criar o objeto BugList. Detalhes: {0}".format(e.message))
        
    def retrieveAllBugs(self):
        '''
            Retorna a lista completa de bugs
        '''
        None
    #endDef   
    def length(self):
        '''
            Retorna o tamanho da lista de bugs ID
        '''
        return self.____numberOfItems
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
        if len(not self.__isEmpty) > 0:
            
            return self.__buglist[self.__nextItem]
        
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
        elif(0 <= self.__nextItem and self.length()):
            hasMore = True
        else:
            hasMore = False
            
        #endIf
        return hasMore        
    #EndDef          
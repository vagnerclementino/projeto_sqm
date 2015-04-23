'''
Created on 23/04/2015

@author: vagner
'''
from control_asfbugscaper.ASFBugScraperError import ASFBugScraperError

class BugList(object):
    '''
    classdocs
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
        except Exception as e:
            raise ASFBugScraperError("Erro ao criar o objeto BugList. Detalhes: {0}".format(e.message))
        
    def retrieveAllBugs(self):
        None
       
    def length(self):
        return self.____numberOfItems
   
    def isEmpty(self):
        return self.__isEmpty
    
    def getAllBugs(self):
        None
        
    def getBug(self, an_bug_id):
        None
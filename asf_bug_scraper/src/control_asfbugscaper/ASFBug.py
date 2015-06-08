'''
Created on 20/05/2015

@author: vagner
'''
from model_asfbugscaper.ASFBugModel import ASFBugModel


class ASFBug(object):
    '''
    classdocs
    '''


    def __init__(self, bugID):
        '''
        Constructor
        '''
        self.__bugID = bugID
        self.__bugStatus = None
        self.__product = None
        self.__component = None
        self.__productVersion = None
        self.__hardware = None
        self.__importance = None
        self.__targetMilestone = None
        self.__assignedTo = None
        self.__reportedDate = None
        self.__reportedBy = None
        self.__lastModificationDate = None
        self.__bugDescription = None
        self.__asfBugModel = ASFBugModel()
        
        
    #endDef
    
    def getBugID(self):
        return self.__bugID  
      
    def setBugID(self, bugID):
        self.__bugID  = bugID
        
    def getBugStatus(self):
        return self.__bugStatus
    #endDef
    
    def setBugStatus(self, bugStatus):
        self.__bugStatus = bugStatus
    #endDef
    
    def getProduct(self):
        return self.__product
    #endDef
    
    def setProduct(self, product):
        self.__product = product
    #endDef
    
    def getComponent(self):
        return self.__component
    #endDef
    
    def setComponent(self, component):
        self.__component = component
    #endDef
    
    def getVersion(self):
        return self.__productVersion
    #endDef
    
    def setVersion(self, version):
        self.__productVersion = version
    #endDef
    
    def getHardware(self):
        return self.__hardware
    #endDef
    
    def setHardware(self, hardware):
        self.__hardware = hardware
    #endDef
    
    
    def getImportance(self):
        return self.__importance
    #endDef
    
    def setImportance(self, importance):
        self.__importance = importance
    #endDef
    
    def getTargetMilestone(self):
        return self.__targetMilestone
    #endDef
    
    def setTargetMilestone(self, targetMilestone):
        self.__targetMilestone = targetMilestone
    #endDef
    
    def getAssignedTo(self):
        return self.__assignedTo
    #endDef
    
    def setAssignedTo(self, assignedTo):
        self.__assignedTo = assignedTo
    #endDef
    
    def getReportedDate(self):
        return self.__reportedDate
    #endDef
    
    def setReportedDate(self, reportedDate):
        self.__reportedDate = reportedDate
    #endDef   
        
    def getReportedBy(self):
        return self.__reportedBy
    #endDef
    
    def setReportedBy(self, reportedBy):
        self.__reportedBy = reportedBy
    #endDef
        
    def getLastModificationDate(self):
        return self.__lastModificationDate
    #endDef
    
    def setLastModificationDate(self,lastModificationDate):
        self.__lastModificationDate = lastModificationDate
    #endDef
    
    def getBugDescription(self):
        return self.__bugDescription
    #endDef
    
    def setBugDescription(self, bugDescription):
        self.__bugDescription = bugDescription
    #endDef
    
    def toString(self):
        asfBugStr = "{\n"        
        asfBugStr = asfBugStr + "bugID: {}\n".format(self.getBugID())
        #asfBugStr = asfBugStr + "bugStatus: {}\n".format(self.getBugStatus())                              
        #asfBugStr = asfBugStr + "product : {}\n".format(self.getProduct())                          
        #asfBugStr = asfBugStr + "component : {}\n".format(self.getComponent())                           
        asfBugStr = asfBugStr + "productVersion : {}\n".format(self.getVersion())                          
        #asfBugStr = asfBugStr + "hardware : {}\n".format(self.getHardware())                          
        #asfBugStr = asfBugStr + "importance : {}\n".format(self.getImportance())                       
        #asfBugStr = asfBugStr + "targetMilestone : {}\n".format(self.getTargetMilestone())                           
        #asfBugStr = asfBugStr + "assignedTo : {}\n".format(self.getAssignedTo())                           
        #asfBugStr = asfBugStr + "reportedDate : {}\n".format(self.getReportedDate())                           
        #asfBugStr = asfBugStr + "reportedBy : {}\n".format(self.getReportedBy())
        #asfBugStr = asfBugStr + "lastModificationDate : {}\n".format(self.getLastModificationDate())
        #asfBugStr = asfBugStr + "bugDescription : {}\n".format(self.getBugDescription())
        asfBugStr = asfBugStr + "}"   
        return asfBugStr
    #endDef
    
    def save(self):
        
        self.__asfBugModel.persisteData(self)
    #endDef    
    def updateVersion(self):
        self.__asfBugModel.updateVersionData(self)
            
        
            
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 18/05/2015

@author: vagner
'''
import requests
from lxml import html
from requests.exceptions import RequestException, ConnectionError, HTTPError,\
    URLRequired, Timeout
from control_asfbugscaper.ASFBugScraperError import ASFBugScraperError
from ubuntu_sso.utils.ui import TRY_AGAIN_BUTTON

class BugScraper(object):
    '''
        Classe responsável por coletar os dados dos bugs no Apache Foundation
    '''

    __BASIC_URL ='https://bz.apache.org/bugzilla/show_bug.cgi?id='
    __SUCESS_CODE = 200
    
    '''
       XPATHS's dos campos a serem recuperados.
    '''
    __BUG_STATUS_XPATH = '//*[@id="static_bug_status"]/text()'
    __PRODUCT_XPATH = '//*[@id="field_container_product"]/text()'
    __COMPONENT_XPATH='//*[@id="field_container_component"]/text()'
    __VERSION_XPATH = '//*[@id="bz_show_bug_column_1"]/table/tr[6]/td/text()' 
    __HARDWARE_XPATH = '//*[@id="bz_show_bug_column_1"]/table/tr[7]/td/text()'
    __IMPORTANCE_XPATH = '//*[@id="bz_show_bug_column_1"]/table/tr[9]/td/text()' 
    __TARGET_MILESTONE_XPATH = '//*[@id="bz_show_bug_column_1"]/table/tr[10]/td/text()' 
    __ASSIGNED_TO_XPATH  = '//*[@id="bz_show_bug_column_1"]/table/tr[11]/td/span/span/text()'
    __BUG_URL_XPATH = '//*[@id="bz_show_bug_column_1"]/table/tr[13]/td/text()'
    __BUG_KEYWORDS_XPATH = '//*[@id="bz_show_bug_column_1"]/table/tbody/tr[14]/td/text()'
    __DUPLICATES_XPATH = '//*[@id="bz_show_bug_column_1"]/table/tr[16]/td/text()'
    __DEPENDS_ON_XPATH = '//*[@id="bz_show_bug_column_1"]/table/tr[17]/td/text()'
    __BLOCKS_XPATH = '//*[@id="bz_show_bug_column_2"]/table/tr[1]/td/text()[1]'
    __REPORTED_DATE_XPATH = '//*[@id="bz_show_bug_column_2"]/table/tr[1]/td/text()[1]'
    __REPORTED_BY_XPATH = '//*[@id="bz_show_bug_column_2"]/table/tr[1]/td/span/span/text()'
    __LAST_MODIFICATION_XPATH = '//*[@id="bz_show_bug_column_2"]/table/tr[2]/td/text()'
    __BUG_DESCRIPTION_XPATH = '//*[@id="c0"]/pre/text()'
    
    def __init__(self):
        '''
        
        '''
        
        self.__parsedHTML = html
       
        
        
    #endDef
    
    def __connect(self, url):
        
        try:
            asfResponse = requests.get(url)            
        except RequestException as e:
            raise ASFBugScraperError('There was an ambiguous exception that occurred while handling your request.Vide erro: {0}'.format(e))
        except ConnectionError as e:
            raise ASFBugScraperError('Ocorreu um erro de conexão. Detalhes: {0}'.format(e))
        except HTTPError as e:
            raise ASFBugScraperError('Ocorreu um erro de HTTP. Detalhes: {0}'.format(e))
        except URLRequired as e:
            raise ASFBugScraperError('A URL informada {0} não é válida. Detalhes: {1}'.format(url,e))
        except Timeout as e:
            raise ASFBugScraperError('Timeout da conexão. Detalhes: {0}'.format(e))
            
        '''----------------------------------------
                    Verificando se a conexao ocorreu
                    corretamente.
        ------------------------------------'''
        status_code = asfResponse.status_code
        
        if status_code == self.__SUCESS_CODE:
            self.__parsedHTML = html.fromstring(asfResponse.text)            
        else:
            raise ASFBugScraperError("Erro ao conectar com a url {0}. Status Code: {1}".format(url,status_code))                                     
    #endDef
    def __getBugStatus(self):
        retString = ""
        bugStatusList = self.__parsedHTML.xpath(self.__BUG_STATUS_XPATH)
        if len(bugStatusList) == 1:
            retString = bugStatusList[0].replace("\n","")
            #Removendo espaços adicionados
            retString = " ".join(retString.split())
            print retString
        else:
            ASFBugScraperError("Erro em recuperar o atributo 'bug_status'. Detalhes: numero de argumentos retornados é invalido")
    #endDef 
    
    def __getProduct(self):
        productList =  self.__parsedHTML.xpath(self.__PRODUCT_XPATH) 
        if len(productList) == 1:
            retString = productList[0]
            retString = retString.strip()
            print retString
        else:
            ASFBugScraperError("Erro em recuperar o atributo 'product'. Detalhes: numero de argumentos retornados é invalido")
            
    #endDef
    
    def __getComponet(self):
        componentList =  self.__parsedHTML.xpath(self.__COMPONENT_XPATH)
        if len(componentList) == 1:
            componentString = componentList[0]
            componentString = componentString.strip()
            print componentString
        else:
            ASFBugScraperError("Erro em recuperar o atributo 'component'. Detalhes: numero de argumentos retornados é invalido")
                
    #endDef
    
    def __getVersion(self):
        
        versionList =  self.__parsedHTML.xpath(self.__VERSION_XPATH)
        try:
            versionString = versionList[0]
            versionString = versionString.replace('\n','')
            versionString = versionString.strip()
            print versionString
        except IndexError as ie:
            ASFBugScraperError("Erro em recuperar o atributo 'version'. O número de atributos é invalido. Detalhes: { }".format(ie.message))
              
    #endDef
    
    def __getHardware(self):
        hardwareList = self.__parsedHTML.xpath(self.__HARDWARE_XPATH)
        try:
            hardwareString = hardwareList[0]
            hardwareString = hardwareString.replace('\n','')
            hardwareString = " ".join(hardwareString.split())
        except IndexError as ie:
            ASFBugScraperError("Erro em recuperar o atributo 'version'. O número de atributos é invalido. Detalhes: { }".format(ie.message))    
            
    #endDef    
    
    def __getImportance(self):
         
        importanceList = self.__parsedHTML.xpath(self.__IMPORTANCE_XPATH)
        try:
            importanceString = importanceList[0]
            importanceString = importanceString.replace('\n','')
            importanceString = " ".join(importanceString.split())
            print importanceString
        except IndexError as ie:
            ASFBugScraperError("Erro em recuperar o atributo 'version'. O número de atributos é invalido. Detalhes: { }".format(ie.message)) 
    #endDef
    
    def __getTargetMilestone(self):
        targetMilestoneList =  self.__parsedHTML.xpath(self.__TARGET_MILESTONE_XPATH)
        try:
            targetMilestoneString = targetMilestoneList[0]
            targetMilestoneString = targetMilestoneString.replace('\n','')
            targetMilestoneString = targetMilestoneString.strip()
            print targetMilestoneString
        except IndexError as ie:
            ASFBugScraperError("Erro em recuperar o atributo 'version'. O número de atributos é invalido. Detalhes: { }".format(ie.message)) 
    #endDef
    
    def __getAssignedTo(self):
        
        assignToList = self.__parsedHTML.xpath(self.__ASSIGNED_TO_XPATH)
        assignToString = self.__parsedHTML.xpath(self.__HARDWARE_XPATH)
        try:
            assignToString = assignToList[0]
            assignToString = assignToString.replace('\n','')
            assignToString = assignToString.strip()
            print assignToString
        except IndexError as ie:
            ASFBugScraperError("Erro em recuperar o atributo 'version'. O número de atributos é invalido. Detalhes: { }".format(ie.message))  
    #endDef
    
    def __getBugURL(self):
        print self.__parsedHTML.xpath(self.__BUG_URL_XPATH)
    #endDef
    
    def __getBugKeywords(self):
        print self.__parsedHTML.xpath(self.__BUG_KEYWORDS_XPATH)
    #endDef
    
    def __getDuplicatesBugs(self):
        print self.__parsedHTML.xpath(self.__DUPLICATES_XPATH)
              
    def __getDependsOn(self):
        print self.__parsedHTML.xpath(self.__DEPENDS_ON_XPATH)
    #endDef
    
    def __getBlocks(self):
        print self.__parsedHTML.xpath(self.__BLOCKS_XPATH)
    #endDef     
    
    def __getReportedDate(self):
        retValList =  self.__parsedHTML.xpath(self.__REPORTED_DATE_XPATH)
        if len(retValList) == 0:
            return None
        else:
            try:
                reportedString = retValList[0]
                reportedString = reportedString.replace('\n','')
                reportedString = reportedString.replace('by','')
                reportedString = reportedString.replace('UTC','')
                reportedString = reportedString.strip()
                print reportedString
            except IndexError as ie:
                ASFBugScraperError("Erro em recuperar o atributo 'version'. O número de atributos é invalido. Detalhes: { }".format(ie.message))
    #endDef
    
    def __getReportedBy(self):
        
        reportedByList =  self.__parsedHTML.xpath(self.__REPORTED_BY_XPATH)
        if len(reportedByList) == 0:
            return None
        else:
            try:
                reportedByString = reportedByList[0]
                reportedByString = reportedByString.replace('\n','')
                reportedByString = reportedByString.strip()
                print reportedByString
            except IndexError as ie:
                ASFBugScraperError("Erro em recuperar o atributo 'version'. O número de atributos é invalido. Detalhes: { }".format(ie.message))
    #endDef
    
    def __getLastModificationDate(self):
        
        lastModificationList =  self.__parsedHTML.xpath(self.__LAST_MODIFICATION_XPATH)
        if len(lastModificationList) == 0:
            return None
        else:
            try:
                lastModification = lastModificationList[0]
                lastModification = lastModification.replace('\n','')
                lastModification = lastModification.replace('by','')
                lastModification = lastModification.replace('(','')
                lastModification = lastModification.replace('UTC','')
                lastModification = lastModification.strip()
                print lastModification
            except IndexError as ie:
                ASFBugScraperError("Erro em recuperar o atributo 'version'. O número de atributos é invalido. Detalhes: { }".format(ie.message))   
    #endDef    
    
    def __getBugDescription(self):
        commentsList =  self.__parsedHTML.xpath(self.__BUG_DESCRIPTION_XPATH)
        if len(commentsList) == 0:
            return None
        else:
            try:
                comments = commentsList[0]
                comments = comments.replace('\n','')
                comments = comments.strip()
                print comments
            except IndexError as ie:
                ASFBugScraperError("Erro em recuperar o atributo 'version'. O número de atributos é invalido. Detalhes: { }".format(ie.message))        
    #endDef       
        
    def scraperBug(self,bugId):
        
        url = self.__BASIC_URL+str(bugId)
        
        self.__connect(url)
        self.__getBugStatus()
        self.__getProduct()
        self.__getComponet()
        self.__getVersion()
        self.__getHardware()
        self.__getImportance()
        self.__getTargetMilestone()
        self.__getAssignedTo()
        self.__getReportedDate()
        self.__getReportedBy()
        self.__getLastModificationDate()
        self.__getBugDescription()
           
    #endDef                               
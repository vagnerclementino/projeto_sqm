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

class BugScraper(object):
    '''
        Classe responsável por coletar os dados dos bugs no Apache Foundation
    '''

    __BASIC_URL ='https://bz.apache.org/bugzilla/show_bug.cgi?id='
    __SUCESS_CODE = 200
    
    def __init__(self):
        '''
        Do nothing
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
            print self.__parsedHTML.xpath('//*[@id="static_bug_status"]/text()')
            print self.__parsedHTML.xpath('//*[@id="field_container_product"]/text()')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_1"]/table/tr[6]/td/text()')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_1"]/table/tr[7]/td/text()')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_1"]/table/tr[9]/td/text()')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_1"]/table/tr[10]/td/text()')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_1"]/table/tr[11]/td/span/span/text()')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_1"]/table/tr[13]/td/text()')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_1"]/table/tbody/tr[14]/td/text()')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_1"]/table/tr[16]/td/text()')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_1"]/table/tr[17]/td/text()')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_2"]/table/tr[1]/td/text()[1]')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_2"]/table/tr[1]/td/span/span/text()[1]')
            print self.__parsedHTML.xpath('//*[@id="bz_show_bug_column_2"]/table/tr[2]/td/text()[1]')
            print self.__parsedHTML.xpath('//*[@id="c0"]/pre/text()')
        else:
            raise ASFBugScraperError("Erro ao conectar com a url {0}. Status Code: {1}".format(url,status_code))                                     
    #endDef
    
    def scraperBug(self,bugId):
        url = self.__BASIC_URL+str(bugId)
        self.__connect(url)
        
        
    
    #endDef                               
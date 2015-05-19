#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 17/05/2015

@author: vagner
'''
from control_asfbugscaper.ASFBugScraperError import ASFBugScraperError
from control_asfbugscaper.ConnectionManager import ConnetionManager


class BugListModel(object):
    '''
    classdocs
    '''

    __connection = None
    def __init__(self):
        '''
        Constructor        
         '''
        
        self.__connection = ConnetionManager()      
    #endDef
    
    
    def retrieveAllIDS(self):
        try:
            self.__connection = ConnetionManager()
            self.__connection.connect()
        
            listRetVal = []
        
            SQL_GET_SQ = '''SELECT BL.BUG_ID
                            FROM SQM.BUG_LIST BL;
                         '''           
            cur =  self.__connection.get_cursor()
            cur.execute(SQL_GET_SQ)
            for record in cur:
                listRetVal.append(record[0])
            self.__connection.close_cursor(cur)
            self.__connection.close_connection()
            return listRetVal
        except Exception as e:
            print(e.message)
            raise ASFBugScraperError(e.message)     
    #endDEf
    
        
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 21/04/2015

@author: Vagner Clementino
'''
import sys
from control_asfbugscaper import ASFBugScraperError
from control_asfbugscaper.LogManager import LogManager
from control_asfbugscaper.BugList import BugList




if __name__ == '__main__':
    try:
        
        log = LogManager()
        bugList = BugList()
        bugList.retrieveAllBugs();
        
        
        while bugList.hasMore():
            bugID = bugList.getNextBugID()
            print bugID            
        #EndWhile
        print "Total de Registros recuperados: {0}".format(counter)    
    except ASFBugScraperError as e:
        e.show_error()
        sys.exit(1)   
        
        
    print('Everythig ins gonna be alright!')     
            

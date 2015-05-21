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
from control_asfbugscaper.BugScraper import BugScraper




if __name__ == '__main__':
    try:
        
        log = LogManager()
        bugList = BugList()
        bugList.retrieveAllBugs()
        scraper = BugScraper()        
        
        while bugList.hasMore():
            bugID = bugList.getNextBugID()
            log.writeToLog("Recuperando informações do BUG {0}".format(bugID))
            bug = scraper.scraperBug(bugID)
            print bug.toString().decode('ascii', 'ignore')
            bug.save()
            print('#-------------------------------------------------------------------------------------------#')
        #EndWhile
        
        print('Everythig ins gonna be alright!')
        log.writeToLog('Everythig ins gonna be alright!')
        sys.exit(0)    
    except ASFBugScraperError as e:
        e.show_error()
        sys.exit(1)
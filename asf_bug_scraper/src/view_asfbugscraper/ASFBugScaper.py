'''
Created on 21/04/2015

@author: Vagner Clementino
'''
from control_asfbugscaper.LogManager import LogManager
import sys

if __name__ == '__main__':
    try:
        
        log = LogManager()
        
        log.writeToLog("Teste-45")
        log2 = LogManager()
        log2.writeToLog("Teste-456")
                
        
    except ASFBugScraperError as e:
        e.show_error()
        sys.exit(1)
        
        
    print('Everythig ins gonna be alright!')     
            

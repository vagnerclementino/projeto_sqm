'''
Created on 21/04/2015

@author: Vagner Clementino
'''
import sys
from control_asfbugscaper import ASFBugScraperError
from control_asfbugscaper.LogManager import LogManager
from control_asfbugscaper.ConnectionManager import ConnetionManager



if __name__ == '__main__':
    try:
        SQL_GET_SQ = '''SELECT * 
                        FROM sqm.bug_list bl
                        where bl.id_bug_list = %s;
                     '''
        log = LogManager()
        
        log.writeToLog("Teste-45")
        log2 = LogManager()
        log2.writeToLog("Teste-456")
        
        cm = ConnetionManager()
        cm.connect()
        cur = cm.get_cursor()
        cur.execute(SQL_GET_SQ, (22,))
        for record in cur:
            line_read = "{0} {1} {2}".format(record[0], record[1], record[2])
            log.writeToLog(line_read)
        cm.close_cursor(cur)
        cm.close_connection()
    except ASFBugScraperError as e:
        e.show_error()
        sys.exit(1)
    except Exception as e:
        print(e.message)
        sys.exit(1)
        
        
    print('Everythig ins gonna be alright!')     
            

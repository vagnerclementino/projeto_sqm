'''
Created on 20/05/2015

@author: vagner
'''
from control_asfbugscaper.ConnectionManager import ConnetionManager
from control_asfbugscaper.ASFBugScraperError import ASFBugScraperError
from datetime import datetime


class ASFBugModel(object):
    '''
    classdocs
    '''

    __connection = None
    def __init__(self):
        '''
        Constructor
        '''
        self.__connection = ConnetionManager()
        self.__connection.connect()
    #endDef     
    def persisteData(self,bug):
        try:
            
            
        
            
        
            SQL_INSERT = '''INSERT INTO "sqm"."temp_bug_data" (id_temp_bug_data,
                                                               bug_id,
                                                               bug_status,
                                                               product,
                                                               component,
                                                               hardware,
                                                               importance,
                                                               target_milestone,
                                                               assigned_to,
                                                               reported_date,
                                                               reported_by,
                                                               last_modification_date,
                                                               bug_description,
                                                               update_date)            

                            VALUES(nextval('temp_bug_data_id_temp_bug_data_seq'),
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s);
                         '''            
            cur =  self.__connection.get_cursor()
            cur.execute(SQL_INSERT, (bug.getBugID(),
                                     bug.getBugStatus(),
                                     bug.getProduct(),
                                     bug.getComponent(),
                                     bug.getHardware(),
                                     bug.getImportance(),
                                     bug.getTargetMilestone(),
                                     bug.getAssignedTo(),
                                     bug.getReportedDate(),
                                     bug.getReportedBy(),
                                     bug.getLastModificationDate(),
                                     bug.getBugDescription(),
                                     datetime.now()
                                     )
                        )
            self.__connection.commit_transation()
        except Exception as e:
            print e.message
            #raise ASFBugScraperError(e.message)
        
    #endDef     

from dataclasses import dataclass
from typing import TypedDict
from robot.api.deco import keyword, library
from autocore.Database import Database



class TeamAssignmentDB:

    def __init__(self, db: Database):
        self.__db = db

    @keyword
    def get_teamassignment_db(self, tname: str):
        """ TODO: Create a database query to retrieve the Team Assignment Details."""
        query = "SELECT  ut.name as Team_Name, u.name as Team_Lead, ul.code as Team_Location FROM kjt.userteam AS ut JOIN kjt.user AS u ON ut.teamLead = u.uid JOIN kjt.userlocation AS ul ON ut.location = ul.lid WHERE ut.name = %s;"
        
    
        result = self.__db.execute(query, (tname,))
        if result and len(result) > 0:
            row = result[0]
            return {
                'Team Name': row['Team_Name'],
                'Team Lead': row['Team_Lead'],
                'Team Location': row['Team_Location']
            }
        else:
            return None
        
    
    @keyword
    def get_agent_uid(self, agent_name: str):
        """ TODO: Create a database query to retrieve the Agent's UID."""
        query = "select * from kjt.user where name = %s;"
         
        return self.__db.execute(query, (agent_name,))[0]['uid']



# QA_DB_CREDS = {
#     "host": "qa-db.letsdochinese.com",
#     "user": "qaauto",
#     "password": "8bbz9k",
#     "port": "3306"
# }
# db = Database(database="kjt", host=QA_DB_CREDS['host'], user=QA_DB_CREDS['user'], password=QA_DB_CREDS['password'],port=QA_DB_CREDS['port'])       
# t = Authority(db=db)
# t.query_name_from_authority_table(aid="df726970-c211-11eb-893a-0afcf0c3c7ed")
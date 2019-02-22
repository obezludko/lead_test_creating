import psycopg2
from lead.lead_get_request import create_lead
from variables import connection_variables,saved_variables

"""lead creating with filled required and non-requaired parameters"""
create_lead()

"""Connect to database using connection variables"""
connection = psycopg2.connect(user = connection_variables.user,
                              password = connection_variables.password,
                              host = connection_variables.host,
                              port = connection_variables.port,
                              database = connection_variables.database)

"""Select created lead row from database"""
def select_lead():
    cursor = connection.cursor()
    click_id = saved_variables.click_id
    lead_select_query = 'select * FROM lead WHERE click_id = %s;'%click_id
    cursor.execute(lead_select_query)
    lead_row = cursor.fetchall()
    return lead_row

print(select_lead())
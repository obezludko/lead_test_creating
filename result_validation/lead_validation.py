import psycopg2
from lead.lead_get_request import create_lead
from variables import connection_variables, saved_variables

"""lead creating with filled required and non-requaired parameters"""
create_lead()

"""Connect to database using connection variables"""
connection = psycopg2.connect(user=connection_variables.user,
                              password=connection_variables.password,
                              host=connection_variables.host,
                              port=connection_variables.port,
                              database=connection_variables.database)

"""Select created lead row from database"""


def select_lead():
    cursor = connection.cursor()
    click_id = saved_variables.click_id
    lead_select_query = 'SELECT * ' \
                        'FROM lead ' \
                        'WHERE click_id = %s;' % click_id
    cursor.execute(lead_select_query)
    lead_cortage = cursor.fetchall()
    lead_row = lead_cortage[0]
    return lead_row


lead_parameters = select_lead()


def lead_click_id():
    lead_click_id = lead_parameters[6]
    return str(lead_click_id)


def lead_external_message_id():
    lead_external_message_id = lead_parameters[10]
    return str(lead_external_message_id)


def lead_extra_param():
    lead_extra_param = lead_parameters[16]
    return lead_extra_param


if lead_click_id() == saved_variables.click_id:
    print("Start click_id validation:\n",
          lead_click_id(), '=', saved_variables.click_id, " - PASSED")
else:
    print("Start click_id validation:\n",
          lead_click_id(), '!=', saved_variables.click_id, " - FAILED")

if lead_external_message_id() == saved_variables.external_message_id:
    print("Start external_message_id validation:\n",
          lead_external_message_id(), '=', saved_variables.external_message_id, " - PASSED")
else:
    print("Start external_message_id validation:\n",
          lead_external_message_id(), '!=', saved_variables.external_message_id, " - FAILED")

if lead_extra_param() == saved_variables.extra_param:
    print("Start extra_param validation:\n",
          lead_extra_param(), '=', saved_variables.extra_param, " - PASSED")
else:
    print("Start extra_param validation:\n",
          lead_extra_param(), '=', saved_variables.extra_param, " - FAILED")

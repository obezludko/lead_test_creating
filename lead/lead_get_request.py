import requests
import DB.saved_variables
import psycopg2
from DB import connection

def create_lead():
    link = 'http://159.69.18.119/lead?'
    lead_params = {
        'payout': DB.saved_variables.payout,
        'extra_param': DB.saved_variables.extra_param,
        'click_id': DB.saved_variables.click_id,
        'partner': DB.saved_variables.partner,
        'currency': DB.saved_variables.currency,
        'external_message_id': DB.saved_variables.external_message_id,
        'external_subscription_id': DB.saved_variables.external_subscription_id
    }
    return requests.get(link,lead_params)

create_lead()

# print('payout:' + DB.saved_variables.payout,
#     '\nextra_param:' + DB.saved_variables.extra_param,
#     '\nclick_id:' + DB.saved_variables.click_id,
#     '\npartner:' + DB.saved_variables.partner,
#     '\ncurrency:' + DB.saved_variables.currency,
#     '\nexternal_message_id:' + DB.saved_variables.external_message_id,
#     '\nexternal_subscription_id:' + DB.saved_variables.external_subscription_id
#       )


connection = psycopg2.connect(user = connection.user,
                              password = connection.password,
                              host = connection.host,
                              port = connection.port,
                              database = connection.database)

def select_lead():
    cursor = connection.cursor()
    click_id = '47946094'
    # click_id = DB.saved_variables.click_id
    lead_select_query = 'select * FROM lead WHERE click_id = %s;'%click_id
    cursor.execute(lead_select_query)
    lead_row = cursor.fetchall()
    return lead_row

print(select_lead())
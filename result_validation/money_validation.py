import psycopg2
from result_validation.lead_validation import *
from variables.saved_variables import payout,currency


connection = psycopg2.connect(user = connection_variables.user,
                              password = connection_variables.password,
                              host = connection_variables.host,
                              port = connection_variables.port,
                              database = connection_variables.database)

def select_currency_options():
    cursor = connection.cursor()
    currency = saved_variables.currency
    currency_select_query = "SELECT * " \
                            "FROM currency " \
                            "WHERE code = '%s'" %currency
    cursor.execute(currency_select_query)
    currency_row = cursor.fetchall()
    return currency_row

print(select_currency_options())
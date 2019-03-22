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
    currency_cortage = cursor.fetchall()
    currency_row = currency_cortage[0]
    return currency_row


currency_parameters = select_currency_options()


def currency_code():
    currency_code = currency_parameters[2]
    return currency_code

if currency_code() == saved_variables.currency:
    print("Start currency_code validation:\n",
              currency_code(), '=', saved_variables.currency)
else:
    print("Start currency_code validation:\n",
          currency_code(), '!=', saved_variables.currency)
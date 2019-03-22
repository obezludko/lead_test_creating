import psycopg2
from result_validation.lead_validation import *
from variables.saved_variables import payout, currency

connection = psycopg2.connect(user=connection_variables.user,
                              password=connection_variables.password,
                              host=connection_variables.host,
                              port=connection_variables.port,
                              database=connection_variables.database)


def select_currency_options():
    cursor = connection.cursor()
    currency = saved_variables.currency
    currency_select_query = "SELECT * " \
                            "FROM currency " \
                            "WHERE code = '%s'" % currency
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
          currency_code(), '=', saved_variables.currency, " - PASSED")
else:
    print("Start currency_code validation:\n",
          currency_code(), '!=', saved_variables.currency)


def currency_rate():
    currency_rate = currency_parameters[4]
    return currency_rate


def lead_money_from_gateway():
    money_from_gateway = lead_parameters[4]
    return money_from_gateway


def validate_money_from_gateway():
    validate_money_from_gateway = currency_rate() * \
                                  float(saved_variables.payout)
    return validate_money_from_gateway


if lead_money_from_gateway() == validate_money_from_gateway():
    print("Start money_from_gateway validation:\n",
          round(lead_money_from_gateway(), 2), '=', validate_money_from_gateway(), " - PASSED")
else:
    print("Start money_from_gateway validation:\n",
          lead_money_from_gateway(), '!=', validate_money_from_gateway(), " - FAILED")



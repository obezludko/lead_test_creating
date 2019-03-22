import requests
import variables.saved_variables


def create_lead():
    link = 'http://159.69.18.119/lead?'
    lead_params = {
        'payout': variables.saved_variables.payout,
        'extra_param': variables.saved_variables.extra_param,
        'click_id': variables.saved_variables.click_id,
        'partner': variables.saved_variables.partner,
        'currency': variables.saved_variables.currency,
        'external_message_id': variables.saved_variables.external_message_id,
        'external_subscription_id': variables.saved_variables.external_subscription_id
    }
    return requests.get(link, lead_params)


import requests
import DB.saved_variables

link = 'http://159.69.18.119/lead?'
lead_params = {
    'payout':DB.saved_variables.payout,
    'extra_param':DB.saved_variables.extra_param,
    'click_id':DB.saved_variables.click_id,
    'partner':DB.saved_variables.partner,
    'currency':DB.saved_variables.currency,
    'external_message_id':DB.saved_variables.external_message_id,
    'external_subscription_id':DB.saved_variables.external_subscription_id
         }

requests.get(link,lead_params)

print('payout:' + DB.saved_variables.payout,
    '\nextra_param:' + DB.saved_variables.extra_param,
    '\nclick_id:' + DB.saved_variables.click_id,
    '\npartner:' + DB.saved_variables.partner,
    '\ncurrency:' + DB.saved_variables.currency,
    '\nexternal_message_id:' + DB.saved_variables.external_message_id,
    '\nexternal_subscription_id:' + DB.saved_variables.external_subscription_id
      )
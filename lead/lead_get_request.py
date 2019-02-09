import requests
from lead.lead_params_generating import LeadQueryParams

link = 'http://lawn.mobstra.com'
lead_params = {
    'payout':LeadQueryParams.get_lead_payout(),
    'extra_param':LeadQueryParams.get_lead_extra_param(),
    'click_id':LeadQueryParams.get_click_for_lead(),
    'partner':LeadQueryParams.generate_partner(),
    'currency':LeadQueryParams.get_lead_currency(),
    'external_message_id':LeadQueryParams.get_lead_external_message_id(),
    'external_subscription_id':LeadQueryParams.get_lead_external_subscription_id()
         }

requests.get(link,lead_params)


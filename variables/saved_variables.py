from lead import lead_params_generating

''' 
Saved params for:
 1) lead generating
 2) using in select queries from database
'''
partner = lead_params_generating.LeadQueryParams.generate_partner()
click_id = lead_params_generating.LeadQueryParams.get_click_for_lead()
external_message_id = lead_params_generating.LeadQueryParams.get_lead_external_message_id()
external_subscription_id = lead_params_generating.LeadQueryParams.get_lead_external_subscription_id()
currency = lead_params_generating.LeadQueryParams.get_lead_currency()
payout = lead_params_generating.LeadQueryParams.get_lead_payout()
extra_param = lead_params_generating.LeadQueryParams.get_lead_extra_param()



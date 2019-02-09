import random
from click_sub.click import set_click_param

def generate_partner():
    partner_list = ['nouniqlead','test', 'test_reliz_shark',
                    'wapclick', 'u', 'testignore', 'leadtestignore',
                    'terd', 'u2', 'testlead', 'test_lead', 'testreb',
                    'v11test', 'v11rebtest2', 'testlead012', 'rebtest012',
                    'testrebsub', 'testrebsub2', 'prerelead', 'eboy', 'PBX']
    random_partner = random.choice(partner_list)
    return random_partner

def define_click_for_lead():
    click_for_lead = set_click_param()
    return click_for_lead

def lead_external_message_id():
    external_message_id = set_click_param() + 'q' + str(random.randint(1,1000))
    return external_message_id

def lead_external_subscription_id():
    external_subscription_id = set_click_param() + 'w' + str(random.randint(1,1000))
    return external_subscription_id

def currency_choice():
    currency_list = ['EUR','USD',
                     'ALL','KWD']
    random_currency = random.choice(currency_list)
    return random_currency

def payout_choice():
    payout = random.randint(0,15)
    return str(payout)

def lead_extra_param():
    extra_param = 'extra ' + str(random.randint(1,10)) + ' param'
    return extra_param





import random
from click_sub.click import set_click_param




external_message_id = str
external_subscription_id = str
currency = str
payout = float
extra_param = str

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


print(())

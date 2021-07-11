'''
title           : helpers.py
description     : Helper functions used for parsing the outcome of OpenSea APIs.
author          : mikejp
date_created    : 20210711
date_modified   : 20210711
version         : 1.0
python_version  : 3.6.8
'''

def parse_coolcats_data(coolcats_dict):
    
    coolcats_id = coolcats_dict['token_id']
    
    try:
        creator_username = coolcats_dict['creator']['user']['username']
    except:
        creator_username = None
    try:
        creator_address = coolcats_dict['creator']['address']
    except:
        creator_address = None
    
    try:
        owner_username = coolcats_dict['owner']['user']['username']
    except:
        owner_username = None
    
    owner_address = coolcats_dict['owner']['address']
    
    traits = coolcats_dict['traits']
    num_sales = int(coolcats_dict['num_sales'])
        
    result = {'coolcats_id': coolcats_id,
              'creator_username': creator_username,
              'creator_address': creator_address,
              'owner_username': owner_username,
              'owner_address': owner_address,
              'traits': traits,
              'num_sales': num_sales}
    
    return result


def parse_sale_data(sale_dict):
    
    is_bundle = False

    if sale_dict['asset'] != None:
        coolcats_id = sale_dict['asset']['token_id']
    elif sale_dict['asset_bundle'] != None:
        coolcats_id = [asset['token_id'] for asset in sale_dict['asset_bundle']['assets']]
        is_bundle = True
    
    
    seller_address = sale_dict['seller']['address']
    buyer_address = sale_dict['winner_account']['address']
    
    try:
        seller_username = sale_dict['seller']['user']['username']
    except:
        seller_username = None    
    try:
        buyer_username = sale_dict['winner_account']['user']['username']
    except:
        buyer_username = None
    
    timestamp = sale_dict['transaction']['timestamp']
    total_price = float(sale_dict['total_price'])
    payment_token = sale_dict['payment_token']['symbol']
    usd_price = float(sale_dict['payment_token']['usd_price'])
    transaction_hash = sale_dict['transaction']['transaction_hash']
    

    result = {'is_bundle': is_bundle,
              'coolcats_id': coolcats_id,
              'seller_address': seller_address,
              'buyer_address': buyer_address,
              'buyer_username': buyer_username,
              'seller_username':seller_username,
              'timestamp': timestamp,
              'total_price': total_price, 
              'payment_token': payment_token,
              'usd_price': usd_price,
              'transaction_hash': transaction_hash}
    
    return result



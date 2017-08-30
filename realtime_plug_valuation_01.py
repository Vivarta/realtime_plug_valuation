# This function needs to be called every time: 
# (1) right after more tokens are purchased, 
# (2) right after a new donation comes in
# (3) right before `ad_return` changes

# A event happening "right before this function call" means: the time that has passed since this event happened is 0.

def get_current_value(
    
    num_token_new, # the number of tokens purchased right before this function call
    
    v_unit_existing, # unit value of one token at the time of last function call
    num_token_existing, # integer, number of token in the pool at the time of last function call
    
    donation, # real, the amount of donation coming in right before this function call,

    ad_return, # float, advertisement return rate over the time frame of t
    t, # real, time passed since last function call
    
    v_unit_base=5 # real, base unit value of one token
    
    ):
    
    new_purchase = v_unit_base * num_token_new
    
    appreciated_value = donation + v_unit_existing * num_token_existing * (1 + ad_return) ** t
    
    total_value = new_purchase + appreciated_value
    
    num_token_total = num_token_new + num_token_existing
    
    return total_value / num_token_total

# # example function call
# num_token_new_ = 100
# v_unit_existing_ = 15
# num_token_existing_ = 2000
# donation_ = 200
# ad_return_ = 0.3
# t_ = 0.5
# v_unit_base_ = 5
# get_current_value(
    # num_token_new_, 
    # v_unit_existing_,
    # num_token_existing_,
    # donation_,
    # ad_return_,
    # t_,
    # v_unit_base_
# )
# # output 16.621553691892448
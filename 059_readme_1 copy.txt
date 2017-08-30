
------------------
function signature
------------------
get_current_value(num_token_new, v_unit_existing, num_token_existing, donation, ad_return, t, v_unit_base=5)


-----
Notes
-----

This function needs to be called every time: 
    (1) right after more tokens are purchased, 
    (2) right after a new donation comes in
    (3) right before `ad_return` changes

A event happening "right before this function call" means: the time that has passed since this event happened is 0.


----------
Parameters
----------
num_token_new: integer, the number of tokens purchased right before this function call
v_unit_existing: real, unit value of one token at the time of the previous function call
num_token_existing: integer, number of token in the pool at the time of the previous function call
donation: real, the amount of donation coming in right before this function call,
ad_return: float, advertisement return rate (as a fraction of `v_unit_existing * num_token_existing`) over the time frame of t
t: real, time passed since the previous function call
v_unit_base (default 5): real, base unit value of one token


------
return
------
float, the current unit value of one token


-------
Example
-------

# For the example described by "spreadsheet_brief.pdf", the function needs to be called twice. The 2nd call uses the returned value of the 1st call as argument `v_unit_existing`.

# 1st call, purchased token and donation
num_token_new_ = 39000
v_unit_existing_ = 5
num_token_existing_ = 0
donation_ = 50000
ad_return_ = 0.041
t_ = 0
v_unit_base_ = 5

v_unit_current_1 = get_current_value(
    num_token_new_, 
    v_unit_existing_,
    num_token_existing_,
    donation_,
    ad_return_,
    t_,
    v_unit_base_
) # 6.282051282051282


# 2nd call, advertisement income
num_token_new_ = 0
v_unit_existing_ = v_unit_current_1
num_token_existing_ = 39000
donation_ = 0
ad_return_ = 0.041
t_ = 1
v_unit_base_ = 5

v_unit_current_2 = get_current_value(
    num_token_new_, 
    v_unit_existing_,
    num_token_existing_,
    donation_,
    ad_return_,
    t_,
    v_unit_base_
) # 6.5396153846153835


# The new value per token is €6.5396153846153835 (based on a total value of €255,045)






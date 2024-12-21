## TODO take the user input
def user_input(res_req,curr_res2):
    """ Taking User Inputs  and doing resource check before taking in money """
    user_inp=str(input("What would you like? (espresso/latte/cappuccino):"))
    input_money=0.0
    res_flag=True
    if user_inp not in ['report','off']:
        res_flag=res_check(user_inp,res_req,curr_res2)
        if res_flag:
            print("Please insert coins.")
            money_quart=int(input("how many quarters?:"))*0.25
            money_dimes=int(input("how many dimes?:"))*0.10
            money_nickles = int(input("how many nickles?:"))*0.05
            money_pennies = int(input("how many pennies?:"))*0.01
            input_money=float(money_quart)+float(money_dimes)+float(money_nickles)+float(money_pennies)
        else:
            input_money=0.0

    return user_inp,input_money,res_flag
def report(curr_res):
    """ reporting current session of the machine"""
    for item in curr_res:
       if item in ['water','milk']:
         print(f" {item}:  {curr_res[item]}ml")
       elif item in ['coffee']:
         print(f" {item}:  {curr_res[item]}g")
       elif item in ['money']:
         print(f" {item}:  ${curr_res[item]}")
def res_check(ma_inp,res_req,curr_res2):
    """ resource check for water , coffee, milk """
    # req_water=res_req[ma_inp]['ingredients']['water']
    # req_coffee=res_req[ma_inp]['ingredients']['coffee']
    # if ma_inp!='espresso':
    #    req_milk=res_req[ma_inp]['ingredients']['milk']
    # else:
    #
    # req_cos=res_req[ma_inp]['cost']
    new_dict={}
    ### resouce check
    for item in ['water','coffee','milk']:
        if curr_res2[item]<res_req[ma_inp]['ingredients'][item]:
            print(f'Sorry there is not enough {item}')
            return False
        elif ma_inp=='espresso' and item=='milk':
            return True
    return True
def check_res(ma_inp,res_req,curr_res2):
    """ money check """
    req_water=res_req[ma_inp[0]]['ingredients']['water']
    req_coffee=res_req[ma_inp[0]]['ingredients']['coffee']
    req_milk=res_req[ma_inp[0]]['ingredients']['milk']
    req_cos=res_req[ma_inp[0]]['cost']
    new_dict={}
    ### resouce check
    # for item in ['water','coffee','milk']:
    #     if curr_res2[item]<res_req[ma_inp[0]]['ingredients'][item]:
    #         print(f'Sorry there is not enough {item}')
    #         return
    ### money check
    if ma_inp[1]<req_cos:
        print("Sorry that's not enough money. Money refunded.")
    elif ma_inp[1]>=req_cos:
        diff1= ma_inp[1]-req_cos
        new_dict['water']=curr_res2['water']-req_water
        new_dict['coffee']=curr_res2['coffee']-req_coffee
        new_dict['milk']=curr_res2['milk']-req_milk
        new_dict['money']=float(curr_res2['money'])+float(req_cos)
        #new_dict['water']
        print(f"Here is ${diff1} in change.")
        print(f"Here is your {ma_inp[0]}. Enjoy!")
        return new_dict

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
MENU['espresso']["ingredients"]["milk"]=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
resources['money']=0.0
curr_res1=resources
flag=True

while flag:
    mach_inp_lst = user_input(MENU, curr_res1)
    mach_inp=mach_inp_lst[0]
    money_inp=mach_inp_lst[1]
    res_fg=mach_inp_lst[2]
    #curr_res1['money']=float(curr_res1['money'])+float(money_inp)
    if mach_inp=='report':
        report(curr_res1)
        flag=True
    elif mach_inp=='off':
        flag=False
    else:
        #mach_inp_lst = user_input(MENU, curr_res1)
        if res_fg:
            curr_res1=check_res(mach_inp_lst,MENU,curr_res1)
            flag=True
        else:
            flag=False
    mach_inp_lst=[]
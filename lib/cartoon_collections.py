def roll_call_dwarves(dwarves_list):
    num = 1
    for name in dwarves_list:
        print(f'{num}. {name}')
        num += 1

def summon_captain_planet(list):
    new_list = []
    for item in list:
        new_list.append(f'{item.capitalize()}!')
    return new_list

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(list):
    for item in list:
        if item == "cheddar" or item == "gouda" or item == "camembert":
            return item
    return None

import random

def attack_handler(target, opponent):
    # turn the dict into a list of (name, data) pairs
    attacks_list = list(target.attacks.items())
    
    # pick one at random
    attack_name, attack_data = random.choice(attacks_list)
    
    print(f"{target.name} uses {attack_name}!")
    opponent.hp -= attack_data["damage"]
    print(f"{opponent} takes {attack_data["damage"]} damage!")
    return attack_name, attack_data

    
  
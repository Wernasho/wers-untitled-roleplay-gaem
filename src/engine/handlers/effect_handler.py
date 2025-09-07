# import json
# from effects import Dmg_over_time, on_turn_start
# def fx_handle(effect_id, target):
#   effect = {}
#   if effect_id == "":
#     print("An internal game error occured and the effect could not load propperly")
#     print("ERR_MISSING_ID")
#   with open(f"../../json/{effect_id}.json") as f:
#     effect = json.load(f)
#   with open("../data/types.txt", 'r') as t:
#     tlist = t.readlines()
  
#   if effect["type"] not in tlist:
#     print("An internal game error occured and the effect could not load propperly")
#     print("ERR_MISSING_TYPE")
#   # elif effect["type"] == "dmgOverTime":
#   #   on_turn_start(, )

"""uhh, this was scrapped because I had no idea what I was doing (I still don't)"""
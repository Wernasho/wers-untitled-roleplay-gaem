from entity import Enemy

default = Enemy(hp=8, lvl=1, atk=2)
default.attacks = {
  "stab": {
    "damage": 2, 
    "no_def": False,
    "effects": None
  }, 
  "tackle": {"damage": 6, "no_def": True, "effects": None}
} # 'no_def' pierces defense.

tank = Enemy(hp=64, lvl=5, atk=4, Def=2)
tank.attacks = {
  "stomp":
  {
    "damage": 8, 
    "no_def": True, 
    "effects": {
      "stunned": {
        "duration": 1, 
        "lvl": 1,
        "onself": False
        }, 
  "bleeding":{
    "duration": 4, "lvl": 1} 
    }
  },
  "jab": {
    "damage": 5,
      "no_def": False, 
      "effects": {
      "bleeding": {
        "duration": 2,
        "lvl": 2,
        "onself": False
      }
    }
  }
}

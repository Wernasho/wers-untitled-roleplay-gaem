from entity import Enemy

da_boss = Enemy(hp=123456789, lvl=10**10, atk=32, Def=8) # peak variable name, I know :>
da_boss.name = "God"
da_boss.attacks = {
  "Dissassembly":{
    "damage": 20,
    "no_def": False,
    "effects": {
      "stunned": {"duration": 2, "lvl": 1}
    }
  },
  "Fortification": {
    "damage": 0,
    "no_def": False,
    "effects": {
      "instant Heal": {
        "duration": 1, "lvl": 5, "onself": True 
      }
    }
  },
  "Punch": {
    "damage": 18,
    "no_def": True,
    "effects": {
      "stunned": { "duration": 2, "lvl":1, "onself": False }
    }
  },
  "Self-Help": {
    "damage": 0,
    "no_def": False,
    "effects": {
      "stunned": {"duration": 3, "lvl":1, "onself": True}, # Indeed, mf stuns himself. Just watch, trust.
      "regen": {"duration": 5, "lvl": 10, "onself": True}
    }
  }, 
  "Polarization": {
    "damage": 0,
    "no_def": True, 
    "effects": {
      "frozen": {"duration": 2, "lvl": 3, "onself": False}
    }
  },
  "aPpel": {
      "damage": 0,
      "no_def": False,
      "effects": None
  }
}
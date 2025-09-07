from entity import Enemy

da_boss = Enemy(hp=123456789, lvl=10**10, atk=32, Def=8) # peak variable name, I know :>
da_boss.name = "God"
da_boss.attacks = {
  "Dissassembly":{
    "id": "dis",
    "damage": 20,
    "no_def": False,
    "effects": {
      "stunned": {"duration": 2, "lvl": 1}
    }
  },
  "Fortification": {
    "id": "fort",
    "damage": 0,
    "no_def": False,
    "effects": {
      "instant Heal": {
        "duration": 1, "lvl": 5, "onself": True 
      }
    }
  },
  "Punch": {
    "id": "punch",
    "damage": 18,
    "no_def": True,
    "effects": {
      "stunned": { "duration": 2, "lvl":1, "onself": False }
    }
  },
  "Self-Help": {
    "id": "self",
    "damage": 0,
    "no_def": False,
    "effects": {
      "stunned": {"duration": 3, "lvl":1, "onself": True}, # Indeed, mf stuns himself. Just watch, trust.
      "regen": {"duration": 5, "lvl": 10, "onself": True}
    }
  }, 
  "Polarization": {
    "id": "polar",
    "damage": 0,
    "no_def": True, 
    "effects": {
      "frozen": {"duration": 2, "lvl": 3, "onself": False}
    }
  }
}
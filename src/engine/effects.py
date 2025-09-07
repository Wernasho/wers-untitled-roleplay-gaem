import json

class Effect:
  def __init__(self, name , duration, description, is_active):
    self.name = name
    self.duration = duration
    self.description = description
    self.is_active = True


class Over_time_dmg(Effect):
  def on_turn_start(self, target):
    with open(f"../data/{self.name}.json") as f:
      data = json.load()
    if self.duration > 0 and self.is_active == True:
      damage = data["damage"]
      target.hp -= damage
      self.duration -= 1
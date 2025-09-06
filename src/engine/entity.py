class Character:
  def __init__(self, name, hp, lvl, atk, Def):
    self.name = name
    self.hp = hp
    self.lvl = 1
    self.atk = atk
    self.Def = Def
    
    def is_alive():
      return hp > 0
    

class Player(Character):
  def __init__(self, name, hp, lvl, atk, Def, mny, max_hp, upp, sta, max_sta, inv, invs):
    super().__init__(self, name, hp, lvl, atk, Def)
    self.xp = 0
    self.mny = 0
    self.max_hp = 16
    self.upp = 0
    self.sta = 6
    self.max_sta = 12
    self.inv = []
    self.invs = 10

    def upgrade(self):
      input("ability to upgrade:")
      if input not in ['hp', 'def', 'atk', 'sta', 'inv']:
        print(f"Error, '{input}' is not a valid statistic. Please retry. ")
      else:
        pass
    
    def lelveup():
      self.xp = 0
      self.level +=1
      self.mny += self.lvl * 10
      self.upp += 10
      print(f"{self.name} lelved up to {self.lvl-1} to {self.level}! {self.name} has gained 10 UpgradePoints!")
    
    def use_skill(skill):
      if self.sta >= skill.cost:
        self.sta -= skill.cost

class Boss(Character):
  def __init__(self, name, hp, lvl, atk, Def):
    super().__init__(name, hp, lvl, atk, Def)
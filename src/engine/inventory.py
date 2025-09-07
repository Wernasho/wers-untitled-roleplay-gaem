from entity import Player

class Inventory:
  def __init__(self ):
    pass

  def add_item(self, item):
    s = Player.invs
    if len(Player.inv) == s:
      print("Yikes! Inventory full, you can't store this. Try upgrading your 'INV' stat for 5 UPP")
      input("Woudl you like to upgrade you inventory capacity? (Y/N): ").upper()
      if input == "Y" and Player.upp >= 5:
        Player.upp -= 5
        s += 2
        print(f"Success! Upgraded inventory from {s-2} to {s}!")
      else:
        print(f"erm... you don't have Enough UPP ({Player.upp} of a needed 5)... Well sucks to suck ig :^")
    else: 
      Player.inv.append(item) 
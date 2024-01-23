import random

choix = ['pierre', 'feuille', 'ciseaux']
bot = random.choice(choix)
player = input("choisir : [pierre], [feuille], [ciseaux] : ")

if player == bot:
  print("bot : " + bot + "  player : " + player) 
  print("égalité")

if player == "pierre":
    if bot == "feuille":
        print("bot : " + bot + "  player : " + player) 
        print("perdu")
    elif bot == "ciseaux":
        print("bot : " + bot + "  player : " + player) 
        print("gagné")
        
if player == "feuille":
    if bot == "ciseaux":
        print("bot : " + bot + "  player : " + player) 
        print("perdu")
    elif bot == "pierre":
        print("bot : " + bot + "  player : " + player) 
        print("gagné")
        
if player == "ciseaux":
    if bot == "pierre":
        print("bot : " + bot + "  player : " + player) 
        print("perdu")
    elif bot == "feuille":
        print("bot : " + bot + "  player : " + player) 
        print("gagné")

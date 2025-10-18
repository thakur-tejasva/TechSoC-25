with open("../your_solution.py") as f:
    exec(f.read())
# Create Pikachu
pikachu = Pokemon("Pikachu", 100, 55, 40, 90, 
                 [("Thunder Shock", 40), ("Quick Attack", 30), ("Agility", 0), ("Thunder", 70)])

# Create Charmander
charmander = Pokemon("Charmander", 90, 52, 43, 65,
                    [("Ember", 35), ("Scratch", 25), ("Growl", 0), ("Flamethrower", 60)])

# Display initial stats
print(pikachu.display_stats())
print(charmander.display_stats())

# Pikachu attacks Charmander with Thunder Shock
pikachu.attack(charmander, 0)
print(charmander.display_stats())

# Check if Charmander fainted
print(f"Charmander fainted: {charmander.is_fainted()}")
with open("../your_solution.py") as f:
    exec(f)
# Create weak Magikarp
magikarp = Pokemon("Magikarp", 30, 10, 55, 80,
                  [("Splash", 0), ("Tackle", 20), ("Flail", 15), ("Bounce", 25)])

# Create strong Gyarados
gyarados = Pokemon("Gyarados", 150, 85, 79, 81,
                  [("Hydro Pump", 80), ("Bite", 45), ("Dragon Rage", 50), ("Hyper Beam", 90)])

print(magikarp.display_stats())
print(gyarados.display_stats())

# Gyarados attacks with Hydro Pump
gyarados.attack(magikarp, 0)
print(magikarp.display_stats())
print(f"Magikarp fainted: {magikarp.is_fainted()}")
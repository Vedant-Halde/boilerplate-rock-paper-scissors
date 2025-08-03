from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

print("Testing against all 4 bots:\n")

print("Quincy:")
play(player, quincy, 1000)

print("\nAbbey:")
play(player, abbey, 1000)

print("\nKris:")
play(player, kris, 1000)

print("\nMrugesh:")
play(player, mrugesh, 1000)

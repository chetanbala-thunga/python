players = []

for profile in range(2):
     players.append({
	"name": ""
	"score": 0,
	"backpack": []
     )}


     players[]["name"] = raw_input("Enter name for player" + str(profile + 1) + ": ")
     print("Enter four (4) items to put into your backpack. ")
     for item in range(4):
	backpack_item = raw_input("Item name: ")
	players[profile]["backpack"].append(backpack_item)
     print(players[profile]["backpack"])

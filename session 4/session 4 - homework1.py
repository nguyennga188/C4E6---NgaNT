inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
    }
##print ( inventory )

##for key in inventory:
##    print ( key, ":", inventory [key])

inventory ["pocket"] = ["seashell", "strange berry", "lint"]

inventory ["backpack"].sort()
inventory ["backpack"].remove("dagger")
inventory ["gold"] = inventory["gold"] + 50
for key in inventory:
    print(key, ":", inventory[key])
    
    


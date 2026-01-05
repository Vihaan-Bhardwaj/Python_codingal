t = {"SGW 2" : "Solo sniper game", "Hello" : "Bonjour", "Halo": "Fps shooter", "Forza Horizon 5" : "Racing game"}
print(t["SGW 2"])
print("Halo" in t)
print(t.get("Fortnite", "Sorry, this key could not be accessed. Try adding it to the dictionary or restarting hubub."))
print(t.items())
print(t.keys())
print(t.values())
for key in t.keys():
    print(key)
for values in t.values():
    print(values)
for key,value in t.items():
    print(key,"--->", value)    
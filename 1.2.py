neved = []

while len(neved) < 3:
    nev = input("Add meg a neved! ")
    if nev == "":
        break
    neved.append(nev)


    
print("elérted a maximum nevek számát(3). a neved:" , neved)

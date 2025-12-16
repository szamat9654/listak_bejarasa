nev = []

while True:
    nev = input("Add meg a neved! ")
    if nev == "":
        break
    nev.append(nev)
    
print(nev)

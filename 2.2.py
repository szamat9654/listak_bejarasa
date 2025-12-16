szavak = []

while True:
    szo = input("Irj be szavakat, amik 'a', vagy 'A' betüvel kezdődnek! ")
    if szo == "":
        break

    if szo [0] == "a" or szo [0] == "A":
        szavak.append(szo)
    
print(szavak)

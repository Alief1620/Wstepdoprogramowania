Wiek = int(input("Podaj Wiek: "))
Cena = 0
if Wiek < 4:
    #print ("0zł")
    Cena = 0
elif Wiek >=4 and Wiek <= 10:
    Cena = 10
else:
    Cena = 20

print(f"Cena Biletu: {Cena}zł")
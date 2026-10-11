import json

class Produkt:
    def __init__(self, nazwa, cena, kategoria, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.kategoria = kategoria
        self.ilosc = ilosc

magazyn = [
    Produkt("mleko", 4.50, "spozywczy", 20),
    Produkt("sól", 1.50, "przyprawa", 20),
    Produkt("kawa", 8.50, "spozywczy", 20),
    Produkt("herbata", 2.50, "spozywczy", 0)
]

dane_do_zapisu = [p.__dict__ for p in magazyn]

with open("magazyn.json", "w", encoding="utf-8") as f:
    json.dump(dane_do_zapisu, f, ensure_ascii=False, indent=4)

with open("magazyn.json", "r", encoding="utf-8") as f:
    dane_do_otwarcia = json.load(f)

print("Wybierz co chcesz zrobic")
print("1. Wyswietl liste produktow")
print("2. Wyswietl dostepne produkty")
print("3. Wyszukaj produkt")
print("4. Wyszukaj produkt do ceny")
print("5. Kup produkt")
print("0. Zakoncz program")

while True:
    co_chcesz_zrobic = int(input("Co chcesz zrobic: "))
    match co_chcesz_zrobic:
        case 1:
            for produkt in dane_do_otwarcia:            
                print(f"Produkt: {produkt["nazwa"]}, cena: {produkt["cena"]}zł")
        case 2:
            for produkt in dane_do_otwarcia:
                if produkt["ilosc"] == 0:
                    print(f"Produkt: {produkt["nazwa"]}, niedostepny")
                else:
                    print(f"Produkt: {produkt["nazwa"]}, cena: {produkt["cena"]}zł")
        case 3:
            wyszukaj = str(input("Wyszukaj produkt: ")).lower()
            for produkt in dane_do_otwarcia:
                if wyszukaj == produkt["nazwa"].lower():
                    print(f"Wyszukany produkt: {produkt["nazwa"]}, {produkt["cena"]}zł")
                else:
                    print(f"Nie znaleziono produktu")
        case 4:
            try:
                wyszukaj_cene = float(input("Wyszukaj produkty po cenie: "))
                for produkt in dane_do_otwarcia:
                    if wyszukaj_cene >= produkt["cena"]:
                        print(f"Wyszukany produkt: {produkt["nazwa"]}, {produkt["cena"]}zł")
                    else:
                        continue
            except ValueError:
                print("Nie podales liczby")
        case 5:
            zakup = str(input("Zakup produkt: "))
            produkt_znaleziony = False
            for produkt in dane_do_otwarcia:
                if zakup == produkt["nazwa"]:
                    produkt_znaleziony = True
                    if produkt['ilosc'] > 0:
                        produkt['ilosc'] -= 1
                        print(f"Zakupiono {produkt["nazwa"]}, pozostalo {produkt["ilosc"]} sztuk")
                        with open("magazyn.json", "w", encoding="utf-8") as f:
                            json.dump(dane_do_otwarcia, f, ensure_ascii=False, indent=4)
                    else:
                        print("Produkt niedostepny")
                    break
            if not produkt_znaleziony:
                print("Nie znaleziono produktu")
                    
        case 0:
            print("Koniec programu")
            break
        case _:
            print("Nie ma takiego wyboru")
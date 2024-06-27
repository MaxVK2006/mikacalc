import pyfiglet

# Functie om een ASCII-banner te printen
def print_ascii_banner(text):
    ascii_banner = pyfiglet.figlet_format(text)
    print(ascii_banner)

# Functie voor optellen
def optellen(x, y):
    return x + y

# Functie voor aftrekken
def aftrekken(x, y):
    return x - y

# Functie voor vermenigvuldigen
def vermenigvuldigen(x, y):
    return x * y

# Functie voor delen
def delen(x, y):
    if y == 0:
        return "Fout: Delen door nul"
    return x / y

# Hoofdfunctie van de rekenmachine
def rekenmachine():
    print_ascii_banner("MikaCalc")
    
    print("Kies een bewerking:")
    print("1. Optellen")
    print("2. Aftrekken")
    print("3. Vermenigvuldigen")
    print("4. Delen")

    while True:
        keuze = input("Voer je keuze in (1/2/3/4): ")

        if keuze in ['1', '2', '3', '4']:
            try:
                getal1 = float(input("Voer het eerste getal in: "))
                getal2 = float(input("Voer het tweede getal in: "))
            except ValueError:
                print("Ongeldige invoer. Voer numerieke waarden in.")
                continue

            if keuze == '1':
                print(f"{getal1} + {getal2} = {optellen(getal1, getal2)}")
            elif keuze == '2':
                print(f"{getal1} - {getal2} = {aftrekken(getal1, getal2)}")
            elif keuze == '3':
                print(f"{getal1} * {getal2} = {vermenigvuldigen(getal1, getal2)}")
            elif keuze == '4':
                resultaat = delen(getal1, getal2)
                print(f"{getal1} / {getal2} = {resultaat}")
            
            volgende_berekening = input("Wil je een nieuwe berekening uitvoeren? (ja/nee): ")
            if volgende_berekening.lower() != 'ja':
                break
        else:
            print("Ongeldige invoer")

if __name__ == "__main__":
    rekenmachine()

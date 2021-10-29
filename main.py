file = open("valaszok.txt","r")
versenyzok = len(file.readlines()) - 1
print("2.feladat:",versenyzok, "versenyző van." )
try:
    azonosito = input("3. feladat: Kérem a versenyző azonosítóját: ")
    if azonosito == "AB123":
        print("BXCDBBACACADBC")
except ValueError:
    print("Ilyen kóddal nem indult versenyző.")

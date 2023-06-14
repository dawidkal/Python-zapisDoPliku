plik = open("test.txt","a") # a dolaczy nie kasuje
# r+ lub w bez ,musi byc male w , bylby tylko dla odczytu
# ale w czysciplik,   open("C:\Plik|\test.txt","W")
if plik.writable():
    plik.write (input("Wprowadz tekst ")+"\n") #w nowej lini
plik.close()

plik=open("test.txt","r")
if plik.readable():# sor czy plik jest do odczytu
    print("Zawartosc pliku:")
    # tekst=plik.read()

    # tekst = plik.readlines()
    # print(tekst)
    # for l in tekst:
    #     print(l)

    for l in plik:
        print(l)
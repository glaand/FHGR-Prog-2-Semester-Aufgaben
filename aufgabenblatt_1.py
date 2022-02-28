def aufgabe1():
    print("---- Aufgabe 1 ----")
    print("Projektgruppe: Raphael Brunold, Benito Rusconi, André Glatzl, Mathias Fröhner")
    print("Projektleiter: Raphael Brunold")
    print("")

def aufgabe2():
    print("---- Aufgabe 2 ----")
    print("a) Der Datensatz beinhaltet Eye Tracking Aufzeichnungen als CSV-Datei und die entsprechende Stimuli-Metrokarten.")
    print("Für den Startpunkt wird ein Fingerzeiger verwendet, und für den Endpunkt wird eine rote Zielscheibe.")
    print("")
    print("b) Der Datensatz hat folgende Metadaten:")
    print(" - Die CSV-Datei beinhaltet 118'126 Zeile.")
    print(" - Insgesamt gibt es 48 Stimulibilder (2 pro Stadt)")
    print(" - Es gibt im Total 3670 Fixationspunkte somit 3659 Scanpfade bzw. (n - 1).")
    print(" - Es ist auch noch die Komplexität pro Metrokarte angegeben.")
    print(" - Insgesamt nehmen 40 Teilnehmende an der Studie teil.")
    print(" - Der komplette Datensatz (CSV + Stimulibilder) ist 75 MB gross.")
    print("")
    print("c) Anbei die drei ausgewählten Forschungsfragen:")
    print("Forschungsfrage 1: Die Versuchspersonen finden sich in farbigen Metro-Karten schneller und vor allem besser zurecht als in graustufigen Metro-Karten. Dank der farblichen Gestaltung ist eine bessere Unterscheidbarkeit der Verkehrslinien möglich.")
    print("Forschungsfrage 4: Mit zunehmender Komplexität steigt auch die Bearbeitungsdauer.")
    print("Forschungsfrage 6: Bei steigender Komplexität der Metro-Karten werden die Sakkaden kürzer und die Fixationen länger.")
    print("")

def aufgabe3(debug=True):
    if debug: print("---- Aufgabe 3 ----")

    def factorial(n):
        if n <= 1: return 1
        return n * factorial(n - 1)

    if debug: 
        print("Fakultät: " + str(factorial(5)))
        print("")
    return factorial

def aufgabe4(debug=True):
    if debug: print("---- Aufgabe 4 ----")

    def binomial_coefficient_factorial(n,k):
        if k > n:
            raise Exception("Error: k muss kleiner/gleich n sein.")
        factorial = aufgabe3(False)
        return factorial(n) / (factorial(n - k) * factorial(k))

    def binomial_coefficient_multiplicative(n,k,i=1):
        if i > k: return 1
        summanden = ((n + 1) - i) / i
        return binomial_coefficient_multiplicative(n,k,i+1) * summanden
    
    n = 70; k = 65;
    res = round(binomial_coefficient_factorial(n,k))
    if debug: print(f"Binomial coefficient (factorial, n = {n}; k = {k}): {res}")

    res = round(binomial_coefficient_multiplicative(n,k))
    if debug: print(f"Binomial coefficient (multiplicative, n = {n}; k = {k}): {res}")

    if debug: print("")

def aufgabe5(debug=True):
    if debug: print("---- Aufgabe 5 ----")
    def ackermann(x,y):
        if debug: print(f"Ackermann: x = {x}; y = {y}")
        if x == 0:
            return y + 1
        elif y == 0:
            return ackermann(x - 1, 1)
        else:
            return ackermann(x - 1, ackermann(x, y - 1))
    ackermann(1, 1)
    if debug: print("")

if __name__ == "__main__":
    aufgabe1()
    aufgabe2()
    aufgabe3()
    aufgabe4()
    aufgabe5()
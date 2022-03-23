def factorial_helper(cumulator, current):
    if current == 0:
        return cumulator
    return factorial_helper(cumulator * current, current - 1)

def factorial(n):
    return factorial_helper(1, n)

def aufgabe6():
    print("----- Aufgabe 6 ------")
    print("(a) Fakultätsfunktion")

    print(f"Wert für n = 5: {factorial(5)}")

    print("")
    print("(b) Fibonacci-Folge")
    def fibonacci_helper(current, penultimate, ultimate):
        if current <= 1:
            return penultimate + ultimate
        return fibonacci_helper(current-1, ultimate, ultimate+penultimate) 

    def fibonacci(n):
        return fibonacci_helper(n-1, 0, 1)

    print(f"Wert für n = 10: {fibonacci(10)}")

    print("")
    print("(c) Summe der ersten n geraden natürlichen Zahlen")
    def sum_even_helper(cumulator, current, count):
        if count == 0:
            return cumulator
        current += 2
        cumulator += current
        count -= 1
        return sum_even_helper(cumulator, current, count)

    def sum_even(n):
        return sum_even_helper(0, 0, n)

    print(f"Wert für n = 10: {sum_even(10)}")
    print("")

def aufgabe7():
    print("----- Aufgabe 7 ------")
    print("(a)")
    a = lambda x: 4*x
    print(f"Wert für 4: {a(4)}")
    print("")

    print("(b)")
    b = lambda x: (x*x)**(1/3)
    print(f"Wert für 5: {b(5)}")
    print("")
    
    print("(c)")
    c = lambda x: sum(x)
    print(f"Wert für [1,2,3,4,5]: {c([1,2,3,4,5])}")
    print("")
    

def aufgabe8():
    print("----- Aufgabe 8 ------")
    def calculate(n, func):
        sumNumber = 0
        for i in range(n):
            sumNumber += func(i+1)
        return sumNumber

    print("(a) Vielfache von 2")
    print(f"Wert für 10: {calculate(10, lambda x: x*2)}")
    print("")

    print("(b) Quadratfunktion")
    print(f"Wert für 6: {calculate(6, lambda x: x*x)}")
    print("")

    print("(c) Fakultätsfunktion")
    print(f"Wert für 4: {calculate(4, factorial)}")
    print("")

def aufgabe9():
    print("----- Aufgabe 9 ------")
    fac = lambda x: 1 if x <= 1 else x*fac(x-1)
    print(f"Wert für 5: {fac(5)}")
    print("")

def aufgabe10():
    print("----- Aufgabe 10 ------")
    mix = [1,2,3,'4', 5.0, 6.3, True, False]

    def listOp(argList, op):
        return op(argList)

    opSort = lambda x: sorted(x, key=lambda y: float(y))
    opInvert = lambda x: x[::-1]
    opConcat = lambda x: ''.join(list(map(lambda y: str(y), x)))
    allInOneOp = lambda x: opConcat(opInvert(opSort(x)))

    print(f"Originalliste: {mix}")
    print(f"Liste sortieren: {listOp(mix, opSort)}")
    print(f"Liste umkehren: {listOp(mix, opInvert)}")
    print(f"Liste konkatenieren: {listOp(mix, opConcat)}")
    print(f"All-in-One Funktion: {listOp(mix, allInOneOp)}")


if __name__ == "__main__":
    aufgabe6()
    aufgabe7()
    aufgabe8()
    aufgabe9()
    aufgabe10()
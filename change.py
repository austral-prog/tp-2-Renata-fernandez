def change():
    expense = 23.75
    money = 100
    vuelto=money-expense
    pesos=int(vuelto)
    cent=int((vuelto-pesos)*100)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print()
    print(f"\nVuelto")
    print()
    print(f"\nPesos:")
    print(pesos)
    print("Centavos:")
    print(cent)

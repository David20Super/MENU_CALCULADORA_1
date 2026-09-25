
while True:
    


    opcion = int(input("ingrese una opción en la consola: "))
    bandera_primer_numero = False
    bandera_segundo_numero = False

    if opcion == 1:
        numero_uno = int(input("Ingrese el primer numero: "))
    elif opcion == 2:
        numero_dos = int(input("Ingrese el segundo numero: "))
    elif opcion >= 3 and opcion <= 9 and (bandera_primer_numero == False or bandera_segundo_numero == False):
        print("DEBE INGRESAR AL MENOS UN NUMERO ENTERO PARA PODER CONTINUAR")
    elif opcion == 3:
        resultado_suma = None
        print(f"")
    elif opcion == 4:
        resultado_resta = None
        print(f"")
    elif opcion == 5:
        resultado_division = None
        print(f"")
    elif opcion == 6:
        resultado_multiplicacion = None
        print(f"")
    elif opcion == 7:
        resultado_potencia = None
        print(f"")
    elif opcion == 8:
        resultado_factorial = None
        print(f"")
    elif opcion == 9:
        resultado_suma = None
        resultado_resta = None
        resultado_division = None
    elif opcion == 10:
        print("CERRANDO....")
        break
    
        
def mostrar_menu()-> None:
    print("1-ingreso 1 | 2-ingreso 2")
    print("3-suma      | 4-resta")
    print("5-división  | 6-multiplicación")
    print("7-potencia  | 8-factorial")
    print("9-todos     | 10-salir")
    
def informar_resultado(numero_uno,numero_dos,resultado:int | float | str, operador:str)->None:
    print(f"{numero_uno}{operador}{numero_dos} = {resultado}")
    
def interactuar_menu(lista_datos:list)->bool:
    print("EN DESAROLLO CUANDO VEAMOS LISTAS")
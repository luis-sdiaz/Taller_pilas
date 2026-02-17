class Caja:
    def __init__(self, codigo, peso):
        self.codigo = codigo
        self.peso = peso

    def __str__(self):
        return f"Caja {self.codigo} - {self.peso} kg"


class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        if self.esta_vacia():
            print("El almacén está vacío.")
        else:
            print("Cajas en el almacén:")
            for caja in reversed(self.elementos):
                print(f" - {caja}")


class Almacen:
    def __init__(self):
        self.pila_cajas = Pila()

    def ingresar_caja(self, caja):
        print(f"Ingresando {caja}")
        self.pila_cajas.apilar(caja)

    def retirar_caja(self):
        caja = self.pila_cajas.desapilar()
        if caja:
            print(f"Retirando {caja}")
        else:
            print("No hay cajas en el almacén.")
        return caja

    def mostrar_estado(self):
        self.pila_cajas.mostrar()


if __name__ == "__main__":
    almacen = Almacen()

    while True:
        print("\n--- Menu ---")
        print("1. Ingresar caja")
        print("2. Retirar caja")
        print("3. Mostrar estado del almacen")
        print("4. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            codigo = input("Codigo de la caja: ")
            peso = input("Peso de la caja (kg): ")
            if codigo and peso.isdigit():
                almacen.ingresar_caja(Caja(codigo, int(peso)))
            else:
                print("Datos inválidos.")
        elif opcion == "2":
            almacen.retirar_caja()
        elif opcion == "3":
            almacen.mostrar_estado()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
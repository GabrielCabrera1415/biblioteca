from os import system

class Libro:

    def __init__(self,titulo:str, autor:str,año:int,disponible:bool):
        self.titulo = titulo
        self.autor = autor 
        self.año = año
        self.disponible = disponible #atributos que nosotros le damos al objeto

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"'{self.titulo}' - {self.autor} ({self.año}) - {estado}"

class LibroFisico(Libro):
    def __init__(self, titulo, autor, año, disponible, ubicacion_estante):
        super().__init__(titulo, autor, año, disponible)  # Llamamos al constructor de la clase padre y recuerda que tienes que poner los atributos de la clase padre
        self.ubicacion_estante = ubicacion_estante

class LibroDigital(Libro):
    def __init__(self, titulo, autor, año, disponible, formato):
        super().__init__(titulo, autor, año, disponible)
        self.formato = formato

class Biblioteca:

    def __init__(self):
        self.libros = [] #atibuto que trabaja internamente con la clase y los objetos, por eso no necesitamos pasarle un valor

    def agregar_libro(self): 
        titulo = input("Titulo: ")
        autor = input("Autor: ") 
        año = int(input("Año: "))
        estado = input("¿Está disponible? (s/n): ").lower()
        if estado == "s":
            disponible = True
        else:
            disponible = False

        fisico = input("¿El libro que quieres agregar es físico? (s/n): ").lower()
        if fisico == "s":
            estante = input("¿En qué estante estará guardado el libro? ")
            libro = LibroFisico(titulo,autor,año,disponible,estante) #Creamos el objeto con sus atributos
            self.libros.append(libro)
            system("cls")  

        else:
           formato = input("¿En qué estante estará guardado el libro? ")
           libro = LibroDigital(titulo,autor,año,True,formato)
           self.libros.append(libro)
           system("cls")  

    def mostrar_libros(self):
        if self.libros != []:                
            for libro in self.libros:
                #print(f"Libro: {libro.titulo}, autor: {libro.autor}, año de publicación {libro.año}, Disponible: {}")
                print(libro)
        else:
            print("No hay libros existentes")
        input()
        system("cls")  

    def buscar_libro(self):
        buscar = input("¿Qué libro desea buscar? \n")
        for libro in self.libros:
            if libro.titulo == buscar:
                print(f"El libro buscado {libro.titulo} es del autor: {libro.autor} con año de publicación {libro.año}\n")
                break
        input()
        system("cls")  


    def prestar_libro(self):
        buscar = input("¿Qué libro desea prestar? \n")
        for libro in self.libros:
            if libro.titulo == buscar and libro.disponible == True:
                print("Libro prestado\n")
                libro.disponible = False
                break
        input()
        system("cls")  



    def devolver_libro(self):
        buscar = input("¿Qué libro desea devolver? \n")
        for libro in self.libros:
            if libro.titulo == buscar and libro.disponible == False:
                print("Libro devuelto\n")
                libro.disponible = True
                break
        input()
        system("cls")  



    def mostrar_disponibles(self):
        print("Libros disponibles: \n")
        for libro in self.libros:
            if libro.disponible == True:
                print(f"Titulo: {libro.titulo}\n")
        input()
        system("cls")  


    def salir(self):
        exit()


def main():
    MiBiblioteca = Biblioteca()

    while True:
        print("=== Menú ===")
        print("1. Agregar libro")
        print("2. Mostrar todos")
        print("3. Buscar por titulo")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Ver disponibles")
        print("7. Salir\n")
        opcion = input("Selecciona una opción: ")
        print("\n")

        match opcion:
            
            case "1":
                system("cls")     
                MiBiblioteca.agregar_libro()
            case "2":
                system("cls")
                MiBiblioteca.mostrar_libros()
            case "3":
                system("cls")
                MiBiblioteca.buscar_libro()
            case "4":
                system("cls")
                MiBiblioteca.prestar_libro()
            case "5":
                system("cls")
                MiBiblioteca.devolver_libro()
            case "6":
                system("cls")
                MiBiblioteca.mostrar_disponibles()
            case "7":
                MiBiblioteca.salir()
                system("cls")
            case _:
                system("cls")
                print("Opción no válida.\n")




if __name__ == "__main__":
    main()


    
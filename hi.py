class Estudiante:
    """
    Clase para representar la información de un estudiante.
    El método __repr__ es para mostrar una representación legible del objeto.
    """
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = int(edad)
        self.nota = float(nota)

    def __repr__(self):
        return f"Estudiante(Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota})"


class GestorEstudiantes:
    """
    Clase que gestiona una lista de estudiantes y realiza operaciones sobre ellos.
    """
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        """Añade un objeto Estudiante a la lista."""
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        """Imprime la lista de todos los estudiantes."""
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return
        print("\n--- Lista de Estudiantes ---")
        for estudiante in self.estudiantes:
            print(estudiante)

    def calcular_estadisticas(self):
        """Calcula y muestra el promedio, la mejor y la peor nota."""
        if not self.estudiantes:
            print("No se pueden calcular estadísticas sin estudiantes.")
            return
        
        # Extrae todas las notas en una lista
        notas = [est.nota for est in self.estudiantes]
        
        promedio = sum(notas) / len(notas)
        mejor_nota = max(notas)
        peor_nota = min(notas)
        
        print("\n--- Estadísticas de Notas ---")
        print(f"Promedio de notas: {promedio:.2f}")
        print(f"Mejor nota: {mejor_nota}")
        print(f"Peor nota: {peor_nota}")

    def ordenar_por_nota(self):
        """Ordena la lista de estudiantes por nota (de menor a mayor) usando una función lambda."""
        # La función lambda le dice a sorted() que use el atributo 'nota' de cada objeto para ordenar.
        self.estudiantes.sort(key=lambda estudiante: estudiante.nota)
        print("\nEstudiantes ordenados por nota ascendente.")


# --- Programa Principal ---

# 1. Crear una instancia del gestor
gestor = GestorEstudiantes()

# 2. Pedir y crear los estudiantes
try:
    num_estudiantes = int(input("Ingresa el número de estudiantes a registrar: "))

    for i in range(num_estudiantes):
        print(f"\n--- Ingresando datos del estudiante {i+1} ---")
        str_user = input("Ingresa nombre, edad y nota (separado por comas): ")
        
        # Dividir la entrada y desempaquetar directamente en variables
        try:
            nombre, edad, nota = str_user.split(',')
            # Crear el objeto estudiante y agregarlo al gestor
            estudiante_nuevo = Estudiante(nombre.strip(), edad.strip(), nota.strip())
            gestor.agregar_estudiante(estudiante_nuevo)
            print(f"¡Estudiante '{nombre}' agregado con éxito!")
        except ValueError:
            print("Error: Asegúrate de ingresar los tres valores separados por comas. Intenta de nuevo.")
            # Podrías agregar lógica para reintentar la entrada del estudiante actual
            continue

except ValueError:
    print("Error: Debes ingresar un número válido.")


# 3. Usar los métodos del gestor para cumplir los requisitos

# Mostrar la lista original
gestor.mostrar_estudiantes()

# Calcular y mostrar estadísticas
gestor.calcular_estadisticas()

# Ordenar la lista por nota
gestor.ordenar_por_nota()

# Mostrar la lista ordenada
gestor.mostrar_estudiantes()
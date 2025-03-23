class Tarea:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = "Pendiente"  # Puede ser "Pendiente" o "Completada"

    def marcar_completada(self):
        self.estado = "Completada"

    def __str__(self):
        return f"ID: {self.id} | {self.nombre}: {self.descripcion} | Estado: {self.estado}"
    
class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.contador_id = 1  # Para generar IDs autoincremental

    def agregar_tarea(self, nombre, descripcion):
        nueva_tarea = Tarea(self.contador_id, nombre, descripcion)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{nombre}' agregada con ID {self.contador_id}")
        self.contador_id += 1

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return
            
        print("\n--- LISTA DE TAREAS ---")
        for tarea in self.tareas:
            print(tarea)

    def listar_por_estado(self, estado):
        tareas_filtradas = [tarea for tarea in self.tareas if tarea.estado == estado]
        
        if not tareas_filtradas:
            print(f"No hay tareas en estado: {estado}")
            return
            
        print(f"\n--- TAREAS EN ESTADO: {estado} ---")
        for tarea in tareas_filtradas:
            print(tarea)

    def marcar_tarea_completada(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                tarea.marcar_completada()
                print(f"Tarea {id_tarea} marcada como completada.")
                return
        print(f"No se encontró una tarea con ID {id_tarea}")

    def eliminar_tarea(self, id_tarea):
        for i, tarea in enumerate(self.tareas):
            if tarea.id == id_tarea:
                tarea_eliminada = self.tareas.pop(i)
                print(f"Tarea '{tarea_eliminada.nombre}' con ID {id_tarea} eliminada.")
                return
        print(f"No se encontró una tarea con ID {id_tarea}")

def main():
    gestor = GestorTareas()
    
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE TAREAS ===")
        print("1. Agregar tarea")
        print("2. Listar todas las tareas")
        print("3. Listar tareas pendientes")
        print("4. Listar tareas completadas")
        print("5. Marcar tarea como completada")
        print("6. Eliminar tarea")
        print("7. Salir")

        opcion = input("\nSelecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            gestor.agregar_tarea(nombre, descripcion)
            
        elif opcion == '2':
            gestor.listar_tareas()
            
        elif opcion == '3':
            gestor.listar_por_estado("Pendiente")
            
        elif opcion == '4':
            gestor.listar_por_estado("Completada")
            
        elif opcion == '5':
            try:
                id_tarea = int(input("ID de la tarea a marcar como completada: "))
                gestor.marcar_tarea_completada(id_tarea)
            except ValueError:
                print("Error: Debes ingresar un número válido.")
                
        elif opcion == '6':
            try:
                id_tarea = int(input("ID de la tarea a eliminar: "))
                gestor.eliminar_tarea(id_tarea)
            except ValueError:
                print("Error: Debes ingresar un número válido.")
                
        elif opcion == '7':
            break
            
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            
    print("¡Gracias por usar el sistema de gestión de tareas!")

if __name__ == "__main__":
    main()

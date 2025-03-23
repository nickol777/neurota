# Lista para almacenar las tareas
List_tareas = []

def rellenar():
    # Crear un nuevo diccionario por cada tarea
    diccionario = {}
    
    diccionario["ID"] = int(input("Ingrese el ID de la tarea: "))
    diccionario["Nombre"] = input("Ingrese el nombre de la tarea: ")
    
    while True:
        estado = int(input("Ingrese el estado de la tarea (1=Pendiente, 2=Completado): "))
        if estado in [1, 2]:  # Validación correcta
            break
        print("Entrada inválida. Por favor, ingrese 1 o 2.")
    
    diccionario["Estado"] = "Pendiente" if estado == 1 else "Completado"
    
    return diccionario  # Retornar la tarea creada

# Bucle para agregar tareas
while True:
    respuesta = input("¿Quieres crear o agregar una tarea? (Si/No): ").strip().lower()
    if respuesta == 's':
        List_tareas.append(rellenar())
    else:
        break

print("\nLista de todas las tareas:")
print(List_tareas)

# Separar las tareas en pendientes y completadas
list_pendientes = []
list_completadas = []

for tarea in List_tareas:
    if tarea["Estado"] == "Pendiente":
        list_pendientes.append(tarea)
    else:
        list_completadas.append(tarea)

# Mostrar las listas separadas
print("\Tareas Pendientes:")
print(list_pendientes)

print("\nTareas Completadas:")
print(list_completadas)

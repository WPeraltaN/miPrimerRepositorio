'''
    Imagina que estás desarrollando un sistema sencillo para gestionar pacientes en un hospital. Dada una lista de diccionarios, donde cada diccionario representa un paciente con su nombre, edad y diagnóstico (Ej: {'Nombre': 'Juan', 'Edad': 20, 'Diagnóstico': 'Gripe'}), realiza lo siguiente:

        1- Recorre la lista y cuenta cuántos pacientes tienen la edad mayor a 40 años.
        2- Crea un diccionario que contenga el número de pacientes por diagnóstico. Por ejemplo, si hay tres pacientes con "gripe y dos con "fractura", el diccionario debería verse así: {"gripe}: 3, "fractura": 2}.
        3- Imprime el conteo de pacientes mayores a 40 años y el diccionario de diagnóstico al final.
'''

listaPaciente = {
    '001': {'Nombre': 'Juan', 'Edad': 60, 'Diagnóstico': 'Calculos renales'},
    '002': {'Nombre': 'Hansel', 'Edad': 42, 'Diagnóstico': 'Calculos renales'},
    '003': {'Nombre': 'Jorhansi', 'Edad': 57, 'Diagnóstico': 'Calculos renales'},
    '004': {'Nombre': 'Jordan', 'Edad': 34, 'Diagnóstico': 'Diabetes'},
    '005': {'Nombre': 'Gorge', 'Edad': 39, 'Diagnóstico': 'Diabetes'}
}

# 1- Recorre la lista y cuenta cuántos pacientes tienen la edad mayor a 40 años.
contadormayores = 0
contadormenores = 0
for id, paciente in listaPaciente.items():
    if paciente['Edad'] > 40:
        contadormayores += 1
    else:
        contadormenores += 1

print(f"Hay {contadormayores} pacientes mayores de 40 años, y {contadormenores} menores de 40 años")



# 2- Crea un diccionario que contenga el número de pacientes por diagnóstico. Por ejemplo, si hay tres pacientes con "gripe y dos con "fractura", el diccionario debería verse así: {"gripe}: 3, "fractura": 2}.
diagnósticos = {}
contador = 1

for id, paciente in listaPaciente.items():
    diagnósticos[paciente['Diagnóstico']] = contador

print(diagnósticos)
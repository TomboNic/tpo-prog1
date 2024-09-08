"""
-----------------------------------------------------------------------------------------------
Título: Gestor de Turnos Medicos V1.0

Fecha: 22/08/2024

Autores: Nicolas Tombolan, Nicolas Bermudez, Valentina Segovia, Mariano Sanabria.

Descripción:

Implementar un sistema que gestione la reserva de turnos medicos para los profe-
sionales de las distintas especialidades que atiende un centro de salud, utilizando
matrices, listas y diccionarios para mantener la información, almacenándola en ar-
chivos para permitir su posterior recuperacion. Aplicar GIT para control de versiones
y recursividad para realizar las busquedas.
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------

import os
import csv

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def reservarTurno():
    imprimirMenuEspecialidades()
    especialidad_idx = int(input("Seleccione una especialidad (número): ")) - 1

    if especialidad_idx < 0 or especialidad_idx >= len(especialidades):
        print("Índice de especialidad no válido.")
        return

    imprimirDiasYHorarios(especialidad_idx)
    dia = input("Ingrese el día para la reserva: ").capitalize()
    horario = input("Ingrese el turno para la reserva (ej. 09:00): ")

    if dia not in dias:
        print("Día no válido.")
        return

    dia_idx = dias.index(dia)
    horarios_disponibles = horarios[especialidad_idx]
    horarios_reservados = []

    if especialidad_idx < len(reservas) and dia_idx < len(reservas[especialidad_idx]):
        horarios_reservados = [turno[0] for turno in reservas[especialidad_idx][dia_idx]]

    horarios_actualizados = [h for h in horarios_disponibles if h not in horarios_reservados]

    if horario in horarios_actualizados:
        print("Ingrese los datos del paciente:")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")

        while len(reservas) <= especialidad_idx:
            reservas.append([])
        while len(reservas[especialidad_idx]) <= dia_idx:
            reservas[especialidad_idx].append([])

        reservas[especialidad_idx][dia_idx].append((horario, nombre, telefono, email))
        print("Reserva realizada con éxito.")
    else:
        print("Horario no disponible.")

def imprimirDiasYHorarios(especialidad_idx):
    if especialidad_idx < 0 or especialidad_idx >= len(especialidades):
        print("Índice de especialidad no válido.")
        return

    print(f"\nHorarios Disponibles para {especialidades[especialidad_idx]}")
    print("="*50)

    for dia_idx, dia in enumerate(dias):
        print(f"{dia.ljust(10)} | ", end="")
        if especialidad_idx < len(horarios) and dia_idx < len(horarios[especialidad_idx]):
            horarios_del_dia = horarios[especialidad_idx]
            horarios_reservados = []
            if especialidad_idx < len(reservas) and dia_idx < len(reservas[especialidad_idx]):
                horarios_reservados = [turno[0] for turno in reservas[especialidad_idx][dia_idx]]
            horarios_actualizados = [h for h in horarios_del_dia if h not in horarios_reservados]
            print(", ".join(horarios_actualizados))
        else:
            print("Error: No disponible.")

    print("="*50)



def modificarTurno():
    pass

def cancelarTurno():
    pass

def imprimirTurnos():
    print("="*50)
    print("    Turnos Reservados")
    print("="*50)
    if reservas:
        for especialidad_idx, dias_reservas in enumerate(reservas):
            for dia_idx, turnos in enumerate(dias_reservas):
                for turno in turnos:
                    horario, nombre, telefono, email = turno
                    print(f"{especialidades[especialidad_idx].ljust(12)} | {dias[dia_idx].ljust(8)} | {horario.ljust(5)} | {nombre.ljust(15)} | {telefono.ljust(15)} | {email}")
    else:
        print("No hay turnos reservados.")
    print("="*50)


def imprimirMenu():
    print("="*30)
    print("        MENÚ PRINCIPAL")
    print("="*30)
    print("1. Reservar Turno")
    print("2. Modificar Turno")
    print("3. Cancelar Turno")
    print("4. Ver Turnos")
    print("5. Salir")
    print("="*30)


def imprimirMenuEspecialidades():
    print("="*30)
    print("     MENÚ DE ESPECIALIDADES MÉDICAS")
    print("="*30)
    print("1. Cardiología")
    print("2. Dermatología")
    print("3. Pediatría")
    print("4. Ginecología")
    print("5. Ortopedia")
    print("="*30)
1
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables

especialidades = ["Cardiología", "Dermatología", "Pediatría", "Ginecología", "Ortopedia"]

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

horarios = [
    ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30"],  # Cardiología
    ["10:00", "10:30", "11:00", "11:30", "12:00"],           # Dermatología
    ["08:00", "08:30", "09:00", "09:30", "10:00"],           # Pediatría
    ["09:00", "09:30", "10:00", "10:30", "11:00"],           # Ginecología
    ["11:00", "11:30", "12:00", "12:30", "13:00"]            # Ortopedia
]

disponibilidad = [
    [True, True, True, True, True, True],   # Cardiología
    [True, True, True, True, True],         # Dermatología
    [True, True, True, True, True],         # Pediatría
    [True, True, True, True, True],         # Ginecología
    [True, True, True, True, True]          # Ortopedia
]

reservas = []

#----------------------------------------------------------------------------------------------
# MENU PRINCIPAL
#----------------------------------------------------------------------------------------------

while True:

    imprimirMenu()

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            reservarTurno()
        elif opcion == 2:
            modificarTurno()
        elif opcion == 3:
            cancelarTurno()
        elif opcion == 4:
            imprimirTurnos()
        elif opcion == 5:
            break
        else:
            print("Opción inválida.")
    except Exception as e:
        print(f"Error: {e}")

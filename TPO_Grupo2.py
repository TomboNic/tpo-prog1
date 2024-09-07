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


def reservar_turno():
    especialidad = especialidades[imprimir_menu_especialidades() - 1]
    imprimir_dias_y_horarios(especialidad)
    
    dia = input("Ingrese el día para la reserva: ").capitalize()
    turno = input("Ingrese el turno para la reserva (ej. 09:00): ")
    
    if especialidad in horariosDisponibles:
        if dia in horariosDisponibles[especialidad]:
            if turno in horariosDisponibles[especialidad][dia]:
                if horariosDisponibles[especialidad][dia][turno]:
                    horariosDisponibles[especialidad][dia][turno] = False
                    print(f"Turno reservado para {especialidad} en {dia} a las {turno}.")
                else:
                    print("El turno ya está reservado.")
            else:
                print("Turno no disponible.")
        else:
            print("Día no disponible.")
    else:
        print("Especialidad no encontrada.")


def modificar_turno():
    return

def cancelar_turno():
    return

def imprimir_turnos():
    return

def lectura_archivo():
    return

def escritura_archivo():
    return

def imprimir_menu():
    print("="*30)
    print("        MENÚ PRINCIPAL")
    print("="*30)
    print("1. Reservar Turno")
    print("2. Modificar Turno")
    print("3. Cancelar Turno")
    print("4. Ver Turnos")
    print("5. Salir")
    print("="*30)

def imprimir_menu_especialidades():
    print("="*30)
    print("     MENÚ DE ESPECIALIDADES MÉDICAS")
    print("="*30)
    print("1. Cardiología")
    print("2. Dermatología")
    print("3. Pediatría")
    print("4. Ginecología")
    print("5. Ortopedia")
    print("="*30)
    opcion = int(input())
    return opcion

def imprimir_dias_y_horarios(especialidad):
    if especialidad in horariosDisponibles:
        print("="*30)
        print(f"    Horarios Disponibles para {especialidad}")
        print("="*30)
        for dia, turnos in horariosDisponibles[especialidad].items():
            print(f"{dia}:")
            for turno, disponible in turnos.items():
                if disponible:
                    print(f"  {turno}")
        print("="*30)
    else:
        print("Especialidad no encontrada.")

def imprimir_menu_especialidades():
    print("="*30)
    print("     MENÚ DE ESPECIALIDADES MÉDICAS")
    print("="*30)
    for i, esp in enumerate(especialidades, 1):
        print(f"{i}. {esp}")
    print("="*30)
    opcion = int(input("Seleccione una especialidad: "))
    return opcion


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables


reservas = []
especialidades = ["Cardiología", "Dermatología", "Pediatría", "Ginecología", "Ortopedia"]

horariosDisponibles = {
    "Cardiología": {
        "Lunes": {"09:00": True, "09:30": True, "10:00": True, "10:30": True, "11:00": True, "11:30": True},
        "Martes": {"14:00": True, "14:30": True, "15:00": True, "15:30": True, "16:00": True},
        "Miércoles": {"09:00": True, "09:30": True, "10:00": True, "10:30": True, "11:00": True},
        "Jueves": {"14:00": True, "14:30": True, "15:00": True, "15:30": True, "16:00": True},
        "Viernes": {"09:00": True, "09:30": True, "10:00": True, "10:30": True, "11:00": True}
    },
    "Dermatología": {
        "Lunes": {"10:00": True, "10:30": True, "11:00": True, "11:30": True, "12:00": True},
        "Martes": {"15:00": True, "15:30": True, "16:00": True, "16:30": True, "17:00": True},
        "Miércoles": {"10:00": True, "10:30": True, "11:00": True, "11:30": True, "12:00": True},
        "Jueves": {"15:00": True, "15:30": True, "16:00": True, "16:30": True, "17:00": True},
        "Viernes": {"10:00": True, "10:30": True, "11:00": True, "11:30": True, "12:00": True}
    },
    "Pediatría": {
        "Lunes": {"08:00": True, "08:30": True, "09:00": True, "09:30": True, "10:00": True},
        "Martes": {"13:00": True, "13:30": True, "14:00": True, "14:30": True, "15:00": True},
        "Miercoles": {"08:00": True, "08:30": True, "09:00": True, "09:30": True, "10:00": True},
        "Jueves": {"13:00": True, "13:30": True, "14:00": True, "14:30": True, "15:00": True},
        "Viernes": {"08:00": True, "08:30": True, "09:00": True, "09:30": True, "10:00": True}
    },
    "Ginecología": {
        "Lunes": {"09:00": True, "09:30": True, "10:00": True, "10:30": True, "11:00": True},
        "Martes": {"14:00": True, "14:30": True, "15:00": True, "15:30": True, "16:00": True},
        "Miércoles": {"09:00": True, "09:30": True, "10:00": True, "10:30": True, "11:00": True},
        "Jueves": {"14:00": True, "14:30": True, "15:00": True, "15:30": True, "16:00": True},
        "Viernes": {"09:00": True, "09:30": True, "10:00": True, "10:30": True, "11:00": True}
    },
    "Ortopedia": {
        "Lunes": {"11:00": True, "11:30": True, "12:00": True, "12:30": True, "13:00": True},
        "Martes": {"16:00": True, "16:30": True, "17:00": True, "17:30": True, "18:00": True},
        "Miércoles": {"11:00": True, "11:30": True, "12:00": True, "12:30": True, "13:00": True},
        "Jueves": {"16:00": True, "16:30": True, "17:00": True, "17:30": True, "18:00": True},
        "viernes": {"16:00": True, "16:30": True, "17:00": True, "17:30": True, "18:00": True}
    }
}



#----------------------------------------------------------------------------------------------
# MENU PRINCIPAL
#----------------------------------------------------------------------------------------------

while True:
    
    imprimir_menu()

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            reservar_turno()
        elif opcion == 2:
            modificar_turno()
        elif opcion == 3:
            cancelar_turno()
        elif opcion == 4:
            imprimir_turnos()
        elif opcion == 5:
            break
        else:
            print("Opción inválida.")
    except Exception as e:
        print(f"Error: {e}")



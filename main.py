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
    return 

def modificarTurno():
    return

def cancelarTurno():
    return

def verTurnos():
    return

def escribirArchivo():
    return

def lecturaArchivo():
    return

def escrituraArchivo():
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


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables




#----------------------------------------------------------------------------------------------
# MENU PRINCIPAL
#----------------------------------------------------------------------------------------------

while True:
    
    imprimir_menu()

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            reservarTurno()
        elif opcion == 2:
            modificarTurno()
        elif opcion == 3:
            cancelarTurno()
        elif opcion == 4:
            verTurnos()
        elif opcion == 5:
            break
        else:
            print("Opción inválida.")
    except Exception as e:
        print(f"Error: {e}")



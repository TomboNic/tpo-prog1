
"""
-----------------------------------------------------------------------------------------------
Título: Gestor de Turnos Médicos V1.0

Fecha: 22/08/2024

Autores: Nicolas Tombolan, Nicolas Bermudez, Valentina Segovia, Mariano Sanabria.

Descripción:

Implementar un sistema que gestione la reserva de turnos médicos para los profe-
sionales de las distintas especialidades que atiende un centro de salud, utilizando
matrices, listas y diccionarios para mantener la información, almacenándola en ar-
chivos para permitir su posterior recuperación. Aplicar GIT para control de versiones
y recursividad para realizar las búsquedas.
-----------------------------------------------------------------------------------------------
"""

# ----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
# ----------------------------------------------------------------------------------------------

import os
import csv


# ----------------------------------------------------------------------------------------------
# FUNCIONES
# ----------------------------------------------------------------------------------------------

def reservarTurno():
    """
    Permite al usuario reservar un turno médico para una especialidad seleccionada.
    """
    indice_especialidad = seleccionarEspecialidad()
    if indice_especialidad is None:
        return

    indice_dia = seleccionarDia()
    if indice_dia is None:
        return

    indice_horario = seleccionarHorario(indice_especialidad, indice_dia)
    if indice_horario is None:
        return

    if verificarDisponibilidad(indice_especialidad, indice_dia, indice_horario):
        nombre, telefono, email = solicitarDatosPaciente()
        registrarReserva(indice_especialidad, indice_dia, indice_horario, nombre, telefono, email)
        print("\nReserva realizada con éxito.\n")
    else:
        print("\nHorario no disponible.\n")


def seleccionarEspecialidad():
    """
    Muestra el menú de especialidades y permite al usuario seleccionar una.

    Retorna el índice de la especialidad seleccionada o None si la selección no es válida.
    """
    imprimirMenuEspecialidades()
    indice_especialidad = int(input("\nSeleccione una especialidad (número): ")) - 1
    if indice_especialidad < 0 or indice_especialidad >= len(especialidades):
        print("\nÍndice de especialidad no válido.\n")
        return None
    return indice_especialidad


def imprimirDias():
    """
    Imprime los días de la semana disponibles para las reservas.
    """
    print("\nDías disponibles:")
    for i, dia in enumerate(dias, start=1):
        print(f"{i}. {dia}")
    print()



def seleccionarDia():
    """
    Solicita al usuario seleccionar un día para la reserva.

    Retorna el índice del día seleccionado o None si el día es inválido.
    """
    imprimirDias()
    indice_dia = int(input(f"\nSeleccione el día (1-{len(dias)}): ")) - 1
    if indice_dia < 0 or indice_dia >= len(dias):
        print("\nÍndice de día no válido.\n")
        return None
    return indice_dia


def imprimirHorariosDisponibles(indice_especialidad, indice_dia):
    """
    Imprime los horarios disponibles para una especialidad y día seleccionados.
    """
    if indice_especialidad < len(especialidades) and indice_dia < len(dias):
        print(f"\nHorarios disponibles para {especialidades[indice_especialidad]} el {dias[indice_dia]}:")
        horarios_disponibles = horarios[indice_especialidad]
        horarios_reservados = reservas[indice_especialidad][indice_dia]

        horarios_actualizados = [h for i, h in enumerate(horarios_disponibles) if horarios_reservados[i] == ""]

        if horarios_actualizados:
            for i, horario in enumerate(horarios_actualizados, start=1):
                print(f"{i}. {horario}")
        else:
            print("No hay horarios disponibles.")
    else:
        print("Error: Datos inválidos.")
    print()


def seleccionarHorario(indice_especialidad, indice_dia):
    """
    Solicita al usuario seleccionar un horario para la reserva de acuerdo a la especialidad y día seleccionados.

    Retorna el índice del horario seleccionado o None si no es válido.
    """
    imprimirHorariosDisponibles(indice_especialidad, indice_dia)
    indice_horario = int(input("\nSeleccione un horario (número): ")) - 1
    if indice_horario < 0 or indice_horario >= len(horarios[indice_especialidad]):
        print("\nÍndice de horario no válido.\n")
        return None
    return indice_horario


def verificarDisponibilidad(indice_especialidad, indice_dia, indice_horario):
    """
    Verifica si un horario está disponible para la reserva.

    Retorna True si está disponible, False si está reservado.
    """
    return reservas[indice_especialidad][indice_dia][indice_horario] == ""


def solicitarDatosPaciente():
    """
    Solicita los datos del paciente para la reserva.

    Retorna el nombre, teléfono y email del paciente.
    """
    print("\nIngrese los datos del paciente:")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    return nombre, telefono, email


def registrarReserva(indice_especialidad, indice_dia, indice_horario, nombre, telefono, email):
    """
    Registra la reserva en el sistema con los datos del paciente.

    Almacena la reserva en la lista de reservas.
    """
    reservas[indice_especialidad][indice_dia][indice_horario] = f"{nombre}, {telefono}, {email}"


def imprimirDiasYHorarios(indice_especialidad):
    """
    Esta función muestra los días de la semana y, para cada día, imprime los horarios disponibles
    de acuerdo a la especialidad seleccionada. Si un horario ya ha sido reservado, no se muestra
    como disponible.

    Entradas:
        - especialidad_idx: índice numérico de la especialidad seleccionada.

    Salidas:
        - Una tabla con los días de la semana y sus respectivos horarios disponibles.
        - Mensaje de error si el índice de la especialidad es inválido.
    """

    if indice_especialidad < 0 or indice_especialidad >= len(especialidades):
        print("\nÍndice de especialidad no válido.\n")
        return

    print(f"\nHorarios Disponibles para {especialidades[indice_especialidad]}")
    print("=" * 50)

    for indice_dia, dia in enumerate(dias):
        print(f"{dia.ljust(10)} | ", end="")
        if indice_especialidad < len(horarios) and indice_dia < len(horarios[indice_especialidad]):
            horarios_del_dia = horarios[indice_especialidad]
            horarios_reservados = []
            if indice_especialidad < len(reservas) and indice_dia < len(reservas[indice_especialidad]):
                horarios_reservados = [turno[0] for turno in reservas[indice_especialidad][indice_dia]]
            horarios_actualizados = [h for h in horarios_del_dia if h not in horarios_reservados]
            print(", ".join(horarios_actualizados))
        else:
            print("Error: No disponible.")

    print("=" * 50)


def imprimirTurnos():
    """
    Esta función muestra una lista de todas las reservas realizadas, incluyendo los datos del
    paciente (nombre, teléfono, email), la especialidad, el día y el horario de la reserva.
    """
    print("=" * 50)
    print("    Turnos Reservados")
    print("=" * 50)

    turnos_reservados = False  # Bandera para verificar si hay reservas

    for especialidad_idx, dias_reservas in enumerate(reservas):
        for dia_idx, turnos in enumerate(dias_reservas):
            for turno_idx, turno in enumerate(turnos):
                if turno:  # Verificar si el turno no está vacío
                    turnos_reservados = True
                    nombre, telefono, email = turno.split(", ")  # Descomponer los datos del paciente
                    horario = horarios[especialidad_idx][turno_idx]
                    print(
                        f"{nombre.ljust(15)} | {telefono.ljust(15)} | {email.ljust(20)} | {especialidades[especialidad_idx].ljust(12)} | {dias[dia_idx].ljust(8)} | {horario.ljust(5)}")

    if not turnos_reservados:
        print("\nNo hay turnos reservados.\n")

    print("=" * 50)


def imprimirMenu():
    print("=" * 30)
    print("        MENÚ PRINCIPAL")
    print("=" * 30)
    print("1. Reservar Turno")
    print("2. Modificar Turno")
    print("3. Cancelar Turno")
    print("4. Ver Turnos")
    print("5. Salir")
    print("=" * 30)


def imprimirMenuEspecialidades():
    """
    Imprime el menú de especialidades médicas disponibles.

    Esta función muestra un menú con las especialidades médicas ofrecidas en el centro de salud.
    El usuario puede seleccionar una especialidad para realizar una reserva.

    Entradas:
        - No requiere entradas.

    Salidas:
        - Un menú con las especialidades disponibles.
    """

    print("=" * 30)
    print("     MENÚ DE ESPECIALIDADES MÉDICAS")
    print("=" * 30)
    print("1. Cardiología")
    print("2. Dermatología")
    print("3. Pediatría")
    print("4. Ginecología")
    print("5. Ortopedia")
    print("=" * 30)


def modificarTurno():
    pass


def cancelarTurno():
    pass


# ----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
# ----------------------------------------------------------------------------------------------
# Declaración de variables

especialidades = ["Cardiología", "Dermatología", "Pediatría", "Ginecología", "Ortopedia"]

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

horarios = [
    ["09:00", "09:30", "10:00", "10:30", "11:00"],  # Cardiología
    ["10:00", "10:30", "11:00", "11:30", "12:00"],  # Dermatología
    ["08:00", "08:30", "09:00", "09:30", "10:00"],  # Pediatría
    ["09:00", "09:30", "10:00", "10:30", "11:00"],  # Ginecología
    ["11:00", "11:30", "12:00", "12:30", "13:00"]  # Ortopedia
]

disponibilidad = [
    [True, True, True, True, True],  # Cardiología
    [True, True, True, True, True],  # Dermatología
    [True, True, True, True, True],  # Pediatría
    [True, True, True, True, True],  # Ginecología
    [True, True, True, True, True]  # Ortopedia
]

reservas = [[["" for _ in range(len(horarios[especialidad]))] for _ in range(len(dias))] for especialidad in
            range(len(especialidades))]

# ----------------------------------------------------------------------------------------------
# MENÚ PRINCIPAL
# ----------------------------------------------------------------------------------------------

while True:

    imprimirMenu()

    try:
        opcion = int(input("\nSeleccione una opción: "))
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
            print("\nOpción inválida.\n")
    except Exception as e:
        print(f"\nError: {e}\n")

#menu

import os


def cargar_preguntas():
    # Preguntas hardcodeadas (puedes cargarlas desde un archivo más adelante)
    preguntas = [
        {
            "pregunta": "¿Cuál es la capital de España?",
            "opciones": ["A. Madrid", "B. Roma", "C. París", "D. Berlín"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Qué planeta es conocido como el planeta rojo?",
            "opciones": ["A. Venus", "B. Marte", "C. Júpiter", "D. Saturno"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿A que continente pertenece España?",
            "opciones": ["A. América del Sur", "B. Oceanía", "C. Europa", "D. Asia"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
            "opciones": ["A. Gabriel García Márquez", "B. Miguel de Cervantes", "C. Lope de Vega", "D. Federico García Lorca"],
            "respuesta_correcta": "B"
        },
    ]
    return preguntas

def mostrar_pregunta(pregunta):
    print("\n" + pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        print(opcion)

def obtener_respuesta():
    while True:
        respuesta = input("Tu respuesta (A, B, C, D): ").upper()
        if respuesta in ["A", "B", "C", "D"]:
            return respuesta
        else:
            print("Entrada no válida. Intenta de nuevo.")

def corregir_respuesta(respuesta, correcta):
    if respuesta == correcta:
        print("✅ ¡Correcto!")
        return True
    else:
        print(f"❌ Incorrecto. La respuesta correcta era {correcta}.")
        return False

def mostrar_resultados(aciertos, total):
    print("\n### RESULTADOS ###")
    print(f"Preguntas totales: {total}")
    print(f"Aciertos: {aciertos}")
    porcentaje = (aciertos / total) * 100
    print(f"Porcentaje de aciertos: {porcentaje:.2f}%")

    if porcentaje == 100:
        print("🎉 ¡Excelente! ¡Perfecto!")
    elif porcentaje >= 75:
        print("😊 ¡Muy bien!")
    elif porcentaje >= 50:
        print("😐 Aceptable, pero puedes mejorar.")
    else:
        print("😓 Necesitas practicar más.")

def empezar_cuestionario():
    preguntas = cargar_preguntas()
    aciertos = 0
    total = len(preguntas)

    for pregunta in preguntas:
        mostrar_pregunta(pregunta)
        respuesta = obtener_respuesta()
        if corregir_respuesta(respuesta, pregunta["respuesta_correcta"]):
            aciertos += 1

    mostrar_resultados(aciertos, total)
def mostrar_menu():
    while True:
        print("\n### MENÚ ###")
        print("1 - Empezar cuestionario")
        print("2 - Ranking (opcional)")
        print("3 - Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            empezar_cuestionario()
        elif opcion == "2":
            print("📊 Ranking aún no implementado.")
        elif opcion == "3":
            print("👋 ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# Programa principal
if __name__ == "__main__":
    mostrar_menu()



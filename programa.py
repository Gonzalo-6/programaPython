import os


def cargar_preguntas():
    return {
        "Deporte": [
            {
                "pregunta": "¿Cuántas copas de Europa tiene el Real Madrid?",
                "opciones": ["A. 17", "B. 16", "C. 15", "D. 14"],
                "respuesta_correcta": "C"
            },
            {
                "pregunta": "¿Quién es deportista español de todos los tiempos?",
                "opciones": ["A. Pau Gasol", "B. Rafael Nadal", "C. Fernando Alonso", "D. Andres Iniesta"],
                "respuesta_correcta": "B"
            }
        ],
        "Cultura": [
            {
                "pregunta": "¿Cuál es mejor libro español ?",
                "opciones": ["A. El Lazarillo de Tormes", "B. La Celestina", "C. Don Quijote de la Mancha", "D. La casa de Bernarda Alba"],
                "respuesta_correcta": "C"
            },
            {
                "pregunta": "¿Qué cuadro está expuesto en el Museo del Prado?",
                "opciones": ["A. El entierro del Conde Orgar", "B. El Guernica", "C. las Meninas", "D. La persistencia de la memoria"],
                "respuesta_correcta": "C"
            }
        ],
        "Geografía": [
            {
                "pregunta": "¿Cuál es la capital de España?",
                "opciones": ["A. Barcelona", "B. Bilbao", "C. Toledo", "D. Madrid"],
                "respuesta_correcta": "D"
            },
            {
                "pregunta": "¿Cuántas Comunidades Autonomas hay en España?",
                "opciones": ["A. 15", "B. 16", "C. 17", "D. 18"],
                "respuesta_correcta": "C"
            }
        ],
        "Historia": [
            {
                "pregunta": "¿En qué año comenzó la Guerra Civil española?",
                "opciones": ["A. 1936", "B. 1939", "C. 1941", "D. 1945"],
                "respuesta_correcta": "B"
            },
            {
                "pregunta": "¿Cuál es el monumento más famoso de españa?",
                "opciones": ["A. La Alhambra", "B. La Mezquita de Cordoba", "C. Catedral de Santiago", "D. Acueducto de Segovia"],
                "respuesta_correcta": "A"
            }
        ]
    }


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


def guardar_resultado(nombre, aciertos, total):
    with open("ranking.txt", "a", encoding="utf-8") as f:
        f.write(f"{nombre},{aciertos},{total}\n")


def mostrar_ranking():
    if not os.path.exists("ranking.txt"):
        print("\n📊 Aún no hay resultados en el ranking.")
        return

    with open("ranking.txt", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    if not lineas:
        print("\n📊 El archivo de ranking está vacío.")
        return

    print("\n--- RANKING DE USUARIOS ---")
    resultados = []
    for linea in lineas:
        try:
            nombre, aciertos, total = linea.strip().split(",")
            aciertos = int(aciertos)
            total = int(total)
            porcentaje = (aciertos / total) * 100
            resultados.append((nombre, aciertos, total, porcentaje))
        except ValueError:
            continue

    resultados.sort(key=lambda x: x[3], reverse=True)

    for i, (nombre, aciertos, total, porcentaje) in enumerate(resultados, start=1):
        print(f"{i}. {nombre} - {aciertos}/{total} ({porcentaje:.2f}%)")


def elegir_tema(preguntas_por_tema):
    print("\n🌍 TEMAS DISPONIBLES:")
    temas = list(preguntas_por_tema.keys())
    for i, tema in enumerate(temas, 1):
        print(f"{i}. {tema}")

    while True:
        opcion = input("Elige un número de tema: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(temas):
            return temas[int(opcion) - 1], preguntas_por_tema[temas[int(opcion) - 1]]
        else:
            print("❌ Opción no válida. Intenta de nuevo.")


def empezar_cuestionario():
    preguntas_por_tema = cargar_preguntas()
    tema, preguntas = elegir_tema(preguntas_por_tema)
    total = len(preguntas)
    aciertos = 0

    print(f"\n🎯 Has elegido el tema: {tema}\n")

    for pregunta in preguntas:
        mostrar_pregunta(pregunta)
        respuesta = obtener_respuesta()
        if corregir_respuesta(respuesta, pregunta["respuesta_correcta"]):
            aciertos += 1

    porcentaje = (aciertos / total) * 100

    print("\n--- RESULTADOS ---")
    print(f"Preguntas totales: {total}")
    print(f"Aciertos: {aciertos}")
    print(f"Porcentaje: {porcentaje:.2f}%")

    if porcentaje >= 75:
        print("🎉 ¡Muy bien!")
    elif porcentaje >= 50:
        print("👍 Bien, pero puedes mejorar.")
    else:
        print("📚 Necesitas practicar más.")

    nombre = input("Introduce tu nombre para guardar tu resultado: ")
    guardar_resultado(f"{nombre} ({tema})", aciertos, total)


def mostrar_menu():
    while True:
        print("\n### MENÚ ###")
        print("1 - Empezar cuestionario")
        print("2 - Ranking")
        print("3 - Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            empezar_cuestionario()
        elif opcion == "2":
            mostrar_ranking()
        elif opcion == "3":
            print("👋 ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")


# Programa principal
if __name__ == "__main__":
    mostrar_menu()

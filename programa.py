import os

def cargar_preguntas():
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
            "pregunta": "¿A qué continente pertenece España?",
            "opciones": ["A. América del Sur", "B. Oceanía", "C. Europa", "D. Asia"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cuál es el libro español más famoso de todos los tiempos'?",
            "opciones": ["A. El lazarillo de Tormes", "B. Don Quijote de la Mancha", "C. La Celestina", "D. La casa de Bernarda Alba"],
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
            continue  # Salta líneas mal formateadas

    resultados.sort(key=lambda x: x[3], reverse=True)  # Orden por porcentaje

    for i, (nombre, aciertos, total, porcentaje) in enumerate(resultados, start=1):
        print(f"{i}. {nombre} - {aciertos}/{total} ({porcentaje:.2f}%)")

def empezar_cuestionario():
    preguntas = cargar_preguntas()
    total = len(preguntas)
    aciertos = 0

    for pregunta in preguntas:
        mostrar_pregunta(pregunta)
        respuesta = obtener_respuesta()
        if corregir_respuesta(respuesta, pregunta["respuesta_correcta"]):
            aciertos += 1

    print("\n--- RESULTADOS ---")
    print(f"Preguntas totales: {total}")
    print(f"Aciertos: {aciertos}")
    porcentaje = (aciertos / total) * 100
    print(f"Porcentaje: {porcentaje:.2f}%")

    if porcentaje >= 75:
        print("🎉 ¡Muy bien!")
    elif porcentaje >= 50:
        print("👍 Bien, pero puedes mejorar.")
    else:
        print("📚 Necesitas practicar más.")

    nombre = input("Introduce tu nombre para guardar tu resultado: ")
    guardar_resultado(nombre, aciertos, total)

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

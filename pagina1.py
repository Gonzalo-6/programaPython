
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

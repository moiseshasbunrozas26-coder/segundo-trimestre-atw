"""Programa inicial del segundo trimestre."""


def saludar(nombre: str) -> str:
    """Devuelve un saludo personalizado."""
    return f"¡Hola, {nombre}! Bienvenido al segundo trimestre."


def main() -> None:
    nombre = input("Ingresa tu nombre: ").strip()

    if not nombre:
        nombre = "estudiante"

    print(saludar(nombre))


if __name__ == "__main__":
    main()


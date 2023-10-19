import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GitHub!")
 
    language = os.getenv("LANGUAGE")
    print(f"¡Hola, mi idioma es {language} desde GitHub!")    

if __name__ == "__main__":
    main()

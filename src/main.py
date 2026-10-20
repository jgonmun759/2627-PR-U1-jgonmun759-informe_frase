def preparar_texto(frase: str) -> str:
    """
    Modifica el texto introducido, eliminando espacios y convirtiendo el texto
    a minúsculas.

	:return: el texto convertido
    """

    return frase.lower().strip()

def analizar_texto(frase: str, palabra_buscada: str) -> tuple[int, int, bool]:
	"""
	Analiza el texto introducido preparado y obtiene el número de caracteres, palabras y
	si contiene la palabra "Python".
	
	:param frase: la frase a analizar
	:return: una tupla con el número de caracteres, palabras, y si contiene o no la palabra determinada
	"""
	
	return len(frase), len(frase.split()), (True if palabra_buscada.lower() in frase else False)

def main():
	frase = input()
	
	frase_preparada = preparar_texto(frase)
	
	if frase_preparada:
		caracteres, palabras, contiene_python = analizar_texto(frase_preparada, "Python")
		
		print(f"Texto: {frase_preparada}")
		print(f"Caracteres: {caracteres}")
		print(f"Palabras: {palabras}")
		print(f"Contiene la palabra python: " + ("sí" if contiene_python else "no"))
	else:
		print("Error: No has introducido ninguna frase.")

if __name__ == "__main__":
    main()
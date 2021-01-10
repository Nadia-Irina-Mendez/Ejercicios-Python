def contarVocales(unTexto):
	vocales=("a", "e", "i", "o", "u")
contVoc=0
for x in unTexto.lower():
      if x =="a" or "e" or "i" or "o" or "u":
                  contVoc=contVoc + 1
			return contVoc

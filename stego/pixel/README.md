# Nombre: `iic3301`
### Dificultad: ``
### Categoría: `stego`
### Autor: anon
### Flag: `DCCTF{m3t4d4t4_c0nt4iNs_ev3ryth1nG}`

### Descripción:
Puedes guardar muchas cosas en 1x1.

### Solución:
La flag se puede encontrar en la metadata de la imagen. Muchas herramientas permiten extraer esta información, una de ellas es `exiftool`.
`exiftool pixel.jpg`, la flag se encuentra en la metatag `XP Title`

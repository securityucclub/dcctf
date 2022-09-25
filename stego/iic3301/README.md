# Nombre: `iic3301`
### Dificultad: `facil`
### Categoría: `stego`
### Autor: [c4ebt](https://c4ebt.github.io/)
### Flag: `DCCTF{iic3301_pr3curs0r_d3_cic4d4}`

### Descripcion:
Cicada 3301: "el enigma más elaborado y misterioso de la era del internet". Una serie de acertijos publicados por una organización secreta para encontrar "individuos altamente inteligentes". Todo efecto tiene una causa: ¿de dónde salieron los miembros originales de Cicada? Quizá esa sea una pregunta que vive mejor sin respuesta...

### Hint:
```
Sabes lo que es la metadata?
```

### Solución:

El archivo inicial es un .wav de una (muy buena) canción. Analizando la metadata usando exiftool se encuentra la tag de artist cuyo contenido es "c3RlZ2hpZGUgd2l0aCB0aGlzIG5vIHNwYWNlcyBubyBhcG9zdHJvcGhl". Este es claramente base64, y decodeando se obtiene "steghide with this no spaces no apostrophe". Steghide es una herramienta de esteganografía que permite embeddear data en archivos multimedia, y decodearla también. Se puede deducir de la metatag de artist que la passphrase para steghide sería el artista de la canción. Reconociendo la canción con cualquier software obtenemos que se llama "Out of Control" y su artista es "Nothing's Carved in Stone". Luego,

`steghide extract -sf 0.wav -p "nothingscarvedinstone"`

extrae el archivo embeddeado en el wav, 1.jpg.
Este es una imagen que dice "iic3301". Nuevamente, analizando la metadata de la imagen, se encuentra la tag "what" con "fgrtuvqr qppgs" como contenido. Esta string es ROT13, y decodeando se obtiene "steghide dcctf". Nuevamente hay que usar la herramienta steghide, esta vez con la passphrase "dcctf".

`steghide extract -sf 1.jpg -p "dcctf"`

Se obtiene una segunda imagen, 2.jpg. Esta itene una string cuyo contenido es enigmático. Tras algo de prueba y error, suerte, o puro ingenio, se puede deducir que las letras ilustradas representan elementos químicos. Convirtiendo cada uno de los elementos a sus respectivos números atómicos, se obtiene una serie de números en base 10, que pueden ser convertidos a texto para obtener la string "flagpls". Siguiendo el patrón,

`steghide extract -sf 2.jpg -p "flagpls"`

entrega el archivo flag.txt, con lo que se termina el desafío.

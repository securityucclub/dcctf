# Nombre: `malabares`
### Dificultad: `fácil`
### Categoría: `web`
### Autor: [Cae](https://c4ebt.github.io/)
### Flag: `DCCTF{typ3_juggling_it_i5!}`

### Descripción:
Un estudiante quiere hacer su propia pagina web con sistema de login y todo, pero apenas sabe programar... Tuvo que hacer malabares para lograr que funcionara lo básico de lo básico. Se buena onda y no lo hackees porfa... `challs.dcctf.xyz:7890/index.php`

### Hint:
```Los comentarios que se escuchan acerca de este sitio...```

### Solución:

Se pueden fuzzear los directorios de la web usando cualquier herramienta de fuzzing. Se encontrará la ruta robots.txt, en la que se ve un disallow: source.zip. Al acceder a /source.zip se descarga lo que parece ser la source del login en index.php. Analizando un poco esta source se puede ver que se genera un string random para el token, por lo que no se conseguirá bypassear el login con diccionarios, y se descarta la fuerza bruta pura ya que el largo del token es muy grande. Se observa que hay dos comparaciones posibles: la data ingresada manualmente, y otra en formato json. Ambas tienen loose comparison, y a través de la comparación json podemos ingresar un int para explotar una vulnerabilidad de type juggling y bypassear el token para mostrar la flag. Luego,

`curl malabares.dcctf.xyz:7890/index.php -H "Content-Type: json" -d '{"input":0}'`

entrega la flag exitosamente.

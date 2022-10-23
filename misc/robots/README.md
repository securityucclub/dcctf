# Nombre: `Robots`
### Dificultad: `Hard (🃏🃏🃏🃏)`
### Categoría: `misc`
### Autor: anon
### Flag: `DCCTF{FIRST LETTERS}`

### Descripción:
El estándar de exclusión de robots, también conocido como el protocolo de la exclusión de robots es un método para evitar que ciertos bots que analizan los sitios web u otros robots que investigan todo o una parte del acceso de un sitio Web, público o privado, agreguen información innecesaria a los resultados de búsqueda.

# Solución:
En la descripción se habla del conocido archivo robots.txt, que se encuentra en la mayor parte de los sitios web en `/robots.txt`. Si accedemos en `https://dcctf.xyz/robots.txt`, nos encontramos un ejemplo de archivo robots.txt, con una serie enorme de "Disallows". Si buscamos " Allow" (nótese el espacio antes) encontraremos una entrada de allow para la ruta `/humans_and_robots`. En esta ruta, vemos nuevamente un robots.txt, esta vez con una estructura diferente. Si observamos con atención, podemos darnos cuenta de que las primeras letras de cada entrada son siempre mayúsculas, y si las unimos todas, junto con los brackets que hay en el sitio, se arma la flag.

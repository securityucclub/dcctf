# Nombre: `Robots`
### Dificultad: `Hard (馃儚馃儚馃儚馃儚)`
### Categor铆a: `misc`
### Autor: anon
### Flag: `DCCTF{FIRST LETTERS}`

### Descripci贸n:
El est谩ndar de exclusi贸n de robots, tambi茅n conocido como el protocolo de la exclusi贸n de robots es un m茅todo para evitar que ciertos bots que analizan los sitios web u otros robots que investigan todo o una parte del acceso de un sitio Web, p煤blico o privado, agreguen informaci贸n innecesaria a los resultados de b煤squeda.

# Soluci贸n:
En la descripci贸n se habla del conocido archivo robots.txt, que se encuentra en la mayor parte de los sitios web en `/robots.txt`. Si accedemos en `https://dcctf.xyz/robots.txt`, nos encontramos un ejemplo de archivo robots.txt, con una serie enorme de "Disallows". Si buscamos " Allow" (n贸tese el espacio antes) encontraremos una entrada de allow para la ruta `/humans_and_robots`. En esta ruta, vemos nuevamente un robots.txt, esta vez con una estructura diferente. Si observamos con atenci贸n, podemos darnos cuenta de que las primeras letras de cada entrada son siempre may煤sculas, y si las unimos todas, junto con los brackets que hay en el sitio, se arma la flag.

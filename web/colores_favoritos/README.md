# Nombre: `Colores Favoritos`
### Dificultad: `Medium (🃏🃏🃏)`
### Categoría: `web`
### Autor: [a-maccormack](https://github.com/a-maccormack)
### Flag: `DCCTF{noob_x03659_W3B}`

### Descripción:
Los mejores hackers del mundo crearon una base de datos para guardar sus colores favoritos en `http://127.0.0.1:3000`. El problema es que al dueño del sitio se le olvidó la contraseña, y tiene una fila de hackers legendarios esperando para agregar sus colores favoritos. Podrás ayudarlos? Consigue la contraseña de admin y completa el desafío.

Usuarios:
- `Tflow`
- `satoshi`
- `Kingpin`
- `geohot`
- `snowden`
- `c0mrade`
- `admin`

# Solución:
La página contiene una vulnerabilidad de [inyección sql](https://www.youtube.com/watch?v=ciNHn38EyRc). Para determinar el tipo de base de datos que utiliza la página, primero debemos ejecutar comandos que [revelen la versión de la base de datos](https://portswigger.net/web-security/sql-injection/examining-the-database). En el caso del problema, el comando que se debe utilizar es `version()`, el cual revela que la base de datos es `PostgreSQL`

#### Input 1
```
'; SELECT version()  --
```

Luego debemos [determinar el nombre de la tabla](https://stackoverflow.com/questions/14730228/postgresql-query-to-list-all-table-names) que contiene la información de los usuarios que buscamos, por lo cual se deberá realizar un query que revele esta información:

#### Input 2
```
'; SELECT table_name  FROM information_schema.tables  WHERE table_schema='public' AND table_type='BASE TABLE'--
```

Este comando nos revela que hay una tabla llamada `users_usuarios`.

Sabiendo el nombre de la tabla, podemos utilizarlo para listar todos sus contenidos...

#### Input 3
```
'; SELECT * FROM users_usuarios; --
```

Esta query nos revela todos los usuarios y sus campos correspondientes. Podemos observar que el usuario `admin` tiene como contraseña `DCCTF{noob_x03659_W3B}`, lo cual corresponde a la flag para este problema.
# Nombre: `admin`
### Dificultad: ``
### Categoría: `web`
### Autor: anon
### Flag: `DCCTF{s4f3sT_p4sW0rD_0n_e4rtH}`

### Descripción:
Perdimos la clave de admin de DCCTF, nos ayudas a entrar?

https://dcctf.xyz/very-secure-login

### Solución:

Si analizamos el código fuente del desafío (presionando f12 / ctrl+u / rightclick+inspect) veremos entre los comentarios `<!-- DCCTF -->` una función que checkea nuestro input de contraseña, con lo que parecen ser muchos bytes en hex. Si decodeamos estos bytes conseguimos la flag directamente.

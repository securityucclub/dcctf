#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

int win(void) {
    char buf[40] = {0};
    int fd = open("flag.txt", O_RDONLY);
    read(fd, buf, 34);
    puts(buf);
    return 0;
}

void main(void) {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);

    char nombre[32];
    char apellido[32];

    puts("Portal de secretos de la realeza. Ingrese su nombre:");
    gets(nombre);
    if (!strcmp(apellido, "Pérez")) {
        win();
    }
    else {
        puts("No eres de la realeza! No puedes acceder a los secretos de su majestad");
    }

    exit(0);
}

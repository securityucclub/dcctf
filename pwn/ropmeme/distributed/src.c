#include <stdio.h>
#include <unistd.h>

int win(void) {
    syscall(0x3b, "/bin/sh\0", NULL, NULL);
    return 0;
}

int main(void) {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);

    char buf[64];

    puts("Podrás ropmerme?");

    gets(buf);
    return 0;
}

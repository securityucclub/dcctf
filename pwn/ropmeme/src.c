#include <stdio.h>

int win(void) {
    syscall(0x3b, "/bin/sh\0", NULL, NULL);
    return 0;
}

int main(void) {
    char buf[64];

    puts("Podrás ropmerme?");

    gets(buf);
    return 0;
}

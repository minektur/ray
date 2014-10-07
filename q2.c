#include<stdio.h>

unsigned int countBits(unsigned char byte);


int main(int argc, char** argv) {
    int x;
    for (x = 0; x < 32; x++) {
        printf("Count of %d is %d\n", x, countBits(x));
    }
}

unsigned int countBits(unsigned char byte) {
    unsigned int count = 0;
    while (byte > 0) {
        if (byte & 1) count ++;
        byte >>= 1;
    }
    return count;
}


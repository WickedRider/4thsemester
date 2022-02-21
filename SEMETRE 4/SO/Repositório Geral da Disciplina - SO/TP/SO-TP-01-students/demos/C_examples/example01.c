// Example of scanf

#include <stdio.h>

int main() {
        int a = 20;
        char s[4];

        printf("before scanf: a = %u\n", a);

        scanf("%4s", s);

        printf("after scanf: a = %u\n", a);
        printf("s = %s\n", s);

        return 0;
}

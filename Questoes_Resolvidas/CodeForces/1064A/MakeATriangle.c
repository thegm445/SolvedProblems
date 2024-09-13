#include <stdio.h>

#define max(A, B) (A > B ? A : B) 
#define swap(A, B) { int temp = A; A = B; B = temp; }

int main() {
    int a, b, c;
    scanf("%d %d %d", &a,&b,&c);

    // Eu usaria o mergesort...mas to com preguiça.
    if (a > b) swap(a, b);
    if (b > c) swap(b, c);
    if (a > b) swap(a, b); 

    int minutes = max(0, c - a - b + 1);

    printf("%d\n",minutes);
    return 0;
}
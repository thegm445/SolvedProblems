#include <stdio.h>


int gcd(int a, int b) {
    return b == 0 ? a : gcd( b, a%b );
}

int main(){
    int t = 0; scanf("%d",&t);
    char yes[] = "YES\n"; char no[] = "NO\n";

    while (t--)
    {
        int a,b; scanf("%d %d", &a, &b);
        printf("%s", gcd(a,b) == b ? yes : no); 
        // No caso de 8 e 6 o gcd > 1 nao era verdade, mas se os vertices iniciais forem um 'subset' é vdd sempre, a%b == 0 então?
    }
}
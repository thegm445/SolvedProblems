#include <stdio.h>

int main(){
    int n = 0; scanf("%d",&n);
    char yes[] = "YES\n"; char no[] = "NO\n";

    while (n--)
    {
        int temp; scanf("%d",&temp);
        printf("%s", temp&3 ? no : yes);
    }
}
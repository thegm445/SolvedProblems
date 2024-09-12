    #include <stdio.h>
    #include <math.h>
    int main(){
        int t; scanf("%d",&t);
        while(t--){
            int n; scanf("%d",&n);
     
            int o_do_dois = sqrt(n/2); //  Em tese tá certo
            int o_do_quatro = sqrt(n/4); // Em tese tá certo também
     
            if( (n%2==0) && ( o_do_dois*o_do_dois == n/2 ) ){
                printf("YES\n");
            }
            else if( (n%4==0) && (o_do_quatro*o_do_quatro) == n/4 ){
                printf("YES\n");
            }
            else {
                printf("NO\n");
            }
        }
    }
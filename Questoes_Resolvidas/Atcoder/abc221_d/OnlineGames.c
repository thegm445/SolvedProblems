#include <stdio.h>
#include <stdlib.h>

#define MAX_EVENTS 400005


typedef struct Event {
    int day;
    int type; 
} Event;


#define less(A, B) ((A) < (B))
#define lesseq(A, B) ((A) <= (B))
#define exch(A, B) \
    {                \
        Event t;      \
        t = A;       \
        A = B;       \
        B = t;       \
    }
#define cmpexch(A, B) \
    {                  \
        if (less(B, A)) \
        exch(A, B);     \
    }

void merge(Event *V, int l, int m, int r) {
    Event *R = malloc(sizeof(Event) * (r - l + 1));
    int i = l, j = m + 1, k = 0;

    while (i <= m && j <= r) {
        if (V[i].day < V[j].day || (V[i].day == V[j].day && V[i].type < V[j].type)) {
            R[k++] = V[i++];
        } else {
            R[k++] = V[j++];
        }
    }

    while (i <= m)
        R[k++] = V[i++];
    while (j <= r)
        R[k++] = V[j++];

    k = 0;
    for (i = l; i <= r; i++)
        V[i] = R[k++];
    free(R);
}

void mergesort(Event *V, int l, int r) {
    if (l >= r)
        return;
    int meio = (l + r) / 2;
    mergesort(V, l, meio);
    mergesort(V, meio + 1, r);
    merge(V, l, meio, r);
}

int main() {
    int n;
    scanf("%d", &n);

    Event events[MAX_EVENTS];
    for (int i = 0; i < n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        events[2 * i].day = a;
        events[2 * i].type = 1;
        events[2 * i + 1].day = a + b;
        events[2 * i + 1].type = -1; 
    }


    mergesort(events, 0, 2 * n - 1);

    int active_players = 0;
    int days_with_k_players[MAX_EVENTS] = {0};
    int prev_day = 0;


    for (int i = 0; i < 2 * n; i++) {
        days_with_k_players[active_players] += events[i].day - prev_day;
        active_players += events[i].type;
        prev_day = events[i].day;
    }

    for (int i = 1; i <= n; i++) {
        printf("%d ", days_with_k_players[i]);
    }
    printf("\n");

    return 0;
}
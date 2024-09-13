#include <bits/stdc++.h>
using namespace std;


#define MOD 998244353
#define ii pair<int,int>


int main() {
    int N, K;
    cin >> N >> K;

    vector<ii> segments(K);
    for (int i = 0; i < K; i++) {
        cin >> segments[i].first >> segments[i].second; 
    }

    vector<long long> dp(N + 1, 0);
    vector<long long> prefix_sum(N + 1, 0); 

    dp[1] = 1;
    prefix_sum[1] = 1;

    for (int i = 2; i <= N; ++i) {
        for (int j = 0; j < K; ++j) {
            int L = segments[j].first;
            int R = segments[j].second;
            int start = max(1, i - R);
            int end = i - L;

            if (end >= start) {
                dp[i] = (dp[i] + prefix_sum[end] - (start > 1 ? prefix_sum[start - 1] : 0)) % MOD;
                if (dp[i] < 0) dp[i] += MOD; 
            }
        }
        prefix_sum[i] = (prefix_sum[i - 1] + dp[i]) % MOD;
    }

    cout << dp[N] << endl;
    return 0;
}
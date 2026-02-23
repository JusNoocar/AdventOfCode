#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
    freopen("test.txt", "r", stdin);

    int n = 140;
    vector<string> a(n + 2);
    for (int i = 0; i < n; ++i){
        string s;
        cin >> s;
        a[i + 1] = "." + s + ".";
    }
    int m = a[1].size();
    string first = "";
    for (int i = 0; i < m; ++i){
        first = first + ".";
    }
    a[0] = a[n + 1] = first;

    int ans = 0;

    vector<vector<int>> dp((n + 2) * m);
    for (int i = 1; i < n + 1; ++i){
        int num = 0;
        int len = 0;

        for (int j = 1; j < m - 1; ++j){
            if (a[i][j] - '0' >= 0 && a[i][j] - '0' <= 9){
                num = num * 10 + (a[i][j] - '0');
                len++;

            }else if (len != 0){
                for (int x = j - len - 1; x <= j; ++x){
                    char el = a[i - 1][x];
                    if (el == '*'){
                        int idx = (i - 1) * m + x;
                        dp[idx].push_back(num);
                    }

                    el = a[i + 1][x];
                    if (el == '*'){
                        int idx = (i + 1) * m + x;
                        dp[idx].push_back(num);
                    }

                }

                char el = a[i][j - len - 1];
                if (el == '*'){
                    int idx = i * m + j - len - 1;
                    dp[idx].push_back(num);
                }
                el = a[i][j];
                if (el == '*'){
                    int idx = i * m + j;
                    dp[idx].push_back(num);
                }

                num = 0; len = 0;

            }
        }
    }

    for (int i = 0; i < (n + 2) * m; ++i){
        //cout << dp[i].size() << "\n";
        if (dp[i].size() == 2){
            ans += dp[i][0] * dp[i][1];
        }
    }

    cout << ans << "\n";


}

#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("test.txt", "r", stdin);
    int n = 100;
    string s0;
    cin >> s0;
    int m = s0.size();
    vector<vector<char>> a(n, vector<char>(m));
    for (int j = 0; j < m; ++j){
        a[0][j] = s0[j];
    }

    for (int i = 1; i < n; ++i){
        for (int j = 0; j < m; ++j){
            cin >> a[i][j];
        }
    }

    for (int j = 0; j < m; ++j){
        for (int i = 0; i < n; ++i){
            if (a[i][j] == 'O'){
                int nxt = i;
                while (nxt > 0 && a[nxt - 1][j] == '.'){
                    nxt--;
                }
                a[i][j] = '.';
                a[nxt][j] = 'O';
            }

        }
    }

    int ans = 0;
    for (int i = 0; i < n; ++i){
        for (int j = 0; j < m; ++j){
            if (a[i][j] == 'O'){
                ans += (n - i);
            }
            //cout << a[i][j] << " ";
        }
        //cout << "\n";
    }
    cout << ans << "\n";

}

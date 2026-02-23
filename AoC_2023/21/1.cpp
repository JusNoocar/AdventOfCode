#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
    freopen("test.txt", "r", stdin);
    ll n = 33;
    string s;
    cin >> s;
    ll m = s.size();
    vector<vector<char>> a(n, vector<char>(m));
    ll start_x, start_y;
    for (ll j = 0; j < m; ++j){
        if (s[j] == 'S'){
            start_x = 0;
            start_y = j;
        }
        a[0][j] = s[j];
    }

    for (ll i = 1; i < n; ++i){
        for (ll j = 0; j < m; ++j){
            cin >> a[i][j];
            if (a[i][j] == 'S'){
                start_x = i;
                start_y = j;
        }
        }
    }

    ll cnt_odd = 0;
    ll cnt_even = 1;
    vector<vector<ll>> used(n, vector<ll>(m, false));
    queue<pair<ll, ll>> que;
    que.push({start_x, start_y});
    used[start_x][start_y] = true;
    for (ll step = 1; step <= 50; ++step){
        ll added = 0;
        ll len = que.size();

        for (ll i = 0; i < len; ++i){
            ll x = que.front().first;
            ll y = que.front().second;
            used[x][y] = true;
            que.pop();

            if (x != 0 && a[x - 1][y] == '.' && !used[x - 1][y]){
                added++;
                used[x - 1][y] = true;
                que.push({x - 1, y});
            }
            if (y != 0 && a[x][y - 1] == '.' && !used[x][y - 1]){
                added++;
                used[x][y - 1] = true;
                que.push({x, y - 1});
            }
            if (x != n - 1 && a[x + 1][y] == '.' && !used[x + 1][y]){
                added++;
                used[x + 1][y] = true;
                que.push({x + 1, y});
            }
            if (y != m - 1 && a[x][y + 1] == '.' && !used[x][y + 1]){
                added++;
                used[x][y + 1] = true;
                que.push({x, y + 1});
            }

        }

        if (step % 2 == 0){
            cnt_even += added;
            //cout << cnt_even<<"\n";
        }else{
            cnt_odd += added;
            //cout << cnt_odd<< "\n";
        }
    }

    cout << cnt_even;


}

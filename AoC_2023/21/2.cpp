#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
    freopen("test.txt", "r", stdin);
    ll n = 131;
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
    a[start_x][start_y] = '.';
    used[start_x][start_y] = true;
    for (ll step = 1; step <= 240; ++step){
        ll added = 0;
        ll len = que.size();

        set<pair<int, int>> to_add;
        for (ll i = 0; i < len; ++i){
            ll x = que.front().first;
            ll y = que.front().second;

            que.pop();


            if (x != 0 && a[x - 1][y] == '.'){
                if (!to_add.count({x - 1, y})) added++;

                to_add.insert({x - 1, y});
            }else if (x == 0 && a[n - 1][y] == '.'){
                if (!to_add.count({n - 1, y})) added++;

                to_add.insert({n - 1, y});
            }
            if (y != 0 && a[x][y - 1] == '.'){
                if (!to_add.count({x, y - 1})) added++;

                to_add.insert({x, y - 1});
            }else if (y == 0 && a[x][m - 1] == '.'){
                if (!to_add.count({x, m - 1})) added++;

                to_add.insert({x, m - 1});
            }


            if (x != n - 1 && a[x + 1][y] == '.'){
                if (!to_add.count({x + 1, y})) added++;

                to_add.insert({x + 1, y});
            }else if (x == n - 1 && a[0][y] == '.'){
                if (!to_add.count({0, y})) added++;

                to_add.insert({0, y});
            }

            if (y != m - 1 && a[x][y + 1] == '.'){
                if (!to_add.count({x, y + 1})) added++;

                to_add.insert({x, y + 1});
            }else if (y == m - 1 && a[x][0] == '.'){
                if (!to_add.count({x, 0})) added++;

                to_add.insert({x, 0});
            }

        }
        for (pair<int, int> u : to_add){
            que.push(u);
        }

        if (step % 2 == 0){
            cnt_even = added;
            cout << step << " " << cnt_even<<"\n";
        }else{
            cnt_odd = added;
            cout << step << " " << cnt_odd<< "\n";
        }
    }

    cout << cnt_even;


}

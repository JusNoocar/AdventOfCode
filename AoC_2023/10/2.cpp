#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
    freopen("test.txt", "r", stdin);

    ll n = 140;
    vector<string> a(n);
    for (ll i = 0; i < n; ++i){
        cin >> a[i];
    }
    ll m = a[0].size();

    ll start_i = 0;
    ll start_j = 0;
    for (ll i = 0; i < n; ++i){
        for (ll j = 0; j < m; ++j){
            if (a[i][j] == 'S'){
                start_i = i;
                start_j = j;
            }
        }
    }

    vector<vector<ll>> map_dist(n, vector<ll>(m, -1));
    //cout << "ok";
    vector<vector<ll>> used(n, vector<ll>(m, 0));
    set<vector<ll>> que;
    que.insert({0, start_i, start_j});
    ll ans = 0;

    while (!que.empty()){
        //cout << que.size();
        vector<ll> inp = *que.begin();
        ll w = inp[0];
        ll i = inp[1];
        ll j = inp[2];
        ans = max(ans, w);
        que.erase(que.begin());
        used[i][j] = 1;


        if (i > 0 && (a[i - 1][j] == '|' || a[i - 1][j] == 'F' || a[i - 1][j] == '7')){
            if (a[i][j] == 'S' || a[i][j] == 'J' || a[i][j] == 'L' || a[i][j] == '|'){
                if (!used[i - 1][j]) que.insert({w + 1, i - 1, j});
            }
        }

        if (i < n - 1 && (a[i + 1][j] == '|' || a[i + 1][j] == 'J' || a[i + 1][j] == 'L')){
            if (a[i][j] == 'S' || a[i][j] == 'F' || a[i][j] == '7' || a[i][j] == '|'){
                if (!used[i + 1][j]) que.insert({w + 1,i + 1, j});
            }
        }

        if (j > 0 && (a[i][j - 1] == '-' || a[i][j - 1] == 'F' || a[i][j - 1] == 'L')){
            if (a[i][j] == 'S' || a[i][j] == 'J' || a[i][j] == '7' || a[i][j] == '-'){
                if (!used[i][j - 1]) que.insert({w + 1,i, j - 1});
            }
        }

        if (j < m - 1 && (a[i][j + 1] == '-' || a[i][j + 1] == 'J' || a[i][j + 1] == '7')){
            if (a[i][j] == 'S' || a[i][j] == 'F' || a[i][j] == 'L' || a[i][j] == '-'){
                if (!used[i][j + 1]) que.insert({w + 1,i, j + 1});
            }
        }

        map_dist[i][j] = w;
    }

    cout << ans << "\n";



    /*
    for (ll i = 0; i < n; ++i){
        for (ll j = 0; j < m; ++j){
            cout << map_dist[i][j] << " ";
        }
        cout << "\n";
    }
    */


    a[start_i][start_j] = '7';
    ll cnt = 0;

    for (ll i = 0; i < n; ++i){
        ll balance = 0;
        for (ll j = 0; j < m; ++j){
            if (map_dist[i][j] != -1){
                if (a[i][j] == '|' || a[i][j] == 'J' || a[i][j] == 'L'){
                    balance = (balance + 1) % 2;
                }
            }else if (balance == 1){
                cnt++;
            }
        }
    }
    cout << cnt << "\n";




}

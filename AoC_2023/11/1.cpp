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

    vector<ll> row(n);
    vector<ll> col(m);

    for (ll i = 0; i < n; ++i){
        bool flag = true;
        for (ll j = 0; j < m; ++j){
            if (a[i][j] != '.') flag = false;
        }

        if (flag){
            if (i == 0) row[i] = 999999;
            else row[i] = row[i - 1] + 1000000;
        }else{
            if (i == 0) row[i] = 0;
            else row[i] = row[i - 1] + 1;
        }
    }

    for (ll j = 0; j < m; ++j){
        bool flag = true;
        for (ll i = 0; i < n; ++i){
            if (a[i][j] != '.') flag = false;
        }

        if (flag){
            if (j == 0) col[j] = 999999;
            else col[j] = col[j - 1] + 1000000;
        }else{
            if (j == 0) col[j] = 0;
            else col[j] = col[j - 1] + 1;
        }
    }
    vector<pair<ll, ll>> galaxy;
    for (ll i = 0; i < n; ++i){
        for (ll j = 0; j < m; ++j){
            if (a[i][j] == '#'){
                galaxy.push_back({i, j});
            }
        }
    }

    ll ans = 0;
    for (ll i = 0; i < galaxy.size(); ++i){
        for (ll j = i + 1; j < galaxy.size(); ++j){
            ll x1 = row[galaxy[i].first];
            ll y1 = col[galaxy[i].second];

            ll x2 = row[galaxy[j].first];
            ll y2 = col[galaxy[j].second];

            ll dist = abs(x2 - x1) + abs(y2 - y1);
            ans += dist;
        }
    }
    cout << ans << "\n";

}

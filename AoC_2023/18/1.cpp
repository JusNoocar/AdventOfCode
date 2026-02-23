#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
    freopen("test.txt", "r", stdin);
    ll n = 2250;
    ll m = 738;
    vector<char> d(m);
    vector<ll> num(m);
    vector<string>color(m);
    ll leftcnt = 0;
    ll rightcnt = 0;
    ll upcnt = 0;
    ll downcnt = 0;
    for (ll q = 0; q < m; ++q){
        cin >> d[q] >> num[q] >> color[q];
        if (d[q] == 'L') leftcnt += num[q];
        if (d[q] == 'R') rightcnt += num[q];
        if (d[q] == 'U') upcnt += num[q];
        if (d[q] == 'D') downcnt += num[q];
    }

    cout << leftcnt << " " << rightcnt << "\n";
    cout << upcnt << " " << downcnt << "\n";
    vector<vector<char>> a(n, vector<char>(n, '.'));
    a[1][1] = '#';

    cout << "ok";
    //ll i1 = 1;
    //ll j1 = 1;
    ll i1 = 1040;
    ll j1 = 1020;
    for (ll q = 0; q < m; ++q){
        if (d[q] == 'L'){
            for (ll k = 0; k < num[q]; ++k){
                j1 -= 1;
                a[i1][j1] = '#';
            }
        }
        if (d[q] == 'R'){
            for (ll k = 0; k < num[q]; ++k){
                j1 += 1;
                a[i1][j1] = '#';
            }
        }
        if (d[q] == 'D'){
            for (ll k = 0; k < num[q]; ++k){
                i1 += 1;
                a[i1][j1] = '#';
            }
        }
        if (d[q] == 'U'){
            for (ll k = 0; k < num[q]; ++k){
                i1 -= 1;
                a[i1][j1] = '#';
            }
        }
    }

    vector<vector<char>> b(n, vector<char>(n, '.'));
    for (ll i = 0; i < n; ++i){
        for (ll j = 0; j < n; ++j){
            if (a[i][j] == '#' && a[i - 1][j] == '#' && a[i + 1][j] == '#'){
                b[i][j] = '|';
            }
            if (a[i][j] == '#' && a[i][j - 1] == '#' && a[i][j + 1] == '#'){
                b[i][j] = '-';
            }
            if (a[i][j] == '#' && a[i - 1][j] == '#' && a[i][j + 1] == '#'){
                b[i][j] = 'L';
            }
            if (a[i][j] == '#' && a[i][j - 1] == '#' && a[i - 1][j] == '#'){
                b[i][j] = 'J';
            }
            if (a[i][j] == '#' && a[i + 1][j] == '#' && a[i][j + 1] == '#'){
                b[i][j] = 'F';
            }
            if (a[i][j] == '#' && a[i][j - 1] == '#' && a[i + 1][j] == '#'){
                b[i][j] = '7';
            }
            //cout << b[i][j];
        }
        //cout << "\n";
    }

    int cnt = 0;
    for (ll i = 0; i < n; ++i){
        ll balance = 0;
        for (ll j = 0; j < n; ++j){
            if (b[i][j] == '|' || b[i][j] == 'J' || b[i][j] == 'L'){
                balance = (balance + 1) % 2;
                cnt++;
            }else if (b[i][j] != '.'){
                cnt++;
            }else if (b[i][j] == '.' && balance == 1){
                cnt++;
            }
        }
    }

    cout << cnt;


    /*
    for (ll i = 1; i < n - 1; ++i){
        ll balance = 0;
        char prev = '.';
        for (ll j = 0; j < n; ++j){
            if (a[i][j] == '#' && prev == '.'){
                balance = (balance + 1) % 2;
                prev = a[i][j];
            }else if (a[i][j] == '.' && balance == 1){

                prev = a[i][j];
                a[i][j] = '$';
            }

        }
    }

    ll ans = 0;
    for (ll i = 0; i < n; ++i){
        for (ll j = 0; j < n; ++j){
            //cout << a[i][j];
            if (a[i][j] != '.') ans ++;
        }
        //cout << "\n";
    }

    cout << ans << "\n";
    */
}

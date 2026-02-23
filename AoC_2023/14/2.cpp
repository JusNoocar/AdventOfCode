#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll n = 100;
ll cycle = 1000000000;
ll m;

vector<vector<vector<char>>> data;
vector<vector<char>> a;
vector<vector<char>> b;

void up(){
    for (ll j = 0; j < m; ++j){
        for (ll i = 0; i < n; ++i){
            if (a[i][j] == 'O'){
                ll nxt = i;
                while (nxt > 0 && a[nxt - 1][j] == '.'){
                    nxt--;
                }
                a[i][j] = '.';
                a[nxt][j] = 'O';
            }

        }
    }
}

void down(){
    for (ll j = 0; j < m; ++j){
        for (ll i = n - 1; i > -1; --i){
            if (a[i][j] == 'O'){
                ll nxt = i;
                while (nxt < n - 1 && a[nxt + 1][j] == '.'){
                    nxt++;
                }
                a[i][j] = '.';
                a[nxt][j] = 'O';
            }

        }
    }
}

void left(){
    for (ll i = 0; i < n; ++i){
        for (ll j = 0; j < m; ++j){
            if (a[i][j] == 'O'){
                ll nxt = j;
                while (nxt > 0 && a[i][nxt - 1] == '.'){
                    nxt--;
                }
                a[i][j] = '.';
                a[i][nxt] = 'O';
            }

        }
    }
}

void right(){
    for (ll i = 0; i < n; ++i){
        for (ll j = m - 1; j > -1; --j){
            if (a[i][j] == 'O'){
                ll nxt = j;
                while (nxt < m - 1 && a[i][nxt + 1] == '.'){
                    nxt++;
                }
                a[i][j] = '.';
                a[i][nxt] = 'O';
            }

        }
    }
}


int main(){
    freopen("test.txt", "r", stdin);
    string s0;
    cin >> s0;
    m = s0.size();
    a.resize(n);
    b.resize(n);
    for (ll i = 0; i < n; ++i){
        a[i].resize(m);
        b[i].resize(m);
    }
    for (ll j = 0; j < m; ++j){
        a[0][j] = s0[j];
        b[0][j] = a[0][j];
    }

    for (ll i = 1; i < n; ++i){
        for (ll j = 0; j < m; ++j){
            cin >> a[i][j];
            b[i][j] = a[i][j];
        }
    }

    int loop1, loop2;
    bool flag = true;
    for (ll i = 0; i < cycle; ++i){
        if (!flag) break;
        up();
        left();
        down();
        right();
        for (ll j = 0; j < i; ++j){
            if (data[j] == a){
                cout << "loop: " <<j << " " << i << "\n";
                loop1 = j;
                loop2 = i;
                flag = false;
                break;
            }
        }
        data.push_back(a);
    }

    ll idx = loop1 + (cycle - loop1 - 1) % (loop2 - loop1);
    a = data[idx];

    ll ans = 0;
    for (ll i = 0; i < n; ++i){
        for (ll j = 0; j < m; ++j){
            if (a[i][j] == 'O'){
                ans += (n - i);
            }
            cout << a[i][j] << " ";
        }
        cout << "\n";
    }
    cout << ans << "\n";

}

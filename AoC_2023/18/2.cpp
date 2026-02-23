#include <bits/stdc++.h>
#define ll long long
using namespace std;


ll get(string s){
    string alph = "0123456789abcdef";

    ll res = 0;
    ll pow = 1;
    ll n = s.size();
    for (ll i = n - 1; i > -1; --i){
        ll num = alph.find(s[i]);
        //ll num = s[i] - '0';
        res += num * pow;

        pow *= 16;
    }
    return res;

}
int main(){
    freopen("test.txt", "r", stdin);
    ll m = 738;
    vector<char> d(m);
    vector<ll> num(m);
    vector<string>color(m);


    for (ll q = 0; q < m; ++q){
        cin >> d[q] >> num[q] >> color[q];
        ll clen = color[q].size();
        color[q] = color[q].substr(1, clen - 2);
    }

    ll ans = 0;
    ll x0 = 0;
    ll y0 = 0;
    ll x1, y1;

    ll xsave, ysave;
    ll boundary = 0;
    for (ll q = 0; q < m; ++q){
        //cout << x1 << " " << y1 << "\n";
        //cout << color[q] << "\n";
        string line = color[q].substr(1, 5);
        char dr = color[q][6];
        //cout << line << " " << dr << "\n";
        ll dist = get(line);
        //cout << dist << "\n";
        boundary += dist;
        if (dr == '0'){
            y1 = y0 + dist;
        }else if (dr == '1'){
            x1 = x0 + dist;
        }else if (dr == '2'){
            y1 = y0 - dist;
        }else if (dr == '3'){
            x1 = x0 - dist;
        }

        ans += x0*y1 - x1*y0;
        if (q == 0){
            xsave = x1;
            ysave = y1;
        }
        x0 = x1; y0 = y1;
    }

    ans += x0*ysave - xsave*y0;

    ans = abs(ans) / 2 + boundary / 2 + 1;
    cout << ans << "\n";



}

#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("test.txt", "r", stdin);

    string s;
    cin >> s;
    s += ",";
    int ans = 0;
    int c = 0;
    for (int i = 0; i < s.size(); ++i){
        if (s[i] == ','){
            ans += c;
            c = 0;
        }else{
            c += s[i];
            c *= 17;
            c %= 256;
        }
    }

    cout << ans << "\n";
}

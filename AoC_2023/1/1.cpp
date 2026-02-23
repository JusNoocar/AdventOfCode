#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("test1.txt", "r", stdin);

    int ans = 0;
    for (int i = 0; i < 1000; ++i){
        string s;
        cin >> s;
        int first=0, last=0;
        //cout << s[0] - '0';
        for (int j = 0; j < s.size(); ++j){
            if (s[j] - '0' >=0 && s[j] - '0' <=9){
                first = s[j] - '0';
                break;
            }
        }
        int n = s.size();
        for (int j = n - 1; j > -1; --j){
            if (s[j] - '0' >=0 && s[j] - '0' <=9){
                last = s[j] - '0';
                break;
            }
        }
        ans += first*10 + last;
        cout << first << " " << last << "\n";
    }
    cout << ans << "\n";


}

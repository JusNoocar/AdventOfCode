#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
    freopen("test.txt", "r", stdin);

    int n = 140;
    vector<string> a(n + 2);
    for (int i = 0; i < n; ++i){
        string s;
        cin >> s;
        a[i + 1] = "." + s + ".";
    }
    int m = a[1].size();
    string first = "";
    for (int i = 0; i < m; ++i){
        first = first + ".";
    }
    a[0] = a[n + 1] = first;

    int ans = 0;

    for (int i = 1; i < n + 1; ++i){
        int num = 0;
        bool check = false;
        for (int j = 1; j < m - 1; ++j){
            if (a[i][j] - '0' >= 0 && a[i][j] - '0' <= 9){
                num = num * 10 + (a[i][j] - '0');


                for (int x = -1; x <= 1; ++x){
                    for (int y = -1; y <= 1; ++y){
                        if (x == 0 && y == 0) continue;
                        char el = a[i + x][j + y];
                        if ((el - '0' < 0 || el - '0' > 9) && (el !='.')){
                            check = true;
                        }
                    }
                }


            }else{
                if (check){
                    ans += num;
                }
                num = 0;
                check = false;

            }
        }
    }

    cout << ans << "\n";


}

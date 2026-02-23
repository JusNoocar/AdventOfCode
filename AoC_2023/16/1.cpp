#include <bits/stdc++.h>
using namespace std;

vector<vector<vector<bool>>> used;

void dfs(int x, int y, char d, vector<string> &a){
    //cout << x << " " << y << " " << d << "\n";
    if (x >= a.size() || y >= a[0].size()) return;
    int idx = 0;
    if (d == 'R') idx = 0;
    else if (d == 'L') idx = 1;
    else if (d == 'U') idx = 2;
    else if (d == 'D') idx = 3;

    if (a[x][y] == '.'){
        used[x][y][idx] = true;
        if (d == 'R') dfs(x, y + 1, d, a);
        else if (d == 'L') dfs(x, y - 1, d, a);
        else if (d == 'U') dfs(x - 1, y, d, a);
        else if (d == 'D') dfs(x + 1, y, d, a);
    }else if (!used[x][y][idx]){
        used[x][y][idx] = true;
        if (a[x][y] == '/'){
            if (d == 'R') dfs(x - 1, y, 'U', a);
            else if (d == 'L') dfs(x + 1, y, 'D', a);
            else if (d == 'U') dfs(x, y + 1, 'R', a);
            else if (d == 'D') dfs(x, y - 1, 'L', a);
        }else if (a[x][y] == '\\'){
            if (d == 'R') dfs(x + 1, y, 'D', a);
            else if (d == 'L') dfs(x - 1, y, 'U', a);
            else if (d == 'U') dfs(x, y - 1, 'L', a);
            else if (d == 'D') dfs(x, y + 1, 'R', a);
        }else if (a[x][y] == '-'){
            if (d == 'R') dfs(x, y + 1, d, a);
            else if (d == 'L') dfs(x, y - 1, d, a);
            else if (d == 'U' || d == 'D'){
                dfs(x, y - 1, 'L', a);
                dfs(x, y + 1, 'R', a);
            }
        }else if (a[x][y] == '|'){
            if (d == 'D') dfs(x + 1, y, d, a);
            else if (d == 'U') dfs(x - 1, y, d, a);
            else if (d == 'L' || d == 'R'){
                dfs(x + 1, y, 'D', a);
                dfs(x - 1, y, 'U', a);
            }
        }

    }

}

int main(){
    freopen("test.txt", "r", stdin);

    int n = 110;
    vector<string> a(n);
    for (int i = 0; i < n; ++i){
        cin >> a[i];
    }
    int m = a[0].size();
    used.resize(n);
    for (int i = 0; i < n; ++i){
        used[i].resize(m);
        for (int j = 0; j < m; ++j){
            used[i][j].assign(4, false);
        }
    }

    dfs(0, 0, 'R', a);
    int ans = 0;
    for (int i = 0; i < n; ++i){
        for (int j = 0; j < m; ++j){

            if (used[i][j][0] || used[i][j][1] || used[i][j][2] || used[i][j][3]){
                ans++;
                cout << "# ";
            }else{
                cout << ". ";
            }
        }
        cout << "\n";
    }
    cout << ans << "\n";

}

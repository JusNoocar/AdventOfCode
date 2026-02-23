#include <bits/stdc++.h>
using namespace std;

vector<string> a;
vector<vector<int>> g;
int dfs(int i, int j){
    if (a[i][j] == '<' && j > 0){
        if (a[i][j - 1] != '#') dfs(i, j - 1);
    }else if (a[i][j] == '>' && j + 1 < a[0].size()){
        if (a[i][j + 1] != '#') dfs(i, j + 1);
    }else if (a[i][j] == '^' && i > 0){
        if (a[i - 1][j] != '#') dfs(i - 1, j);
    }else if (a[i][j] == '' && i + 1 < a.size()){
        if (a[i + 1][j] != '#') dfs(i + 1, j);
    }else{
        if (j > 0 && a[i][j - 1] != '#') dfs(i, j - 1);
        if (j + 1 < a[0].size() && a[i][j + 1] != '#') dfs(i, j + 1);
        if (i > 0 && a[i - 1][j] != '#') dfs(i - 1, j);
        if (i + 1 < a.size() && a[i + 1][j] != '#') dfs(i + 1, j);
    }
}
int main(){
    freopen("test.txt", 'r', stdin);
    int n = 10;
    a.resize(n);
    for (int i = 0; i < n; ++i){
        cin >> a[i];
    }
    int m = a[0];

    g.resize(n * m);

    for (int i = 0; i < n; ++i){
        for (int j = 0; j < m; ++j){

        }
    }
    for (int j = 0; j < m; ++j){
        dfs(0, j);
    }

}

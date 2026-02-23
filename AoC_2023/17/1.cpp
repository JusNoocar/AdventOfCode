#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000000;
vector<vector<int>> a;
int n, m;
void dejkstra(int start_x, int start_y){
    vector<vector<int>> dist(n, vector<int>(m, INF));
    dist[start_x][start_y] = 0;
    //dist[start_x][start_y] = a[start_x][start_y];

    set<pair<int, pair<int, string>>> que;
    que.insert({0, {start_x * m + start_y, "EEE"}});
    while (!que.empty()){
        int w = (*que.begin()).first;
        int xy = (*que.begin()).second.first;
        int x = xy / m; int y = xy % m;
        cout << x << " " << y << " ";
        string p = "";
        p = ((*que.begin()).second).second;
        cout << p << "\n";
        que.erase(que.begin());

        if (x != 0 && p[2] != 'D' && p != "UUU"){
            if (dist[x - 1][y] > dist[x][y] + a[x - 1][y]){
                for (auto i = que.begin(); i != que.end(); ++i){
                    if ((*i).first == dist[x - 1][y] && (*i).second.first == (x - 1) * m + y){
                        que.erase(i);
                    }
                }

                dist[x - 1][y] = dist[x][y] + a[x - 1][y];
                string next_p = p.substr(1, 2) + "U";
                //cout << next_p << "\n";


                que.insert({dist[x - 1][y], {(x - 1) * m + y, next_p}});
            }
        }

        if (x != n - 1 && p[2] != 'U' && p != "DDD"){
            if (dist[x + 1][y] > dist[x][y] + a[x + 1][y]){
                for (auto i = que.begin(); i != que.end(); ++i){
                    if ((*i).first == dist[x + 1][y] && (*i).second.first == (x + 1) * m + y){
                        que.erase(i);
                    }
                }

                dist[x + 1][y] = dist[x][y] + a[x + 1][y];
                string next_p = p.substr(1, 2) + "D";
                que.insert({dist[x + 1][y], {(x + 1) * m + y, next_p}});
            }
        }

        if (y != 0 && p[2] != 'R' && p != "LLL"){
            if (dist[x][y - 1] > dist[x][y] + a[x][y - 1]){
                for (auto i = que.begin(); i != que.end(); ++i){
                    if ((*i).first == dist[x][y - 1] && (*i).second.first == x * m + y - 1){
                        que.erase(i);
                    }
                }

                dist[x][y - 1] = dist[x][y] + a[x][y - 1];
                string next_p = p.substr(1, 2) + "L";
                que.insert({dist[x][y - 1], {x * m + y - 1, next_p}});
            }
        }

        if (y != m - 1 && p[2] != 'L' && p != "RRR"){
            if (dist[x][y + 1] > dist[x][y] + a[x][y + 1]){
                for (auto i = que.begin(); i != que.end(); ++i){
                    if ((*i).first == dist[x][y + 1] && (*i).second.first == x * m + y + 1){
                        que.erase(i);
                    }
                }

                dist[x][y + 1] = dist[x][y] + a[x][y + 1];
                string next_p = p.substr(1, 2) + "R";
                que.insert({dist[x][y + 1], {x * m + y + 1, next_p}});
            }
        }


    }

    cout << dist[n - 1][m - 1] << "\n";
}


int main(){
    freopen("test.txt", "r", stdin);
    n = 13;
    a.resize(n);
    string s;
    cin >> s;
    m = s.size();
    a[0].resize(m);
    for (int j = 0; j < m; ++j){
        a[0][j] = s[j] - '0';
    }

    for (int i = 1; i < n; ++i){
        a[i].resize(m);
        for (int j = 0; j < m; ++j){
            char x;
            cin >> x;
            a[i][j] = x - '0';
        }
    }

    cout << "ok";
    dejkstra(0, 0);

}

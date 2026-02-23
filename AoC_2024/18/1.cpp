#include <iostream>
#include <vector>
#include <set>

const int n = 71;
const int INF = 1000000000;
int Dijkstra(int start, int end, std::vector<std::set<std::pair<int, int>>>& g) {

  std::vector<int> dist(n * n, INF);
  dist[start] = 0;

  std::set<std::pair<int, int>> que;
  que.insert({0, start});

  while (!que.empty()) {
    int v = que.begin() -> second;
    que.erase(que.begin());
    for (auto [w, u] : g[v]) {
      if (dist[v] + w < dist[u]) {
        que.erase({dist[u], u});
        dist[u] = dist[v] + w;
        que.insert({dist[u], u});
      }
    }
  }
  int ans = INF;
  return dist[end];
}


int main() {
  freopen("random_test.txt", "r", stdin);

  std::vector<std::set<std::pair<int, int>>> g(n * n);

  int start = 0;
  std::vector<int> ends;
  std::vector<std::vector<char>> maze(n, std::vector<char>(n, '.'));
  int end = n * n - 1;

  int m = 1024;
  for (int i = 0; i < m; ++i) {
    int posi, posj;
    char comma;
    std::cin >> posi >> comma >> posj;
    maze[posi][posj] = '#';
  }

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
        if (maze[i][j] == '#') {
          continue;
        }
        int idx = i * n + j;
        if (i != 0 && maze[i - 1][j] != '#') {
            int idx1 = (i - 1) * n + j;
            g[idx].insert({1, idx1});
        }
        if (i != n - 1 && maze[i + 1][j] != '#') {
            int idx1 = (i + 1) * n + j;
            g[idx].insert({1, idx1});
        }
        if (j != 0 && maze[i][j - 1] != '#') {
            int idx1 = i * n + j - 1;
            g[idx].insert({1, idx1});
        }
        if (j != n - 1 && maze[i][j + 1] != '#') {
            int idx1 = i * n + j + 1;
            g[idx].insert({1, idx1});
        }
    }
  }
  std::cout << start << " " << end << "\n";

  std::cout << Dijkstra(start, end, g);

  for (int q = 1024; q < 3450; ++q) {
    int i, j;
    char comma;
    std::cin >> i >> comma >> j;
    maze[i][j] = '#';
    int idx = i * n + j;
    if (i != 0 && maze[i - 1][j] != '#') {
      int idx1 = (i - 1) * n + j;
      g[idx].erase({1, idx1});
    }
    if (i != n - 1 && maze[i + 1][j] != '#') {
      int idx1 = (i + 1) * n + j;
      g[idx].erase({1, idx1});
    }
    if (j != 0 && maze[i][j - 1] != '#') {
      int idx1 = i * n + j - 1;
      g[idx].erase({1, idx1});
    }
    if (j != n - 1 && maze[i][j + 1] != '#') {
      int idx1 = i * n + j + 1;
      g[idx].erase({1, idx1});
    }
    if (Dijkstra(start, end, g) == INF) {
      std::cout << i << " " << j;
    }
  }
}

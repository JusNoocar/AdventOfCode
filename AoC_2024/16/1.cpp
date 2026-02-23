#include <iostream>
#include <vector>
#include <set>

const int n = 141;
const int INF = 1000000000;
int Dijkstra(int start, std::vector<int>& ends, std::vector<std::vector<std::pair<int, int>>>& g) {

  std::vector<int> dist(n * n * 4, INF);
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
  for (int end : ends) {
    ans = std::min(ans, dist[end]);
  }
  return ans;
}


int main() {
  freopen("test.txt", "r", stdin);

  std::vector<std::vector<std::pair<int, int>>> g(n * n * 4);

  int start;
  std::vector<int> ends;
  std::vector<std::vector<char>> maze(n, std::vector<char>(n));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
        std::cin >> maze[i][j];
        if (maze[i][j] == 'S') {
          start = (i * n + j) * 4 + 3;
        } else if (maze[i][j] == 'E') {
          for (int q = 0; q < 4; ++q) {
            ends.push_back((i * n + j) * 4 + q);
          }
        }
    }
  }

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
        if (maze[i][j] == '#') {
          continue;
        }
        int idx = (i * n + j) * 4;
        if (i != 0 && maze[i - 1][j] != '#') {
            int idx1 = ((i - 1) * n + j) * 4;
            g[idx].push_back({1, idx1 + 2});
        }
        if (i != n - 1 && maze[i + 1][j] != '#') {
            int idx1 = ((i + 1) * n + j) * 4;
            g[idx + 2].push_back({1, idx1});
        }
        if (j != 0 && maze[i][j - 1] != '#') {
            int idx1 = (i * n + j - 1) * 4;
            g[idx + 3].push_back({1, idx1 + 1});
        }
        if (j != n - 1 && maze[i][j + 1] != '#') {
            int idx1 = (i * n + j + 1) * 4;
            g[idx + 1].push_back({1, idx1 + 3});
        }
        g[idx].push_back({0, idx + 2});
        g[idx + 2].push_back({0, idx});
        g[idx + 1].push_back({0, idx + 3});
        g[idx + 3].push_back({0, idx + 1});

        g[idx].push_back({1000, idx + 1});
        g[idx].push_back({1000, idx + 3});

        g[idx + 1].push_back({1000, idx});
        g[idx + 1].push_back({1000, idx + 2});

        g[idx + 2].push_back({1000, idx + 1});
        g[idx + 2].push_back({1000, idx + 3});

        g[idx + 3].push_back({1000, idx});
        g[idx + 3].push_back({1000, idx + 2});
    }
  }
  std::cout << start << "\n";
  for (int i = 0; i < 4; ++i) {
      std::cout << ends[i] << " ";
  }

  std::cout << Dijkstra(start, ends, g);
}

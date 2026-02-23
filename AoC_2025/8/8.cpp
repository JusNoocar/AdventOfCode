#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <math.h>
#include <cstdio>
#include <string>
#include <cstring>
#include <sstream>

struct Pt {
    long long x, y, z;
    Pt() {}
    Pt(long long x, long long y, long long z) : x(x), y(y), z(z) {}

};

std::vector<int> p;
std::vector<int> sz;

int get(int u) {
    if (p[u] == u) {
        return u;
    }
    return p[u] = get(p[u]);
}
bool merge(int u, int v) {
    int rootu = get(u);
    int rootv = get(v);
    if (rootu == rootv) return false;

    if (sz[rootu] >= sz[rootv]) {
        sz[rootu] += sz[rootv];
        p[rootv] = rootu;
    } else {
        sz[rootv] += sz[rootu];
        p[rootu] = rootv;
    }

    return true;
}

long long dist(Pt a, Pt b) {
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y) + (a.z - b.z) * (a.z - b.z);
}

int main() {
    freopen("8.txt", "r", stdin);

    int n;
    std::cin >> n;
    std::vector<Pt> data(n);
    p.resize(n);
    for (int i = 0; i < n; ++i) {
        p[i] = i;
    }
    sz.assign(n, 1);

    for (int i = 0; i < n; ++i) {
        std::string s;
        std::cin >> s;
        std::string str;
        std::stringstream ss(s); 
        getline(ss, str, ',');
        long long x = std::stoi(str);
        getline(ss, str, ',');
        long long y = std::stoi(str);
        getline(ss, str, ',');
        long long z = std::stoi(str);
        std::cout << x <<" " << y << " " << z << "\n";
        // int x, y, z;
        // std::cin >> x >> y >> z;
        data[i] = Pt(x, y, z);
    }

    std::vector<std::pair<int, int>> prs;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            prs.push_back({i, j});
        }
    }
    std::cout << "ok\n";

    std::sort(prs.begin(), prs.end(), [data](std::pair<int, int> a, std::pair<int, int> b) {
        return dist(data[a.first], data[a.second]) < dist(data[b.first], data[b.second]);
    });
    std::cout << "ok\n";

    int i = 0;
    long long last = 0;
    while (i < prs.size()) {
        int a = prs[i].first;
        int b = prs[i].second;
        if (merge(a, b)) {
            last = data[a].x * data[b].x;
        }
        ++i;
    }
    std::cout << "ok\n";

    std::set<int> used;
    std::vector<int> res;

    for (int i = 0; i < n; ++i) {
        int root = get(i);
        if (used.find(root) == used.end()) {
            res.push_back(sz[root]);
            used.insert(root);
        }
    }
    std::sort(res.begin(), res.end());
    int k = res.size();
    for (int x : res) {
        std::cout << x << " ";
    }
    std::cout << "\n";
    long long ans = res[k - 1] * res[k - 2] * res[k - 3];
    std::cout << ans << "\n";
    std::cout << last;


}

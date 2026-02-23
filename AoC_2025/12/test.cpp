#include <iostream>

using ll = long long;
bool mat[506][506];


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);

    ll n, m, k;
    std::cin >> n >> m >> k;

    ll m_min = ( n * (k + 1) + 1) / 2;
    if (k == 0) m_min = n - 1;
    ll m_max = (k + 1) + (n - 1) * (n - 2) / 2;


    if (k + 1 >= n || m < m_min || m > m_max) {
        std::cout << "NO" << std::endl;
    } else {
        std::cout << "YES" << std::endl;
        int count = 0;

        for (int i = 1; i <= k + 1; ++i) {
            std::cout << i << " " << n << "\n";
            mat[i][n] = mat[n][i] = true;
            ++count;
        }

        for (int i = 1; i < n - 1; ++i) {
            if (!mat[i][i + 1]) {
                std::cout << i << " " << i + 1 << "\n";
                mat[i][i + 1] = mat[i + 1][i] = true;
                ++count;
            }
        }
        
        if (k > 0 && n > 2 && !mat[n - 1][1]) {
            std::cout << n - 1 << " " << 1 << "\n";
            mat[n - 1][1] = mat[1][n - 1] = true;
            ++count;
        }

        for (int i = 1; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (count < m && !mat[i][j]) {
                    std::cout << i << " " << j << "\n";
                    mat[i][j] = mat[j][i] = true;
                    ++count;
                }
            }
        }
    }


}

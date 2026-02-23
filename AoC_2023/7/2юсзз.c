#include <bits/stdc++.h>
using namespace std;


struct pt{
    string s;
    vector<int> v;
    int rank;
    int bid;
};
int main(){
    freopen("test.txt", "r", stdin);

    int n = 1000;
    vector<pt> a(n);

    vector<char> cards = {'2','3','4','5','6','7','8','9','T','J','Q','K','A'};
    for (int i = 0; i < n; ++i){
        cin >> a[i].s >> a[i].bid;

        vector<pair<int, int>> data;
        for (int j = 0; j < cards.size(); ++j){
            char type = cards[j];
            int cnt = count(a[i].s.begin(), a[i].s.end(), type);
            data.push_back({cnt, j});
        }

        sort(data.rbegin(), data.rend());

        int r;

        if (data[0].first == 5) r = 6;
        else if (data[0].first == 4) r = 5;
        else if (data[0].first == 3 && data[1].first == 2) r = 4;
        else if (data[0].first == 3) r = 3;
        else if (data[0].first == 2 && data[1].first == 2) r = 2;
        else if (data[0].first == 2) r = 1;
        else r = 0;

        a[i].rank = r;

        vector<int> add(5);
        for (int j = 0; j < 5; ++j){
            int pos = find(cards.begin(), cards.end(), a[i].s[j]) - cards.begin();
            add[j] = pos;
        }
        a[i].v = add;

    }

    sort(a.begin(), a.end(), [](pt x, pt y){
         if (x.rank == y.rank){
            if (x.s == y.s){
                return x.bid < y.bid;
            }
            return x.v < y.v;
         }
         return x.rank < y.rank;
    });

    int ans = 0;
    for (int i = 0; i < a.size(); ++i){
        //cout << a[i].s << " " << a[i].bid << "\n";
        ans += a[i].bid * (i + 1);
    }

    cout << ans << "\n";

}

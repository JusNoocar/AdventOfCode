#include <bits/stdc++.h>
using namespace std;

struct pt{

};
int main(){
    freopen("test.txt", "r", stdin);

    string s;
    cin >> s;
    s += ",";
    int ans = 0;
    string c = "";

    map<int, map<string, pair<int, int>>> hashmap;
    for (int i = 0; i < s.size(); ++i){
        if (s[i] == ','){
            string name;
            int label = 0;
            int num = 0;
            bool f = true;
            char type = '=';
            for (int j = 0; j < c.size(); ++j){
                if (c[j] == '=' || c[j] == '-'){
                    type = c[j];
                    f = false;
                }else if (f){
                    name = name + c[j];
                    label += c[j];
                    label *= 17;
                    label %= 256;
                }else{
                    num += (c[j] - '0');
                }

            }
            cout << name << " " << label << " " << num << "\n";
            if (type == '-'){
                hashmap[label].erase(name);
            }else{
                if (hashmap[label].count(name)){
                    hashmap[label][name].first = num;
                }else{
                    hashmap[label][name] = {num, i};
                }

            }

            c = "";
        }else{
            c = c + s[i];
        }
    }


    for (auto [label, val] : hashmap){
        vector<pair<int,int>> to_sort;
        for (auto [name, v] : val){
            auto [num, idx] = v;
            to_sort.push_back({idx, num});


        }
        sort(to_sort.begin(), to_sort.end());

        for (int j = 0; j < to_sort.size(); ++j){
            ans += (label + 1) * (j + 1) * to_sort[j].second;
        }
    }
    cout << ans << "\n";
}


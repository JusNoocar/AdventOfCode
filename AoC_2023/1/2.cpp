#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("test1.txt", "r", stdin);

    vector<string> nums = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int ans = 0;
    for (int i = 0; i < 1000; ++i){
        string s;
        cin >> s;
        int first=0, last=0;
        int n = s.size();

        int idxfirst = n-1, idxlast = 0;
        //cout << s[0] - '0';
        for (int j = 0; j < n; ++j){
            if (s[j] - '0' >=0 && s[j] - '0' <=9){
                first = s[j] - '0';
                idxfirst = j;
                break;
            }
        }

        for (int j = n - 1; j > -1; --j){
            if (s[j] - '0' >=0 && s[j] - '0' <=9){
                last = s[j] - '0';
                idxlast = j;
                break;
            }
        }

        for (int j = 0; j < nums.size(); ++j){
            string word = nums[j];
            if (s.find(word) != std::string::npos){
                size_t idx = s.find(word);
                size_t idx1 = s.rfind(word);
                //cout << idx << "\n";
                if (idx <= idxfirst){
                    idxfirst = idx;
                    first = j + 1;
                }

                if (idxlast <= idx1){
                    idxlast = idx1;
                    last = j + 1;
                }
            }

        }
        ans += first*10 + last;
        //cout << ans << "\n";
    }
    cout << ans << "\n";


}

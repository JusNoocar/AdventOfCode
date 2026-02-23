#include <iostream>
#include <vector>
#define ll long long
using namespace std;
const ll INF = 1000000000;
int main(){

    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i = 0; i < n; ++i){
        cin >> a[i];
    }

    vector<ll> mx(n + 1);
    mx[0] = 0;
    ll mn = 0;
    ll max_center = -INF;

    ll sum = 0;
    for (ll i = 0; i < n; ++i){

        sum += a[i];
        mn = min(mn, sum);
        max_center = max(max_center, sum - mn);
        mx[i + 1] = max(mx[i], sum);
    }

    //cout << max_center << "\n";

    ll max_borders = -INF;
    sum = 0;
    for (ll i = n - 1; i > 0; --i){
        sum += a[i];

        max_borders = max(max_borders, sum + mx[i]);
    }

    //cout << max_borders<< "\n";

    cout << max(max_center, max_borders);

}

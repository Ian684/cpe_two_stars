
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test;
    cin >> test;

    while (test--) {
        int m, n;
        cin >> m >> n;

        vector<int> col1(m), row1(n);
        int ans1 = 0;

        for (int i = 0; i < m; i++) {
            cin >> col1[i];
            ans1 += col1[i];
        }

        for (int i = 0; i < n; i++) {
            cin >> row1[i];
        }

        for (int r : row1) {
            int i = 0;
            int temp = r;

            sort(col1.begin(), col1.end(), greater<int>());

            while (temp > 0 && i < m) {
                if (col1[i] > 0) {
                    col1[i]--;
                    temp--;
                }
                i++;
            }

            ans1 += temp;
        }

        cout << ans1 << '\n';
    }

    return 0;
}


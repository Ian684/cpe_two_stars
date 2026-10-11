
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test;
    cin >> test;

    for (int ca = 1; ca <= test; ca++) {
        int n, m, k;
        cin >> n >> m >> k;

        cout << "Case " << ca << ": ";

        if (k <= 3) {
            cout << k << '\n';
            continue;
        }

        if (k > m) {
            cout << "sequence nai\n";
            continue;
        }

        int ans = n + 1;
        int cnt[101] = {};
        int now = 0;
        deque<int> x;

        int a = 0, b = 0, c = 0;

        for (int right = 0; right < n; right++) {
            int temp;

            if (right <= 2)
                temp = right + 1;
            else
                temp = (a + b + c) % m + 1;

            if (temp <= k) {
                if (cnt[temp] == 0)
                    now++;
                cnt[temp]++;
            }

            x.push_back(temp);

            while (now == k) {
                ans = min(ans, (int)x.size());

                int l = x.front();
                x.pop_front();

                if (l <= k) {
                    cnt[l]--;
                    if (cnt[l] == 0)
                        now--;
                }
            }

            a = b;
            b = c;
            c = temp;

            if (ans == k)
                break;
        }

        if (ans == n + 1)
            cout << "sequence nai\n";
        else
            cout << ans << '\n';
    }

    return 0;
}


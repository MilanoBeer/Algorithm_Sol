#include <bits/stdc++.h>
using namespace std;


int dp[300][300];
bool mineral[300][300];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr), cout.tie(nullptr);

	int n, m;
	cin >> n >> m;

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			cin >> mineral[i][j];

	dp[0][0] = mineral[0][0];

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (i != 0)
				dp[i][j] = max(dp[i][j], dp[i - 1][j] + mineral[i][j]);
			if (j!=0)
				dp[i][j] = max(dp[i][j], dp[i][j - 1] + mineral[i][j]);
		}
	}
	cout << dp[n - 1][m - 1] << '\n';

	return 0;
}
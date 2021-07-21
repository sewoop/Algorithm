#include <bits/stdc++.h>

using namespace std;

int freq[26];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;

    // for (char a = 'a'; a <= 'z'; a++) {
    //     int cnt = 0;
    //     for (auto c : s)
    //         if (a == c) cnt++;
    //     cout << cnt << ' ';
    // }

    for (auto c: s)
        freq[c - 'a']++;
    for (int i = 0; i < 26; i++)
        cout << freq[i] << ' ';
}
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<pair<int, char>> stack;
    string batch;

    cin >> batch;

    int answer = 0, count = 0;
    int index;
    
    for (int i = 0; i < batch.size(); i++) {
        if (batch[i] == '(') {
            stack.push(make_pair(i, batch[i]));
            count += 1;
        } else if (stack.top().second == '(' && batch[i] == ')') {
            index = stack.top().first;
            stack.pop();
            if (index + 1 == i) {
                count -= 1;
                answer += count;
            } else {
                answer += 1;
                count -= 1;
            }
        }
    }

    cout << answer;

}
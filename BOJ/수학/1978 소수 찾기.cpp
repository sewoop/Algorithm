#include <iostream>
#include <fstream>

using namespace std;

int cnt = 0;
bool sosu(int a){
    if(a <= 1)
        return false;

    for (size_t i = 2; i < a; i++)
    {
        if(a%i==0)
            return false;
    }
    return true;
}

/*
    소수 : 1과 자신밖에 없는 것

    2~13까지 계속 나누기

*/

int main(){
    // ifstream read("input.inp");

    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);

    int n,a;

    cin >> n;

    for (size_t i = 0; i < n; i++)
    {
        cin >> a;
        if(sosu(a)){
            cnt++;
        }
    }

    cout << cnt << endl;
    
    return 0;
}
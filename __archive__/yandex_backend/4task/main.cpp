// #include <iostream>
// #include <cmath>
// #include <vector>

// using namespace std;

// int main(){

//     return 0;
// }


#include <bits/stdc++.h>
using namespace std;
using ushort = unsigned short;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, d;
    cin >> n >> m >> d;
    vector<string> grid(n);
    for(int i = 0; i < n; i++){
        cin >> grid[i];
    }
    vector<ushort> dist(n * m, (ushort)d);

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            char c = grid[i][j];
            if (c == 'X' || c == 'x') {
                dist[i*m + j] = 0;
            }
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            ushort cur = dist[i*m + j];
            if(cur == 0) continue;
            if(i > 0)
                cur = min<ushort>(cur, dist[(i-1)*m + j] + 1);
            if(j > 0)
                cur = min<ushort>(cur, dist[i*m + (j-1)] + 1);
            dist[i*m + j] = cur;
        }
    }

    for(int i = n-1; i >= 0; i--){
        for(int j = m-1; j >= 0; j--){
            ushort cur = dist[i*m + j];
            if(cur == 0) continue;
            if(i + 1 < n)
                cur = min<ushort>(cur, dist[(i+1)*m + j] + 1);
            if(j + 1 < m)
                cur = min<ushort>(cur, dist[i*m + (j+1)] + 1);
            dist[i*m + j] = cur;
        }
    }

    vector<ushort> prev(m, 0), curr(m, 0);
    int best = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(dist[i*m + j] >= d){
                if(i == 0 || j == 0){
                    curr[j] = 1;
                } else {
                    curr[j] = 1 + min<ushort>({
                        prev[j],
                        curr[j-1],
                        prev[j-1]
                    });
                }
                best = max(best, (int)curr[j]);
            } else {
                curr[j] = 0;
            }
        }
        swap(prev, curr);
    }

    cout << best << "\n";
    return 0;
}
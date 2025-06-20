#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int N;
    ll L, S;
    cin >> N >> L >> S;

    unordered_map<int, pair<ll,ll>> last_report;
    vector<string> output;

    for (int i = 0; i < N; i++) {
        string type;
        cin >> type;
        if (type == "TAXI") {
            ll t; int id; ll p;
            cin >> t >> id >> p;
            last_report[id] = {t, p};
        }
        else if (type == "ORDER") {
            ll T, order_time;
            int order_id;
            ll A;
            cin >> T >> order_id >> A >> order_time;

            vector<int> ok;
            ll max_travel = S * order_time;

            for (auto &it : last_report) {
                int id = it.first;
                ll t_i = it.second.first;
                ll p_i = it.second.second;
                ll delta_t = T - t_i;
                ll D = S * delta_t;
                ll worst;
                if((p_i%L) <= (A%L)){
                    if(D>((A-p_i)%L)){
                        worst=L-1;
                    }
                    else{
                        worst = (A-p_i)%L;
                    }
                }
                else{
                    if(D>((A-p_i+L)%L)){
                        worst=L-1;
                    }
                    else{
                        worst = (A-p_i+L)%L;
                    }
                }
                if (worst <= max_travel) {
                    ok.push_back(id);
                    if (ok.size() == 5) break;
                }
            }

            if (ok.empty()) {
                output.push_back("-1");
            } else {
                sort(ok.begin(), ok.end());
                string line;
                for (int x : ok) {
                    if (!line.empty()) line += ' ';
                    line += to_string(x);
                }
                output.push_back(line);
            }
        }
    }

    for (auto &line : output) {
        cout << line << "\n";
    }

    return 0;
}
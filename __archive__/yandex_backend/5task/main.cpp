#include <bits/stdc++.h>
using namespace std;

// Trie node for digit‐string codes
struct Node {
    int word_id;                // index of word ending here, or -1
    array<Node*, 10> nxt;       // children for digits '0'..'9'
    Node() : word_id(-1) { nxt.fill(nullptr); }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    int m = s.size();

    int n;
    cin >> n;
    vector<string> dict(n);
    for(int i = 0; i < n; i++){
        cin >> dict[i];
    }

    // Build mapping letter → code (T9 style with repeats)
    array<string, 26> code;
    auto fill = [&](string letters, char digit){
        for(int i = 0; i < (int)letters.size(); i++){
            code[ letters[i] - 'A' ] = string(i+1, digit);
        }
    };
    fill("ABC", '2');
    fill("DEF", '3');
    fill("GHI", '4');
    fill("JKL", '5');
    fill("MNO", '6');
    fill("PQRS",'7');
    fill("TUV", '8');
    fill("WXYZ",'9');

    // Build a trie of the numeric codes of dictionary words
    Node *root = new Node();
    for(int i = 0; i < n; i++){
        // convert dict[i] to its digit‐string code
        string cstr;
        cstr.reserve(dict[i].size() * 3);
        for(char ch : dict[i]){
            // uppercase guaranteed
            cstr += code[ch - 'A'];
        }
        // insert into trie
        Node *cur = root;
        for(char d : cstr){
            int di = d - '0';
            if(!cur->nxt[di])
                cur->nxt[di] = new Node();
            cur = cur->nxt[di];
        }
        // mark word ending (keep first if duplicates)
        if(cur->word_id == -1)
            cur->word_id = i;
    }

    // DP over positions in s: dp[i]=true if prefix s[0..i-1] is decodable
    vector<char> dp(m+1, 0);
    dp[0] = 1;
    // back pointers: from position j we came from i using word_id
    vector<pair<int,int>> back(m+1, {-1,-1});

    for(int i = 0; i < m; i++){
        if(!dp[i]) continue;
        Node *cur = root;
        // try to extend from i forward, following trie
        for(int j = i; j < m; j++){
            int di = s[j] - '0';
            if(!cur->nxt[di]) break;
            cur = cur->nxt[di];
            if(cur->word_id != -1 && !dp[j+1]){
                dp[j+1] = 1;
                back[j+1] = {i, cur->word_id};
                // early exit if we reached end
                if(j+1 == m) break;
            }
        }
    }

    // reconstruct solution (guaranteed at least one exists)
    vector<string> answer;
    int pos = m;
    while(pos > 0){
        auto [prev, wid] = back[pos];
        answer.push_back(dict[wid]);
        pos = prev;
    }
    reverse(answer.begin(), answer.end());

    // output with spaces
    for(int i = 0; i < (int)answer.size(); i++){
        if(i) cout << ' ';
        cout << answer[i];
    }
    cout << "\n";

    return 0;
}
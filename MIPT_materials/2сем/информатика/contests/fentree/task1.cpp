#include <iostream>
using namespace std;
#define len 100000
class fentree{
    public:
    int tree[len + 1];
    int minn[len + 1];
    int maxx[len + 1];
    void maketree(){
        for(int i = 0; i<=len; i++){
            tree[i] = ( i*i % 12345) + ( i*i*i % 23456);
        }
        return;
    }
    void updatetree(int el, int val){
        tree[el] = val;
        return;
    }
    void getvalue(int l, int r){
        int mi = 100001;
        int ma = -10000;
        for (int i = l; i <= r; i++){
            mi = min(mi, tree[i]);
            ma = max(ma, tree[i]);
        }
        cout<<ma - mi<<endl;
        return;
    }
};
int main(){
    fentree tr;
    tr.maketree();
    int n;
    cin>>n;
    int a, b;
    for(int i = 0; i<n; i++){
        cin>>a>>b;
        if (a>0){
            tr.getvalue(a, b);
        }
        else{
            tr.updatetree(-1*a, b);
        }
    }
}




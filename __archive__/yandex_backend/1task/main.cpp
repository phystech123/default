#include<iostream>
#include<string>
#include<cmath>

using namespace std;

int main(){
    int n,m,x,y,number=0;
    cin >> n >> m >> x >> y;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    int** home = new int*[n];
    for(int i = 0; i < n; i++){
        home[i] = new int[m];
        for(int j = 0; j < m; j++){
            home[i][j]=0;
        }
    }

    for(int i = 0; i < n; i++){
        for(int i_x = 0; i_x < x; i_x++){
            string temp;
            getline(cin, temp);
            for(int j = 0; j < m; j++){
                for(int j_y = 0; j_y < y; j_y++){
                    if (temp[j*y+j_y] == 'X') {
                        home[i][j]++;
                    }
                }
                if((i_x==x-1) && (home[i][j] >= ceil(x*y/2.))){   
                    number+=1;
                }
            }
        }
    }
    for(int i = 0; i < n; i++){
        delete[] home[i];
    }
    cout<<number;
    delete[] home;
    return 0;
}
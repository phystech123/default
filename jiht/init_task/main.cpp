#include <algorithm>
#include <array>
#include<iostream>
#include<cmath>
#include <iterator>
#include<vector>
#include<random>
#include<fstream>
#include<string>
// #include<nlohmann/json>
#include<omp.h>

using namespace std;

// to generate random coordinates and speeds
std::random_device r_;
std::default_random_engine e1(r_());
// std::uniform_real_distribution<> dist1();
// std::uniform_real_distribution<> dist2(-1, 1);
// std::uniform_int_distribution<int> dist3 (0, 1);

class coord{
    public:

    double a=0, b=0, c=0;
    coord(double x, double y, double z):a{x}, b{y}, c{z}{}
    coord(const coord& sec){*this=sec;}
    coord& operator=(const coord &sec){
        this->a = sec.a;
        this->b = sec.b;
        this->c = sec.c;
        return *this;
    }
    ~coord(){}
    coord operator+(coord sec){
        return coord(this->a+sec.a, this->b+sec.b, this->c+sec.c);
    }
    coord operator-(coord sec){
        return coord(this->a-sec.a, this->b-sec.b, this->c-sec.c);
    }
    double operator*(coord sec){
        return this->a*sec.a + this->b*sec.b + this->c*sec.c;
    }
};
coord operator*(double t, coord X){
    return coord(X.a*t, X.b*t, X.c*t);
}
coord operator*(coord X, double t){
    return coord(X.a*t, X.b*t, X.c*t);
}
coord operator/(coord X, double t){
    return coord(X.a/t, X.b/t, X.c/t);
}





class atom{
    public:
    vector<coord> coor;
    vector<coord> speed;
    double M=0;
    double R=0;
    atom(double M, double R, double a, double b, double c,
            double d, double e, double f):M{M}, R{R}{
            coor.push_back(coord(a, b, c));
            speed.push_back(coord(d, e, f));
        }
    atom(const atom& at){*this=at;}
    atom& operator=(const atom &sec){
        this->coor = sec.coor;
        this->speed = sec.speed;
        this->M = sec.M;
        this->R = sec.R;
        return *this;
    }
    ~atom(){}
};



class solver{
    public:

    double LENGTH = 1; //length of simulation cell
    double t = 1e-3; //step value
    int rep = 1e5; //number of repetitions
    int N = 1e1; //number of atoms
    //parameters of L-D potential
    double eps = 0.5;
    double sigm = 0.1;

    vector<atom> gas; //array of atoms
    
    solver(){
        double M=1, R=0.01;
        std::uniform_real_distribution<> d1(R, LENGTH-R);
        std::uniform_real_distribution<> d2(-0.1, 0.1);
        for(int i = 0; i < N; i++){
            gas.push_back(atom(M, R, d1(e1),d1(e1),d1(e1),d2(e1),d2(e1),d2(e1)));
        }
    };

    solver(int N, vector<atom> &g):N{N}{gas=g;}
    solver(int N, vector<atom> &&g):N{N}{gas=g;}
    solver(solver&)=delete;
    solver(solver&&)=delete;
    solver& operator=(solver &sec)=delete;
    solver& operator=(solver &&sec)=delete;
    ~solver(){}

    double mod(double x, double l){
        double t = fmod(x, l);
        return (t < 0) ? t + l : t;
    }
    coord cond_check(const coord& c, double R){
        return coord(this->mod(c.a-R, LENGTH-2*R) + R, this->mod(c.b-R, LENGTH-2*R) + R, this->mod(c.c-R, LENGTH-2*R) + R);
    }

    void solve_verle(){
        // initial conditions
        for(atom &at: gas){
            at.coor.push_back(at.coor[0]+at.speed[0]*t);
        }

        for(int i = 2; i < rep; i++){
            for(int j = 0; j < N; j++){
                atom &obj = gas[j];
                coord A = coord(0,0,0);
                for(int k = 0; k < N; k++){
                    if(k==j) continue;
                    double r = (obj.coor[i-1]-gas[k].coor[i-1])*(obj.coor[i-1]-gas[k].coor[i-1]);
                    r = std::max(r, 1e-10);
                    A = A + (24*eps/obj.M)*(2*pow(sigm, 12)/pow(r,7) - pow(sigm, 6)/pow(r, 4))*(obj.coor[i-1]-gas[k].coor[i-1]);
                }
                obj.coor.push_back(cond_check(2*obj.coor[i-1] - obj.coor[i-2] + A*pow(t,2), obj.R));
            }
        }
    }
    
    void solve_R_K(){
        for(int i = 1; i < rep; i++){
            for(int j = 0; j < N; j++){
                atom &obj = gas[j];

                coord A = coord(0,0,0);
                for(int k = 0; k < N; k++){
                    if(k==j) continue;
                    double r = (obj.coor[i-1]-gas[k].coor[i-1])*(obj.coor[i-1]-gas[k].coor[i-1]);
                    r = std::max(r, 1e-10);
                    A = A + (24*eps/obj.M)*(2*pow(sigm, 12)/pow(r,7) - pow(sigm, 6)/pow(r, 4))*(obj.coor[i-1]-gas[k].coor[i-1]);
                }
                coord k1_x = obj.speed[i-1];
                coord k1_v = A;

                A=coord(0,0,0);
                for(int k = 0; k < N; k++){
                    if(k==j) continue;
                    double r = ((obj.coor[i-1] + k1_x*t/2)-gas[k].coor[i-1])*((obj.coor[i-1]+ k1_x*t/2)-gas[k].coor[i-1]);
                    r = std::max(r, 1e-10);
                    A = A + (24*eps/obj.M)*(2*pow(sigm, 12)/pow(r,7) - pow(sigm, 6)/pow(r, 4))*((obj.coor[i-1] + k1_x*t/2)-gas[k].coor[i-1]);
                }
                coord k2_x = obj.speed[i-1]+k1_v*t/2;
                coord k2_v = A;

                A=coord(0,0,0);
                for(int k = 0; k < N; k++){
                    if(k==j) continue;
                    double r = ((obj.coor[i-1] + k2_x*t/2)-gas[k].coor[i-1])*((obj.coor[i-1]+ k2_x*t/2)-gas[k].coor[i-1]);
                    r = std::max(r, 1e-10);
                    A = A + (24*eps/obj.M)*(2*pow(sigm, 12)/pow(r,7) - pow(sigm, 6)/pow(r, 4))*((obj.coor[i-1] + k2_x*t/2)-gas[k].coor[i-1]);
                }
                coord k3_x = obj.speed[i-1]+k2_v*t/2;
                coord k3_v = A;


                A=coord(0,0,0);
                for(int k = 0; k < N; k++){
                    if(k==j) continue;
                    double r = ((obj.coor[i-1] + k3_x*t)-gas[k].coor[i-1])*((obj.coor[i-1]+ k3_x*t)-gas[k].coor[i-1]);
                    r = std::max(r, 1e-10);
                    A = A + (24*eps/obj.M)*(2*pow(sigm, 12)/pow(r,7) - pow(sigm, 6)/pow(r, 4))*((obj.coor[i-1] + k3_x*t)-gas[k].coor[i-1]);
                }
                coord k4_x = obj.speed[i-1]+k3_v*t;
                coord k4_v = A;

               obj.coor.push_back(cond_check(obj.coor[i-1] + (t/6)*(k1_x + 2*(k2_x + k3_x) + k4_x), obj.R));
               obj.speed.push_back(obj.speed[i-1] + (t/6)*(k1_v + 2*(k2_v + k3_v) + k4_v));

            }
        }
        return;
    }

    void print(std::string file_name, int n=1){
        ofstream file(file_name);
        int it = 0;
        for(const atom &at:gas){
            file << "Number:" << it << ", mass:" << at.M << ", radius:" << at.R <<"\n";
            file << "time,x,y,z,x_,y_,z_\n";
            for(int i = 0; i < rep; i+=n){
                file << i*t << ", " << at.coor[i].a << ", " << at.coor[i].b << ", " << at.coor[i].c << ", " << at.speed[i].a << ", " << at.speed[i].b << ", " << at.speed[i].c << "\n";
            }
            it++;
        }
        file.close();
        return;
    }

    void print_v(std::string file_name, int n=1){
        ofstream file(file_name);
        int it = 0;
        for(const atom &at:gas){
            file << "Number:" << it << ", mass:" << at.M << ", radius:" << at.R <<"\n";
            file << "time,x,y,z\n";
            for(int i = 0; i < rep; i+=n){
                file << i*t << ", " << at.coor[i].a << ", " << at.coor[i].b << ", " << at.coor[i].c << "\n";
            }
            it++;
        }
        file.close();
        return;
    }

    void export_xyz(std::string file_name, int n=1){
        ofstream file(file_name);
        for(int i = 0; i < rep; i+=n){
            file << N << "\nLattice=\"1 0 0 0 1 0 0 0 1\" Properties=species:S:1:pos:R:3:radius:R:1\n";
            for(int j = 0; j < N; j++){
                file << j << " " << gas[j].coor[i].a << " " << gas[j].coor[i].b << " " << gas[j].coor[i].c << " " << gas[j].R << "\n";
            }
        }
        file.close();
        return;
    }
};




int main(){
    solver S;
    // S.solve_verle();
    // S.print_v("data/verle.csv", 100);
    S.solve_R_K();
    S.print("data/main.csv", 100);
    S.export_xyz("data/main.xyz", 100);
    return 0;
}

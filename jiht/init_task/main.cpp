#include<algorithm>
#include<iostream>
#include<cmath>
#include<vector>
#include<random>
#include<fstream>
#include<string>
#include<omp.h>
#include<iomanip>
#include <nlohmann/json.hpp>
// #include <cstddef>
// #include <iterator>

using namespace std;
using json = nlohmann::json;


// to generate random coordinates and speeds
std::random_device r_;
std::default_random_engine e1(r_());



// class for coordinate
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
}; // functions for coordinates
coord operator*(double t, coord X){
    return coord(X.a*t, X.b*t, X.c*t);
}
coord operator*(coord X, double t){
    return coord(X.a*t, X.b*t, X.c*t);
}
coord operator/(coord X, double t){
    return coord(X.a/t, X.b/t, X.c/t);
}


// class for one atom
class atom{
    public:
    vector<coord> coor;
    vector<coord> speed;
    double M=0;
    double R=0;
    atom(){}
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


// to solve
class solver{
public:
    double LENGTH = 1; //length of simulation cell
    double t = 1e-4; //step value
    int rep = 1e6; //number of repetitions
    int N = 10; //number of atoms
    //parameters of L-D potential
    double eps = 0.5;
    double sigm = 0.1;
    double v_med = 0.1;

    atom* gas = nullptr; //vector of atoms
    
    // initialization with parser
    solver(int argc, char* argv[]){
        ifstream f(argv[1]);  // read config
        json data = json::parse(f);
        LENGTH=data["LENGHT"];
        t=data["t"];
        rep=data["rep"];
        N=data["N"];
        eps=data["eps"];
        sigm=data["sigm"];
        v_med=data["v_med"];
        gas = new atom[N];
        if(data["manual"]==0){// automatic random initialization 
            double M=1, R=0.01/N;
            std::uniform_real_distribution<> d1(0, LENGTH); // distribution for coordinates
            std::uniform_real_distribution<> d2(-v_med, v_med); // distribution for speeds
            // inition 
            for(int i = 0; i < N; i++){
                gas[i] = atom(M, R, d1(e1),d1(e1),d1(e1),d2(e1),d2(e1),d2(e1));
            }
        }
        else if(data["manual"]==1){// manual initialization
            for(int i = 0; i < N; i++){
                gas[i] = atom(data["atoms"][i][0],data["atoms"][i][1],
                    data["atoms"][i][2],data["atoms"][i][3],data["atoms"][i][4],
                    data["atoms"][i][5],data["atoms"][i][6],data["atoms"][i][7]
                );
            }
        }
        else if(data["manual"]==2){// automatic definate initialization 
            double M=data["mass"], R=data["radius"];
            std::normal_distribution<> d2(v_med, v_med/5); // distribution for speeds
            std::uniform_int_distribution<int> d3(0,1);
            int sg[]={-1,1};
            // inition 
            double ll = ceil(pow(N,1./3));
            for(int i = 0; i < N; i++){
                gas[i] = atom(M, R, LENGTH*mod(floor(i/1),ll)/ll, LENGTH*mod(floor(i/ll),ll)/ll,  LENGTH*mod(floor(i/pow(ll,2)),ll)/ll,d3(e1)*d2(e1),d3(e1)*d2(e1),d3(e1)*d2(e1));
            }
        }
    }

    // automatic initialization without parser
    solver(){
        double M=1, R=0.01;
        std::uniform_real_distribution<> d1(0, LENGTH); // distribution for coordinates
        std::uniform_real_distribution<> d2(-0.1, 0.1); // distribution for speeds
        // inition 
        gas = new atom[N];
        for(int i = 0; i < N; i++){
            gas[i] = atom(M, R, d1(e1),d1(e1),d1(e1),d2(e1),d2(e1),d2(e1));
        }
    }

    // rule of five
    solver(solver&)=delete;
    solver(solver&&)=delete;
    solver& operator=(solver &sec)=delete;
    solver& operator=(solver &&sec)=delete;
    ~solver(){delete[] gas;}

    // function for truth mod
    inline double mod(double x, double l){
        double t = fmod(x, l);
        return (t < 0) ? t + l : t;
    }
    // function to realise periodic conditions
    inline coord cond_check(const coord& c, double R){
        return coord(this->mod(c.a, LENGTH), this->mod(c.b, LENGTH), this->mod(c.c, LENGTH));
    }
    // function for sign
    inline double sign(double x){
        return x < 0 ? -1 : 1;
    }
    // function for minimal image
    inline coord min_image(coord r){
        return coord(abs(r.a)<LENGTH/2 ? r.a : -1*this->sign(r.a)*(LENGTH-abs(r.a)),
        abs(r.b)<LENGTH/2 ? r.b : -1*this->sign(r.b)*(LENGTH-abs(r.b)),
        abs(r.c)<LENGTH/2 ? r.c : -1*this->sign(r.c)*(LENGTH-abs(r.c))
        );
    }
    // calculating for verle 
    inline coord A_verle(coord &current, coord &previous) {
        coord delta = min_image(current - previous);
        return current + delta;
    }


    // verle scheme
    void solve_verle(){
        this->solve_R_K(); //initial conditions 

        for(int i = 2; i < rep; i++){
            #pragma omp parallel for
            for(int j = 0; j < N; j++){
                atom &obj = gas[j]; //current atom

                coord A(0,0,0); //total acceleration
                for(int k = 0; k < N; k++){
                    if(k==j) continue; //self-skip
                    coord r_im = this->min_image(obj.coor[i-1]-gas[k].coor[i-1]); //min_image coordinates
                    double r = (r_im)*(r_im); //module of distance
                    A = A + (24*eps/obj.M)*(2*pow(sigm, 12)/pow(r,7) - pow(sigm, 6)/pow(r, 4))*r_im; //add to total acceleration
                }
                #pragma omp critical
                {
                obj.coor.push_back(cond_check(A_verle(obj.coor[i-1], obj.coor[i-2]) + A*pow(t,2), obj.R));
                }
            }
        }
    }
    // R-K_4-5 scheme
    void solve_R_K(int rep=2){
        for(int i = 1; i < rep; i++){//frames
            for(int j = 0; j < N; j++){//atoms
                
                atom &obj = gas[j]; //current atom

                coord A = coord(0,0,0); //total acceleration
                for(int k = 0; k < N; k++){
                    if(k==j) continue; //self-skip
                    coord r_im = this->min_image(obj.coor[i-1]-gas[k].coor[i-1]); //min_image coordinates
                    double r = (r_im)*(r_im); //module of distance
                    r = std::max(r, 1e-10); //bad practices
                    A = A + (24*eps/obj.M)*(2*pow(sigm, 12)/pow(r,7) - pow(sigm, 6)/pow(r, 4))*r_im; //add to total acceleration
                }
                coord k1_x = obj.speed[i-1]; //RK coefficient
                coord k1_v = A; //RK coefficient

                A=coord(0,0,0);
                for(int k = 0; k < N; k++){
                    if(k==j) continue;
                    coord r_im = this->min_image(obj.coor[i-1]-gas[k].coor[i-1]);
                    double r = (r_im + k1_x*t/2)*(r_im + k1_x*t/2);
                    r = std::max(r, 1e-10);
                    A = A + (24*eps/obj.M)*(2*pow(sigm, 12)/pow(r,7) - pow(sigm, 6)/pow(r, 4))*(r_im + k1_x*t/2);
                }
                coord k2_x = obj.speed[i-1]+k1_v*t/2;
                coord k2_v = A;

                A=coord(0,0,0);
                for(int k = 0; k < N; k++){
                    if(k==j) continue;
                    coord r_im = this->min_image(obj.coor[i-1]-gas[k].coor[i-1]);
                    double r = (r_im + k2_x*t/2)*(r_im + k2_x*t/2);
                    r = std::max(r, 1e-10);
                    A = A + (24*eps/obj.M)*(2*pow(sigm, 12)/pow(r,7) - pow(sigm, 6)/pow(r, 4))*(r_im+ k2_x*t/2);
                }
                coord k3_x = obj.speed[i-1]+k2_v*t/2;
                coord k3_v = A;


                A=coord(0,0,0);
                for(int k = 0; k < N; k++){
                    if(k==j) continue;
                    coord r_im = this->min_image(obj.coor[i-1]-gas[k].coor[i-1]);
                    double r = (r_im + k3_x*t)*(r_im + k3_x*t);
                    r = std::max(r, 1e-10);
                    A = A + (24*eps/obj.M)*(2*pow(sigm, 12)/pow(r,7) - pow(sigm, 6)/pow(r, 4))*(r_im + k3_x*t);
                }
                coord k4_x = obj.speed[i-1]+k3_v*t;
                coord k4_v = A;

               obj.coor.push_back(cond_check(obj.coor[i-1] + (t/6)*(k1_x + 2*(k2_x + k3_x) + k4_x), obj.R)); //append coordinate(frame)
               obj.speed.push_back(obj.speed[i-1] + (t/6)*(k1_v + 2*(k2_v + k3_v) + k4_v)); //append speed(frame)
            }
        }
        return;
    }


    // print to csv for R-K
    void print_R_K(std::string file_name, int n=1){
        ofstream file(file_name);
        int it = 0;
        for(int j = 0; j < N; j++){
            const atom &at = gas[j];
            file << "Number:" << it << ", mass:" << at.M << ", radius:" << at.R <<endl;
            file << "time,x,y,z,x_,y_,z_" << endl;
            for(int i = 0; i < rep; i+=n){
                file << setprecision(12) << i*t << ", " << at.coor[i].a << ", " << at.coor[i].b << ", " << at.coor[i].c << ", " << at.speed[i].a << ", " << at.speed[i].b << ", " << at.speed[i].c << endl;
            }
            it++;
        }
        file.close();
        return;
    }
    // print to csv for verle
    void print_v(std::string file_name, int n=1){
        ofstream file(file_name);
        int it = 0;
        for(int j = 0; j < N; j++){
            const atom &at = gas[j];
            file << "Number:" << it << ", mass:" << at.M << ", radius:" << at.R <<std::endl;
            file << "time,x,y,z" << std::endl;
            for(int i = 0; i < rep; i+=n){
                file << setprecision(12) << i*t << ", " << at.coor[i].a << ", " << at.coor[i].b << ", " << at.coor[i].c << std::endl;
            }
            it++;
        }
        file.close();
        return;
    }
    // print to xyz
    void export_xyz(std::string file_name, int n=1){
        ofstream file(file_name);
        for(int i = 0; i < rep; i+=n){
            file << N << "\nLattice=\"" << LENGTH << " 0 0 0 " << LENGTH << " 0 0 0 " << LENGTH << "\" Properties=species:S:1:pos:R:3:radius:R:1\n";
            for(int j = 0; j < N; j++){
                file << j << " " << gas[j].coor[i].a << " " << gas[j].coor[i].b << " " << gas[j].coor[i].c << " " << gas[j].R << endl;
            }
        }
        file.close();
        return;
    }
    // energy and impulse
    void print_en_im(std::string file_name, int n=1){
        ofstream file(file_name);
        double* E_p = new double[rep];
        double* E_k = new double[rep];
        double* Px = new double[rep];
        double* Py = new double[rep];
        double* Pz = new double[rep];
        file << "time,energy_p,energy_k,imp_x,imp_y,imp_z\n";
        for(int i = 1; i < rep-1; i+=n){
            E_p[i]=0, E_k[i]=0, Px[i]=0, Py[i]=0, Pz[i]=0;
            for(int j = 0; j < N; j++){

                for(int k = 0; k < N; k++){
                    if(k==j) continue; //self-skip
                    coord r_im = this->min_image(gas[j].coor[i]-gas[k].coor[i]); //min_image coordinates
                    double r = (r_im)*(r_im); //module of distance
                    E_p[i] += 2*eps*(pow(sigm, 12)/pow(r,6) - pow(sigm, 6)/pow(r, 3)); //add to total acceleration
                }
                E_k[i]+=min_image((gas[j].coor[i+1]-gas[j].coor[i-1])) * min_image((gas[j].coor[i+1]-gas[j].coor[i-1]))*gas[j].M/(8*t*t);
                Px[i]+=min_image((gas[j].coor[i+1]-gas[j].coor[i-1])).a*gas[j].M/(2*t);
                Py[i]+=min_image((gas[j].coor[i+1]-gas[j].coor[i-1])).b*gas[j].M/(2*t);
                Pz[i]+=min_image((gas[j].coor[i+1]-gas[j].coor[i-1])).c*gas[j].M/(2*t);
            }
            file << setprecision(12) << i*t << ", " << E_p[i] << ", " << E_k[i] << ", " << Px[i]<< ", " << Py[i] << ", " << Pz[i] << endl;
        }
        file.close();
        delete[] E_p;
        delete[] E_k;
        delete[] Px;
        delete[] Py;
        delete[] Pz;
        return;
    }
    // speeds
    void print_speeds(std::string file_name, int n=1){
        ofstream file(file_name);
        file << "time";
        for(int i = 0; i < N; i++){
            file << ","+to_string(i)+"_x,"+to_string(i)+"_y,"+to_string(i)+"_z";
        }
        file << endl;
        for(int i = 1; i < rep-1; i+=n){
            file << i*t;
            for(int j = 0; j < N; j++){
                file << ", " << min_image(gas[j].coor[i+1]-gas[j].coor[i-1]).a/(2*t) << ", " << min_image(gas[j].coor[i+1]-gas[j].coor[i-1]).b/(2*t) << ", " << min_image(gas[j].coor[i+1]-gas[j].coor[i-1]).c/(2*t);
            }
            file << endl;
        }
    }
    // autocorrelation function
    void print_corr_func(std::string file_name, int n=1){
        ofstream file(file_name);
        file << "time,corr_func\n";
        double* corr_func = new double[rep];
        for(int i = 0; i < rep; i++){
            corr_func[i]=0;
        }
        for(int att = 0; att < N; att++){
            atom at = gas[att];
            #pragma omp parallel for
            for(int i = 1; i < rep-1; i++){
                for(int j = i+1; j < rep-1; j++){
                    corr_func[i] += min_image((at.coor[j+1]-at.coor[j-1])) * min_image((at.coor[j-i+1]-at.coor[j-i-1]))/(4*pow(t,2))*t;
                }
            }
        }
        for(int i = 0; i < rep; i++){
            corr_func[i]/=N;
            file << setprecision(12) << i*t << ", " << corr_func[i] << endl;
        }
        file.close();
        delete[] corr_func;
        return;
    }
};



int main(int argc, char* argv[]){
    solver S(argc, argv);
    S.solve_verle();


    ifstream f(argv[1]);  // read config
    json data = json::parse(f);

    if(!data["corr_func_on"]){
        S.print_v(data["ways"]["verle"], S.rep>1e3?S.rep/1e3:1);
        // S.solve_R_K(S.rep);
        // S.print_R_K("data/main.csv", 100);

        // S.export_xyz("data/main.xyz", 1);
        // S.print_en_im("data/energy.csv", 1);
        // S.print_speeds("data/speeds.csv", 1);
        // S.print_corr_func("data/corr_func.csv", 1);

        // S.export_xyz("data/main.xyz",  1e-3/S.t>1?1e-3/S.t:1);
        // S.print_en_im("data/energy.csv",  1e-3/S.t>1?1e-3/S.t:1);
        // S.print_speeds("data/speeds.csv",  1e-3/S.t>1?1e-3/S.t:1);
        // S.print_corr_func("data/corr_func.csv",  1e-3/S.t>1?1e-3/S.t:1);


        S.export_xyz(data["ways"]["xyz"],  S.rep>1e3?S.rep/1e3:1);
        S.print_en_im(data["ways"]["energy"],  S.rep>1e3?S.rep/1e3:1);
        S.print_speeds(data["ways"]["speeds"],  S.rep>1e3?S.rep/1e3:1);
    }
    else if(data["corr_func_on"]){
        S.print_corr_func(data["ways"]["corr_func"],  S.rep>1e3?S.rep/1e3:1);
    }

    return 0;
}

#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
#include<nlohmann/json.hpp> //import json as new type
// #include<typeinfo>

// extern "C" {
// #include <libavutil/imgutils.h>
// #include <libavcodec/avcodec.h>
// #include <libswscale/swscale.h>
// }

using namespace std;
using json = nlohmann::json; //renaming namespace

// ------------------------- declaration of functions -----------------------------------
void sep(double* arr, int N, double h);
// void eyler(double* arr, int N, double* X, double* V);
void entry(double* X, double* Y, int N, string FILE);
// void hoin(double* arr, int N, double* X, double* V);
void RK4(double* arr, int N, double* , double*, double*,double*,double*,double* );

void RK4_coord(double* arr, int N, double* x, double* x_, double* y,double* y_,double* z,double* z_);

// ------------------------------------ parameters of system -----------------------------
double k = 0;
double m = 0;
double l0 = 0;

// double alpha = 0;
// double betta = 0;

//-------------------------------- main --------------------------------------------------
int main(int argc, char* argv[]){
    if(argc != 2) return 1;   // bad check
    // cout << argv[1]<< endl;
    ifstream f(argv[1]);  // read config
    json data = json::parse(f);





    double h = data["h"];  // renaming of param
    const int N = data["N"];
    k = data["k"];
    m = data["m"];
    l0 = data["l0"];
    double* arr = new double[N];  // partitioning grid
    sep(arr, N, h);

    double* l = new double[N];   // arrays of values
    double* l_ = new double[N];
    double* phi = new double[N];
    double* phi_ = new double[N];
    double* psi = new double[N];
    double* psi_ = new double[N];

    double* x = new double[N];
    double* x_ = new double[N];
    double* y = new double[N];
    double* y_ = new double[N];
    double* z = new double[N];
    double* z_ = new double[N];

    l[0] = data["l"]; // initial conditions
    l_[0] = data["l_"];
    phi[0] = data["phi"];
    phi_[0] = data["phi_"];
    psi[0] = data["psi"];
    psi_[0] = data["psi_"];

    x[0] = data["x"];
    x_[0] = data["x_"];
    y[0] = data["y"];
    y_[0] = data["y_"];
    z[0] = data["z"];
    z_[0] = data["z_"];

    // choice of algo
    if(data["algo"] == "eyler"){
        // eyler(arr, N, M1, M2, M3);
    }
    else if(data["algo"] == "hoin"){
        // hoin(arr, N, M1, M2, M3);
    }
    else if(data["algo"] == "RK4"){
        RK4(arr, N, l, l_, phi, phi_, psi, psi_);
        RK4_coord(arr, N, x, x_, y, y_, z, z_);
    }

    json files = data["files"][0]; // not necessarily but makes easier

    entry(arr, l, N, files["l"]); // output
    entry(arr, l_, N, files["l_"]);
    entry(arr, phi, N, files["phi"]);
    entry(arr, psi, N, files["psi"]);
    entry(arr, psi_, N, files["psi_"]);
    entry(arr, phi_, N, files["phi_"]);

    entry(arr, x, N, files["x"]);
    entry(arr, x_, N, files["x_"]);
    entry(arr, y, N, files["y"]);
    entry(arr, y_, N, files["y_"]);
    entry(arr, z, N, files["z"]);
    entry(arr, z_, N, files["z_"]);

    cout << m << k;
    return 0;
}





// grid
void sep(double* arr, int N, double h){
    arr[0] = 0;
    for(int i = 1; i < N; i++){
        arr[i] = arr[i-1] + h;
    }
}

// output
void entry(double* X, double* Y, int N, string FILE){ 
    ofstream file;
    file.open(FILE);
    file << "t; x\n";
    for(int i =0; i < N; i++){
        file << X[i]<<"; "<<Y[i]<<"\n";
    }
    file.close();
}



// euler method
// void eyler(double* arr, int N, double* M1, double* M2, double* M3){
//     for(int i = 1; i < N; i++){
//         // x(i+1) = xi + dT*Vi
//         // V(i+1) = v(i) - w**2*x
//         M1[i] = M1[i-1] + (arr[i] - arr[i-1])*M2[i-1];
//         M2[i] = M2[i-1] - (arr[i] - arr[i-1])*pow(W, 2) * M1[i-1];
//     }
// }

// hoin method
// void hoin(double* arr, int N, double* X, double* V){
//         for(int i = 1; i < N; i++){
//         // x(i+1) = xi + dT*Vi
//         // V(i+1) = v(i) - w**2*x
//             X[i] = X[i-1] + (arr[i] - arr[i-1])*(V[i-1] + V[i-1] - (arr[i] - arr[i-1])*pow(W, 2) * X[i-1])/2;
//             V[i] = V[i-1] - (arr[i] - arr[i-1])*pow(W, 2) * (X[i-1] + X[i-1] + (arr[i] - arr[i-1])*V[i-1])/2; 
//         } 
// }



// Runge-Kutta method of order 4 (wrong realization)
void RK4(double* arr, int N, double* l, double* l_, double* phi,double* phi_,double* psi,double* psi_){

    for(int i = 1; i < N; i++){
// ---------------------------------------------------------------
        double h = arr[i] - arr[i-1];

        double k1_l = h*(l_[i-1]);
        double k1_l_ = h*(l[i-1]*(pow(phi_[i-1], 2)*pow(cos(psi[i-1]), 2) + pow(psi_[i-1], 2) - k/m) + l0*k/m);
        double k1_phi = h*(phi_[i-1]);
        double k1_phi_ = h*2*(l[i-1]*phi_[i-1]*sin(psi[i-1])*(psi_[i-1]) - l_[i-1]*phi_[i-1]*cos(psi[i-1]))/(l[i-1]*cos(psi[i-1]));
        double k1_psi = h*(psi_[i-1]);
        double k1_psi_ = -1*h*((l[i-1])*pow(phi_[i-1],2)*cos(psi[i-1])*sin(psi[i-1]) + 2*(l_[i-1]*(psi_[i-1])))/(l[i-1]);

        double k2_l = h*(l_[i-1] + k1_l_/2.);
        double k2_l_ = h*((l[i-1] + k1_l/2.)*(pow(phi_[i-1]+k1_phi_/2., 2)*pow(cos(psi[i-1] + k1_psi/2.), 2) + pow(psi_[i-1] + k1_psi_/2., 2) - k/m)+l0*k/m);
        double k2_phi = h*(phi_[i-1] + k1_phi_/2.);
        double k2_phi_ = h*2*((l[i-1] + k1_l/2.)*(phi_[i-1]+k1_phi_/2.)*sin(psi[i-1]+k1_psi/2.)*(psi_[i-1]+k1_psi_/2.) - (l_[i-1] + k1_l_/2.)*(phi_[i-1]+k1_phi_/2.)*cos(psi[i-1]+k1_psi/2.))/((l[i-1] + k1_l/2.)*cos(psi[i-1] + k1_psi/2.));
        double k2_psi = h*(psi_[i-1] + k1_psi_/2.);
        double k2_psi_ = -1*h*((l[i-1] + k1_l/2.)*pow(phi_[i-1] + k1_phi_/2.,2)*cos(psi[i-1] + k1_psi/2.)*sin(psi[i-1] + k1_psi/2.) + 2*(l_[i-1] + k1_l_/2.)*(psi_[i-1] + k1_psi_/2.))/(l[i-1] + k1_l/2.);

        
        double k3_l = h*(l_[i-1] + k2_l_/2.);
        double k3_l_ = h*((l[i-1] + k2_l/2.)*(pow(phi_[i-1]+k2_phi_/2., 2)*pow(cos(psi[i-1] + k2_psi/2.), 2) + pow(psi_[i-1] + k2_psi_/2., 2) - k/m)+l0*k/m);
        double k3_phi = h*(phi_[i-1] + k2_phi_/2.);
        double k3_phi_ = h*2*((l[i-1] + k2_l/2.)*(phi_[i-1]+k2_phi_/2.)*sin(psi[i-1]+k2_psi/2.)*(psi_[i-1]+k2_psi_/2.) - (l_[i-1] + k2_l_/2.)*(phi_[i-1]+k2_phi_/2.)*cos(psi[i-1]+k2_psi/2.))/((l[i-1] + k2_l/2.)*cos(psi[i-1] + k2_psi/2.));
        double k3_psi = h*(psi_[i-1] + k2_psi_/2.);
        double k3_psi_ = -1*h*((l[i-1] + k2_l/2.)*pow(phi_[i-1] + k2_phi_/2.,2)*cos(psi[i-1] + k2_psi/2.)*sin(psi[i-1] + k2_psi/2.) + 2*(l_[i-1] + k2_l_/2.)*(psi_[i-1] + k2_psi_/2.))/(l[i-1] + k2_l/2.);


        double k4_l = h*(l_[i-1] + k3_l_);
        double k4_l_ = h*((l[i-1] + k3_l)*(pow(phi_[i-1]+k3_phi_, 2)*pow(cos(psi[i-1] + k3_psi), 2) + pow(psi_[i-1] + k3_psi_, 2) - k/m)+l0*k/m);
        double k4_phi = h*(phi_[i-1] + k3_phi_);
        double k4_phi_ = h*2*((l[i-1] + k3_l)*(phi_[i-1]+k3_phi_)*sin(psi[i-1]+k3_psi)*(psi_[i-1]+k3_psi_) - (l_[i-1] + k3_l_)*(phi_[i-1]+k3_phi_)*cos(psi[i-1]+k3_psi))/((l[i-1] + k3_l)*cos(psi[i-1] + k3_psi));
        double k4_psi = h*(psi_[i-1] + k3_psi_);
        double k4_psi_ = -1*h*((l[i-1] + k3_l)*pow(phi_[i-1] + k3_phi_,2)*cos(psi[i-1] + k3_psi)*sin(psi[i-1] + k3_psi) + 2*(l_[i-1] + k3_l_)*(psi_[i-1] + k3_psi_))/(l[i-1] + k3_l);


        l[i] = l[i-1] + (1/6.)*(k1_l + 2*(k2_l+k3_l) + k4_l);
        l_[i] = l_[i-1] + (1/6.)*(k1_l_ + 2*(k2_l_+k3_l_) + k4_l_);
        phi[i] = phi[i-1] + (1/6.)*(k1_phi + 2*(k2_phi+k3_phi) + k4_phi);
        phi_[i] = phi_[i-1] + (1/6.)*(k1_phi_ + 2*(k2_phi_+k3_phi_) + k4_phi_);
        psi[i] = psi[i-1] + (1/6.)*(k1_psi + 2*(k2_psi+k3_psi) + k4_psi);
        psi_[i] = psi_[i-1] + (1/6.)*(k1_psi_ + 2*(k2_psi_+k3_psi_) + k4_psi_);




        // my own hysteresis

        // k = k / (pow((l[i-1] - l0)/l0, 3) + 1);
    } 
}



void RK4_coord(double* arr, int N, double* x, double* x_, double* y,double* y_,double* z,double* z_){
    for(int i =1 ; i < N; i++){
        double h = arr[i] - arr[i-1];
        x[i] = x[i-1] + h*x_[0];
        x_[i] = x_[0];
        y[i] = y[i-1] + h*y_[0];
        y_[i] = y_[0];
        z[i] = z[i-1] + h*z_[0];
        z_[i] = z_[0];
        // x[i] = x_[i] = y[i] = y_[i] = z[i] = z_[i] = 0;
    }
}



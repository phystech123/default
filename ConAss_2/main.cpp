#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
#include<nlohmann/json.hpp> //import json as new type
// #include<typeinfo>


using namespace std;
using json = nlohmann::json; //renaming namespace

// ------------------------- declaration of functions -----------------------------------
void sep(double* arr, int N, double h);
void entry(double* X, double* Y, int N, string FILE, int p);
void RK4(double* arr, int N, double*,double*,double*,double* );

// ------------------------------------ parameters of system -----------------------------
double g = 0;
double l = 0;
double m = 0;

double alpha_1 = 0;
double alpha_2 = 0;

double x_0 = 0;
double y_0 = 0;
double z_0 = 0;
double hsq_0 = 0;


//-------------------------------- main --------------------------------------------------
int main(int argc, char* argv[]){
    if(argc != 2) return 1;   // bad check
    // cout << argv[1]<< endl;
    ifstream f(argv[1]);  // read config
    json data = json::parse(f);


    double h = data["params_model"]["h"];  // renaming of param
    const int N = data["params_model"]["rep"];
    int skip = data["params_model"]["skip"];

    g = data["params_sys"]["g"];
    l = data["params_sys"]["l"];
    m = data["params_sys"]["m"];

    alpha_1 = data["params_sys"]["alpha_1"];
    alpha_2 = data["params_sys"]["alpha_2"];

    x_0 = data["params_sys"]["x_0"];
    y_0 = data["params_sys"]["y_0"];
    z_0 = data["params_sys"]["z_0"];
    hsq_0 = pow(x_0, 2) + pow(y_0, 2) + pow(z_0, 2);

    double* arr = new double[N];  // partitioning grid
    sep(arr, N, h);

    double* phi = new double[N]; // arrays of values
    double* phi_ = new double[N];
    double* theta = new double[N];
    double* theta_ = new double[N];

    phi[0] = data["init_cond"]["phi"]; // initial conditions
    phi_[0] = data["init_cond"]["phi_"];
    theta[0] = data["init_cond"]["theta"];
    theta_[0] = data["init_cond"]["theta_"];


    if(data["params_model"]["algo"] == "RK4"){
        RK4(arr, N, phi, phi_, theta, theta_);
    }

    json files = data["params_model"]["files"]; // not necessarily but makes easier

    entry(arr, phi, N, files["phi"], (N>skip)?N/skip:N);
    entry(arr, phi_, N, files["phi_"],(N>skip)?N/skip:N);
    entry(arr, theta, N, files["theta"], (N>skip)?N/skip:N);
    entry(arr, theta_, N, files["theta_"], (N>skip)?N/skip:N);

    delete[] arr;
    delete[] phi;
    delete[] phi_;
    delete[] theta;
    delete[] theta_;

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
void entry(double* X, double* Y, int N, string FILE, int p){ 
    ofstream file;
    file.open(FILE);
    file << "t; x\n";
    for(int i =0; i < N; i+=p){
        file << X[i]<<"; "<<Y[i]<<"\n";
    }
    file.close();
}





// Runge-Kutta method of order 4
void RK4(double* arr, int N, double* phi,double* phi_,double* theta,double* theta_){
    
    for(int i = 1; i < N; i++){
        double h = arr[i] - arr[i-1];

        double r3_1 = pow(l*l + hsq_0 - 2*l*(x_0*sin(phi[i-1])*cos(theta[i-1]) + y_0*sin(phi[i-1])*sin(theta[i-1]) + z_0*cos(phi[i-1])), 1.5); 
        double k1_phi = h*(phi_[i-1]);
        double k1_phi_ = h*(sin(phi[i-1])*cos(phi[i-1])*pow(theta_[i-1],2) - (g/l)*sin(phi[i-1]) - alpha_1*alpha_2*(x_0*cos(phi[i-1])*cos(theta[i-1]) + y_0*cos(phi[i-1])*sin(theta[i-1]) - z_0*sin(phi[i-1]))/(m*l*r3_1));
        double k1_theta = h*(theta_[i-1]);
        double k1_theta_ = h*(alpha_1*alpha_2*(x_0*sin(theta[i-1]) - y_0*cos(theta[i-1]))/(m*l*r3_1*sin(phi[i-1])) - 2*cos(phi[i-1])/sin(phi[i-1])*phi_[i-1]*theta_[i-1]);

        
        double r3_2 = pow(l*l + hsq_0 - 2*l*(x_0*sin(phi[i-1]+k1_phi/2.)*cos(theta[i-1]+k1_theta/2.) + y_0*sin(phi[i-1]+k1_phi/2.)*sin(theta[i-1]+k1_theta/2.) + z_0*cos(phi[i-1]+k1_phi/2.)), 1.5); 
        double k2_phi = h*(phi_[i-1]+k1_phi_/2.);
        double k2_phi_ = h*(sin(phi[i-1]+k1_phi/2.)*cos(phi[i-1]+k1_phi/2.)*pow(theta_[i-1]+k1_theta_/2.,2) - (g/l)*sin(phi[i-1]+k1_phi/2.) - alpha_1*alpha_2*(x_0*cos(phi[i-1]+k1_phi/2.)*cos(theta[i-1]+k1_theta/2.) + y_0*cos(phi[i-1]+k1_phi/2.)*sin(theta[i-1]+k1_theta/2.) - z_0*sin(phi[i-1]+k1_phi/2.))/(m*l*r3_1));
        double k2_theta = h*(theta_[i-1]+k1_theta_/2.);
        double k2_theta_ = h*(alpha_1*alpha_2*(x_0*sin(theta[i-1]+k1_theta/2.) - y_0*cos(theta[i-1]+k1_theta/2.))/(m*l*r3_1*sin(phi[i-1]+k1_phi/2.)) - 2*(cos(phi[i-1]+k1_phi/2.)/sin(phi[i-1]+k1_phi/2.))*(phi_[i-1]+k1_phi_/2.)*(theta_[i-1]+k1_theta_/2.));

        double r3_3 = pow(l*l + hsq_0 - 2*l*(x_0*sin(phi[i-1]+k2_phi/2.)*cos(theta[i-1]+k2_theta/2.) + y_0*sin(phi[i-1]+k2_phi/2.)*sin(theta[i-1]+k2_theta/2.) + z_0*cos(phi[i-1]+k2_phi/2.)), 1.5); 
        double k3_phi = h*(phi_[i-1]+k2_phi_/2.);
        double k3_phi_ = h*(sin(phi[i-1]+k2_phi/2.)*cos(phi[i-1]+k2_phi/2.)*pow(theta_[i-1]+k2_theta_/2.,2) - (g/l)*sin(phi[i-1]+k2_phi/2.) - alpha_1*alpha_2*(x_0*cos(phi[i-1]+k2_phi/2.)*cos(theta[i-1]+k2_theta/2.) + y_0*cos(phi[i-1]+k2_phi/2.)*sin(theta[i-1]+k2_theta/2.) - z_0*sin(phi[i-1]+k2_phi/2.))/(m*l*r3_1));
        double k3_theta = h*(theta_[i-1]+k2_theta_/2.);
        double k3_theta_ = h*(alpha_1*alpha_2*(x_0*sin(theta[i-1]+k2_theta/2.) - y_0*cos(theta[i-1]+k2_theta/2.))/(m*l*r3_1*sin(phi[i-1]+k2_phi/2.)) - 2*(cos(phi[i-1]+k2_phi/2.)/sin(phi[i-1]+k2_phi/2.))*(phi_[i-1]+k2_phi_/2.)*(theta_[i-1]+k2_theta_/2.));


        double r3_4 = pow(l*l + hsq_0 - 2*l*(x_0*sin(phi[i-1]+k3_phi)*cos(theta[i-1]+k3_theta) + y_0*sin(phi[i-1]+k3_phi)*sin(theta[i-1]+k3_theta) + z_0*cos(phi[i-1]+k3_phi)), 1.5); 
        double k4_phi = h*(phi_[i-1]+k3_phi_);
        double k4_phi_ = h*(sin(phi[i-1]+k3_phi)*cos(phi[i-1]+k3_phi)*pow(theta_[i-1]+k3_theta_,2) - (g/l)*sin(phi[i-1]+k3_phi) - alpha_1*alpha_2*(x_0*cos(phi[i-1]+k3_phi)*cos(theta[i-1]+k3_theta) + y_0*cos(phi[i-1]+k3_phi)*sin(theta[i-1]+k3_theta) - z_0*sin(phi[i-1]+k3_phi))/(m*l*r3_1));
        double k4_theta = h*(theta_[i-1]+k3_theta_);
        double k4_theta_ = h*(alpha_1*alpha_2*(x_0*sin(theta[i-1]+k3_theta) - y_0*cos(theta[i-1]+k3_theta))/(m*l*r3_1*sin(phi[i-1]+k3_phi)) - 2*(cos(phi[i-1]+k3_phi)/sin(phi[i-1]+k3_phi))*(phi_[i-1]+k3_phi_)*(theta_[i-1]+k3_theta_));


        phi[i] = phi[i-1] + (1/6.)*(k1_phi + 2*(k2_phi+k3_phi) + k4_phi);
        phi_[i] = phi_[i-1] + (1/6.)*(k1_phi_ + 2*(k2_phi_+k3_phi_) + k4_phi_);
        theta[i] = theta[i-1] + (1/6.)*(k1_theta + 2*(k2_theta+k3_theta) + k4_theta);
        theta_[i] = theta_[i-1] + (1/6.)*(k1_theta_ + 2*(k2_theta_+k3_theta_) + k4_theta_);
    } 
}




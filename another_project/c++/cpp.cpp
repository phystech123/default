#include<iostream>
#include<string>
#include<cmath>
#include<ctime>
#include<iomanip>
#include<fstream>
using namespace std;
// int foo(int n){
//     int sum = 1;
//     for(int i = 1; i<=n; i++){
//         sum*=i;
//     }
//     cout<< sum;
// }

// int main(){
//     int n;
//     cin>>n;
//     foo(n);

//     string a = "hello, dear";

//     string b = "hello, \
// dear";

//     string c = "hello, " "d" "ear";

//     cout<< '\n'<< a << '\n' << b << '\n'<< c << '\n';

//     return 0;
// }
// int foo(int n){
//     int sum = 1;
//     for(int i = 1; i<=n; i++){
//         sum*=i;
//     }
//     cout<< sum;
// }

// int main(){
//     int n;
//     cin>>n;
//     foo(n);

//     string a = "hello, dear";

//     string b = "hello, \
// dear";

//     string c = "hello, " "d" "ear";

//     cout<< '\n'<< a << '\n' << b << '\n'<< c << '\n';

//     return 0;
// }




// int main(){
//     // int c;
//     // cin>> c;
//     // int a[c];
//     // for(int i =0; i<c; i++){
//     //     a[i]=i;
//     // }
//     // for(int i =0; i<c; i++){
//     //     cout<<i<<'\t';
//     // }
//     // int z = false?10/2:10/5;
//     // cout<<'\n'<<10/3<<'\n'<<z<<'\n';

//     //    time_t now = time(0);
//     //    char* dt = ctime(&now);
//     //    clog<<dt;
    
    
    
    
//     return 0;
// }


using namespace std;

class Box {
   public:
      double getVolume(void) {
         return length * breadth * height;
      }
      void setLength( double len ) {
         length = len;
      }
      void setBreadth( double bre ) {
         breadth = bre;
      }
      void setHeight( double hei ) {
         height = hei;
      }
      
      // Overload + operator to add two Box objects.
      Box operator+(const Box& b) {
         Box box;
         box.length = this->length + b.length;
         box.breadth = this->breadth + b.breadth;
         box.height = this->height + b.height;
         return box;
      }
      
    int foo(const Box& b){
        cout<< b.length;
        return 9;
    }
      
   private:
      double length;      // Length of a box
      double breadth;     // Breadth of a box
      double height;      // Height of a box
};

// Main function for the program
int main() {
   Box Box1;                // Declare Box1 of type Box
   Box Box2;                // Declare Box2 of type Box
   Box Box3;                // Declare Box3 of type Box
   double volume = 0.0;     // Store the volume of a box here
 
   // box 1 specification
   Box1.setLength(6.0); 
   Box1.setBreadth(7.0); 
   Box1.setHeight(5.0);
 
   // box 2 specification
   Box2.setLength(12.0); 
   Box2.setBreadth(13.0); 
   Box2.setHeight(10.0);
 
   // volume of box 1
   volume = Box1.getVolume();
   cout << "Volume of Box1 : " << volume <<endl;
 
   // volume of box 2
   volume = Box2.getVolume();
   cout << "Volume of Box2 : " << volume <<endl;

   // Add two object as follows:
   Box3 = Box1 + Box2;
   Box3.foo(Box1);


   return 0;
}

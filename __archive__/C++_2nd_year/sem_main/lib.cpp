#include<iostream>
extern int x;
class Foo{
void foo(int &x){
    x*=2;
}
};

template<class T, class ... argT>
void print(T arg, argT... args){
    std::cout << arg;
    print(args...);
}

template<class F, class... argT>
void funcc(F func, argT&&... args){
    func(std::forward(args...));
}

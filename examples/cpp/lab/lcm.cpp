#include <iostream>
#include <string>

int main() {
    int a=21,b=6,x=a,y=b;while(y){int r=x%y;x=y;y=r;}std::cout<<(a/x*b)<<"\n";
    return 0;
}

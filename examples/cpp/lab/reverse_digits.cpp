#include <iostream>
#include <string>

int main() {
    int n=123456,rev=0;while(n){rev=rev*10+n%10;n/=10;}std::cout<<rev<<"\n";
    return 0;
}

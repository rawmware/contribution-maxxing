#include <iostream>
#include <string>

int main() {
    std::string s="level",t="hello";auto pal=[](const std::string&x){for(size_t i=0;i<x.size()/2;i++)if(x[i]!=x[x.size()-1-i])return false;return true;};std::cout<<pal(s)<<" "<<pal(t)<<"\n";
    return 0;
}

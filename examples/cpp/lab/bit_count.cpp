#include <iostream>
#include <string>

int main() {
    unsigned int x=0xB5u;int n=0;while(x){n+=int(x&1u);x>>=1;}std::cout<<n<<"\n";
    return 0;
}

#include <iostream>
#include <string>

int main() {
    int a[3][3]={{1,2,3},{4,5,6},{7,8,9}},sum=0;for(int i=0;i<3;i++)sum+=a[i][i];std::cout<<sum<<"\n";
    return 0;
}

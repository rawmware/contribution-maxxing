#include <iostream>
#include <string>

int main() {
    int v[]={12,-5,7,3,0},lo=v[0],hi=v[0];for(int i=1;i<5;i++){if(v[i]<lo)lo=v[i];if(v[i]>hi)hi=v[i];}std::cout<<lo<<" "<<hi<<"\n";
    return 0;
}

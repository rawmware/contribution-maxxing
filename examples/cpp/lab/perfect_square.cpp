#include <iostream>
#include <string>

int main() {
    int v[]={0,49,50},out[3];for(int k=0;k<3;k++){int i=0;while(i*i<v[k])i++;out[k]=(i*i==v[k]);}std::cout<<out[1]<<" "<<out[2]<<"\n";
    return 0;
}

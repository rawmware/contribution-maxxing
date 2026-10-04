#include <iostream>
#include <string>

int main() {
    int v[]={1,2,3,4,5},n=5,k=2;for(int r=0;r<k;r++){int first=v[0];for(int i=0;i<n-1;i++)v[i]=v[i+1];v[n-1]=first;}for(int i=0;i<n;i++)std::cout<<(i?" ":"")<<v[i];std::cout<<"\n";
    return 0;
}

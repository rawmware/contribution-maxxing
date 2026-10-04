#include <iostream>
#include <string>

int main() {
    int v[]={5,1,4,2,8};for(int i=0;i<5;i++)for(int j=0;j<4-i;j++)if(v[j]>v[j+1]){int t=v[j];v[j]=v[j+1];v[j+1]=t;}for(int i=0;i<5;i++)std::cout<<(i?" ":"")<<v[i];std::cout<<"\n";
    return 0;
}

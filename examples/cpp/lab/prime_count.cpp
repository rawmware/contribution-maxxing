#include <iostream>
#include <string>

int main() {
    int prime[31];for(int i=0;i<=30;i++)prime[i]=1;prime[0]=prime[1]=0;for(int p=2;p*p<=30;p++)if(prime[p])for(int j=p*p;j<=30;j+=p)prime[j]=0;int n=0;for(int i=2;i<=30;i++)n+=prime[i];std::cout<<n<<"\n";
    return 0;
}

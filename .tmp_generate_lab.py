from pathlib import Path
import json
root=Path(__file__).parent

# Each example is a small standalone, deterministic algorithm exercise, with
# an observable output that the lab verifier checks.
algorithms = [
("array_max", "Find the largest value in an integer array.", "7", "int v[]={-4,7,2,0};int m=v[0];for(int i=1;i<4;i++)if(v[i]>m)m=v[i];printf(\"%d\\n\",m);"),
("binary_search", "Return the index of a value in a sorted array, or -1.", "2", "int v[]={1,3,5,7,9};int lo=0,hi=4,x=5,ans=-1;while(lo<=hi){int mid=lo+(hi-lo)/2;if(v[mid]==x){ans=mid;break;}if(v[mid]<x)lo=mid+1;else hi=mid-1;}printf(\"%d\\n\",ans);"),
("bit_count", "Count set bits using a portable shift loop.", "5", "unsigned int x=0xB5u;int n=0;while(x){n+=(int)(x&1u);x>>=1;}printf(\"%d\\n\",n);"),
("bubble_sort", "Sort a short array in place with bubble sort.", "1 2 4 5 8", "int v[]={5,1,4,2,8};for(int i=0;i<5;i++)for(int j=0;j<4-i;j++)if(v[j]>v[j+1]){int t=v[j];v[j]=v[j+1];v[j+1]=t;}for(int i=0;i<5;i++)printf(\"%s%d\",i?\" \":\"\",v[i]);puts(\"\");"),
("clamp", "Constrain a number to an inclusive interval.", "10 -3 4", "int v[]={17,-9,4};int lo=-3,hi=10;for(int i=0;i<3;i++){int x=v[i];if(x<lo)x=lo;if(x>hi)x=hi;printf(\"%s%d\",i?\" \":\"\",x);}puts(\"\");"),
("collatz_steps", "Count Collatz transitions to reach one.", "111", "unsigned long long n=27;int steps=0;while(n!=1){n=n%2?3*n+1:n/2;steps++;}printf(\"%d\\n\",steps);"),
("digit_sum", "Sum decimal digits of a nonnegative integer.", "27", "int n=9876,sum=0;while(n){sum+=n%10;n/=10;}printf(\"%d\\n\",sum);"),
("extended_gcd", "Compute Bezout coefficients with iterative extended Euclid.", "6 2 -3", "int a=240,b=46,old_r=a,r=b,old_s=1,s=0,old_t=0,t=1;while(r){int q=old_r/r;int z=old_r-q*r;old_r=r;r=z;z=old_s-q*s;old_s=s;s=z;z=old_t-q*t;old_t=t;t=z;}printf(\"%d %d %d\\n\",old_r,old_s,old_t);"),
("insertion_sort", "Sort values with insertion sort.", "-1 3 3 7 9", "int v[]={9,3,7,-1,3};for(int i=1;i<5;i++){int x=v[i],j=i;while(j>0&&v[j-1]>x){v[j]=v[j-1];j--;}v[j]=x;}for(int i=0;i<5;i++)printf(\"%s%d\",i?\" \":\"\",v[i]);puts(\"\");"),
("is_palindrome", "Check whether a lowercase ASCII word is a palindrome.", "1 0", "const char*s=\"level\";int n=(int)strlen(s),ok=1;for(int i=0;i<n/2;i++)if(s[i]!=s[n-1-i])ok=0;const char*t=\"hello\";int m=(int)strlen(t),ok2=1;for(int i=0;i<m/2;i++)if(t[i]!=t[m-1-i])ok2=0;printf(\"%d %d\\n\",ok,ok2);"),
("lcm", "Find the least common multiple using GCD reduction.", "42", "int a=21,b=6,x=a,y=b;while(y){int r=x%y;x=y;y=r;}printf(\"%d\\n\",a/x*b);"),
("linear_search", "Find the first matching value in an unsorted array.", "3", "int v[]={4,8,15,16,23,42},x=16,i=0;while(i<6&&v[i]!=x)i++;printf(\"%d\\n\",i<6?i:-1);"),
("max_subarray", "Find the maximum contiguous subarray sum (Kadane's algorithm).", "6", "int v[]={-2,1,-3,4,-1,2,1,-5,4},best=v[0],cur=v[0];for(int i=1;i<9;i++){cur=cur>0?cur+v[i]:v[i];if(cur>best)best=cur;}printf(\"%d\\n\",best);"),
("matrix_trace", "Sum the main diagonal of a square matrix.", "15", "int a[3][3]={{1,2,3},{4,5,6},{7,8,9}},sum=0;for(int i=0;i<3;i++)sum+=a[i][i];printf(\"%d\\n\",sum);"),
("merge_sorted", "Merge two sorted arrays into ascending order.", "0 1 2 3 7 8", "int a[]={0,2,7},b[]={1,3,8},o[6],i=0,j=0,k=0;while(i<3&&j<3)o[k++]=a[i]<b[j]?a[i++]:b[j++];while(i<3)o[k++]=a[i++];while(j<3)o[k++]=b[j++];for(i=0;i<6;i++)printf(\"%s%d\",i?\" \":\"\",o[i]);puts(\"\");"),
("min_max", "Find the minimum and maximum in one pass.", "-5 12", "int v[]={12,-5,7,3,0},lo=v[0],hi=v[0];for(int i=1;i<5;i++){if(v[i]<lo)lo=v[i];if(v[i]>hi)hi=v[i];}printf(\"%d %d\\n\",lo,hi);"),
("modular_power", "Compute modular exponentiation by repeated squaring.", "445", "long long base=7,exp=128,mod=1000,result=1;while(exp){if(exp&1)result=result*base%mod;base=base*base%mod;exp>>=1;}printf(\"%lld\\n\",result);"),
("perfect_square", "Test an integer for being a perfect square without floating point.", "1 0", "int v[]={0,49,50},out[3];for(int k=0;k<3;k++){int i=0;while(i*i<v[k])i++;out[k]=(i*i==v[k]);}printf(\"%d %d\\n\",out[1],out[2]);"),
("prime_count", "Count primes up to thirty with the Sieve of Eratosthenes.", "10", "int prime[31];for(int i=0;i<=30;i++)prime[i]=1;prime[0]=prime[1]=0;for(int p=2;p*p<=30;p++)if(prime[p])for(int j=p*p;j<=30;j+=p)prime[j]=0;int n=0;for(int i=2;i<=30;i++)n+=prime[i];printf(\"%d\\n\",n);"),
("reverse_digits", "Reverse the decimal digits of a nonnegative integer.", "654321", "int n=123456,rev=0;while(n){rev=rev*10+n%10;n/=10;}printf(\"%d\\n\",rev);"),
("rotate_left", "Rotate an array left by two positions.", "3 4 5 1 2", "int v[]={1,2,3,4,5},n=5,k=2;for(int r=0;r<k;r++){int first=v[0];for(int i=0;i<n-1;i++)v[i]=v[i+1];v[n-1]=first;}for(int i=0;i<n;i++)printf(\"%s%d\",i?\" \":\"\",v[i]);puts(\"\");"),
("string_length", "Measure a null-terminated string without library length helpers.", "polyglot 8", "const char*s=\"polyglot\";size_t n=0;while(s[n])n++;printf(\"%s %zu\\n\",s,n);"),
("sum_array", "Accumulate integer values in a single pass.", "15", "int v[]={1,2,3,4,5},sum=0;for(int i=0;i<5;i++)sum+=v[i];printf(\"%d\\n\",sum);"),
("unique_count", "Count distinct values in a small integer array.", "4", "int v[]={2,1,2,3,1,4},n=6,count=0;for(int i=0;i<n;i++){int seen=0;for(int j=0;j<i;j++)if(v[j]==v[i])seen=1;if(!seen)count++;}printf(\"%d\\n\",count);"),
("vector_dot", "Compute the dot product of two integer vectors.", "32", "int a[]={1,2,3},b[]={4,5,6},sum=0;for(int i=0;i<3;i++)sum+=a[i]*b[i];printf(\"%d\\n\",sum);"),
]

catalog=[]
for name, desc, expected, cbody in algorithms:
    # C: each translation unit is standalone and warning-clean under C11.
    csrc='#include <stdio.h>\n#include <string.h>\n#include <stddef.h>\n\nint main(void) {\n    '+cbody+'\n    return 0;\n}\n'
    (root/f'examples/c/lab/{name}.c').parent.mkdir(parents=True,exist_ok=True)
    (root/f'examples/c/lab/{name}.c').write_text(csrc,encoding='utf-8')
    # C++ uses standard library output; algorithm statements are equivalent.
    cppbody=cbody.replace('printf("%d\\n",m);','std::cout << m << "\\n";')
    # Produce C++ source from same logic by converting printf/puts calls only;
    # use explicit per-output translation for portable, idiomatic iostream code.
    couts={
      'array_max':'int v[]={-4,7,2,0};int m=v[0];for(int i=1;i<4;i++)if(v[i]>m)m=v[i];std::cout<<m<<"\\n";',
      'binary_search':'int v[]={1,3,5,7,9};int lo=0,hi=4,x=5,ans=-1;while(lo<=hi){int mid=lo+(hi-lo)/2;if(v[mid]==x){ans=mid;break;}if(v[mid]<x)lo=mid+1;else hi=mid-1;}std::cout<<ans<<"\\n";',
      'bit_count':'unsigned int x=0xB5u;int n=0;while(x){n+=int(x&1u);x>>=1;}std::cout<<n<<"\\n";',
      'bubble_sort':'int v[]={5,1,4,2,8};for(int i=0;i<5;i++)for(int j=0;j<4-i;j++)if(v[j]>v[j+1]){int t=v[j];v[j]=v[j+1];v[j+1]=t;}for(int i=0;i<5;i++)std::cout<<(i?" ":"")<<v[i];std::cout<<"\\n";',
      'clamp':'int v[]={17,-9,4};int lo=-3,hi=10;for(int i=0;i<3;i++){int x=v[i];if(x<lo)x=lo;if(x>hi)x=hi;std::cout<<(i?" ":"")<<x;}std::cout<<"\\n";',
      'collatz_steps':'unsigned long long n=27;int steps=0;while(n!=1){n=n%2?3*n+1:n/2;steps++;}std::cout<<steps<<"\\n";',
      'digit_sum':'int n=9876,sum=0;while(n){sum+=n%10;n/=10;}std::cout<<sum<<"\\n";',
      'extended_gcd':'int a=240,b=46,old_r=a,r=b,old_s=1,s=0,old_t=0,t=1;while(r){int q=old_r/r;int z=old_r-q*r;old_r=r;r=z;z=old_s-q*s;old_s=s;s=z;z=old_t-q*t;old_t=t;t=z;}std::cout<<old_r<<" "<<old_s<<" "<<old_t<<"\\n";',
      'insertion_sort':'int v[]={9,3,7,-1,3};for(int i=1;i<5;i++){int x=v[i],j=i;while(j>0&&v[j-1]>x){v[j]=v[j-1];j--;}v[j]=x;}for(int i=0;i<5;i++)std::cout<<(i?" ":"")<<v[i];std::cout<<"\\n";',
      'is_palindrome':'std::string s="level",t="hello";auto pal=[](const std::string&x){for(size_t i=0;i<x.size()/2;i++)if(x[i]!=x[x.size()-1-i])return false;return true;};std::cout<<pal(s)<<" "<<pal(t)<<"\\n";',
      'lcm':'int a=21,b=6,x=a,y=b;while(y){int r=x%y;x=y;y=r;}std::cout<<(a/x*b)<<"\\n";',
      'linear_search':'int v[]={4,8,15,16,23,42},x=16,i=0;while(i<6&&v[i]!=x)i++;std::cout<<(i<6?i:-1)<<"\\n";',
      'max_subarray':'int v[]={-2,1,-3,4,-1,2,1,-5,4},best=v[0],cur=v[0];for(int i=1;i<9;i++){cur=cur>0?cur+v[i]:v[i];if(cur>best)best=cur;}std::cout<<best<<"\\n";',
      'matrix_trace':'int a[3][3]={{1,2,3},{4,5,6},{7,8,9}},sum=0;for(int i=0;i<3;i++)sum+=a[i][i];std::cout<<sum<<"\\n";',
      'merge_sorted':'int a[]={0,2,7},b[]={1,3,8},o[6],i=0,j=0,k=0;while(i<3&&j<3)o[k++]=a[i]<b[j]?a[i++]:b[j++];while(i<3)o[k++]=a[i++];while(j<3)o[k++]=b[j++];for(i=0;i<6;i++)std::cout<<(i?" ":"")<<o[i];std::cout<<"\\n";',
      'min_max':'int v[]={12,-5,7,3,0},lo=v[0],hi=v[0];for(int i=1;i<5;i++){if(v[i]<lo)lo=v[i];if(v[i]>hi)hi=v[i];}std::cout<<lo<<" "<<hi<<"\\n";',
      'modular_power':'long long base=7,exp=128,mod=1000,result=1;while(exp){if(exp&1)result=result*base%mod;base=base*base%mod;exp>>=1;}std::cout<<result<<"\\n";',
      'perfect_square':'int v[]={0,49,50},out[3];for(int k=0;k<3;k++){int i=0;while(i*i<v[k])i++;out[k]=(i*i==v[k]);}std::cout<<out[1]<<" "<<out[2]<<"\\n";',
      'prime_count':'int prime[31];for(int i=0;i<=30;i++)prime[i]=1;prime[0]=prime[1]=0;for(int p=2;p*p<=30;p++)if(prime[p])for(int j=p*p;j<=30;j+=p)prime[j]=0;int n=0;for(int i=2;i<=30;i++)n+=prime[i];std::cout<<n<<"\\n";',
      'reverse_digits':'int n=123456,rev=0;while(n){rev=rev*10+n%10;n/=10;}std::cout<<rev<<"\\n";',
      'rotate_left':'int v[]={1,2,3,4,5},n=5,k=2;for(int r=0;r<k;r++){int first=v[0];for(int i=0;i<n-1;i++)v[i]=v[i+1];v[n-1]=first;}for(int i=0;i<n;i++)std::cout<<(i?" ":"")<<v[i];std::cout<<"\\n";',
      'string_length':'std::string s="polyglot";std::cout<<s<<" "<<s.size()<<"\\n";',
      'sum_array':'int v[]={1,2,3,4,5},sum=0;for(int i=0;i<5;i++)sum+=v[i];std::cout<<sum<<"\\n";',
      'unique_count':'int v[]={2,1,2,3,1,4},n=6,count=0;for(int i=0;i<n;i++){int seen=0;for(int j=0;j<i;j++)if(v[j]==v[i])seen=1;if(!seen)count++;}std::cout<<count<<"\\n";',
      'vector_dot':'int a[]={1,2,3},b[]={4,5,6},sum=0;for(int i=0;i<3;i++)sum+=a[i]*b[i];std::cout<<sum<<"\\n";',
    }
    cppsrc='#include <iostream>\n#include <string>\n\nint main() {\n    '+couts[name]+'\n    return 0;\n}\n'
    (root/f'examples/cpp/lab/{name}.cpp').parent.mkdir(parents=True,exist_ok=True)
    (root/f'examples/cpp/lab/{name}.cpp').write_text(cppsrc,encoding='utf-8')
    catalog.append({'name':name,'description':desc,'expected':expected,'c':f'examples/c/lab/{name}.c','cpp':f'examples/cpp/lab/{name}.cpp'})
(root/'examples/lab-catalog.json').write_text(json.dumps(catalog,indent=2)+'\n',encoding='utf-8')
print(f'Generated {len(catalog)} matching C/C++ examples.')

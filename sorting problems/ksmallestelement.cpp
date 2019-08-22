#include <iostream>
using namespace std;
int small(int a[],int n,int k)
{
    for(int i=0;i<k;i++)
    {
        int pos = i;
        int small = a[pos];
        for(int j=i+1;j<n;j++)
        {
            if(a[j]<small)
            {
                small= a[j];
                pos = j;
            }
        }
        int temp = a[i];
        a[i]= a[pos];
        a[pos]=temp;
    }
    return a[k-1];
}
int main()
{
    int b[100],n,k;
    cout<<"enter the size of the array"<<endl;
    cin>>n;
    cout<<"enter the elements";
    for(int i=0;i<n;i++)
        cin>>b[i];
    cout<<"enter k value"<<endl;
    cin>>k;
    cout<<"the "<<k<<" smallest element is "<<small(b,n,k);
}

// output

    // enter the array size : 5
    // enter the elements : 10 4 5 6 18
    // enter the k value : 3
    // the 3 smallest element is : 6

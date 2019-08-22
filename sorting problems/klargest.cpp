#include<iostream>
using namespace std;
void klarge(int a[],int n,int k)
{
    for(int i=0;i<k;i++)
    {
        int pos=i;
        int large = a[pos];
        for(int j= i+1;j<n;j++)
        {
            if(a[j]>large)
            {
                large=a[j];
                pos=j;
            }
        }
        int temp = a[i];
        a[i]=a[pos];
        a[pos]=temp;
        cout<<a[i]<<endl;
    }
}
int main()
{
    int b[100],n,k;
    cout<<"enter the array size :";
    cin>>n;
    cout<<"enter the elements :";
    for(int i=0;i<n;i++)
        cin>>b[i];
    cout<<"enter the number of elements to be displayed (k value) :";
    cin>>k;
    klarge(b,n,k);
}

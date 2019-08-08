#include<stdio.h>
#include<iostream>
using namespace std;
int highest(int arr[],int n)
{
    int maxi = arr[0];
    for(int i=0;i<n;i++)
    {
        if(arr[i]>maxi)
            maxi=arr[i];
    }
return maxi;
}
int main()
{
   int arr[20],n;
   cout<<"enter the array size"<<endl;
   cin>>n;
   cout<<"enter the elements"<<endl;
   for(int i=0;i<n;i++)
   {
        cin>>arr[i];

   }
   cout<<"the highest number is : "<<highest(arr,n);
}

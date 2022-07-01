//C++ program for quicksort

#include<iostream.h>

using namespace std;

int partn(int a[],int sta,int end)
{
	int piv=a[end];
	int i=(sta-1);
	
	for(int j=sta;j<=end-1;j++)
	{
		if(a[j]<piv)
		{
			i++;
			int t=a[i];
			a[i]=a[j];
			a[j]=t;
		}
	}
	
	int t=a[i+1];
	a[i+1]=a[end];
	a[end]=t;
	return(i+1);
}

void qui(int a[],int sta,int end)
{
	if(sta<end)
	{
		int p=partn(a,sta,end);
		qui(a,sta,p-1);
		qui(a,p+1,end);
	}
}

void printArr(int a[],int m)
{
	int i;
	for(i=0;i<m;i++)
	
	cout<<a[i]<< " ";
	
}

int main()
{
	int a[]={23, 8, 28, 13, 18, 26};
	int m=sizeof(a)/sizeof(a[0]);
	cout<<"Before sorting array elements are- \n";
	
	printArr(a ,m);
	qui(a,0,m-1);
	cout<<"\nAfter sorting array elements are- \n";
	printArr(a ,m);
	
	return 0;
}




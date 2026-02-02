#include <iostream>

using namespace std;

int main()
{
    string name;
    cout << "What is your name?"<<endl;
    cin>>name;
    cout<<"Hello"<<name<<endl;
    int id;
    cout << "What is your id?"<<endl;
    cin>>id;
    cout<<"Your ID is"<<id<<endl;
  
    int var1;
    cout<<"Var1: "<<endl;
    cin>>var1;
    cout<<"Var2: "<<endl;
    cin>>var2;
    int sum;
    sum = var1+var2;
    int diff;
    diff =var1-var2;
    int prod;
    prod = var1*var2;
    cout<<"var1: " <<var1 <<"\n";
    cout<<"var2: " <<var2 <<"\n";
    cout<<"Sum: " <<sum <<"\n";
    cout<<"Diff: " <<diff <<"\n";
    cout<<"Prod: " <<prod <<endl;

  

    cout<<"*"<<"\n"<<"**"<<"\n"<<"***"<<"\n"<<"**"<<"\n"<<"*"<<endl;
    return 0;
}

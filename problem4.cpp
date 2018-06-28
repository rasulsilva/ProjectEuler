/*
rasul silva
Project Euler
problem 4
*/
//answer: 906609
#include <stdio.h>
#include <iostream>
using namespace std;

int ispalindrome(int num){
    int orig = num;
    int n = num;
    int nrev =0;
    int ones;

    while(num != 0){
        ones = num % 10;
        nrev = (10*nrev) + ones;
        num = num/10;
    }//at conclusion of while nrev is generated

    if (nrev == orig) return 1;
    else return 0;
}


int main(){
  int max = 0;
  int prod = 0;
  for (int i = 1; i<1000; i++){
      for (int j = 1; j<1000; j++){
          prod = i * j;
          if ((ispalindrome(prod) == 1) && (prod > max)){
              max = prod;
          }

      }
  }
  cout << "max: " << max << endl;
  return 0;
};

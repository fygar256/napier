#!/usr/bin/python3
import mpmath
mpmath.mp.dps=10000

kaijou = 1
number = 1000
napier = mpmath.mpf('1.0')
 
for i in range(1,number+1):
  kaijou *= i;
  napier += mpmath.mpf('1.0') / kaijou;
 
print("計算結果 e =",end='')
print(napier)
print("mppmath.e =",end='')
print(mpmath.e) 

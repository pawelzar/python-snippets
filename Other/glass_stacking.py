You are given a number, N, of glasses. Your job is to determine the largest pyramid that can be built with the glasses provided, and then create that pyramid in the output.

A glass is represented in ASCII as follows:


 ***    
 * *    
 * *    
*****
Input
A single integer: N, indicating the number of glasses.
Output
The ASCII pyramid

Example for N between 6 and 9:


       ***       
       * *       
       * *       
      *****      
    ***   ***    
    * *   * *    
    * *   * *    
   ***** *****   
 ***   ***   *** 
 * *   * *   * * 
 * *   * *   * * 
***** ***** *****
Constraints
0<N<30
Example
Input
4
Output
    ***    
    * *    
    * *    
   *****   
 ***   *** 
 * *   * * 
 * *   * * 
***** *****


n = int(input())

count = 0
height = 0
while count + height < n:
    height += 1
    count += height

for i in range(1, height + 1):
    for line in [' ***  ', ' * *  ', ' * *  ', '***** ']:
        print('{:^{}}'.format(line * i, height * 6)[:-1])

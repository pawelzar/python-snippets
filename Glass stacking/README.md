# Glass stacking

You are given a number, N, of glasses. Your job is to determine the largest pyramid that can be built with the glasses provided, and then create that pyramid in the output.

A glass is represented in ASCII as follows:

```
 ***    
 * *    
 * *    
*****
```

### INPUT:

A single integer: N, indicating the number of glasses.

### OUTPUT:

The ASCII pyramid

Example for N between 6 and 9:

```
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
```

### CONSTRAINTS:

0 < N < 30

### EXAMPLE:

Input

```
4
```

Output

```
    ***    
    * *    
    * *    
   *****   
 ***   *** 
 * *   * * 
 * *   * * 
***** *****
```

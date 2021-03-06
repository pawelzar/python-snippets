# Autobiographical number

Your program must read N positive integer X and print for each of them:
1 if X is an autobiographical number.
0 if X is not autobiographical.

An autobiographical number is a number whose first digit counts how many zeros are in the number, the second digit counts how many ones are in the number, and so on.
More formally, a number is autobiographical if it contains O occurrences of the digit M where O is the digit at index M in the number.
For example, 1210 is an autobiographical number because it contains:

The 0 digit 1 time.

The 1 digit 2 times.

The 2 digit 1 time.

The 3 digit 0 times.

### INPUT:

Line 1 : 1 integer N

N next lines : 1 integer X

### OUTPUT:

N lines: for each integer X, 1 if it is autobiographical, 0 otherwise.

### CONSTRAINTS:

1 ≤ N < 5

0 ≤ X < 10000000000

### EXAMPLE:

Input

```
2
1210
22
```

Output

```
1
0
```

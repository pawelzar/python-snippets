# Burrows-Wheeler transform

Compute the Burrows-Wheeler transform of the given string. The algorithm is as follows:

Given a string, say BAHAMAS, compute the list of all cyclic rotations of the string:

```
BAHAMAS
SBAHAMA
ASBAHAM
MASBAHA
AMASBAH
HAMASBA
AHAMASB
```

Sort this list of strings lexicographically, and the result is the string made of the last characters of each line, preceded by the position of the original text in this sorted list:

```
AHAMASB 1
AMASBAH 2
ASBAHAM 3
BAHAMAS 4 <-- original text
HAMASBA 5
MASBAHA 6
SBAHAMA 7
```

The result is therefore 4BHMSAAA.

### INPUT:

A string s made of uppercase letters: A-Z.

### OUTPUT:

The Burrows-Wheeler transform of the given string.

### CONSTRAINTS:

0 < length of s < 200

### EXAMPLE:

Input

```
BAHAMAS
```


Output
```
4BHMSAAA
```

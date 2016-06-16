The program:
You program must read two strings message and key and output the decrypted message using the Vigenère cipher.

The character 'a' is by convention equivalent to 0 and 'z' is equivalent to '25'.

Decryption rules:
if message[i] = ' ' (space) then decrypted_message[i] = ' ' (space)

else decrypted_message[i] = (message[i] - key[i]) modulo 26

In this exercise, message and key have the same length.

INPUT:
Line 1: a string message.
Line 2: a string key.

OUTPUT:
message decrypted using the Vigenère cipher.

CONSTRAINTS:
message contains only lowercase letters and spaces.

EXAMPLE:
Input
cpfioiang
abcabcabc
Output
codingame


message = [ord(x)-97 for x in input()]
key = [ord(x)-97 for x in input()]
print("".join(' 'if a == -65 else chr(97 + (a-b) % 26) for a, b in zip(message, key)))

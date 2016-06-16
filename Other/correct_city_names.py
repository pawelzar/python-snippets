"""
Given a well written list of cities, your program must clean another list of cities that are sometime miswritten.

Miswritten cities can contain or lack spaces, or have a different case than expected.

INPUT:
Line 1: The number N of cities.
Next N lines: A string cityName.
Next line: The number M of cities to clean.
Next M lines: A string uncleanedCityName.

OUTPUT:
M lines: Strings containing cleaned city names.

CONSTRAINTS:
2 ≤ N ≤ 5
1 ≤ M ≤ 20
1 ≤ length of cityName ≤ 30
1 ≤ length of uncleanedCityName ≤ 30

EXAMPLE:
Input
2
Montpellier
New York
3
new york
NewYork
montpellier
Output
New York
New York
Montpellier


01 Test 1
2
Montpellier
New York
3
new york
NewYork
montpellier
New York
New York
Montpellier
02 Test 2
2
Kyoto
Tokyo
1
tokyo
Tokyo
03 Test 3
2
Saint Petersburg
San Francisco
1
San Fran Cisco
San Francisco
04 Test 4
2
Helsinki
Hanoi
2
Hanoi
Helsinki
Hanoi
Helsinki
05 Test 5
5
Sydney
Newcastle upon Tyne
Marrakech
Le Mans
Vienna
20
le mans
Newcastle Upon Tyne
MarraKech
sydney
LeMans
VIENNA
NEWCASTLEuponTYNE
SYDNEY
Marr a kech
Newcastle upon Tyne
vienna
marrakech
Vien na
le Mans
Newcastleupon Tyne
Sydney
Lemans
m A R R A K E C H
VIenna
SydneY
Le Mans
Newcastle upon Tyne
Marrakech
Sydney
Le Mans
Vienna
Newcastle upon Tyne
Sydney
Marrakech
Newcastle upon Tyne
Vienna
Marrakech
Vienna
Le Mans
"""

correct = {}
for i in range(int(input())):
	word = input()
	correct["".join(word.lower().split())] = word

incorrect = [input() for i in range(int(input()))]
for word in incorrect:
	print(correct["".join(word.lower().split())])

# Python 2.7 short version
c={}
for i in range(input()):w=raw_input();c["".join(w.lower().split())]=w
for w in [raw_input() for i in range(input())]:print c["".join(w.lower().split())]

# Python 3.5 short version
i=input;c={}
for _ in range(int(i())):w=i();c["".join(w.lower().split())]=w
for w in[i()for _ in range(int(i()))]:print(c["".join(w.lower().split())])

# Kata Roman Numerals

## Background
The Romans wrote numbers using letters : I, V, X, L, C, D, M. (notice these letters have lots of straight lines and are hence easy to hack into stone tablets)

## Exercise
Write a function that converts a number to a roman numeral.
Eg. The number "5" should return "V"

## Rules for Roman numerals

### Roman letters (Numerals) value
| Value | Numeral |
| ----- | ------- |
|1	    |  I      |
|5      |  V      |
|10	    |  X      |
|50     |  L      |
|100    |	 C      |
|500    |	 D      |
|1000   |	 M      |

### Rule 1: Repetation 
When certain numerals are repeated, the number represented by them is their sum. 
For example, II = 1 + 1 = 2, or XX = 10 + 10 = 20, or, XXX = 10 + 10 + 10 = 30.

### Rule 2: Max 3 Repetation
It is to be noted that no Roman numerals can come together more than 3 times. 
For example, we cannot write 40 as XXXX

### Rule 3: V, L and D are note repeated
The letters V, L, and D are not repeated.

### Rule 4: Subtraction numerals
Only I, X, and C can be used as subtractive numerals. 
There can be 6 combinations when we subtract. These are: 
IV = 5 - 1 = 4; IX = 10 - 1 = 9; XL = 50 - 10 = 40; 
XC = 100 - 10 = 90; CD = 500 - 100 = 400; and CM = 1000 - 100 = 900

### Rule 5: Sum with greater numerals
When a Roman numeral is placed after another Roman numeral of greater value, the result is the sum. 
For example, VIII = 5 + 1 + 1 + 1 = 8, or, XV = 10 + 5 = 15,

### Rule 6: Subtraction numerals
When a Roman numeral is placed before another Roman numeral of greater value, 
the result is the difference between the numerals. 
For example, IV = 5 - 1 = 4, or, XL = 50 - 10 = 40, or XC = 100 - 10 = 90

### Rule 7: Numeral between 2 greater numerals
When a Roman numeral of a smaller value is placed between two numerals of greater value, 
it is subtracted from the numeral on its right. 
For example, XIV = 10 + (5 - 1) = 14, or, XIX = 10 + (10 - 1) = 19
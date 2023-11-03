<h1>Handbook on Programming in Python</h1>

**AP Computer Science Principles 2023-2024**

Sawyer Haldemann

<!-- This is a comment (which will not be displayed in the live file);
replace all "???" with your own text. -->




___





<h1>Table of Contents</h1>

- [1. Compiling and Running](#1-compiling-and-running)
- [2. Data Types](#2-data-types)
- [3. Console I/O](#3-console-io)
- [4. Arithmetic Operations](#4-arithmetic-operations)
- [5. Assignment Operations](#5-assignment-operations)
- [6. Comments](#6-comments)
- [7. Decision Structures](#7-decision-structures)
- [8. Conditional Operators](#8-conditional-operators)
- [9. Logic Operators](#9-logic-operators)
- [10. Advanced Decision Structures](#10-advanced-decision-structures)
- [11. String Methods](#11-string-methods)
- [12. Random Generation](#12-random-generation)
- [13. Looping Structures](#13-looping-structures)
- [14. Functions/Methods](#14-functionsmethods)
- [15. Elementary Data Structures](#15-elementary-data-structures)
  - [15.1 Arrays/Lists](#151-arrayslists)
  - [15.2 Matrices](#152-matrices)
- [References](#references)




___





# 1. Compiling and Running

Not compiled.

Run using *python fileName.py*


___





# 2. Data Types

int: Whole numbers, positive/negative

float: Any real number

str: Characters: letters, numbers, symbols

bool: True or False

list: Contains items of other data types

tuple: A list, but unchangable

dict: Like a list, but connects two items

set: Like a list, but no specific order

range: A sequence of numbers

```python
a = int(1)
b = float(2.439857)
c = str("Hello, 1, #&*(")
d = False
e = list(1, 2.384759, "Hello", False)
f = tuple(2, 3, 5, 7, 11)
g = {"name": "Sawyer", "age": 17}
h = set(2, 4, 8, 16, 32, 64)
i = range(1, 11, 2)
```

___





# 3. Console I/O

*print()* will print whatever is inside

*input()* will take an imput from the user

*input("")* will give a prompt first

___





# 4. Arithmetic Operations

+, -, *, and / work normally: addition, subtraction, multiplication, division

Double asterisks for exponents

% for mod, returns remainder

\ for division, minus remainder

abs() gives absolute value

*import math*

sqrt() gives the square root

___





# 5. Assignment Operations

x = y

x += y (x + y)

*same for any opperation*

x++ does not work



___





# 6. Comments

```python
#one line
"""
Multiple
Lines
"""
```


___





# 7. Decision Structures

if

elif

else


___





# 8. Conditional Operators

==

!= (not equal)

'<'

'>'

'<='

'>='

___





# 9. Logic Operators

*and, or, not*

___





# 10. Advanced Decision Structures



n = 1 if *condition* else 2



___





# 11. String Methods

lower/upper() *change case*

strip() *remove 'whitespace', spaces, from start/end*

split() *can specify what to 'split' by, default is spaces/whitespace*

join() *self explanatory*

index() *gets the index*

replace *('removed', 'added')*

starts/endswith() *true or false*

count() *Counts*

isdigit/alpha() *True/False, number/letter*

capitalize() *first yes, rest not.*
___





# 12. Random Generation

*import random*

.randint() *plus range*

.random() *0 to 1*

.uniform() *float in a range*

.choice(list)

.shuffle() *Very useful*


___





# 13. Looping Structures

for *var* in *range/list:

*i in range(1, 10)*

*item in list*

while *condition*

'break' to exit early

'continue' to skip

___





# 14. Functions/Methods

def f(thing):
  
  some = thing
  
  return some

___





# 15. Elementary Data Structures

:/


## 15.1 Arrays/Lists

list, tuple






## 15.2 Matrices

*import numpy as np*

np.array([[1, 2], [3, 4]])

*each set of numbers is a row. each next row is below the others:*

1  2

3  4



___


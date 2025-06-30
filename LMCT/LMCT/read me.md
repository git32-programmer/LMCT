# LMCT (Logical Mathematical File Turtle) Module Documentation

## Overview

LMCT is a comprehensive utility module providing the following feature sets:

- Logical operations and Boolean algebra
- Mathematical calculations and number theory
- Filesystem operations and management
- Turtle graphics and geometric shapes
- String manipulation and validation
- Time and date operations
- Input validation and security checks

## Dependencies

Required modules: **time, os, math, turtle, shutil, re, typing, pathlib, dataclasses, subprocess, functools, logging, matplotlib, itertools**

## Installation

```bash
pip install required-module-name
```

### To learn more about pip commands, please refer to [pip command tutorial](https://www.runoob.com/w3cnote/python-pip-install-usage.html)

## Usage Example

```python
from LMCT import factorial, square

print(factorial(5))  # Output: 120
square(100)          # Draws a square with side length 100
```

## Function List

### 1. Logical Operations

| Function Name | Parameters                    | Return Type | Description                               |
| ------------- | ----------------------------- | ----------- | ----------------------------------------- |
| nand          | a: bool, b: bool              | bool        | Performs NAND logical operation           |
| nor           | a: bool, b: bool              | bool        | Performs NOR logical operation            |
| xand          | a: bool, b: bool              | bool        | Performs XAND logical operation           |
| three_and     | a: bool, b: bool, c: bool     | bool        | Three-input AND gate operation            |
| three_or      | a: bool, b: bool, c: bool     | bool        | Three-input OR gate operation             |
| three_nor     | a: bool, b: bool, c: bool     | bool        | Three-input NOR gate operation            |
| three_nand    | a: bool, b: bool, c: bool     | bool        | Three-input NAND gate operation           |
| if_return     | boolean: bool, a: Any, b: Any | Any         | Returns a if boolean is True, otherwise b |

### 2. Mathematical Functions

| Function Name | Parameters                          | Return Type | Description                                |
| ------------- | ----------------------------------- | ----------- | ------------------------------------------ |
| even_odd      | mode: str, num: int                 | str         | Determines if number is even or odd        |
| calculate     | mode: str, num1: float, num2: float | float       | Performs various mathematical calculations |
| factorial     | n: int                              | int         | Calculates factorial of n                  |
| fibonacci     | n: int                              | int         | Calculates nth Fibonacci number            |
| prime_check   | n: int                              | bool        | Checks if number is prime                  |
| gcd           | a: int, b: int                      | int         | Calculates greatest common divisor         |
| lcm           | a: int, b: int                      | int         | Calculates least common multiple           |
| permutation   | n: int, r: int                      | int         | Calculates permutations                    |
| combination   | n: int, r: int                      | int         | Calculates combinations                    |

### 3. File Operations

| Function Name | Parameters                    | Return Type | Description                  |
| ------------- | ----------------------------- | ----------- | ---------------------------- |
| safe_cmd      | command: str                  | None        | Executes safe system command |
| file_print    | file_path: str                | None        | Prints file content          |
| file_write    | file_path: str, content: str  | None        | Writes content to file       |
| file_append   | file_path: str, content: str  | None        | Appends content to file      |
| file_delete   | file_path: str                | None        | Deletes file                 |
| file_rename   | file_path: str, new_name: str | None        | Renames file                 |
| file_copy     | file_path: str, new_path: str | None        | Copies file                  |
| file_size     | file_path: str                | int/str     | Gets file size               |
| file_info     | file_path: str                | dict/str    | Gets file information        |

### 4. Turtle Graphics

| Function Name | Parameters                        | Return Type | Description                |
| ------------- | --------------------------------- | ----------- | -------------------------- |
| square        | length: int                       | None        | Draws square               |
| triangle      | length: int                       | None        | Draws equilateral triangle |
| rectangle     | length: int, width: int           | None        | Draws rectangle            |
| star          | size: int                         | None        | Draws five-pointed star    |
| parallelogram | length: int, width: int           | None        | Draws parallelogram        |
| polygon       | number_of_sides: int, length: int | None        | Draws regular polygon      |
| ellipse       | width: int, height: int           | None        | Draws ellipse              |
| spiral        | size: float, turns: int           | None        | Draws spiral               |
| flower        | petals: int, size: int            | None        | Draws flower pattern       |
| fractal_tree  | size: int, depth: int             | None        | Draws fractal tree         |
| snowflake     | size: int, depth: int             | None        | Draws snowflake pattern    |
| heart         | size: int                         | None        | Draws heart shape          |

### 5. String Functions

| Function Name    | Parameters | Return Type | Description                       |
| ---------------- | ---------- | ----------- | --------------------------------- |
| string_reverse   | text: str  | str         | Reverses string                   |
| palindrome_check | text: str  | bool        | Checks if string is palindrome    |
| word_count       | text: str  | int         | Counts words in string            |
| string_to_list   | text: str  | list        | Converts string to character list |
| list_to_string   | list: list | str         | Converts list to string           |
| string_to_tuple  | text: str  | tuple       | Converts string to tuple          |

### 6. Base Conversion

| Function Name          | Parameters           | Return Type | Description                     |
| ---------------------- | -------------------- | ----------- | ------------------------------- |
| binary_to_decimal      | binary_str: str      | int         | Converts binary to decimal      |
| decimal_to_binary      | decimal_num: int     | str         | Converts decimal to binary      |
| binary_to_hexadecimal  | binary_str: str      | str         | Converts binary to hexadecimal  |
| hexadecimal_to_binary  | hexadecimal_str: str | str         | Converts hexadecimal to binary  |
| decimal_to_hexadecimal | decimal_num: int     | str         | Converts decimal to hexadecimal |
| hexadecimal_to_decimal | hexadecimal_str: str | int         | Converts hexadecimal to decimal |
| decimal_to_octal       | decimal_num: int     | str         | Converts decimal to octal       |

### 7. Time Functions

| Function Name   | Parameters                 | Return Type | Description                          |
| --------------- | -------------------------- | ----------- | ------------------------------------ |
| time_convert    | time_str: str, format: str | str         | Converts time format                 |
| date_calculate  | date_str: str, days: int   | str         | Calculates date addition/subtraction |
| time_difference | time1: str, time2: str     | str         | Calculates time difference           |

### 8. Validation Functions

| Function Name     | Parameters    | Return Type | Description                    |
| ----------------- | ------------- | ----------- | ------------------------------ |
| email_validate    | email: str    | bool        | Validates email format         |
| phone_validate    | phone: str    | bool        | Validates phone number format  |
| password_strength | password: str | str         | Checks password strength level |

## License

This module is free to use and modify. Attribution is appreciated but not required.

Original author: damnTurboWarp/Aherent/git32-peogrammer

## Contact Information

Please see the first **README.md** file in the repository (two folders up) for contact details.
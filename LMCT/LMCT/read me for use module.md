# LMCT (Logic Math File Turtle)

## Module Overview

**cnLMCT** is a comprehensive utility module that offers a wide range of functions, including logical operations, mathematical calculations, file system operations, turtle graphics drawing, string manipulation, base conversion, time processing, and input validation.

## Module Information

* ​**Version**​: Official version cnLMCT 10.6.8
* ​**Author**​: Egg TurboWarp
* ​**QQ Email**​: codemao23@qq.com
* ​**CodeMao Personal Center**​: [Personal Center](https://shequ.codemao.cn/user/1274549095)
* ​**Bilibili**​: [Bilibili](https://space.bilibili.com/1402822998?spm_id_from=333.1007.0.0)
* ​**Date**​: 2025-05-12
* ​**Last Updated**​: 2025-05-14 19:33

### Function Set

* Logical and boolean operations
* Mathematical calculations and number theory
* File system operations and turtle graphics drawing
* String processing and validation
* Time and date operations
* Input validation and security checks

## Module Structure and Function List

### 1. Log Management

| Function                       | Description                                                                 |
| -------------------------------- | ----------------------------------------------------------------------------- |
| Log file creation and rotation | Automatically manage log files to prevent an excessive number of junk files |
| Log level control              | Support multi-level log filtering                                           |
| Log formatting                 | Unify log output format                                                     |

### 2. Auxiliary Functions

| Function Name | Function                                                | Parameters | Return Value       |
| --------------- | --------------------------------------------------------- | ------------ | -------------------- |
| process\_data | Simple data processing, returns None if an error occurs | data: T    | Optional[T]        |
| chinese\_name | Decorator to add a Chinese name to a function           | name: str  | Decorated function |

### 3. Logic Operations

| Function Name         | Function                                   | Parameters    | Return Value        |
| ----------------------- | -------------------------------------------- | --------------- | --------------------- |
| NAND Gate             | Perform NAND logical operation             | a, b: bool    | bool                |
| NOR Gate              | Perform NOR logical operation              | a, b: bool    | bool                |
| XNOR Gate             | Perform XNOR logical operation             | a, b: bool    | bool                |
| Three-Input AND Gate  | Perform three-input AND logical operation  | a, b, c: bool | bool                |
| Three-Input OR Gate   | Perform three-input OR logical operation   | a, b, c: bool | bool                |
| Three-Input NOR Gate  | Perform three-input NOR logical operation  | a, b, c: bool | bool                |
| Three-Input NAND Gate | Perform three-input NAND logical operation | a, b, c: bool | bool                |
| Conditional Return    | Conditional judgment to return a value     | boolean       | Same type as a or b |

### 4. Math Functions

| Function Name           | Function                                | Parameters            | Return Value                        |
| ------------------------- | ----------------------------------------- | ----------------------- | ------------------------------------- |
| Even/Odd Check          | Check the parity of a number            | mode: str, num: int   | str                                 |
| Calculate               | Perform various mathematical operations | mode: str, num1, num2 | Calculation result or error message |
| Factorial               | Calculate the factorial                 | n: int                | int or 'Invalid input'              |
| Fibonacci               | Calculate the Fibonacci sequence        | n: int                | int or 'Invalid input'              |
| Prime Check             | Check if a number is prime              | n: int                | bool                                |
| Greatest Common Divisor | Calculate the greatest common divisor   | a, b: int             | int                                 |
| Least Common Multiple   | Calculate the least common multiple     | a, b: int             | int                                 |
| Permutation             | Calculate the number of permutations    | n, r: int             | int or 'Invalid input'              |
| Combination             | Calculate the number of combinations    | n, r: int             | int or 'Invalid input'              |

### 5. File Operations

| Function Name    | Function                              | Parameters            | Return Value             |
| ------------------ | --------------------------------------- | ----------------------- | -------------------------- |
| Safe Command     | Safely execute system commands        | command: str          | None                     |
| File Print       | Print the content of a file           | file\_path: str       | None                     |
| File Write       | Write content to a file               | file\_path, content   | None                     |
| File Append      | Append content to a file              | file\_path: str       | None                     |
| File Delete      | Delete a file                         | file\_path: str       | None                     |
| File Rename      | Rename a file                         | file\_path, new\_name | None                     |
| File Copy        | Copy a file                           | file\_path, new\_path | None                     |
| File Size        | Get the size of a file                | file\_path: str       | int or 'File not found'  |
| File Information | Get detailed information about a file | file\_path: str       | dict or 'File not found' |
| File Search      | Search for matching files             | directory, pattern    | list[str]                |

### 6. Turtle Graphics

| Function Name      | Function             | Parameters         | Return Value |
| -------------------- | ---------------------- | -------------------- | -------------- |
| Draw Square        | Draw a square        | length: int        | None         |
| Draw Triangle      | Draw a triangle      | length: int        | None         |
| Draw Rectangle     | Draw a rectangle     | length, width: int | None         |
| Draw Star          | Draw a star          | size: int          | None         |
| Draw Parallelogram | Draw a parallelogram | length, width: int | None         |
| Draw Polygon       | Draw a polygon       | sides, length: int | None         |
| Draw Ellipse       | Draw an ellipse      | width, height: int | None         |
| Draw Spiral        | Draw a spiral        | size, turns: int   | None         |
| Draw Flower        | Draw a flower        | petals, size: int  | None         |
| Draw Fractal Tree  | Draw a fractal tree  | size, depth: int   | None         |
| Draw Snowflake     | Draw a snowflake     | size, depth: int   | None         |
| Draw Heart         | Draw a heart         | size: int          | None         |

### 7. String Functions

| Function Name    | Function                              | Parameters           | Return Value |
| ------------------ | --------------------------------------- | ---------------------- | -------------- |
| String Reverse   | Reverse a string                      | text: str            | str          |
| Palindrome Check | Check if a string is a palindrome     | text: str            | bool         |
| Word Count       | Count the number of words in a string | text: str            | int          |
| String to List   | Convert a string to a list            | text: str            | list         |
| List to String   | Convert a list to a string            | list: list           | str          |
| String to Tuple  | Convert a string to a tuple           | text: str            | tuple        |
| String to ASCII  | Convert a string to ASCII codes       | text: str, sep: str  | str          |
| ASCII to String  | Convert ASCII codes to a string       | ascii: str, sep: str | str          |

### 8. Base Conversion

| Function Name          | Function                       | Parameters        | Return Value |
| ------------------------ | -------------------------------- | ------------------- | -------------- |
| Binary to Decimal      | Convert binary to decimal      | binary: str       | int          |
| Decimal to Binary      | Convert decimal to binary      | decimal\_num: int | str          |
| Binary to Hexadecimal  | Convert binary to hexadecimal  | binary\_str: str  | str          |
| Hexadecimal to Binary  | Convert hexadecimal to binary  | hex\_str: str     | str          |
| Decimal to Hexadecimal | Convert decimal to hexadecimal | decimal\_num: int | str          |
| Hexadecimal to Decimal | Convert hexadecimal to decimal | hex\_str: str     | int          |
| Decimal to Octal       | Convert decimal to octal       | decimal\_num: int | str          |

### 9. Time Functions

| Function Name               | Function                             | Parameters                  | Return Value                 |
| ----------------------------- | -------------------------------------- | ----------------------------- | ------------------------------ |
| Time Conversion             | Convert time formats                 | time\_str: str, format: str | str or ValueError            |
| Date Calculation            | Perform date addition or subtraction | date\_str: str, days: int   | str or 'Invalid date'        |
| Time Difference Calculation | Calculate the time interval          | time1, time2: str           | str or 'Invalid time format' |

### 10. Validation Functions

| Function Name           | Function                                | Parameters    | Return Value         |
| ------------------------- | ----------------------------------------- | --------------- | ---------------------- |
| Email Validation        | Validate the format of an email address | email: str    | bool                 |
| Phone Validation        | Validate the format of a phone number   | phone: str    | bool                 |
| Password Strength Check | Check the strength of a password        | password: str | str (strength level) |

## Dependencies

* Python compiler, version 3.6 or higher
* Install the following modules: `time, os, math, turtle, shutil, re, typing, pathlib, dataclasses, subprocess, functools, logging`
* ​**Installation command**​: `pip install module_name` (run in CMD)

## Usage Example

```python
>>> from cnLMCT import factorial
>>> factorial(5)
120
```

## Notes

1. All functions have built-in automatic logging.
2. Comprehensive error handling mechanisms are in place.
3. Automatic resource recycling is implemented.
4. Thread-safe design is adopted.
5. Memory-efficient implementation is achieved.

## License

* This module can be freely used and modified. However, important code should not be easily modified.
* If you make modifications, please indicate the source.
* Original author: Eggy TurboWarp
* Likes and purchase records on CodeMao and GitHub platforms belong to the original author.
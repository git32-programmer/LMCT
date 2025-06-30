# LMCT module types

1. international edition
2. chinese edition

# LMCT description

## A module for programming beginners. It's very good.
## Author is damnTurboWarp, a member at the Codemao community.

# LMCT language

## LMCT module is pure python code, it's very easy to learn.
## I don't publish to PyPI, because I feel it sucks.

# LMCT peculiarity

## This module can record your used functions and time to a log file (C:\lmct prefetch folder).
## Module system:Windows

# LMCT author url, These urls is china country only(True?)

|author|url|
|--|--|
|damnTurboWarp|[Codemao community](https://shequ.codemao.cn/user/1274549095)|
|codemao23|QQ mail:codemao23@qq.com|
|nsjcehbwueibgxcwue(steam)|mail:codemao23@qq.com|
|git32-programmer|mail:github_2025@qq.com|

# LMCT document(comments)

```python
"""
    LMCT (Logical Mathematical File Turtle) Module
    Version: cnLMCT 16.4.87
    Author: damnTurboWarp
    Author Name Note: "damnturbowarp" is my codemao username
    QQ Email: codemao23@qq.com
    Date: 2025-05-12
    Last Updated: 2025-06-30 11:34am :)

    Description:
        A comprehensive utility module providing the following feature sets:
        - Logical operations and Boolean algebra
        - Mathematical calculations and number theory
        - Filesystem operations and management
        - Turtle graphics and geometric shapes
        - String manipulation and validation
        - Time and date operations
        - Input validation and security checks

    Features:
        - Built-in logging for all functions
        - Comprehensive error handling
        - Type hints and documentation
        - Cross-platform compatibility
        - Resource management
        - Security considerations

    Module Structure:
        This module contains 12 main sections with over 69 functions:

        1. Log Management (Lines 142-156)
            - Log file creation and rotation
            - Log level control
            - Log formatting

        2. Helper Functions (Lines 159-171)
            - Data processing
            - Configuration management

        3. Logical Operations (Lines 172-215)
            - Basic gates: nand, nor, xand
            - Extended operations: three_and, three_or, three_nor, three_nand
            - Complex logic: if_return

        4. Mathematical Functions (Lines 213-397)
            - Logic: even_odd, prime_check
            - Tools: calculate, factorial, fibonacci
            - Number theory: gcd, lcm
            - Combinatorics: permutation, combination, matrix
            - Others: probability and statistics

        5. File Operations (Lines 396-443)
            - Control: safe_cmd
            - File tools: file_print, zip, encrypt, decrypt
            - Basic I/O: file_write, file_append, file_delete
            - Resource management: file_rename, file_copy, file_move
            - File information: file_size, file_info, file_search
            - Images: img_pcs, img_rotate

        6. Turtle Graphics (Lines 525-652)
            - Basic shapes: square, triangle, rectangle
            - Complex shapes: star, parallelogram, polygon
            - Curves: ellipse, spiral, heart
            - Advanced graphics: flower, fractal_tree, snowflake

        7. String Functions (Lines 660-707)
            - Text control: string_reverse, palindrome_check
            - Text analysis: word_count
            - Text tools: string_to_list, list_to_string, string_to_tuple, string_to_ascii, ascii_to_string

        8. Base Conversion (Lines 718-758)
            - Binary: binary_to_decimal, binary_to_hexadecimal
            - Decimal: decimal_to_binary, decimal_to_hexadecimal, decimal_to_octal
            - Hexadecimal: hexadecimal_to_binary, hexadecimal_to_decimal

        9. Time Functions (Lines 758-790)
            - Time conversion: time_convert
            - Time calculation: date_calculate, time_difference

        10. Validation Functions (Lines 793-831)
            - Input validation: email_validate, phone_validate
            - Security: password_strength
    
        11. Others (Lines 831-845)
            - Undefined: draw_3d
    
        12. Internal Functions (Lines 843-875)
            - Management: LogManager, TurtleManager
            - Other functions: safe_operation

    Dependencies:
        - Python 3.6+
        - Required modules: time, os, math, turtle, shutil, re, typing, pathlib, dataclasses, subprocess, functools, logging, matplotlib, pillow, mpl_toolkits.mpl3d
        - Install dependencies using: pip install module_name (run in cmd)
        - No external dependencies required

    Usage:
        Import the module and use any function directly:
        >>> from LMCT import factorial
        >>> factorial(5)
        120

    Notes:
        - All functions include automatic logging
        - Built-in error handling
        - Automatic resource cleanup
        - Thread-safe operations
        - Memory-efficient implementation

    License [copyright(C)]:
        This module is free to use and modify.
        Attribution is appreciated but not required.
        All likes and purchase records on the codemao platform (and GitHub) belong to the original author.
        Original author: damnTurboWarp/Aherent/git32-peogrammer (my usernames on other platforms, see README.md in the repository for profile URLs)
        Co-author (you): Please sign
    End line: 805(This version has been abridged!)
    Variable: i
    Type declaration: module
"""

```
# I may publish this module on PyPI (but it's very low priority)
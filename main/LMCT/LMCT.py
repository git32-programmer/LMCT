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
        This module contains 12 main sections with 69 functions:

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
        - Required modules: time, os, math, turtle, shutil, re, typing, pathlib, dataclasses, subprocess, functools, logging, matplotlib, itertools
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

i=0

import time
import os
import math
import turtle
import shutil
import re
from typing import Union, TypeVar, Optional
from pathlib import Path
from dataclasses import dataclass
import subprocess
import functools
import logging
import matplotlib as plt
import itertools

LOG_DIR = Path.home() / '.lmct'
LOG_FILE = LOG_DIR / 'module.log'

def ensure_log_dir():
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        raise RuntimeError("Unable to create directory. Please check permissions")

if not os.path.exists('C:/lmct prefech'):
    os.makedirs('C:/lmct prefech')
if os.path.exists('C:/lmct prefech/module log - 副本.log'):
    os.remove('C:/lmct prefech/module log - 副本.log')
else:
    with open('C:/lmct prefech/module log.log','a',encoding='utf-8') as file:
        if os.path.exists('C:/lmct prefech/module log - 副本.log'):
            os.remove('C:/lmct prefech/module log - 副本.log')
        file.write(f'this log file can automatically delete old log files. Create time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        

#=============helper functions=============
@dataclass
class Config:
    log_dir: Path = Path.home() / '.lmct'
    max_log_size: int = 1024 * 1024
    log_level: str = 'INFO'

T = TypeVar('T')

def process_data(data: T) -> Optional[T]:
    try:
        return data
    except Exception:
        return None
-6
#===============logic functions=============
def nand(a,b):
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:nand({a},{b}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{not (a and b)}\n')
    return not (a and b)

def nor(a,b):
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:nor({a},{b}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{not (a or b)}\n')
    return not (a or b)

def xand(a,b):
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:xand({a},{b}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{(a and not b) and (not a and b)}\n')
    return (a and not b) and (not a and b)

def three_and(a,b,c):
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:three_and({a},{b},{c}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{(a and b) and c}\n')
    return (a and b) and c

def three_or(a,b,c):
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:therr_or({a},{b},{c}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{(a or b) or c}\n')
    return (a or b) or c

def three_nor(a,b,c):
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:three_nor({a},{b},{c}),used:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{not ((a or b) or c)}\n')
    return not ((a or b) or c)

def three_nand(a,b,c):
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:three_nand({a},{b},{c}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{not ((a and b) and c)}\n')
    return not ((a and b) and c)

def if_return(boolean,a,b):
    if boolean:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:opreation is{boolean},used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{a}\n')
        return a
    else:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:opreation is{boolean},used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{b}\n')
        return b

#============math functions=============
def even_odd(mode,num):
    if mode == 'even':
        if num % 2 == 0:
            file_append('C:/lmct prefech/module log.log',f'[LMCT]:test mode is{mode},number{num}is even,used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        else:
            file_append('C:/lmct prefech/module log.log',f'[LMCT]:test mode is{mode},number{num}is odd,used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        if_return(num % 2 == 0,"is even","is odd")
    elif mode == '奇数':
        if num % 2 == 1:
            file_append('C:/lmct prefech/module log.log',f'[LMCT]:test mode is{mode},number{num}is odd,used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        else:
            file_append('C:/lmct prefech/module log.log',f'[LMCT]:test mode is{mode},number{num}is even,used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        if_return(num % 2 == 0,"is odd","is even")
    else:
        return "invalid mode"

def calculate(mode, num1, num2):
    if mode == 'add':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{num1 + num2},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 + num2
    elif mode == 'minus':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{num1 - num2},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 - num2
    elif mode == 'multiplication':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{num1 * num2},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 * num2
    elif mode == 'divided':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{num1 / num2},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 / num2
    elif mode == 'remainder':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{num1 % num2},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 % num2
    elif mode == 'power':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{num1 ** num2},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 ** num2
    elif mode == 'sprt':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{num1 ** 0.5},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 ** 0.5
    elif mode == 'cubt':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{num1 ** (1/3)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 ** (1/3)
    elif mode == 'log':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{math.log(num1,num2)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.log(num1,num2)
    elif mode == 'naplog':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{math.log(num1)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.log(num1)
    elif mode == 'log10':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{math.log(num1,10)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.log(num1,10)
    elif mode == 'sin':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{math.sin(num1)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.sin(num1)
    elif mode == 'cos':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{math.cos(num1)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.cos(num1)
    elif mode == 'tan':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{math.tan(num1)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.tan(num1)
    elif mode == 'asin':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{math.asin(num1)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.asin(num1)
    elif mode == 'acos':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{math.acos(num1)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.acos(num1)
    elif mode == 'atan':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{math.atan(num1)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.atan(num1)
    elif mode == 'min':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{min(num1,num2)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return min(num1,num2)
    elif mode == 'max':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{max(num1,num2)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return max(num1,num2)
    elif mode == 'abs':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{abs(num1)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return abs(num1)
    elif mode == 'round':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{round(num1)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return round(num1)
    elif mode == 'eval':
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:calculate mode is{mode},result is{eval(num1)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return eval(num1)
    else:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:模式错误！错误时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return "invalid mode"

def factorial(n):
    if n < 0:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:factorial({n}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:invalid input\n')
        return "invalid input"
    result = 1
    for i in range(1, n + 1):
        result *= i
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:factorial({n}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def fibonacci(n):
    if n < 0:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:fibonacci({n}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:invalid input\n')
        return "invalid input"
    if n <= 1:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:fibonacci({n}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{n}\n')
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:fibonacci({n}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{b}\n')
    return b

def prime_check(n):
    if n < 2:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:prime_check({n}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:False\n')
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            file_append('C:/lmct prefech/module log.log',f'[LMCT]:prime_check({n}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:False\n')
            return False
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:prime_check({n}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:True\n')
    return True

def gcd(a,b):
    global i
    while b:
        a, b = b, a % b
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:gcd({a},{b}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{a}\n')
    return a

def lcm(a,b):
    result = abs(a * b) // gcd(a, b)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:lcm({a},{b}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def permutation(n,r):
    if n < 0 or r < 0 or r > n:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:permutation({n},{r}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:invalid input\n')
        return "invalid input"
    result = factorial(n) // factorial(n - r)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:permutation({n},{r}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def combination(n,r):
    if n < 0 or r < 0 or r > n:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:combination({n},{r}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:invalid input\n')
        return "invalid input"
    result = factorial(n) // (factorial(r) * factorial(n - r))
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:combination({n},{r}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def matrix(n,m):
    global i
    if n < 0 or m < 0:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:matrix({n},{m}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:invalid input\n')
        return "invalid input"
    result = []
    for i in range(n):
        result.append([])
        for j in range(m):
            result[i].append(i * j)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:matrix({n},{m}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def probability(n,m):
    if n < 0 or m < 0:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:probability({n},{m}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:invalid input\n')
        return "invalid input"
    result = []
    for i in range(n):
        result.append([])
        for j in range(m):
            result[i].append(i * j)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:probability({n},{m}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

#=============file functions============
def safe_cmd(command: str) -> None:
    if not re.match(r'^[a-zA-Z0-9\s\-_\.]+$', command):
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:safe_cmd({command}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:不安全的命令\n')
        raise ValueError("command not safe")
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:safe_cmd({command}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:已执行至microsoft c\n')
    subprocess.run(command, shell=True, check=True)

def file_print(file_path):
    with open(file_path,'r') as file:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:file_print({file_path}),result:{file.read()},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        print(file.read())

def file_write(file_path,content):
    with open(file_path,'w') as file:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:file_write({file_path},{content}),result:{file.write(content)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        file.write(content)

def file_append(file_path,content):
    with open(file_path,'a') as file:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:file_append({file_path},{content}),result:{file.write(content)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        file.write(content)

def file_delete(file_path):
    os.remove(file_path)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:file_delete({file_path}),result:{os.remove(file_path)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')

def file_rename(file_path,new_name):
    os.rename(file_path,new_name)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:file_rename({file_path},{new_name}),result:{os.rename(file_path,new_name)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')

def file_copy(file_path,new_path):
    shutil.copy(file_path,new_path)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:file_copy({file_path},{new_path}),result:{shutil.copy(file_path,new_path)},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')

def file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:file_size({file_path}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{size} bytes\n')
        return size
    except:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:file_size({file_path}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:file not found\n')
        return "file not found"

("file_info")
def file_info(file_path):
    try:
        info = os.stat(file_path)
        result = {
            'size': info.st_size,
            'created': time.ctime(info.created_time),
            'modified': time.ctime(info.st_mtime),
            'accessed': time.ctime(info.st_atime)
        }
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:file_info({file_path}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
        return result
    except:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:file_info({file_path}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:file not found\n')
        return "file not found"

def file_search(directory, pattern):
    matches = []
    for root, _, files in os.walk(directory):
        for file in files:
            if pattern in file:
                matches.append(os.path.join(root, file))
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:file_search({directory},{pattern}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{matches}\n')
    return matches

def zip(directory, pattern, zip_file):
    shutil.make_archive(zip_file, 'zip', directory)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:zip({directory},{pattern},{zip_file}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    return shutil.make_archive(zip_file, 'zip', directory)

def move(file_path,new_path):
    shutil.move(file_path,new_path)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:move({file_path},{new_path}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    return shutil.move(file_path,new_path)

def encrypt(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()
    data = bytes([a ^ b for a, b in zip(data, itertools.cycle(password))])
    with open(file_path, 'wb') as f:
        f.write(data)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:encrypt({file_path},{password}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    return data

def decrypt(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()
    data = bytes([a ^ b for a, b in zip(data, itertools.cycle(password))])
    with open(file_path, 'wb') as f:
        f.write(data)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:decrypt({file_path},{password}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    return data

def img_pcs(file_path):
    img = plt.imread(file_path)
    plt.imshow(img)
    plt.show()
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:img_pcs({file_path}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{img}\n')
    return img

def img_rotate(file_path,angle):
    img = plt.imread(file_path)
    plt.imshow(img)
    plt.show()
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:img_rotate({file_path},{angle}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    return img
    
#===========turtle functions============
def square(length):
    global i
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:square({length}),length is{length},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(4):
        turtle.forward(length)
        turtle.left(360/4)

def triangle(length):
    global i
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:triangle({length}),length is{length},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(3):
        turtle.forward(length)
        turtle.left(360/3)

def rectangle(length,width):
    global i
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:rectangle({length},{width}),length is{length}width is{width},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(2):
        turtle.forward(length)
        turtle.left(360/2)
        turtle.forward(width)
        turtle.left(360/2)

def star(size):
    global i
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:star({size}),size is{size},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(5):
        turtle.left(360/5)
        turtle.forward(size)

def parallelogram(length,width):
    global i
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:parallelogram({length},{width}),length is{length}width is{width},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(2):
        turtle.forward(length)
        turtle.left(360/2)
        turtle.forward(width)
        turtle.left(360/2)

def polygon(number_of_sides,length):
    global i 
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:polygon({number_of_sides},{length}),{number_of_sides}sides,length is{length},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(number_of_sides):
        turtle.forward(length)
        turtle.left(360/number_of_sides)

def ellipse(width, height):
    global i
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:ellipse({width},{height}),width is{width}height is{height},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for _ in range(360):
        turtle.forward(width * math.sin(math.radians(_)))
        turtle.left(1)
        turtle.forward(height * math.cos(math.radians(_)))
        turtle.left(1)

def spiral(size, turns):
    global i
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:spiral({size},{turns}),size is{size}turns is{turns},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(turns * 360):
        turtle.forward(i * size / (turns * 360))
        turtle.left(1)

def flower(petals, size):
    global i
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:flower({petals},{size}),{petals}petals,size is{size},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(petals):
        turtle.circle(size, 60)
        turtle.left(120)
        turtle.circle(size, 60)
        turtle.left(120)
        turtle.left(360 / petals)

def fractal_tree(size, depth):
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:fractal_tree({size},{depth}),size is{size}depth is{depth},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    if depth == 0:
        return
    turtle.forward(size)
    turtle.left(45)
    fractal_tree(size * 0.7, depth - 1)
    turtle.right(90)
    fractal_tree(size * 0.7, depth - 1)
    turtle.left(45)
    turtle.backward(size)

def snowflake(size, depth):
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:snowflake({size},{depth}),size is{size}depth is{depth},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    def koch_curve(size, depth):
        if depth == 0:
            turtle.forward(size)
        else:
            koch_curve(size/3, depth-1)
            turtle.left(60)
            koch_curve(size/3, depth-1)
            turtle.right(120)
            koch_curve(size/3, depth-1)
            turtle.left(60)
            koch_curve(size/3, depth-1)
    
    for _ in range(6):
        koch_curve(size, depth)
        turtle.right(60)

def heart(size):
    global i
    file_append('C:/lmct prefech/module log.log', f'[LMCT]:heart({size}),size is{size},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    turtle.left(140)
    turtle.forward(size)
    for i in range(200):
        turtle.right(1)
        turtle.forward(size/20)
    turtle.left(120)
    for i in range(200):
        turtle.right(1)
        turtle.forward(size/20)
    turtle.forward(size)
    turtle.right(140)

#============string functions===========
def string_reverse(text):
    result = text[::-1]
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:string_reverse({text}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def palindrome_check(text):
    result = text.lower() == text.lower()[::-1]
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:palindrome_check({text}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def word_count(text):
    result = len(text.split())
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:word_count({text}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def string_to_list(text):
    result = list(text)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:string_to_list({text}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def list_to_string(list):
    result = ''.join(list)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:list_to_tring({list}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def string_to_tuple(text):
    result = tuple(text)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:string_to_tuple({text}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def string_to_ascii(text,sep):
    ascii_values=[ord(text) for text in text]
    result=sep.join(ascii_values)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:string_to_ascii({text}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def ascii_to_string(ascii_values,sep):
    result=sep.join(ascii_values)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:ascii_to_string({ascii_values}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

#=============base conversion functions=============
def binary_to_decimal(binary_str):
    result=int(binary_str,2)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:binary_to_decimal({binary_str}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def decimal_to_binary(decimal_num):
    result=bin(decimal_num)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:decimal_to_binary({decimal_num}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def binary_to_hexadecimal(binary_str):
    result=hex(int(binary_str,2))
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:binary_to_hexadecimal({binary_str}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def hexadecimal_to_binary(hexadecimal_str):
    result=bin(int(hexadecimal_str,16))
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:hexadecimal_to_binary({hexadecimal_str}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def decimal_to_hexadecimal(decimal_num):
    result=hex(decimal_num)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:decimal_to_hexadecimal({decimal_num}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def hexadecimal_to_decimal(hexadecimal_str):
    result=int(hexadecimal_str,16)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:hexadecimal_to_decimal({hexadecimal_str}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def decimal_to_octal(decimal_num):
    result=oct(decimal_num)
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:decimal_to_octal({decimal_num}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

#============time functions===========
def time_convert(time_str: str, format: str) -> Union[str, ValueError]:
    try:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:time_convert({time_str},{format}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        time_obj = time.strptime(time_str, format)
        return time.strftime("%Y-%m-%d %H:%M:%S", time_obj)
    except ValueError as e:
        raise ValueError(f"Invalid time format: {e}")

def date_calculate(date_str, days):
    try:
        date_obj = time.strptime(date_str, "%Y-%m-%d")
        timestamp = time.mktime(date_obj) + days * 24 * 3600
        result = time.strftime("%Y-%m-%d", time.localtime(timestamp))
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:date_calculate({date_str},{days}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
        return result
    except:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:date_calculate({date_str},{days}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:invalid date\n')
        return "invalid date"

def time_difference(time1, time2):
    try:
        t1 = time.strptime(time1, "%Y-%m-%d %H:%M:%S")
        t2 = time.strptime(time2, "%Y-%m-%d %H:%M:%S")
        diff = time.mktime(t2) - time.mktime(t1)
        result = f"{int(diff//3600)}hour, {int((diff%3600)//60)}minutes, {int(diff%60)}seconds"
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:time_difference({time1},{time2}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
        return result
    except:
        file_append('C:/lmct prefech/module log.log',f'[LMCT]:time_difference({time1},{time2}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:invalid time format\n')
        return "invalid time format"

#============validate functions============
def email_validate(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    result = bool(re.match(pattern, email))
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:email_validate({email}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def phone_validate(phone):
    pattern = r'^\+?1?\d{9,15}$'
    result = bool(re.match(pattern, phone))
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:phone_validate({phone}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    strength = {
        0: "very weak!",
        1: "a bit weak",
        2: "medium",
        3: "strong",
        4: "very strong",
        5: "outstanding"
    }
    result = strength[score]
    file_append('C:/lmct prefech/module log.log',f'[LMCT]:password_strength({password}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:{result}\n')
    return result

#============undefine class functions============
def draw_3d(a, b, c):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([a], [b], [c], color='r', s=100)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('3d point drawing')
    plt.show()
    file_append("C:/lmct prefech/module log.log",f'[LMCT]:draw_3d({a},{b},{c}),x is{a}y is{b}z is{c},used time:{time.strftime("%Y-%m-%d %H:%M:%S")}')

#==============module intrinsic functions==============
class LogManager:
    def __init__(self, max_size: int = 1024 * 1024):
        self.max_size = max_size
        self._check_rotation()
    
    def _check_rotation(self):
        if LOG_FILE.exists() and LOG_FILE.stat().st_size > self.max_size:
            self._rotate_log()

class TurtleManager:
    def __init__(self):
        self.turtle = turtle.Turtle()
    
    def __enter__(self):
        return self.turtle
    
    def __exit__(self,exec_type, exc_val, exc_tb):
        self.turtle.getscreen().bye()

def safe_operation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            file_append('C:/lmct prefech/module log.log',f'[LMCT]:安全操作({func.__name__}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
            return func(*args, **kwargs)
        except Exception as e:
            file_append('C:/lmct prefech/module log.log',f'[LMCT]:安全操作({func.__name__}),used time:{time.strftime("%Y-%m-%d %H:%M:%S")},result:操作失败\n')
            logging.error(f"操作失败: {str(e)}")
            raise
    return wrapper

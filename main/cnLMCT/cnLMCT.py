"""
    LMCT (逻辑数学文件海龟) 模块
    版本: cnLMCT 16.4.87
    作者: damnTurboWarp
    作者名称注释: "damnturbowarp" 是我的编程猫用户名
    QQ邮箱: codemao23@qq.com
    日期: 2025-05-12
    最后更新: 2025-06-30 11:34am :)

    描述:
    一个综合性的实用工具模块，提供以下功能集合：
    - 逻辑运算和布尔代数
    - 数学计算和数论
    - 文件系统操作和管理
    - 海龟图形和几何形状
    - 字符串操作和验证
    - 时间和日期操作
    - 输入验证和安全检查

    特点:
    - 所有函数都包含内置日志记录
    - 全面的错误处理
    - 类型提示和文档
    - 跨平台兼容性
    - 资源管理
    - 安全考虑

    模块结构:
    本模块包含9个主要部分，共69个函数：

    1. 日志管理 (第142-156行)
       - 日志文件创建和轮转
       - 日志级别控制
       - 日志格式化

    2.辅助函数 (第160-178行)
       - 中文名装饰器
       - 数据处理
       - 配置管理

    3. 逻辑运算 (第180-223行)
       - 基本门：与非、或非、同或
       - 扩展运算：三输入与门、三输入或门、三输入或非门、三输入与非门
       - 复杂逻辑：条件返回

    4. 数学函数 (第225-409行)
       - 逻辑：奇偶判断、素数检查
       - 工具：计算、计算阶乘、计算斐波那契数列
       - 数论：最大公约数、最小公倍数
       - 组合数学：排列、组合、矩阵
       - 其他：概率和统计

    5. 文件操作 (第412-459行)
       - 控制：安全命令
       - 文件工具：文件打印、压缩和解压、加密、解密
       - 基本I/O：文件写入、文件追加、文件删除
       - 资源管理：文件删除、文件重命名、文件复制、文件移动
       - 文件信息：文件大小、文件信息、文件搜索
       - 图像：图像处理、图像旋转

    6. 海龟图形 (第538-665行)
       - 基本图形：绘制正方形、绘制三角形、绘制矩形
       - 复杂图形：星形、平行四边形、多边形
       - 曲形：绘制椭圆、绘制螺旋、绘制心形
       - 高等图形：绘制花朵、绘制分形树、绘制雪花

    7. 字符串函数 (第668-715行)
       - 文本控制：字符串反转、回文检查
       - 文本分析：词数统计
       - 文本工具：字符串转列表、列表转字符串、字符串转元组、字符串转ASCII码、ASCII码转字符串

    8. 进制转换 (第725-765行)
       - 二进制：二进制转十进制、二进制转十六进制
       - 十进制：十进制转二进制、十进制转十六进制、十进制转八进制
       - 十六进制：十六进制转二进制、十六进制转十进制

    9. 时间函数 (第761-793行)
       - 时间转换：时间转换
       - 时间计算：日期计算、时间差计算

    10. 验证函数 (第796-834行)
       - 输入验证：邮箱验证、电话验证
       - 安全：密码强度检查
    
    11. 其他 (第837-846行)
       - 未定义：绘点3D
    
    12. 内部函数 (第849-878行)
       - 管理：日志管理、海龟绘图管理
       - 其他函数：安全操作

    依赖:
    - Python 3.6+
    - 此模块依赖模块：time, os, math, turtle, shutil, re, typing, pathlib, dataclasses, subprocess, functools, logging, matplotlib, itertools
    - 依赖模块需使用这条命令下载：pip install 模块名|要在cmd中运行
    - 无需外部依赖

    使用:
    导入模块并直接使用任何函数：
    >>> from LMCT import factorial
    >>> factorial(5)
    120

    注意事项:
    - 所有函数都包含自动日志记录
    - 内置错误处理
    - 自动资源清理
    - 线程安全操作
    - 内存高效实现

    许可证[copyright(C)]:
        本模块可自由使用和修改。
        欢迎注明出处，但不强制要求。
        所有在编程猫平台(和github上)的作品点赞和购买记录，都归原作者所有。
        原作:damnTurboWarp/Aherent/git32-peogrammer(都是我在其他平台的名称，定位置个人中心的url请详见README.md(在所在仓库里))
        副作(你):请签名
    结束行号：957
    变量:i
    类型声明:module
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
        raise RuntimeError("无法创建日志目录，请检查权限")

if not os.path.exists('C:/lmct prefech'):
    os.makedirs('C:/lmct prefech')
if os.path.exists('C:/lmct prefech/模块日志 - 副本.log'):
    os.remove('C:/lmct prefech/模块日志 - 副本.log')
else:
    with open('C:/lmct prefech/模块日志.log','a',encoding='utf-8') as file:
        if os.path.exists('C:/lmct prefech/模块日志 - 副本.log'):
            os.remove('C:/lmct prefech/模块日志 - 副本.log')
        file.write(f'这个日志文件可以自动删除旧的日志文件。创建时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        

#在这句注释以下，是辅助代码，请不要删除，会影响模块运行
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

def chinese_name(name):
    def decorator(func):
        func.__chinese_name__ = name
        return func
    return decorator

#以下是逻辑函数，灵感来自"图灵完备"，有稍微改动，但不会影响原版功能。
@chinese_name("与非门")
def nand(a,b):
    file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:与非门({a},{b}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{not (a and b)}\n')
    return not (a and b)

@chinese_name("或非门")
def nor(a,b):
    file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:或非门({a},{b}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{not (a or b)}\n')
    return not (a or b)

@chinese_name("同或门")
def xand(a,b):
    file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:同或门({a},{b}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{(a and not b) and (not a and b)}\n')
    return (a and not b) and (not a and b)

@chinese_name("三输入与门")
def three_and(a,b,c):
    file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:三输入与门({a},{b},{c}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{(a and b) and c}\n')
    return (a and b) and c

@chinese_name("三输入或门")
def three_or(a,b,c):
    file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:三输入或门({a},{b},{c}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{(a or b) or c}\n')
    return (a or b) or c

@chinese_name("三输入或非门")
def three_nor(a,b,c):
    file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:三输入或非门({a},{b},{c}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{not ((a or b) or c)}\n')
    return not ((a or b) or c)

@chinese_name("三输入与非门")
def three_nand(a,b,c):
    file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:三输入与非门({a},{b},{c}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{not ((a and b) and c)}\n')
    return not ((a and b) and c)

@chinese_name("条件返回")
def if_return(boolean,a,b):
    if boolean:
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:条件为{boolean},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{a}\n')
        return a
    else:
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:条件为{boolean},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{b}\n')
        return b

#以下是数学函数，有融入逻辑运算
@chinese_name("奇偶判断")
def even_odd(mode,num):
    if mode == '偶数':
        if num % 2 == 0:
            file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:测试模式为{mode},数字{num}是偶数,使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        else:
            file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:测试模式为{mode},数字{num}是奇数,使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        if_return(num % 2 == 0,"是偶数","是奇数")
    elif mode == '奇数':
        if num % 2 == 1:
            file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:测试模式为{mode},数字{num}是奇数,使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        else:
            file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:测试模式为{mode},数字{num}是偶数,使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        if_return(num % 2 == 0,"是奇数","是偶数")
    else:
        return "不是一个数字！(NAN)"
    
@chinese_name("计算")
def calculate(mode, num1, num2):
    if mode == '加法':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{num1 + num2},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 + num2
    elif mode == '减法':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{num1 - num2},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 - num2
    elif mode == '乘法':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{num1 * num2},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 * num2
    elif mode == '除法':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{num1 / num2},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 / num2
    elif mode == '取余数':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{num1 % num2},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 % num2
    elif mode == '幂':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{num1 ** num2},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 ** num2
    elif mode == '平方根':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{num1 ** 0.5},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 ** 0.5
    elif mode == '立方根':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{num1 ** (1/3)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return num1 ** (1/3)
    elif mode == '对数':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{math.log(num1,num2)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.log(num1,num2)
    elif mode == '自然对数':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{math.log(num1)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.log(num1)
    elif mode == '以10为底的对数':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{math.log(num1,10)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.log(num1,10)
    elif mode == '正弦':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{math.sin(num1)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.sin(num1)
    elif mode == '余弦':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{math.cos(num1)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.cos(num1)
    elif mode == '正切':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{math.tan(num1)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.tan(num1)
    elif mode == '反正弦':
        file_append('C:/lmct prefech/模块日志.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{math.asin(num1)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.asin(num1)
    elif mode == '反余弦':
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{math.acos(num1)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.acos(num1)
    elif mode == '反正切':
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{math.atan(num1)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return math.atan(num1)
    elif mode == '求最小':
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{min(num1,num2)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return min(num1,num2)
    elif mode == '求最大':
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{max(num1,num2)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return max(num1,num2)
    elif mode == '绝对值':
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{abs(num1)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return abs(num1)
    elif mode == '四舍五入':
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{round(num1)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return round(num1)
    elif mode == '字符串转算术':
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:计算模式为{mode},结果为{eval(num1)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return eval(num1)
    else:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:模式错误！错误时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        return "不是有效的模式！(NAVM)"
    
@chinese_name("阶乘")
def factorial(n):
    if n < 0:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:阶乘({n}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:无效输入\n')
        return "无效输入"
    result = 1
    for i in range(1, n + 1):
        result *= i
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:阶乘({n}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("斐波那契")
def fibonacci(n):
    if n < 0:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:斐波那契({n}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:无效输入\n')
        return "无效输入"
    if n <= 1:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:斐波那契({n}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{n}\n')
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:斐波那契({n}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{b}\n')
    return b

@chinese_name("素数检查")
def prime_check(n):
    if n < 2:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:素数检查({n}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:False\n')
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:素数检查({n}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:False\n')
            return False
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:素数检查({n}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:True\n')
    return True

@chinese_name("最大公约数")
def gcd(a,b):
    global i
    while b:
        a, b = b, a % b
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:最大公约数({a},{b}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{a}\n')
    return a

@chinese_name("最小公倍数")
def lcm(a,b):
    result = abs(a * b) // gcd(a, b)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:最小公倍数({a},{b}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("排列")
def permutation(n,r):
    if n < 0 or r < 0 or r > n:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:排列({n},{r}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:无效输入\n')
        return "无效输入"
    result = factorial(n) // factorial(n - r)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:排列({n},{r}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("组合")
def combination(n,r):
    if n < 0 or r < 0 or r > n:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:组合({n},{r}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:无效输入\n')
        return "无效输入"
    result = factorial(n) // (factorial(r) * factorial(n - r))
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:组合({n},{r}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("矩阵")
def matrix(n,m):
    global i
    if n < 0 or m < 0:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:矩阵({n},{m}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:无效输入\n')
        return "无效输入"
    result = []
    for i in range(n):
        result.append([])
        for j in range(m):
            result[i].append(i * j)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:矩阵({n},{m}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("概率和统计")
def probability(n,m):
    if n < 0 or m < 0:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:概率和统计({n},{m}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:无效输入\n')
        return "无效输入"
    result = []
    for i in range(n):
        result.append([])
        for j in range(m):
            result[i].append(i * j)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:概率和统计({n},{m}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

#以下是文件管理的函数，可以管理你的电脑
@chinese_name("安全命令")
def safe_cmd(command: str) -> None:
    if not re.match(r'^[a-zA-Z0-9\s\-_\.]+$', command):
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:安全命令({command}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:不安全的命令\n')
        raise ValueError("不安全的命令")
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:安全命令({command}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:已执行至microsoft c\n')
    subprocess.run(command, shell=True, check=True)

@chinese_name("文件打印")
def file_print(file_path):
    with open(file_path,'r') as file:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件打印({file_path}),结果:{file.read()},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        print(file.read())

@chinese_name("文件写入")
def file_write(file_path,content):
    with open(file_path,'w') as file:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件写入({file_path},{content}),结果:{file.write(content)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        file.write(content)

@chinese_name("文件追加")
def file_append(file_path,content):
    with open(file_path,'a') as file:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件追加({file_path},{content}),结果:{file.write(content)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        file.write(content)

@chinese_name("文件删除")
def file_delete(file_path):
    os.remove(file_path)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件删除({file_path}),结果:{os.remove(file_path)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')

@chinese_name("文件重命名")
def file_rename(file_path,new_name):
    os.rename(file_path,new_name)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件重命名({file_path},{new_name}),结果:{os.rename(file_path,new_name)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')

@chinese_name("文件复制")
def file_copy(file_path,new_path):
    shutil.copy(file_path,new_path)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件复制({file_path},{new_path}),结果:{shutil.copy(file_path,new_path)},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')

@chinese_name("文件大小")
def file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件大小({file_path}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{size} bytes\n')
        return size
    except:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件大小({file_path}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:文件未找到\n')
        return "文件未找到"

@chinese_name("文件信息")
def file_info(file_path):
    try:
        info = os.stat(file_path)
        result = {
            'size': info.st_size,
            'created': time.ctime(info.st_ctime),
            'modified': time.ctime(info.st_mtime),
            'accessed': time.ctime(info.st_atime)
        }
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件信息({file_path}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
        return result
    except:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件信息({file_path}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:文件未找到\n')
        return "文件未找到"

@chinese_name("文件搜索")
def file_search(directory, pattern):
    matches = []
    for root, _, files in os.walk(directory):
        for file in files:
            if pattern in file:
                matches.append(os.path.join(root, file))
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件搜索({directory},{pattern}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{matches}\n')
    return matches

@chinese_name("压缩和解压")
def zip(directory, pattern, zip_file):
    shutil.make_archive(zip_file, 'zip', directory)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:压缩和解压({directory},{pattern},{zip_file}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    return shutil.make_archive(zip_file, 'zip', directory)

@chinese_name("文件移动")
def move(file_path,new_path):
    shutil.move(file_path,new_path)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:文件移动({file_path},{new_path}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    return shutil.move(file_path,new_path)

@chinese_name("加密")
def encrypt(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()
    data = bytes([a ^ b for a, b in zip(data, itertools.cycle(password))])
    with open(file_path, 'wb') as f:
        f.write(data)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:加密({file_path},{password}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    return data

@chinese_name("解密")
def decrypt(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()
    data = bytes([a ^ b for a, b in zip(data, itertools.cycle(password))])
    with open(file_path, 'wb') as f:
        f.write(data)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:解密({file_path},{password}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    return data

@chinese_name("图像处理")
def img_pcs(file_path):
    img = plt.imread(file_path)
    plt.imshow(img)
    plt.show()
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:图像处理({file_path}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{img}\n')
    return img

@chinese_name("图像旋转")
def img_rotate(file_path,angle):
    img = plt.imread(file_path)
    plt.imshow(img)
    plt.show()
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:图像旋转({file_path},{angle}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    return img
    
#以下是海龟画图函数，参考我的模块"etpt"，可以在我的编程猫主页上查找这个模块
@chinese_name("绘制正方形")
def square(length):
    global i
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制正方形({length}),边长为{length},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(4):
        turtle.forward(length)
        turtle.left(360/4)

@chinese_name("绘制三角形")
def triangle(length):
    global i
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制三角形({length}),边长为{length},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(3):
        turtle.forward(length)
        turtle.left(360/3)

@chinese_name("绘制矩形")
def rectangle(length,width):
    global i
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制矩形({length},{width}),长为{length}宽为{width},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(2):
        turtle.forward(length)
        turtle.left(360/2)
        turtle.forward(width)
        turtle.left(360/2)

@chinese_name("绘制星形")
def star(size):
    global i
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制星形({size}),大小为{size},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(5):
        turtle.left(360/5)
        turtle.forward(size)

@chinese_name("绘制平行四边形")
def parallelogram(length,width):
    global i
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制平行四边形({length},{width}),长为{length}宽为{width},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(2):
        turtle.forward(length)
        turtle.left(360/2)
        turtle.forward(width)
        turtle.left(360/2)

@chinese_name("绘制多边形")
def polygon(number_of_sides,length):
    global i 
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制多边形({number_of_sides},{length}),{number_of_sides}边形边长为{length},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(number_of_sides):
        turtle.forward(length)
        turtle.left(360/number_of_sides)

@chinese_name("绘制椭圆")
def ellipse(width, height):
    global i
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制椭圆({width},{height}),宽为{width}高为{height},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for _ in range(360):
        turtle.forward(width * math.sin(math.radians(_)))
        turtle.left(1)
        turtle.forward(height * math.cos(math.radians(_)))
        turtle.left(1)

@chinese_name("绘制螺旋")
def spiral(size, turns):
    global i
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制螺旋({size},{turns}),大小为{size}圈数为{turns},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(turns * 360):
        turtle.forward(i * size / (turns * 360))
        turtle.left(1)

@chinese_name("绘制花朵")
def flower(petals, size):
    global i
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制花朵({petals},{size}),{petals}片花瓣大小为{size},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for i in range(petals):
        turtle.circle(size, 60)
        turtle.left(120)
        turtle.circle(size, 60)
        turtle.left(120)
        turtle.left(360 / petals)

@chinese_name("绘制分形树")
def fractal_tree(size, depth):
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制分形树({size},{depth}),大小为{size}深度为{depth},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    if depth == 0:
        return
    turtle.forward(size)
    turtle.left(45)
    fractal_tree(size * 0.7, depth - 1)
    turtle.right(90)
    fractal_tree(size * 0.7, depth - 1)
    turtle.left(45)
    turtle.backward(size)

@chinese_name("绘制雪花")
def snowflake(size, depth):
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制雪花({size},{depth}),大小为{size}深度为{depth},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
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

@chinese_name("绘制心形")
def heart(size):
    global i
    file_append('C:/lmct prefech/module log.log', f'[逻辑数学文件海龟提示]:绘制心形({size}),大小为{size},使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
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

#以下是字符串管理的函数
@chinese_name("字符串反转")
def string_reverse(text):
    result = text[::-1]
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:字符串反转({text}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("回文检查")
def palindrome_check(text):
    result = text.lower() == text.lower()[::-1]
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:回文检查({text}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("词数统计")
def word_count(text):
    result = len(text.split())
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:词数统计({text}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("字符串转列表")
def string_to_list(text):
    result = list(text)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:字符串转列表({text}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("列表转字符串")
def list_to_string(list):
    result = ''.join(list)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:列表转字符串({list}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("字符串转元组")
def string_to_tuple(text):
    result = tuple(text)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:字符串转元组({text}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("字符串转ASCII码")
def string_to_ascii(text,sep):
    ascii_values=[ord(text) for text in text]
    result=sep.join(ascii_values)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:字符串转ASCII码({text}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("ASCII码转字符串")
def ascii_to_string(ascii_values,sep):
    result=sep.join(ascii_values)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:ASCII码转字符串({ascii_values}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

#以下是进制转换的函数
@chinese_name("二进制转十进制")
def binary_to_decimal(binary_str):
    result=int(binary_str,2)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:二进制转十进制({binary_str}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("十进制转二进制")
def decimal_to_binary(decimal_num):
    result=bin(decimal_num)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:十进制转二进制({decimal_num}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("二进制转十六进制")
def binary_to_hexadecimal(binary_str):
    result=hex(int(binary_str,2))
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:二进制转十六进制({binary_str}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("十六进制转二进制")
def hexadecimal_to_binary(hexadecimal_str):
    result=bin(int(hexadecimal_str,16))
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:十六进制转二进制({hexadecimal_str}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("十进制转十六进制")
def decimal_to_hexadecimal(decimal_num):
    result=hex(decimal_num)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:十进制转十六进制({decimal_num}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("十六进制转十进制")
def hexadecimal_to_decimal(hexadecimal_str):
    result=int(hexadecimal_str,16)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:十六进制转十进制({hexadecimal_str}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("十进制转八进制")
def decimal_to_octal(decimal_num):
    result=oct(decimal_num)
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:十进制转八进制({decimal_num}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

#以下是时间管理的函数
@chinese_name("时间转换")
def time_convert(time_str: str, format: str) -> Union[str, ValueError]:
    try:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:时间转换({time_str},{format}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        time_obj = time.strptime(time_str, format)
        return time.strftime("%Y-%m-%d %H:%M:%S", time_obj)
    except ValueError as e:
        raise ValueError(f"Invalid time format: {e}")

@chinese_name("日期计算")
def date_calculate(date_str, days):
    try:
        date_obj = time.strptime(date_str, "%Y-%m-%d")
        timestamp = time.mktime(date_obj) + days * 24 * 3600
        result = time.strftime("%Y-%m-%d", time.localtime(timestamp))
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:日期计算({date_str},{days}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
        return result
    except:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:日期计算({date_str},{days}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:无效日期\n')
        return "无效日期"

@chinese_name("时间差计算")
def time_difference(time1, time2):
    try:
        t1 = time.strptime(time1, "%Y-%m-%d %H:%M:%S")
        t2 = time.strptime(time2, "%Y-%m-%d %H:%M:%S")
        diff = time.mktime(t2) - time.mktime(t1)
        result = f"{int(diff//3600)}小时, {int((diff%3600)//60)}分钟, {int(diff%60)}秒"
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:时间差计算({time1},{time2}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
        return result
    except:
        file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:时间差计算({time1},{time2}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:无效时间格式\n')
        return "无效时间格式"

#以下是验证的函数
@chinese_name("邮箱验证")
def email_validate(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    result = bool(re.match(pattern, email))
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:邮箱验证({email}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("电话验证")
def phone_validate(phone):
    pattern = r'^\+?1?\d{9,15}$'
    result = bool(re.match(pattern, phone))
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:电话验证({phone}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

@chinese_name("密码强度检查")
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
        0: "非常弱",
        1: "弱",
        2: "中等",
        3: "强",
        4: "非常强",
        5: "优秀"
    }
    result = strength[score]
    file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:密码强度检查({password}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:{result}\n')
    return result

#以下是绘画(not turtle)的函数
@chinese_name("绘点3D")
def draw_3d(a, b, c):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([a], [b], [c], color='r', s=100)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('3D点绘图')
    plt.show()

# 以下是模块内部函数，请不要删除，会报错
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
            file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:安全操作({func.__name__}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
            return func(*args, **kwargs)
        except Exception as e:
            file_append('C:/lmct prefech/module log.log',f'[逻辑数学文件海龟提示]:安全操作({func.__name__}),使用时间:{time.strftime("%Y-%m-%d %H:%M:%S")},结果:操作失败\n')
            logging.error(f"操作失败: {str(e)}")
            raise
    return wrapper

# 提供中文别名
# 中文函数名列表（添加到模块末尾）
函数列表 = {
    # 逻辑运算
    "与非门": nand,
    "或非门": nor,
    "同或门": xand,
    "三输入与门": three_and,
    "三输入或门": three_or,
    "三输入或非门": three_nor,
    "三输入与非门": three_nand,
    "条件返回": if_return,
    
    # 数学函数
    "奇偶判断": even_odd,
    "计算": calculate,
    "阶乘": factorial,
    "斐波那契": fibonacci,
    "素数检查": prime_check,
    "最大公约数": gcd,
    "最小公倍数": lcm,
    "排列": permutation,
    "组合": combination,
    
    # 文件操作
    "安全命令": safe_cmd,
    "文件打印": file_print,
    "文件写入": file_write,
    "文件追加": file_append,
    "文件删除": file_delete,
    "文件重命名": file_rename,
    "文件复制": file_copy,
    "文件大小": file_size,
    "文件信息": file_info,
    "文件搜索": file_search,
    
    # 海龟图形
    "绘制正方形": square,
    "绘制三角形": triangle,
    "绘制矩形": rectangle,
    "绘制星形": star,
    "绘制平行四边形": parallelogram,
    "绘制多边形": polygon,
    "绘制椭圆": ellipse,
    "绘制螺旋": spiral,
    "绘制花朵": flower,
    "绘制分形树": fractal_tree,
    "绘制雪花": snowflake,
    "绘制心形": heart,
    
    # 字符串操作
    "字符串反转": string_reverse,
    "回文检查": palindrome_check,
    "词数统计": word_count,
    "字符串转列表": string_to_list,
    "列表转字符串": list_to_string,
    "字符串转元组": string_to_tuple,
    "字符串转ASCII":string_to_ascii,
    "ASCII转字符串":ascii_to_string,

    #进制转换
    "二进制转十进制":binary_to_decimal,
    "十进制转二进制":decimal_to_binary,
    "二进制转十六进制":binary_to_hexadecimal,
    "十六进制转二进制":hexadecimal_to_binary,
    "十进制转十六进制":decimal_to_hexadecimal,
    "十六进制转十进制":hexadecimal_to_decimal,
    "十进制转八进制":decimal_to_octal,
    # 时间函数
    "时间转换": time_convert,
    "日期计算": date_calculate,
    "时间差计算": time_difference,
    
    # 验证函数
    "邮箱验证": email_validate,
    "电话验证": phone_validate,
    "密码强度检查": password_strength
}
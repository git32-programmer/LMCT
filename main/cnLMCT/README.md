# LMCT (逻辑数学文件海龟) 模块文档

## 概述

LMCT 是一个综合性的实用工具模块，提供以下功能集合：

* 逻辑运算和布尔代数
* 数学计算和数论
* 文件系统操作和管理
* 海龟图形和几何形状
* 字符串操作和验证
* 时间和日期操作
* 输入验证和安全检查

## 需要的模块:**time, os, math, turtle, shutil, re, typing, pathlib, dataclasses, subprocess, functools, logging, matplotlib, itertools**

## 安装

**bash**

```bash
pip install 需要的模块名
```

### 如果想知道更多关于pip命令的知识，请详见[pip命令学习](https://www.runoob.com/w3cnote/python-pip-install-usage.html)

## 使用示例

**python**

```
from LMCT import factorial, square

print(factorial(5))  # 输出: 120
square(100)          # 绘制边长为100的正方形
```

## 函数列表

### 1. 逻辑运算

| 函数名 (中文) | 参数                          | 输出类型 | 描述             |
| ------------- | ----------------------------- | -------- | ---------------- |
| 与非门        | a: bool, b: bool              | bool     | 执行与非逻辑运算 |
| 或非门        | a: bool, b: bool              | bool     | 执行或非逻辑运算 |
| 同或门        | a: bool, b: bool              | bool     | 执行同或逻辑运算 |
| 三输入与门    | a: bool, b: bool, c: bool     | bool     | 三输入与门运算   |
| 三输入或门    | a: bool, b: bool, c: bool     | bool     | 三输入或门运算   |
| 三输入或非门  | a: bool, b: bool, c: bool     | bool     | 三输入或非门运算 |
| 三输入与非门  | a: bool, b: bool, c: bool     | bool     | 三输入与非门运算 |
| 条件返回      | boolean: bool, a: Any, b: Any | Any      | 根据条件返回a或b |

### 2. 数学函数

| 函数名 (中文) | 参数                                | 输出类型 | 描述                    |
| ------------- | ----------------------------------- | -------- | ----------------------- |
| 奇偶判断      | mode: str, num: int                 | str      | 判断数字的奇偶性        |
| 计算          | mode: str, num1: float, num2: float | float    | 执行各种数学计算        |
| 阶乘          | n: int                              | int      | 计算n的阶乘             |
| 斐波那契      | n: int                              | int      | 计算斐波那契数列的第n项 |
| 素数检查      | n: int                              | bool     | 检查数字是否为素数      |
| 最大公约数    | a: int, b: int                      | int      | 计算最大公约数          |
| 最小公倍数    | a: int, b: int                      | int      | 计算最小公倍数          |
| 排列          | n: int, r: int                      | int      | 计算排列数              |
| 组合          | n: int, r: int                      | int      | 计算组合数              |

### 3. 文件操作

| 函数名 (中文) | 参数                            | 输出类型 | 描述               |
| ------------- | ------------------------------- | -------- | ------------------ |
| 安全命令      | command: str                    | None     | 执行安全的系统命令 |
| 文件打印      | file\_path: str                 | None     | 打印文件内容       |
| 文件写入      | file\_path: str, content: str   | None     | 写入内容到文件     |
| 文件追加      | file\_path: str, content: str   | None     | 追加内容到文件     |
| 文件删除      | file\_path: str                 | None     | 删除文件           |
| 文件重命名    | file\_path: str, new\_name: str | None     | 重命名文件         |
| 文件复制      | file\_path: str, new\_path: str | None     | 复制文件           |
| 文件大小      | file\_path: str                 | int/str  | 获取文件大小       |
| 文件信息      | file\_path: str                 | dict/str | 获取文件信息       |

### 4. 海龟图形

| 函数名 (中文)  | 参数                                | 输出类型 | 描述           |
| -------------- | ----------------------------------- | -------- | -------------- |
| 绘制正方形     | length: int                         | None     | 绘制正方形     |
| 绘制三角形     | length: int                         | None     | 绘制等边三角形 |
| 绘制矩形       | length: int, width: int             | None     | 绘制矩形       |
| 绘制星形       | size: int                           | None     | 绘制五角星     |
| 绘制平行四边形 | length: int, width: int             | None     | 绘制平行四边形 |
| 绘制多边形     | number\_of\_sides: int, length: int | None     | 绘制正多边形   |
| 绘制椭圆       | width: int, height: int             | None     | 绘制椭圆       |
| 绘制螺旋       | size: float, turns: int             | None     | 绘制螺旋线     |
| 绘制花朵       | petals: int, size: int              | None     | 绘制花朵图案   |
| 绘制分形树     | size: int, depth: int               | None     | 绘制分形树     |
| 绘制雪花       | size: int, depth: int               | None     | 绘制雪花图案   |
| 绘制心形       | size: int                           | None     | 绘制心形图案   |

### 5. 字符串操作

| 函数名 (中文) | 参数       | 输出类型 | 描述                   |
| ------------- | ---------- | -------- | ---------------------- |
| 字符串反转    | text: str  | str      | 反转字符串             |
| 回文检查      | text: str  | bool     | 检查字符串是否为回文   |
| 词数统计      | text: str  | int      | 统计字符串中的单词数   |
| 字符串转列表  | text: str  | list     | 将字符串转换为字符列表 |
| 列表转字符串  | list: list | str      | 将列表转换为字符串     |
| 字符串转元组  | text: str  | tuple    | 将字符串转换为元组     |

### 6. 进制转换

| 函数名 (中文)    | 参数                  | 输出类型 | 描述             |
| ---------------- | --------------------- | -------- | ---------------- |
| 二进制转十进制   | binary\_str: str      | int      | 二进制转十进制   |
| 十进制转二进制   | decimal\_num: int     | str      | 十进制转二进制   |
| 二进制转十六进制 | binary\_str: str      | str      | 二进制转十六进制 |
| 十六进制转二进制 | hexadecimal\_str: str | str      | 十六进制转二进制 |
| 十进制转十六进制 | decimal\_num: int     | str      | 十进制转十六进制 |
| 十六进制转十进制 | hexadecimal\_str: str | int      | 十六进制转十进制 |
| 十进制转八进制   | decimal\_num: int     | str      | 十进制转八进制   |

### 7. 时间函数

| 函数名 (中文) | 参数                        | 输出类型 | 描述               |
| ------------- | --------------------------- | -------- | ------------------ |
| 时间转换      | time\_str: str, format: str | str      | 时间格式转换       |
| 日期计算      | date\_str: str, days: int   | str      | 计算日期加减       |
| 时间差计算    | time1: str, time2: str      | str      | 计算两个时间的差值 |

### 8. 验证函数

| 函数名 (中文) | 参数          | 输出类型 | 描述             |
| ------------- | ------------- | -------- | ---------------- |
| 邮箱验证      | email: str    | bool     | 验证邮箱格式     |
| 电话验证      | phone: str    | bool     | 验证电话号码格式 |
| 密码强度检查  | password: str | str      | 检查密码强度等级 |

## 许可证

本模块可自由使用和修改。欢迎注明出处，但不强制要求。

原作: damnTurboWarp/Aherent/git32-peogrammer

## 联系方式请详见仓库里的第一个**README.md**文件(两个文件夹外)

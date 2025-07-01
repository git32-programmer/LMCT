from .cnLMCT import (
    # 日志管理
    ensure_log_dir,
    LogManager,
    # 辅助函数
    process_data,
    chinese_name,
    # 逻辑运算
    nand,
    nor,
    xand,
    three_and,
    three_or,
    three_nor,
    three_nand,
    if_return,
    # 数学函数
    even_odd,
    calculate,
    factorial,
    fibonacci,
    prime_check,
    gcd,
    lcm,
    permutation,
    combination,
    # 文件操作
    safe_cmd,
    file_print,
    file_write,
    file_append,
    file_delete,
    file_rename,
    file_copy,
    file_size,
    file_info,
    file_search,
    # 海龟图形
    square,
    triangle,
    rectangle,
    star,
    parallelogram,
    polygon,
    ellipse,
    spiral,
    flower,
    fractal_tree,
    snowflake,
    heart,
    # 字符串函数
    string_reverse,
    palindrome_check,
    word_count,
    string_to_list,
    list_to_string,
    string_to_tuple,
    string_to_ascii,
    ascii_to_string,
    # 进制转换
    binary_to_decimal,
    decimal_to_binary,
    binary_to_hexadecimal,
    hexadecimal_to_binary,
    decimal_to_hexadecimal,
    hexadecimal_to_decimal,
    decimal_to_octal,
    # 时间函数
    time_convert,
    date_calculate,
    time_difference,
    # 验证函数
    email_validate,
    phone_validate,
    password_strength,
    # 模块内部类和函数
    TurtleManager,
    safe_operation,
    函数列表
)

__all__ = [
    # 日志管理
    'ensure_log_dir',
    'LogManager',
    # 辅助函数
    'process_data',
    'chinese_name',
    # 逻辑运算
    'nand',
    'nor',
    'xand',
    'three_and',
    'three_or',
    'three_nor',
    'three_nand',
    'if_return',
    # 数学函数
    'even_odd',
    'calculate',
    'factorial',
    'fibonacci',
    'prime_check',
    'gcd',
    'lcm',
    'permutation',
    'combination',
    # 文件操作
    'safe_cmd',
    'file_print',
    'file_write',
    'file_append',
    'file_delete',
    'file_rename',
    'file_copy',
    'file_size',
    'file_info',
    'file_search',
    # 海龟图形
    'square',
    'triangle',
    'rectangle',
    'star',
    'parallelogram',
    'polygon',
    'ellipse',
    'spiral',
    'flower',
    'fractal_tree',
    'snowflake',
    'heart',
    # 字符串函数
    'string_reverse',
    'palindrome_check',
    'word_count',
    'string_to_list',
    'list_to_string',
    'string_to_tuple',
    'string_to_ascii',
    'ascii_to_string',
    # 进制转换
    'binary_to_decimal',
    'decimal_to_binary',
    'binary_to_hexadecimal',
    'hexadecimal_to_binary',
    'decimal_to_hexadecimal',
    'hexadecimal_to_decimal',
    'decimal_to_octal',
    # 时间函数
    'time_convert',
    'date_calculate',
    'time_difference',
    # 验证函数
    'email_validate',
    'phone_validate',
    'password_strength',
    # 模块内部类和函数
    'TurtleManager',
    'safe_operation',
    '函数列表'
]

ensure_log_dir()

__version__ = '16.4.87'    
__author__ = '蛋仔TurboWarp'
__description__ = '一个用于Python编程的实用工具库'
__license__ = 'MIT'
__url__ = '404 not found ◑▽◐'
__keywords__ = ['实用工具', 'Python', '工具库', 'cnLMCT', '汉化']
__classifiers__ = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]
__platform__ = 'Windows'
__python_version__ = '3.10'
__doc__="""
    LMCT (逻辑数学文件海龟) 模块
    版本: cnLMCT 16.4.87
    更新描述(待实现):1.添加矩阵运算、2.概率和统计、3.zip/rar文件夹处理、4.加密和解密、5.数据库操作、6.JSON/XML处理、7.3d绘图、8.动画、9.图像处理(jpg/png/gif/bmp)、10.NLP处理、11.正则表达式增强、12.编码转换(可能会出现‘手持两把锟斤拷，嘴里直呼烫烫烫’)、13.时区支持、14.日历功能、15.数据验证、16.easygui图形计算器、17.命令行工具(其他命令)、18.查询天气(requests)、19.文本翻译、20.硬件控制(micro:bit v2、arduino...)、21.打印时间("\r转义字符来方便循环显示时间，搭配while True循环)")
    作者: damnTurboWarp
    作者名称注释: "damnturbowarp" 是我的编程猫用户名
    QQ邮箱: codemao23@qq.com
    日期: 2025-05-12
    最后更新: 2025-05-14 19:33

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
    本模块包含9个主要部分，共69多个函数：

    1. 日志管理 (第120-135行)
       - 日志文件创建和轮转
       - 日志级别控制
       - 日志格式化

    2.辅助函数 (第141-159行)
       - 中文名装饰器
       - 数据处理
       - 配置管理

    3. 逻辑运算 (第172-214行)
       - 基本门：与非、或非、异或、同或
       - 扩展运算：三输入与非、三输入或非
       - 复杂逻辑：多数表决、蕴含

    4. 数学函数 (第217-373行)
       - 基本算术
       - 高级数学：阶乘、斐波那契
       - 数论：最大公约数、最小公倍数
       - 组合数学：排列、组合

    5. 文件操作 (第377-452行)
       - 基本I/O：读取、写入、追加
       - 文件管理：删除、重命名、复制
       - 文件工具：大小、信息、搜索
       - 文件安全：command_prompt_symbol

    6. 海龟图形 (第455-582行)
       - 基本形状：正方形、三角形、矩形
       - 复杂形状：星形、平行四边形、多边形
       - 高级图形：椭圆、螺旋、花朵
       - 分形图案：树、雪花
       - 特殊形状：心形

    7. 字符串函数 (第585-632行)
       - 文本操作：反转、回文检查
       - 文本分析：词数统计
       - 类型转换：列表、元组
       - ASCII码转换：字符串、ASCII码

    8. 进制转换 (第635-675行)
       - 二进制转换：二进制、十进制、十六进制
       - 十进制转换：十进制、二进制、十六进制
       - 十六进制转换：十六进制、二进制、十进制

    9. 时间函数 (第678-710行)
       - 时间转换
       - 日期计算
       - 时间差计算

    10. 验证函数 (第713-751行)
       - 输入验证：邮箱、电话
       - 安全：密码强度

    依赖:
    - Python 3.6+
    - 此模块依赖模块：time, os, math, turtle, shutil, re,typing,pathlib,dataclasses,subprocess,functools,logging,easygui,requests,itertools,matplotlib,pillow,mpl_toolkits.mpl3d,
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
    结束行号：955
    变量:i
    类型声明:module
"""
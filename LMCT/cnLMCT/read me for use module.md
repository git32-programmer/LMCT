# LMCT(logic math file turtle)

## 模块概述

**cnLMCT**是一个综合性实用工具模块，提供逻辑运算、数学计算、文件系统操作、海龟图形绘制、字符串操作、进制转换、时间处理和输入验证等功能。

## 模块信息

* **版本**: 正式版 cnLMCT 10.6.8
* **作者**:蛋仔TurboWarp
* **QQ邮箱**:codemao23@qq.com
* **编程猫个人中心**:[个人中心](https://shequ.codemao.cn/user/1274549095)
* **bilibili**:[bilibili](https://space.bilibili.com/1402822998?spm_id_from=333.1007.0.0)
* **日期**:2025-05-12
* **最后更新**:2025-05-14 19:33
  
  ### 功能集合:
  
  * 逻辑运算与布尔运算
  * 数学计算和数论
  * 文件系统操作 海龟图形绘制
  * 字符串处理与验证
  * 时间日期操作
  * 输入验证与安全检查
    
    ## 模块结构与函数列表
    
    ## 1.日志管理
    
    |功能|描述|
|--|--|
|日志文件创建与轮转|自动管理日志文件防止垃圾文件过多|
|日志级别控制|支持多级日志过滤|
|日志格式化|统一日志输出格式|
    
    

## 2.辅助函数

|函数名|功能|参数|返回值|
|--|--|--|--|
|process_data|简单数据处理，出错返回None|data:t|Optional[T]|
|chinese_name|为函数添加中文名装饰器|name:str|装饰后的函数

## 3.逻辑运算

|函数名|功能|参数|返回值|
|--|--|--|--|
|与非门|执行与非逻辑运算|a,b:bool|bool|
|或非门|执行或非逻辑运算|a,b:bool|bool|
|同或门|执行同或逻辑运算|a,b:bool|bool|
|三输入与门|三输入与逻辑运算|a,b,c:bool|bool|
|三输入或门|三输入或逻辑运算|a,b,c:bool|bool|
|三输入或非门|三输入或非逻辑运算|a,b,c:bool|bool|
|三输入非与门|三输入与非逻辑运算|a,b,c:bool|bool|
|条件返回|条件判断返回值|boolean|同a或b类型

## 4.数学函数

|函数名|功能|参数|返回值|
|--|--|--|--|
|奇偶判断|判断数字奇偶性|mode:str,num:int|str|
|计算|执行多种数学运算|mode:str,num1,num2|计算结果或错误信息|
|阶乘|计算阶乘|n:int|int或'无效输入'|
|斐波那契|计算斐波那契数列|n:int|int或'无效输入'|
|素数检查|检查素数|n:int|bool|
|最大公约数|计算最大公约数|a,b:int|int|
|最小公倍数|计算最小公倍数|a,b:int|int|
|排列|计算排列数|n,r:int|int或'无效输入'|
|组合|计算组合数|n,r:int|int或'无效输入'|

#### 5.文件操作

|函数名|功能|参数|返回值|
|--|--|--|--|
|安全命令|安全执行系统命令|command:str|None|
|文件打印|打印文件内容|file_path:str|None|
|文件写入|写入内容到文件|file_path,content|None|
|文件追加|追加内容到文件|file_path:str|None|
|文件删除|删除文件|file_path:str|None|
|文件重命名|重命名文件|file_path,new_name|None|
|文件复制|复制文件|file_path,new_path|None|
|文件大小|获取文件大小|file_path:str|int或'文件未找到'|
|文件信息|获取文件详细信息|file_path: str|dict或'文件未找到'|
|文件搜索| 搜索匹配文件|directory, pattern| list[str]|

## 6.海龟图形

|函数名|功能|参数|返回值|
|--|--|--|--|
|绘制正方形|绘制正方形|length:int|None|
|绘制三角形|绘制三角形|length:int|None|
|绘制矩形|绘制矩形|length,width:int|None|
|绘制星型|绘制星型|size:int|None|
|绘制平行四边形|绘制平行四边形|length,width:int|None|
|绘制多边形|绘制多边形|sides,length:int|None|
|绘制椭圆|绘制椭圆|width,height:int|None|
|绘制螺旋|绘制螺旋|size,turns:int|None|
|绘制花朵|绘制花朵|petals,size:int|None|
|绘制分形树|绘制分形树|size,depth:int|None|
|绘制雪花|绘制雪花|size,depth:int|None|
|绘制心形|绘制心形|size:int|None|

## 7.字符串函数

|函数名|功能|参数|返回值|
|--|--|--|--|
|字符串反转|反转字符串|text:str|str|
|回文检查|检查回文|text:str|bool|
|词数统计|统计单词数量|text:str|int|
|字符串转列表|字符串转列表|text:str|list|
|列表转字符串|列表转字符串|list:list|str|
|字符串转元组|字符串转元组|text:str|tuple|
|字符串转ASCII|字符串转ASCII码|text:str,sep:str|str|
|ASCII转字符串|ASCII码转字符串|ascii:str,sep:str|

## 8.进制转换

|函数名|功能|参数|返回值|
|--|--|--|--|
|二进制转十进制|二进制转十进制|binary:str:str|int|
|十进制转二进制|十进制转二进制|decimal_num:int|str|
|二进制转十六进制|二进制转十六进制|binary_str:str|str|
|十六进制转二进制|十六进制转二进制|hex_str:str|str|
|十进制转十六进制|十进制转十六进制|hex_str:str|str|
|十六进制转十进制|十六进制转十进制|hex_str:str|int|
|十进制转八进制|十进制转八进制|decimal_num:int|str|

## 9.时间函数

|函数名|功能|参数|返回值|
|--|--|--|--|
|时间转换|时间格式转换|time_str:str,format;str|str或ValueError|
|日期计算|日期加减计算|date_str:str,days:int|str或'无效日期'|
|时间差计算|计算时间间隔|time1,time2:str|str或'无效时间格式'|

## 10.验证函数

|函数名|功能|参数|返回值|
|--|--|--|--|
|邮箱验证|验证邮箱格式|email:str|bool|
|电话验证|验证电话格式|phone:str|bool|
|密码强度检查|检查密码强度|password:str|str (强度等级)|

## 依赖

* 1.Python编译器，版本为3.6以上
* 2.安装模块 `time,os,math,turtle,shutil,re,typing,pathlib,dataclasses,subprocess,functools,logging`
* ​**安装命令**​：`pip install 模块名` (需在 CMD 中运行)

## 使用示例

```python
>>> from cnLMCT import factorial
>>> factorial(5)
120
```

## 注意事项

1. 所有函数内置自动日志记录
2. 全面的错误机制
3. 自动资源回收
4. 线程安全设计
5. 内存高效实现

## 许可证

* 此模块可以自由使用和修改，不能轻易修改重要代码

* 如果你修改了，请注明出处
* 原作者:蛋仔TurboWarp
* 编程猫和GitHub平台的点赞和购买记录都归原作者所有
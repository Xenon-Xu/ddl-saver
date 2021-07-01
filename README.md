# ddl-saver

A visualization software for DDL (deadline) planning (latest version 0.1.2)

Developed using Qt and Python

UI interface language: Simplified Chinese 简体中文

## Functions:
* DDL visible table     *(name, date & time, importance, time remaining, completed or not, etc.)*
* DDL simple management *(add, delete, modify, etc.)*
* DDL notification      *(color mark, popup window notification, win10toast notification(optional) )*
* Can run in the backgroud *(provide real-time monitoring of DDL countdown)*
* ...

## UI interface example:

![image](https://user-images.githubusercontent.com/66453626/124095780-94b37e80-da8c-11eb-8c71-d3bcbb9a186f.png)

***Note***: *There is a constant 'SHOW_WIN10_NOTIFICATION' in code 'constants.py', which uses 'win10toast' module.
If you don't want use this (and don't want to show win10 toast in the application in any circumstance), please set*
```
SHOW_WIN10_NOTIFICATION = False
```
*to avoid it.*

# DDL 拯救者 （最新版本0.1.2）

（我再错过DDL我当场把这个电脑屏幕给吃掉）

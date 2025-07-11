# winxp_quanpin_freq_dict
提取winxp全拼输入法的词频词序字序用于导入win10/11自带拼音输入法

Copyright (C) 2025 gamefunc   
----------------
    Author: gamefunc:    
    website: https://www.gamefunc.top:9029    
    github: https://github.com/gamefunc    
    qq: 32686647    
    weixin & tel: 18576539615: name: gamefunc
    mail: fevefun@hotmail.com
    使用或修改本项目必须保留以上信息在用户可见位置;
    free to use and modify, but need keep the above information.  
    Redistribution or modification must retain the original author information: 
        (gamefunc @ QQ-32686647) in all source and binary forms.
    This project is licensed under the GNU General Public License v3.0;
    

```python
应该不少老人习惯了WINXP全拼输入法可以盲打,    
然后用WIN10_11的输入法经常打错字而且速度还慢;    
WIN7时使用XP的全拼输入法直接复制:    
    "c:/window/system32/WINPY.IME"
    "c:/window/system32/WINPY.MB"
到同目录,同时导入注册表:
    "HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Control/Keyboard Layouts/E0010804"
即可;

win10我在2017年时使用了录制方式导出了字序和词序,用到了今年2025.6.18:
    "https://github.com/gamefunc/winXpQuanPinRecord"

2025.6.18我更新电脑从intel i5_2550k_z77 升级到 amd_7700_b650, 顺路升级为win11;
    偶尔知道了原来winxp下自身就有可以把全拼输入法"WINPY.MB"的字序词频导出的工具:
        "c:/program files/windows nt/accessories/imegen.exe"
        逆转换 -> 选择 "winpy.mb" 文件, 点 逆转换,
            之后会生成对应的 "WINPY.txt";

该脚本就是处理导出的"WINPY.txt", 让他可通过:
    "https://github.com/studyzy/imewlconverter"
    进行转换为用户自定义短语;

使用:
    如后面图片所示, 把导出的: "Win10微软拼音词库.dat"
    改名为: "ChsPinyinEUDPv1.lex"
    复制(覆盖): "%appdata%/Microsoft/InputMethod/Chs/ChsPinyinEUDPv1.lex"
    即可; 不需要在设置的自定义短语中导入,因为会卡死的; 
    之后如果要清除这些自定义短语就直接删除 "ChsPinyinEUDPv1.lex" 文件即可;
    

```   

![image](https://github.com/gamefunc/winxp_quanpin_freq_dict/blob/main/imgs/comp0.jpg)    
![image](https://github.com/gamefunc/winxp_quanpin_freq_dict/blob/main/imgs/comp1.jpg)    
![image](https://github.com/gamefunc/winxp_quanpin_freq_dict/blob/main/imgs/sl0.jpg)    
![image](https://github.com/gamefunc/winxp_quanpin_freq_dict/blob/main/imgs/sl1.jpg)    
![image](https://github.com/gamefunc/winxp_quanpin_freq_dict/blob/main/imgs/sl2.jpg)    
![image](https://github.com/gamefunc/winxp_quanpin_freq_dict/blob/main/imgs/winset0.jpg)    
![image](https://github.com/gamefunc/winxp_quanpin_freq_dict/blob/main/imgs/winset1.jpg)    
![image](https://github.com/gamefunc/winxp_quanpin_freq_dict/blob/main/imgs/winset2.jpg)    
![image](https://github.com/gamefunc/winxp_quanpin_freq_dict/blob/main/imgs/winset3.jpg)    
![image](https://github.com/gamefunc/winxp_quanpin_freq_dict/blob/main/imgs/winset4.jpg)    
![image](https://github.com/gamefunc/winxp_quanpin_freq_dict/blob/main/imgs/winset5.jpg)    
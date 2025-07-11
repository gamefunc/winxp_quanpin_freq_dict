"""
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

"""
import os, sys, json
import regex as re

F = os.path.dirname(__file__)


# WINPY.TXT路径:
WINPY_TXT_PATH = os.path.join(F, "WINPY.TXT")

# 深蓝导入用的词汇txt输出路径:
SENLAN_SRC_OUT_PATH = os.path.join(F, "out_senlan_src.txt")
# 输出的分割符:
SPLIT_SYMBOL = "\t"


# 有的拼音里面超过100个字, 会卡死, 限制最大6页大概60个就可以了;
NUM_PER_PINYIN_MAX = 88

""" 记录组合, 与 MAX_PRE_LINE有关, 最后排序出去:{
    "a": ["啊", "阿", ...],
    "aba": ["阿爸", ...],
    "le": ["肋", ...]
}
"""
PINYIN_DICT = {}


# 分离汉字与拼音的RE表达式:
HAN_PINYIN_PATTERN = re.compile(r"^(.+?)([a-zA-Z].*)$")




"""
分离 WINPY_TXT_PATH 每行得出:
    黄牌警告huangpaijing: ('黄牌警告', 'huangpaijing')
    肋jin: ('肋', 'jin')
    肋lei jin: ('肋', 'lei jin')
"""
def get_han_pinyin(line: str) -> tuple[str, str] | None:
    global HAN_PINYIN_PATTERN
    m = re.match(HAN_PINYIN_PATTERN, line.strip())
    if m:
        han_char = m.group(1)
        pinyin_part = m.group(2).strip()
        return (han_char, pinyin_part)
    else:
        return None

"""
读取 WINPY_TXT_PATH 并 更新 PINYIN_DICT:
"""
def update_PINYIN_DICT() -> None:
    global PINYIN_DICT

    # 记录是否已进入 "[Text]":
    is_into_text = False

    with open(WINPY_TXT_PATH, "r", encoding="utf-16") as f:
    # with open(WINPY_TXT_PATH, "rb") as f:
        for src_line in f:
            line = src_line.strip()
            if not line: continue

            # 未进入 "[Text]"之后, 所以不处理:
            if not is_into_text: 
                if line == "[Text]": is_into_text = True; 
                continue
            
            # 之后都是进入[Text]后的:
            han_pinyins = get_han_pinyin(line)

            # 没找到打印一下:
            if not han_pinyins:
                print(f"没han_pin: {line = }"); continue
            
            # 如果不是返回了2个, 打印一下:
            if len(han_pinyins) != 2:
                print(f"没有分离出2个: {line = }"); continue
            han, pinyins = han_pinyins

            # # 打印一下某些关键字:
            # for test_s in ["警告", "十一国庆节", "肋", "牞"]:
            #     if test_s in line:
            #         print(f"'{line}': {han_pinyins = }"); print()

            # "肋le jin" 出来的是: ('肋', 'le jin') 需要处理一下pin只取第一个:
            pinyin_units = pinyins.split()
            pinyin = pinyin_units[0]

            # # 打印多读音的字并保存:
            # if len(pinyin_units) > 1: 
            #     print(f"多读音的字: {line = }, {han_pinyins = }")
            #     with open("多读音的字词.txt", "a", encoding="utf-8") as of:
            #         of.write(f"{line = }; {han_pinyins = }; {pinyin = }\n")


            # 添加到 PINYIN_DICT 方便自己转换格式:
            if pinyin not in PINYIN_DICT: PINYIN_DICT[pinyin] = []
            PINYIN_DICT[pinyin].append(han)



"""
保存 PINYIN_DICT 到 txt, 需要先运行: update_PINYIN_DICT():
"""
def save_PINYIN_DICT_to_json_txt() -> None:
    global PINYIN_DICT
    with open("PINYIN_DICT.txt", "w", encoding="utf-8") as f:
        d = json.dumps(PINYIN_DICT, ensure_ascii=False, indent=2)
        f.write(d)

            
"""
运行:
"""
def main() -> None:
    global PINYIN_DICT

    # 查看一下原始文件编码:
    with open(WINPY_TXT_PATH, "rb") as f: print(f.read(100))

    update_PINYIN_DICT()
    # save_PINYIN_DICT_to_json_txt()

    out_txt = ""
    for pinyin in PINYIN_DICT:
        # 词频, 就是输入的选择位:
        i = 1
        for han in PINYIN_DICT[pinyin]:
            out_txt += f"{pinyin}{SPLIT_SYMBOL}{han}{SPLIT_SYMBOL}{i}\n"
            i += 1
            if i >= NUM_PER_PINYIN_MAX:
                print(f"{pinyin = }: 总: {len(PINYIN_DICT[pinyin])}条, "
                      f"超过: {NUM_PER_PINYIN_MAX} 条, 截断不再加;")
                break

    
    with open(SENLAN_SRC_OUT_PATH, "w", encoding="utf-16") as f:
        f.write(out_txt)

    with open(SENLAN_SRC_OUT_PATH, "rb") as f:
        print(f.read(100))



# 运行:
try:
    main()
    print("执行完毕")
except Exception as e:
    print(f"main()运行出错: {e = }")


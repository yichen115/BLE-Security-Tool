import sys

def colorize(text, color=None, attrib=None):
    """
    用来高亮显示文本
    参考: https://github.com/longld/peda/blob/master/lib/utils.py
    """
    COLORS = {"black": "30", "red": "31", "green": "32", "yellow": "33",
                "blue": "34", "purple": "35", "cyan": "36", "white": "37"}
    CATTRS = {"regular": "0", "bold": "1", "underline": "4", "strike": "9",
                "light": "1", "dark": "2", "invert": "7"}

    CPRE = '\033['
    CSUF = '\033[0m'

    ccode = ""
    if attrib:
        for attr in attrib.lower().split():
            attr = attr.strip(",+|")
            if attr in CATTRS:
                ccode += ";" + CATTRS[attr]
    if color in COLORS:
        ccode += ";" + COLORS[color]
    return CPRE + ccode + "m" + text + CSUF

def green(text, attrib=None):
    return colorize(text, "green", attrib)

def red(text, attrib=None):
    return colorize(text, "red", attrib)

def cyan(text, attrib=None):
    return colorize(text, "cyan", attrib)

def purple(text, attrib=None):
    return colorize(text, "purple", attrib)

def yellow(text, attrib=None):
    return colorize(text, "yellow", attrib)

def blue(text, attrib=None):
    return colorize(text, "blue", attrib)
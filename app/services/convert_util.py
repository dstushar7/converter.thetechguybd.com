import re
from app.services import convert as doConvert


def doCharMap(text, charMap):
    for srcKey, keyVal in charMap.items():
        text = preg_replace(srcKey, keyVal, text)
    return text


def mb_strlen(str_val):
    return len(str_val)


# returns the i-th byte of the multi-byte string str_val
def mbCharAt(str_val, i):
    try:
        return str_val[i]
    except:
        pass


# returns the javascript 'substring' method equivalent
def subString(string, frm, to):
    # return mb_substr(string, from, to - from)
    return string[frm:to]


def preg_replace(srcKey, keyVal, text):
    #srcKey = "@"+srcKey+"@"
    return re.sub(srcKey, keyVal, text)


# New Add
def replace_eKar_after_whitespace(text):
    result = []
    for i, char in enumerate(text):
        if char == "‡" and (i == 0 or text[i - 1] in [" ", "\n"]):
            result.append("†")
        else:
            result.append(char)
    return "".join(result)


def unicode_to_bijoy(text: str) -> str:
    """
    Example function to convert from Unicode to Bijoy using your custom module.
    """
    converter = doConvert.Unicode()  # Adjust to match your actual class or function
    return converter.convertUnicodeToBijoy(text)


def bijoy_to_unicode(text: str) -> str:
    """
    Placeholder function for the opposite conversion (Bijoy to Unicode).
    """
    return text

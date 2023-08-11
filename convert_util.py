import re

def doCharMap(text, charMap):
    for srcKey, keyVal in charMap.items():
        text = preg_replace(srcKey, keyVal, text)
    return text

def mb_strlen(str):
    return len(str)

# returns the i-th byte of the multi-byte string str
def mbCharAt(str, i):
    # return mb_substr(str, i, 1)
    try:
        return str[i]
    except:
        pass

# returns the javascript 'substring' method equivalent
def subString(string, frm, to):
    # return mb_substr(string, from, to - from)
    return string[frm:to]

def preg_replace(srcKey, keyVal, text):
    #srcKey = "@"+srcKey+"@"
    return re.sub(srcKey, keyVal, text)


def replace_eKar_after_whitespace(text):
    result = []
    i = 0
    if text.startswith('‡'):
        result.append('†')
        i += 1
    while i < len(text):
        if i < len(text) - 1 and text[i] == ' ' and text[i + 1] == '‡':
            result.append(text[i])  # Append the whitespace
            result.append('†')      # Replace '‡' with '†'
            i += 1                  # Skip the next character
        else:
            result.append(text[i])
        i += 1
    return ''.join(result)


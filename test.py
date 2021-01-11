import chardet
s = '\u30\u2e\u30\u31'

print(s.encode("utf-16").decode("unicode_escape"))  # 你好
print(str(s))  # 你好
print(repr(s))  # '你好'
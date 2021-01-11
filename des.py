#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding:utf-8
# @Author : Benjamin
# @Time   : 2020/7/15 15:47

# des模式  填充方式  ECB加密方式
from pyDes import des, PAD_PKCS5, ECB

#  秘钥  （如果和Java对接，两边要有相同的秘钥）
DES_KEY = "12345678"

s = '哈哈'.encode()  # 这里中文要转成字节， 英文好像不用

des_obj = des(DES_KEY, ECB, DES_KEY, padmode=PAD_PKCS5)  # 初始化一个des对象，参数是秘钥，加密方式，偏移， 填充方式


secret_bytes = des_obj.encrypt(s)   # 用对象的encrypt方法加密
s = des_obj.decrypt("")   # 用对象的decrypt方法解密
print(secret_bytes,s)

def encrypt(s):
    s = s.encode()  # 这里中文要转成字节
    secret_bytes = des_obj.encrypt(s)  # 用对象的encrypt方法加密
    return secret_bytes.hex()


def decrypt(secret_bytes):
    secret_bytes = bytes.fromhex(secret_bytes)  # 这里中文要转成字节
    s = des_obj.decrypt(secret_bytes)  # 用对象的decrypt方法解密
    return s.decode()


test = encrypt("123")

print(test)
print(decrypt(test))

#! /usr/bin/env python
# coding=utf-8


import win32com.server.util, win32com.client

# 以下代码解决输出乱码问题
import sys

# print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf8')


# print sys.getdefaultencoding()

class __PyWinJsAes:

    def __init__(self):

        js = win32com.client.Dispatch('MSScriptControl.ScriptControl')
        js.Language = 'JavaScript'
        js.AllowUI = False
        js.AddCode(self.__readJsFile("jsfiles/aes.js"))
        js.AddCode(self.__readJsFile("jsfiles/aesutil.js"))
        self.jsengine = js

    def __readJsFile(self, filename):

        fp = file(filename, 'r')
        lines = ''
        for line in fp:
            lines += line
        return lines

    def __driveJsCode(self, func, paras):

        if paras:
            return self.jsengine.Run(func, paras[0], paras[1])
        else:
            return self.jsengine.Run(func)

    def encrypt(self, text, key):
        return self.__driveJsCode("DoAesEncrypt", [text, key])

    def decrypt(self, text, key):
        #         print text,key
        return self.__driveJsCode("DoAesDecrypt", [text, key])


JsAes = __PyWinJsAes()

if __name__ == '__main__':
    p = JsAes.decrypt("U2FsdGVkX19FDZhhIeMCH9SHfLg8B34NUbWxnuRFtc++fkhyKov9urtLuG7qatqm TP2/LEy+g35Jarbm5KoGCg==",
                      "456")
    print
    '*' * 20
    print
    p
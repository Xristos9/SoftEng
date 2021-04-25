import re

def check_blank(word0,word1,word2,word3):
    if word0 == "" or word1 == "" or word2 == "" or word3 == "":
        return False
    else:
        return True

def checker(pas):
    if(len(pas)<8):
        return False


    stringArray = list(pas)

    digitFlag = False
    symbolFlag = False
    upperFlag = False

    for i in stringArray:
        if re.match('\d', i):
           digitFlag = True

        if re.match('[A-Z]', i):
            upperFlag = True

        if re.match('[ -/:-@[-`{-~]', i):
            symbolFlag = True


    if digitFlag == True and upperFlag == True and symbolFlag == True:
        return True
    else:
        return False
import os
    	
#utlis
def parse(text):
	return readToken(tokenize(text))

def tokenize(string):
	return string.replace('（',' （ ').replace('）',' ） ').split()

def readToken(tokens):
	if len(tokens) == 0:
		raise SyntaxError('读取文本长度为0')
	token = tokens.pop(0)
	if token == '（':
   		l = []
   		while tokens[0]!='）':
   			l.append(readToken(tokens))
   		tokens.pop(0)
   		return l
	elif token == '）':
   		raise SyntaxError('错误的 ） ')
	else:
   		return token
#环境
# str = "（（赋 甲 10） （乘 甲 （乘 甲 甲）））"
dic = {}

def eval(parseText):

	parseText = transNum(parseText)
	if type(parseText)==int or type(parseText)==float:#不可分割的基本类型
		return parseText
	else:
		for x in parseText:#列表或者字符类型
			if type(x)==list:
				eval(x)
			else:
				if x == '赋':
					dic[parseText[1]] = eval(parseText[2])
					return
				elif x == '加':
					if parseText in firParseText:
						print(parseText[1],"加",parseText[2],"结果为",eval(parseText[1])+eval(parseText[2]))
						return
					return eval(parseText[1])+eval(parseText[2])
				elif x == '减':
					if parseText in firParseText:
						print(parseText[1],"减",parseText[2],"结果为",eval(parseText[1])-eval(parseText[2]))
						return
					return eval(parseText[1])-eval(parseText[2])
				elif x == '乘':
					if parseText in firParseText:
						print(parseText[1],"乘",parseText[2],"结果为",eval(parseText[1])*eval(parseText[2]))
						return
					return eval(parseText[1])*eval(parseText[2])
				elif x == '除':
					if parseText in firParseText:
						print(parseText[1],"除",parseText[2],"结果为",eval(parseText[1])/eval(parseText[2]))
						return
					return eval(parseText[1])/eval(parseText[2])
				else :
					return dic[x]

def transNum(parseText):
	try:
		return int(parseText)
	except Exception as e:
		try:
			return float(parseText)
		except Exception as e:
			return parseText
				
def repl():
    while True:
    	str = input()
    	if str is not None:
    		try:
    			global firParseText
    			firParseText = parse(str)
    			eval(firParseText)
    		except Exception as e:
    			print('拼写错误')
    		
repl()
os.system("pause")
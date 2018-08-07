country=input('請問你是哪一國的人:')
age=input('請輸入年齡：')
age=int(age)
if country == '台灣' :
	if age <18 :
		print('抱歉，你還不能開車')
	else :
		print('你可以開車')

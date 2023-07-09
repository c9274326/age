driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有！')
	raise SystemExit
age =  int(input('請問你的年齡？'))#input 存下來的都是字串
if driving == '有':
	if age >= 18:
		print('你通過測驗了！')
	else :
		print('奇怪 你怎麼有開過車？')
elif driving == '沒有':
	if int(age) < 18:
		print('再過幾年就可以考了！')
	else:
		print('奇怪 你怎麼還不去考駕照？')



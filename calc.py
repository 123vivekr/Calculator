from tkinter import *

root = Tk()
res = StringVar()
res.set(' ')
expression = ''

def button_press(no):
	global expression
	if(no == '='):
		res.set('Result= '+ str(gen_result()))
		return
	elif(no == '<'):
		expression=expression[:-1]
		res.set(expression)
		return
	expression=expression+str(no)
	res.set(expression)

def gen_result():
	if (expression == ''):
		return 'please enter valid expression'

	return eval(expression.replace('x', '*'))


root.title("Calculator")
root.geometry('180x200')

top = LabelFrame(root, bg='white', fg='cyan')
top.grid(row=0, column=0)
result = Label(top, textvariable=res)
result.grid(row=0, column=0)


#numpad
numpad = Frame(root)
numpad.grid(row=1,column=0, sticky='W')
#creating buttons
buttons = []
for i in range(1,10):
	buttons.append(Button(numpad, text='{}'.format(i), command=lambda x=i: button_press(x))) #learn
b0=(Button(numpad, text='0', command=lambda: button_press(0)))
count = 0
for i in range(3):
	for j in range(3):
			buttons[count].grid(row=i, column=j)
			count += 1
b0.grid(row=4,column=1)

#arithmetic operation buttons
arithop = Frame(root)
arithop.grid(row=1, column=1, sticky='W')
Button(arithop, text='+', command= lambda: button_press('+')).grid(row=1,column=0)
Button(arithop, text='-', command= lambda: button_press('-')).grid(row=2,column=0)
Button(arithop, text='x', command= lambda: button_press('x')).grid(row=3,column=0)
Button(arithop, text='/', command= lambda: button_press('/')).grid(row=4,column=0)
Button(arithop, text='=', command= lambda: button_press('=')).grid(row=5,column=0)
Button(arithop, text='<', command= lambda: button_press('<')).grid(row=0,column=0)

root.mainloop()
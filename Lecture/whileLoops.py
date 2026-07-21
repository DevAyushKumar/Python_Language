'''Python while loop
As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.'''
count=5
while (count>0):
    print(count, end="")
    count = count - 1
'''here, the count varaibles is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter varaible (the varaible, in our case) or the loop will continue forever'''

'''Else with while loop
We can use the else statement with the while loop. Essentially what else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed'''
x=5
while (x>0):
    print(x)
    x-=1
else:
    print('counter is 0')
    
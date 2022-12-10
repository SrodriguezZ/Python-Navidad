from colorama import init,Fore, Back, Style
num = 15
print(Fore.GREEN+'FELIZ NAVIDAD'.center(25,'-'))
for i in range(num):
    print(' '*(num-i-1)+'*'*(2*i+1))

for n in range(int(num/2)):
    print(' '*int(num-num/4)+'*'*int(num/2))
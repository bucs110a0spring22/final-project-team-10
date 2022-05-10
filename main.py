import pygame
from src import Controller
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    mainloop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

#Group Final Project Rep Exercise (3/22)
mylist = []

print("Enter 4 numbers:")

def add2List(a,b,c,d):
  mylist.extend([a,b,c,d])
  for i in range(4):
    print(mylist[i])
  mylist[0], mylist[-1] = mylist[-1], mylist[0]
  print(mylist)
  
a = int(input("1."))
b = int(input("2."))
c = int(input("3."))
d = int(input("4."))

add2List(a,b,c,d)

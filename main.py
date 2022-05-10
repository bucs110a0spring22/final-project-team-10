import pygame
#import your controller
from src import Controller

def main():
  pygame.init()
  while True:
    Controller.mainloop()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

main()


#Group Final Project Rep Exercise (3/22)
def add2List(a,b,c,d):
  mylist = []
  print("Enter 4 numbers:")
  mylist.extend([a,b,c,d])
  for i in range(4):
    print(mylist[i])
  mylist[0], mylist[-1] = mylist[-1], mylist[0]
  print(mylist)
  
#a = int(input("1."))
#b = int(input("2."))
#c = int(input("3."))
#d = int(input("4."))

#add2List(a,b,c,d)

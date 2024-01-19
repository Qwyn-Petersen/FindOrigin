def closest2_origin():

  x2 = 0
  switch = True

  while(switch):
    
    x = x2/100
    if (3*x**2 - 4*x + 1 == 0):
      print(x)
      switch = False
    else:
      x2 += 1
  
def main():
  closest2_origin()

if __name__=="__main__":
    main()
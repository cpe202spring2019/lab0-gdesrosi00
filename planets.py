def weight_on_planets():
   weight = input("What do you weigh on earth? ")
   weight = int(weight)
   print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(weight * .38, weight * 2.34))
   
if __name__ == '__main__':
   weight_on_planets()

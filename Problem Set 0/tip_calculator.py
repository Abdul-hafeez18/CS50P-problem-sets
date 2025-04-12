def main():
    cost=dollars_to_float(input("COST OF THE FOOD"))
    tip=percent_to_float(input("TIP YOU WANT TO GIVE IN PERCENTAGE"))
    total_tip=cost*tip
    print(f"total tip is ${total_tip:.2f}")

def dollars_to_float(demo_cost):
  word1= float(demo_cost.replace("$",""))
  return word1

def percent_to_float(demo_tip):
   word2=float(demo_tip.replace("%",""))/100
   return word2

main()

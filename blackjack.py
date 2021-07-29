import random
count = 0
count1=0
rangedrawx=list(range(1,11))
rangedrawy=list(range(1,11))
x = []
x.append(random.choices(rangedrawx, weights = [1,1,1,1,1,1,1,1,1,4], k=1)[0]);
y = []
y.append(random.choices(rangedrawy, weights = [1,1,1,1,1,1,1,1,1,4], k=1)[0]);
print("Player =",y[0])
print("Dealer =",x[0])
while y[count] < 21 and y[count - 1] < 21:
  hs = input("Do you want to hit or stand h/s \n")
  if hs == "h":
    y.append(random.choices(rangedrawy, weights = [1,1,1,1,1,1,1,1,1,4], k=1)[0]+y[count]);
    count +=1
    if y[count] - y[count-1] != 1 and y[count] - y[count-1] != 11:
      print ("You drew",y[count] - y[count-1], "\nYou now have",y[count])
    if y[count] - y[count-1] == 1 or y[count] - y[count-1] == 11:
      elevone = input("You drew an ace! Would you like to add 1 or 11 to your count (1/11) \n")
      if elevone == "1":
        y[count] = y[count-1]+1
        print ("You drew 1\nYou now have", y[count])
      elif elevone == "11":
        y[count] =y[count-1]+11
        print ("You drew 11\nYou now have", y[count])
      else:
        print("That is neither 1 or 11 so I'll choose the best number for you")
        if y[count] <= 10:
          y[count - 1] = y[count-1]+11
          print ("You drew 11\nYou now have", y[count - 1])
        else:
          y[count - 1] = y[count-1]+1
          print ("You drew 1\nYou now have", y[count - 1])
  elif hs == "s":
    count +=1
    y.append(0)
    break
  else:
    print("You didnt enter h/s so I'm going to stand for you")
    break
if y[count] > 21:
  print(y[count])
  print("Bust!")
elif y[1] == 21:
  print("Blackjack! (Natural)")
elif y[count] == 21:
  print("Blackjack!")
else:
  while x[count1] < 17:
    if count1 < 17:
      x.append(random.choices(rangedrawx, weights = [1,1,1,1,1,1,1,1,1,4], k=1)[0]+(x[count1]));
      count1 +=1
      if x[count1] - x[count1-1] ==1:
        if x[count1] >= 6 and x[count1] < 11:
          x[count1] = x[count1-1]+11
          print ("The dealer drew 11\nThe dealer now has", x[count1 - 1])
        else:
          x[count1] = x[count-1]+1
          print ("The dealer drew 1\nThe dealer now has", x[count1])  
      else:
        print("The dealer drew",x[count1]-x[count1 -1],"\nThe dealer now has",x[count1])
    else:
      break
  if y[count] > x[count1] and y[count] <= 21 or x[count1] > 21:
    print("Dealer =",x[count1],"\nPlayer =",y[count])
    print("Player wins!")
  elif y[count] == x[count1]:
    print("Dealer =",x[count1],"\nPlayer =",y[count])
    print("Tie!")
  else:
    print("Dealer =",x[count1],"\nPlayer =",y[count])
    print("Player loses!") 

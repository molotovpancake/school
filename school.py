def main():

  print ("Hello Alex")
  ui = input ("What timetable week are you on? (Answer 'week 1' for week 1 or anything else for week 2.) ")
  
  #items
  books = ["French \n", "RE \n", "English \n", "History \n", "Math \n", "Geography \n" , "Chemistry \n", "Biology \n", "Physics \n", "PE kit \n"]
  dailyquip = "Journal\nPencil case\nTimetable\n"
  #week 1
  end = False
  while end == False:
  try:
    if ui == ("week 1"):
        weekday = input ("What day is it? ")
        if weekday == ("Monday"):
          print ("You need the following items: \n" + books[0] + books[1] + books[2] + books[3] + dailyquip)
        else:
          if weekday == ("Tuesday"):
            print ("You need the following items: \n" + books[4] + books[2] )  
            
            
            end = True
    else:
      if ui == ("week 2"):
      else:
        print ("That is not a valid week.")
  
   #week 2
  
  except:
    print ("That is not a valid answer.")
main()

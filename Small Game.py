print("  ***Welcome To The Game***  ")
num=str(input("Do You Play This Game ? "))
if num.lower()!="yes":
    quit()
print("Okey Let's Play This Game")
score=0
answer=str(input("What Does CPU Stand for ?"))
if answer=="Central processing unit":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does TCP Stand for ?"))
if answer=="Transmission Control Protocol":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does IP Stand for ?"))
if answer=="Internet Protocol":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does DSP Stand for ?"))
if answer=="Deputy Superintendent of Police":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does SSB Stand for ?"))
if answer=="Service Selection Board":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does APK Stand for ?"))
if answer=="Android Application Package":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does API Stand for ?"))
if answer=="Application Programming Interface":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does ASCII Stand for ?"))
if answer=="American Standard Code for Information Interchange":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does ATM Stand for ?"))
if answer=="Automated Teller Machine":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does AWS Stand for ?"))
if answer=="Amazon Web Services":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does BBC Stand for ?"))
if answer=="British Broadcasting Corporation":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does BCA Stand for ?"))
if answer=="Bachelor of Computer Applications":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does BCCI Stand for ?"))
if answer=="Board of Control of Cricket in India":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
answer=str(input("What Does BHIM Stand for ?"))
if answer=="Bharat Interface for Money":
    print('Correct Answer!')
    score+=1
else:
    
        print("InCorrect!")
print("Your Score"  +str(score)+  "Question Currect")
print("YourScore "  +str((score/5)*60)+  "%.")

    
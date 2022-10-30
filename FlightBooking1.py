import datetime
import os


  
def code_check(ref_no):
    
        
    if ref_no>99 and ref_no<1000:#range between 99-1000
        print("code is valid")
        return True
    else:
        count=1#false statement
        while(count):
            ref_no=int(input("Enter 3 digit code between 99 and 1000\n"))
            if ref_no>99 and ref_no<1000:
                return ref_no
                count=0
        
def check_file(f_name,l_name,ref_no):#File checking if it exist before or not
    try:
        file=open(f_name+l_name+str(ref_no)+".txt","r")
        file.close()
        print("only one seat can be booked at a time")
        print("-------------------------------------")
        return False
    except FileNotFoundError:
        return True
    
def flight_book():#main for details information and creating file
    total=0
    f_name=str(input("Enter first name?\n")).lower()
    l_name=str(input("Enter last name?\n")).lower()
    ref_no=int(input("Enter 3 digit code between 99 and 1000\n"))
    if(code_check(ref_no)):
        if(check_file(f_name,l_name,ref_no)):
        
            
            d_address=str(input("Enter customer destination address?\n")).lower()
            nation=str(input("Enter customer nationality?\n")).lower()
            religion=str(input("Enter customer religion\n")).lower()
            if religion=='muslim' :
                print("customer food type is halal\n")
            else:
                print("meal is not halal\n")
            print("Since booking for 2020 only.")
            date1=int(input("Select month of booking eg jan=01,feb=02\n"))
            if date1<0 or date1 >12:
                date1=int(input("Invalid,Select month of booking eg jan=01,feb=02\n"))
            date2=int(input("Select a day,which day you want to book\n"))
            if date2<0 or date2>30:
                date2=int(input("Invalid day,Select a day(00-31),which day you want to book\n"))
            print("What time is your flight is ?")
            time1=int(input("select between 01-23 hours\n"))
            if time1<0 or time1>23:
                print("Invalid hours,What time is your flight is ?")
            time2=int(input("select between 00-61 minutes ?\n"))
            if time2<0 or time2>60:
                time2=int(input("Invalid,minutes ?\n"))
            total=total+1
            #creating file if not pre exist using fname,last name and code   
            record=open(f_name+l_name+str(ref_no)+".txt","w")
            record.write(f_name+" "+l_name+" "+str(ref_no)+" "+d_address+" "+nation+" "+religion+" "+str(date1)+" "+str(date2)+" "+str(time1)+" "+str(time2)+" "+str(total))
            
            record.close()


            #summary
            print("First Name           : "+f_name)
            print("Last Name            : "+l_name)
            print("Nationality          : "+nation)
            print("Customer code        : "+str(ref_no))
            print("Flight               : "+d_address)
            
            print("Flight Date time    : "+"DATE :"+str(date2)+"-"+str(date1)+"-"+str(2020)+" "+"TIME: "+str(time1)+":"+str(time2))
            
        else:
            print("customer is not allowed to book more than 1 time")
    else:
        print("Invalid, value plaese try again")
        
def check_halal():#opening pre exist file to get information about halal or not
    f_name=str(input("Enter customer first name?\n")).lower()
    l_name=str(input("Enter customer last name?\n")).lower()
    ref_no=int(input("Enter 5digit code between 9999 and 100000\n"))
    try:
        record=open(f_name+l_name+str(ref_no)+".txt","r")#trying to open a file name that contain fname lname and code
        new1=record.read()
        new_file=new1.split()#making list function
        if new_file[5]=='muslim' or new_file[5]=='islam':#main condition wheather halal or not
                print("customer is qualified for halal\n")
        else:
            print("meal does not include halal\n")
        
    except FileNotFoundError:#if file could not found
        print("Customer details not Found")
def check_seats():
    f_name=str(input("Enter customer first name?\n")).lower()
    l_name=str(input("Enter customer last name?\n")).lower()
    ref_no=int(input("Enter 5digit code between 9999 and 100000\n"))
    try:
        record=open(f_name+l_name+str(ref_no)+".txt","r")
        new1=record.read()
        new_file=new1.split()
        #Printing summary
        print("--------------------Booking Details----------")
        print('Customer Full name      :'+new_file[0] +" "+new_file[1])
        print('Customer Nationality    :'+new_file[5])
        print("Customer flight         :"+new_file[3]+" To "+new_file[4])
        print('Customer reference code :'+str(new_file[2]))
        print("Flight Booking date     :"+str(new_file[8])+"-"+str(new_file[7]+"-"+str(2019)+" Time "+str(new_file[9])+"::"+new_file[10]))
        print("Total seats available :"+str(50-int(new_file[11])))
                    
        print('---------------------------------------------')
        
        
        
    except FileNotFoundError:
        print("reservation not found")

    
def cancel_booking():
    f_name=str(input("Enter customer first name?\n")).lower()
    l_name=str(input("Enter customer last name?\n")).lower()
    ref_no=int(input("Enter 5digit code between 9999 and 100000\n"))
    try:
        record=open(f_name+l_name+str(ref_no)+".txt","r")
        new1=record.read()
        new_file=new1.split()
    
        
        #final confirm and asking current date and time
        ask=str(input("Are you sure you want to cancel this flight? y/n \n")).lower()
        if ask=='y':
            print("Please enter todays date and time/since flight cannot be canceled before 2 hours flight")
            date1=int(input("what month is today eg jan=01,feb=02\n"))
            if date1<0 or date1 >12:
                date1=int(input("Invalid,Select month  eg jan=01,feb=02\n"))
            date2=int(input("Select a days,today\n"))
            if date2<0 or date2>30:
                date2=int(input("Invalid day,Select a day(00-31),which day is today\n"))
            
            time1=int(input("what time is now, 01-23 hours?\n"))
            if time1<0 or time1>23:
                print("Invalid hours,What time is now ?")
            time2=int(input("select what time is now between 00-61 minutes ?\n"))
            if time2<0 or time2>60:
                time2=int(input("Invalid,minutes try again ?\n"))

            #condition before 2 hours flight cannot be canceled 
            if date1<int(new_file[7]):#checking remaining month is more than 1 month or not
                os.remove(f_name+l_name+str(ref_no)+".txt")
                print("Flight canceled successfully")
            if date1==int(new_file[7]):#if same month flight but need to cancel
                if date2<int(new_file[8]):#if remaining day is more than 1 day or not
                    os.remove(f_name+l_name+str(ref_no)+".txt")
                    print("Flight canceled successfully")
            if date1==int(new_file[7]):#if day is same check hours
                if date2==int(new_file[8]):#check hours befor cancel
                    if (int(new_file[9])-time1)>2:#if still more than 2 hours left it allow to cancel seats
                        os.remove(f_name+l_name+str(ref_no)+".txt")
                        print("flight is canceled successfully")
                    else:
                        print("Flight cannot be canceled before 2 hours late")#if flight is less than 2 hours
                
                        
        
    except FileNotFoundError:
        print("Customer detail is not found")
 #main for calling functions with choice and count.               
count=1
while(count):
	
	choice=int(input("enter numbers\n"+"1.book flight\n"+"2.check seats\n"+"3.check halal\n"+"4.cancel booking\n"))
	if(choice==1):
		flight_book()
	elif (choice ==2):
		check_seats()
	elif choice==3:
		check_halal()	
	elif choice ==4:
		cancel_booking()	
	else:
		count=1    
    


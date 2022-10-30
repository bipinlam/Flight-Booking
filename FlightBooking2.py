import datetime
import csv
import os
        
  

def booking_seats():#main function for passanger details.
    customers=[]# list to record details
    total=50#Total no of seats
    availabel_seats=0# this will updated every loop as a count
    
    if availabel_seats>0 or availabel_seats<51:#conditions and customer details
        first_name=str(input("Enter customer first name?\n"))
        last_name=str(input("Enter customer last name?\n"))
        current_address=str(input("Enter customer current address?\n"))
        destination_address=str(input("Enter customer destination address?\n"))
        nationality=str(input("Enter customer nationality?\n"))
        religion=str(input("Enter customer religion\n"))
        code=int(input("Enter 3 digit code between 99 and 1000\n"))
        if code<100 or code>999:#condition for 3 digit code
            code=int(input("Enter 3 digit code between 99 and 1000\n"))
        a_time=datetime.datetime.today()#time
            

        #append all data into customers list.
        customers.append(first_name)
        customers.append(last_name)
        customers.append(current_address)
        customers.append(destination_address)
        customers.append(nationality)
        customers.append(religion)
        customers.append(str(code))
        customers.append(str(a_time))
        #creating files with fname lname and code
        with open(first_name+last_name+str(code)+".csv","a",newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(customers)

        #creating count txt file to count no of seats booked
        try:
            recordfile=open('customer_count.txt','r')
            seat=int(recordfile.read())
            recordfile.close()
            recordfile=open('customer_count.txt','w')
            recordfile.write(str(seat+1))
        except FileNotFoundError:#if file not found it create new file to start count
            recordfile=open('customer_count.txt','w')
            recordfile.write(str(1))
            recordfile.close()
            
        csvfile.close()
        #creating summary display
        
        print("*************************************************")
        print("---------Booking successfully recorded-----------")
        print("First Name           : "+first_name)
        print("Last Name            : "+last_name)
        print("Nationality          : "+nationality)
        print("Customer code        : "+str(code))
        print("Flight Information   : "+current_address+" To "+destination_address)
        print("Conformation time    : " +str(a_time))
        if customers[5]=='muslim' or customers[5]=='islam':#halal condition 
            print("Note--Customer food Include 'halal'")
        else:
            print("Note--Customer food does not Include 'halal'")
            
            
            
        
        
        
        
        
        
        
        recordfile=open('customer_count.txt','r')#displaying total avilable seats
        availabel_seats=str(total-int(recordfile.read()))
        print('Total availabel seats    :'+availabel_seats)
        recordfile.close()
        print("-------------------------------------------------")
        print("*************************************************")
    else:# if seats are full or more than 50 it display.
        print("you are unable to register either seats are full or customer already registered")
            
            
            

        
def check_booking():#checking customer info 
    
    first_name=str(input('Enter first name of customer\n'))
    last_name=str(input('Enter last name of customer\n'))
    code=int(input("Enter customer code\n"))
    try:#try to open file that contain fname lname and code.
        with open(first_name+last_name+str(code)+'.csv','r') as csvfile:
            datareader=csv.reader(csvfile)
            for line in datareader:#reading datas in file.
                
                
                print("--------------Customer Information----------------")#display summary
                print("First Name           : "+line[0])
                print("Last Name            : "+line[1])
                print("Nationality          : "+line[4])
                print("Customer code        : "+line[6])
                print("Flight Information   : "+line[2]+" To "+line[3])
                print("Conformation time    : " +line[7])
                if line[5]=='muslim' or line[5]=='islam':
                    print("Note--Customer food Include 'halal'")
                else:
                    print("Note--Customer food does not Include 'halal'")
                print("-------------------------------------------------")
                

    except FileNotFoundError:#if file does not found it display.
        print("Sorry customer information is not been recorded or not found.")
    
    
    
    
def cancel_booking():#cancel booking.
    first_name=str(input('Enter first name of customer\n'))
    last_name=str(input('Enter last name of customer\n'))
    code=int(input("Enter customer code\n"))
    try:#opening file contain fname lname and code
        with open(first_name+last_name+str(code)+'.csv','r') as csvfile:
            datareader=csv.reader(csvfile)
            for line in datareader:
                #display summary from datas in file
                print("--------------Customer Information----------------")
                print("First Name           : "+line[0])
                print("Last Name            : "+line[1])
                print("Nationality          : "+line[4])
                print("Customer code        : "+line[6])
                print("Flight Information   : "+line[2]+" To "+line[3])
                print("Conformation time    : " +line[7])
                if line[5]=='muslim' or line[5]=='islam':
                    print("Note--Customer food Include 'halal'")
                else:
                    print("Note--Customer food does not Include 'halal'")
                    
        
                print("-------------------------------------------------")
                #delete file from system or cancel seats
                os.remove(first_name+last_name+str(code)+'.csv')
                print("booking has been successfully canceled")
                
                

    except FileNotFoundError:#if file not found it display
        print("Sorry customer information is not been recorded or not found.")
    
    


    
    
#main
v=1
while(v):#display initial loads
	print('-----------Welcome to AIH airways ---------\n')
	print('Choose any options\n')
	print('1 Book a AIH flights\n')
	print('2 Find Customer details \n')
	print('3 Cancel a flight\n')
	print('Press any other number to Exit')
	choice=int(input())#asking option
	if(choice==1):
		booking_seats()
	elif (choice ==2):
		check_booking()
		
	elif choice ==3:
		cancel_booking()
	else:
		v=0	  

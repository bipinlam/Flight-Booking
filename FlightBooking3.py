import datetime
import os

def book_flight():#creating files and adddiing passanger details
    total=60 #total no of seats availabel in flight
    first_name=str(input('Customer First Name?\n'))
    sur_name=str(input('Customer Last Name?\n'))
    address=str(input('Customer Current Address?\n'))
    address1=str(input('Customer Flight To?\n'))
    nationality=str(input('Customer Nationality?\n'))
    religion=str(input('Customer Religion?\n'))
    customer_key=int(input('Customer Unique code of 3 digit\n'))
    
    if customer_key<100 or customer_key>999:
        print('Please enter unique number between 99-1000')
        customer_key=int(input('Customer Unique code of 3 digit\n'))
            
    a_time=datetime.datetime.today()#adding current time for booking confermation
    record_file=open(first_name+sur_name+str(customer_key)+'.txt','w')#giving a file name
    record_file.write(first_name+' '+sur_name+' '+address+' '+address1+' '+nationality+' '+religion+' '+str(customer_key)+' '+str(a_time)+' :')#data inside a file
    try:#creating another file to count seats record
        recordfile=open('customer_data.txt','r')
        seat=int(recordfile.read())
        recordfile.close()
        recordfile=open('customer_data.txt','w')
        recordfile.write(str(seat+1))
    except FileNotFoundError:
        recordfile=open('customer_data.txt','w')
        recordfile.write(str(1))
        recordfile.close()
        
    record_file.close()
    #display resut
    print('******************booking summary*********************')
    print('Customer First Name      :'+first_name)
    print('Customer Last Name       :'+sur_name)
    print('Customer Flight from     :'+address+' To ' +address1)
    print('Customer code            :'+str(customer_key))
    print('Booked Confermation Time :'+str(a_time))


    if religion=='muslim'or religion=='islam':
        print("Meal Include halal")#halal Include
    else:
        print("Meal does not Include Halal")#Halal not Include
        
            
            
    record_file.close()
    recordfile=open('customer_data.txt','r')
    print('Total availabel seats    :'+(str(total-int(recordfile.read()))))
    recordfile.close()
    print('*******************************************************')
    

   
    
  
def customer_detail():#Passanger Booking Information,re-opening file and getting data
	fst_name=str(input('Enter first name of passenger\n'))
	lst_name=str(input('Enter last name of passenger\n'))
	code=int(input('Enter passenger code'))
	try:
		file=open(fst_name+lst_name+str(code)+'.txt','r')
		data=file.read()
		firstdata=''
		lastname=''
		address=''
		nation=''
		code=''
		g=0
		for value in data:
			firstdata+=value
			if value==' ':
				if(g==0):
					firstname=firstdata# first data value from file name,given input name.
				if(g==1):
					lastname=firstdata
				if(g==2):
					address=firstdata
				if(g==3):
					address1=firstdata
				if(g==4):
					nationality=firstdata
				
                                   
				g=g+1
				firstdata=''
		print('----------Customer Information------')		
		print('firstname    :'+firstname)
		print('lastname     :'+lastname)
		print('Address      :'+address)
		print('Flight To    :'+address1)
		print('Nationality  :'+nationality)		
	except FileNotFoundError:
		print('Customer information does not exit')    
    

def cancel_flight():#flight cancel after booking a flight.
	fst_name=str(input('Enter customer first name\n'))
	lst_name=str(input('Enter customer last name\n'))
	code=int(input('Enter unique code'))
	try:
		file=open(fst_name+lst_name+str(code)+'.txt','r')
		data=file.read()
		o_date=''
		o_time=''
		firstdata=''
		t=0
		for value in data:
                    
			firstdata+=value
			if value==' ':
				if(t==7):#time data place Hours
					o_date=firstdata
				if(t==8):#minutes
					for datas in firstdata:
						if datas==' ':
							break
						else:
							o_time=o_time+datas	
				t=t+1
				firstdata=''
		order_datetime=datetime.datetime.strptime(o_date+o_time, '%Y-%m-%d %H:%M:%S.%f')
		now_date=datetime.datetime.today()
		t_hours=now_date-order_datetime
		t_hours=(t_hours.total_seconds() / 3600)
	    
		if t_hours >2:#comparing with availabel hours befor flight
			print('order cannot be cancled ')
		else:
			working_di=os.getcwd()
			os.remove(working_di+'/'+fst_name+lst_name+str(code)+'.txt')
			record_file=open('customer_data.txt','r')
			seats=int(record_file.read())
			record_file.close()
			record_file=open('customer_data.txt','w')
			record_file.write(str(seats-1))
			record_file.close()
			print('Order has been cancled')
	except FileNotFoundError:
		print('Passenger with given information does not exit!')   

v=1
while(v):#initial display.
	print('-----------Welcome to Buddha airways ---------\n')
	print('Choose any options\n')
	print('1=>Book a flight\n')
	print('2=>Get Customer details \n')
	print('3=>Cancel a flight\n')
	print('Press any othe number to Exit')
	choice=int(input())#choice to ask multiple options
	if(choice==1):
		book_flight()#booking function
	elif (choice ==2):
		customer_detail()#customer info functions
		
	elif choice ==3:
		cancel_flight()	#cancel requests
	else:
		v=0	  



    



		
    
		
    


            
        
        
        
    
        

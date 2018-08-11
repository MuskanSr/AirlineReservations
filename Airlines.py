# Airline Reservation System


import  pickle
print ("====================================")
print ("====================================")
print ("====================================")
print ("==== AIRLINE MANAGEMENT SYSTEM =====")
print ("====================================")
print ("====================================")
print ("====================================")


class aires:
    input('Press Enter to continue...')
    def Enquiry(self,TId):
      self.TId=input("Please Enter Ticket ID :")
      global TId
      if TId == YourTId:      
         with open('Airline.txt', 'r') as file1:
         file1.read(-1)
         print ('Ticket ID: ',TId,'\nArName:',ArName,'\nArTo: ',ArTo,'\nArFrom:',ArFrom,'\nCustomer Name: ',CustomeName,'\nMobile                                     Number: ',CustMobNo)
      elif TId != YourTId:
         print('Invalid Ticket ID')
    def reservation(self,Arname,ArTo,ArFrom,Custname,CustMobNo.):

     global TId
     global ArName
     global ArTo
     global ArFrom
     global CustName
     global CustMobNumber
   
      self.ArName=input("Please Enter Airline Name :")
      self.ArTo=input("Please Enter To :")
      self.ArFrom=input("Please Enter From :")
      self.CustName=input("Please Enter Your Name :")
      self.CustMobNumber=input("Please Enter Your Mobile Numbers :")  
      

       with open('Airline.txt', 'w') as file:
         file.write('Ticket ID:'+TId)
         file.write('Airline Name :'+ArName)
         file.write('To :'+ArTo)
         file.write('From:'+ArFrom)
         file.write('Name:'+CustName)
         file.write('Mobile numbers:'+CustMobNumber)
    
   print("Successfully Booked Reservation your Ticket ID is : " + TId)

   def CancelTicket(self):
       global TId
       YourTId=input("Please Enter Ticket ID :")   
       if TId == YourTId:
      global ArName
      global ArTo
      global ArFrom
      global CustName
      global CustMobNumber
      ArName=''
      ArTo=''
      ArFrom=""
      CustName=''
      CustMobNumber=''
      print ('Ticket canceled successfully.')
   elif TId != YourTId:
      print('Invalid Ticket ID') 
   

  def menu(self):
     print  (‘=========Menu==========’) 
     print ('                                               ')
     print ('=========== 1. Airline Enquiry ================')
     print ('=========== 2. Airline Reservation=============')
     print ('=========== 3. Cancel Ticket ==================')
     print ('=========== 4. Quit Application ===============')
     print ('                                               ')
     print ('===============================================')
      

   
self.count = 0
global TId
TId="A1001"
global ArName  
global ArTo   
global ArFrom
global CustomeName
global CustMobNo

while (count < 9):
   menu()
   MenuID=input("Enter (1-4) Number :")
   if MenuID=="1":
       Enquiry()
   elif MenuID=="2":
      Reservation()
   elif MenuID=="3":
      CancelTicket()
   elif MenuID=="4":
      count=10

   count=count+1
   
print ("Good bye!")


      
      

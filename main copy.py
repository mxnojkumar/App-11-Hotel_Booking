import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv('hotels.csv', dtype={"id": str})

class Hotel:
    watermark = "The real Estate Company"
    
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        
    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = 'no'
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if hotel is available or not"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False
    
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)
    
    def __eq__(self, other) -> bool:
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False
        
        
class Ticket(ABC):
    
    @abstractmethod
    def generate():
        pass
        

class ResevationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
        
    def generate(self):
        content = f"""
        Thank you for your reservation
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content
    
    @property # Acts like a variable and not like a function 
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name
    
    @staticmethod # Not related with any attributes, but somehow related to functionality
    def convert(amount):
        return amount * 1.5
    
    
class DigitalTicket(Ticket):
    def generate():
        print("Here is your Eticket")
        

hotel1 = Hotel("134")
print(hotel1.watermark)
print(hotel1.name)

hotel2 = Hotel("188")
print(hotel2.watermark)
print(hotel2.name)

print(Hotel.watermark)
print(Hotel.get_hotel_count(df))
# print(Hotel.name) Gives error, class(here object) Hotel has no attribute 'name'.

ticket = ResevationTicket(customer_name=" john smith ", hotel_object=hotel1)
print(ticket.the_customer_name)
print(ticket.generate())

converted = ticket.convert(10)
print(converted)    
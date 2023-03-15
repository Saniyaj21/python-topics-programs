# single inheritence 
class phone:
    def __init__(self,model,ram,memory):
        self.model=model
        self.ram=ram
        self.memory=memory
        

    def details():
        print("This phone details")
    
    def price():
        print("Price is ..")
    

class smartPhone(phone):
    def __init__(self,model,ram,memory,battery):
        self.model=model
        self.ram=ram
        self.memory=memory
        self.battery=battery

    def details():
        print("This is smartphone details")


phone1 = phone("vivo", "4GB", "64GB")

nemSmPhone = smartPhone("oppo", "8GB", "128GB", "6000 MAH")
phone.details()
smartPhone.details()



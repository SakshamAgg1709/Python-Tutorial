#Multilevel Inheritance

class Dad:
    dance = 3
    basketball = 1
    pass

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I dance in {self.dance} no of ways"
    pass

class Grandson(Son):
    dance = 6
    # basketball = 4
    def isdance(self):
        return f"Jackson yeah!"\
            f"Yes I dance very awesomely  in {self.dance} no of ways"
    pass


darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())#Grandson wala method work karega because usne Son ko inherit kiya h aur isdance method ko overwrite kiya h
print(harry.dance)
"""Quiz"""

print(harry.basketball)# Grandson Son ko inherit kar rha h aur Son Dad ko inherit kar rha h
"""Agar Son mein basketball = 5 hota to ye 5 print karta 
Sabse pehle Grandson apne andar basketball dhundhega nhi mila to Son mein dhundhega 
"""

"""My Class"""

class ElectronicGadget:
    computer = {"RAM":"12GB" , "Processor":"Intel i9"}
    Printer = "Hey! I print all your documents"

class PocketGadget(ElectronicGadget):
    calculator = "Hey! , Give me numbers and I will play with them"


class Mobile(PocketGadget):
    mobile = "Hey I can do anything you say!"


iMac = ElectronicGadget()
calc = PocketGadget()
iPhone = Mobile()

print(iPhone.computer)
print(iMac.Printer)
print(calc.mobile)# = > I will give an error because neither Pocketgadegt nor ElectronicGadget do not have mobile attribute"""
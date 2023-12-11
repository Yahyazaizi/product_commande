
class product:
    productNumber = 0

    def __init__(self,reference,designation,prix_vente,prix_dachat,stock):
             self.__reference = reference
             self.__designation = designation
             self.__prix_vente = prix_vente
             self.__prix_dachat = prix_dachat
             self.__stock = stock
             product.productNumber += 1

    def setreference(self,reference) :
        self.__reference = reference

    @property
    def getreference(self):
             return self.__reference

    def setdesignation(self, designation):
        self.__designation = designation

    @property
    def getdesignation(self):
        return self.__designation

    def setprix_vente(self, sellPrice):
        self.__sellPrice = sellPrice

    @property
    def getprix_vente(self):
        return self.__sellPrice

    def setprix_dachat(self, prix_dachat):
        self.__prix_dachat = prix_dachat

    @property
    def getprix_dachat(self):
        return self.__prix_dachat

    def setStock(self, stock):
        self.__stock = stock

    @property
    def getStock(self):
        return self.__stock

    def returnProductNumber (self):
        return product.productNumber

    def __str__(self):
       return "reference: "+str(self.__reference)+"\ndesignation: "+str(self.__designation)+"\nprix_vente: "+str(self.__prix_vente)+"\nprix_dachat: "+str(self.__prix_dachat)

    def attendues (self):
        return product.productNumber
class commande:
     def __init__(self,date,quantites):
         self.date=date
         self.quantites=quantites

     def __str__(self):
         return "date: " + str(self.date) + "\nquantites: " + str(self.quantites)

playstion=product(1,"gaime","3000dh","4000dh",1000)
print(playstion)
commande1=commande("10/01/2023",2000)
print(commande1)
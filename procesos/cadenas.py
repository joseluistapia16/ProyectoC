class Cadena:

    def getNumber(self,value):
        msg = ""
        for i in range(1,len(value)):
            msg= msg+ value[i]
        return msg
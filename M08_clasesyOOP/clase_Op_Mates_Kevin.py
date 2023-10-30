class Op_Mates:
    def __init__(self, lista,num):
        if not isinstance(lista,list):
            #self.lista=[]
            raise ValueError('Los datos ingresados son inválidos, debe ingresar una lista')
        
        for num  in lista:
            if not isinstance(num,int):
                #self.lista=[]
                raise TypeError('La lista debe contener números enteros')
        
        self.lista = lista

    def hallar_primo(self):
        for i in self.lista:
            if self.__hallar_primo(i):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')
    
    def conv_grados(self, medidai, medidaf):
        for i in self.lista:
            print(i, '°', medidai, 'son', self.__conv_grados(i, medidai, medidaf), '°', medidaf)

    def factorial(self):
        for i in self.lista:
            print('El factorial de', i, 'es', self.__factorial(i))

    def __hallar_primo(self, nro):
        primo=True
        for i in range(2,nro):
            if nro % i == 0:
                primo=False
                break
        return primo
    
    def moda(self):
        frecuencia = {}
        for i in self.lista:
            if i in frecuencia:
                frecuencia[i] += 1
            else:
                frecuencia[i] = 1
            
        mas_repetido = None
        rep = 0

        for i, frecuencia in frecuencia.items():
            if frecuencia > rep:
                mas_repetido = i
                rep = frecuencia
            
        return mas_repetido, rep

    def __conv_grados(self,i, medidai, medidaf):
                
        if (medidai == 'c' or medidai == 'C') and (medidaf == 'f' or medidaf == 'F'):
            GC = (i * 9/5) + 32
        elif (medidai == 'c' or medidai == 'C') and (medidaf == 'k' or medidaf == 'K'):
            GC = i  + 273.15
        elif (medidai == 'f' or medidai == 'F') and (medidaf == 'c' or medidaf == 'C'):
            GC = (i  - 32) * 5/9
        elif (medidai == 'k' or medidai == 'K') and (medidaf == 'c' or medidaf == 'C'):
            GC = i  - 273.15
        return GC

    def __factorial(self, num):
        if type(num) == int:
        
            if (num < 0):
                return 'Inválido!, ingrese solo números positivos'
            if (num <= 1):
                return 1
                    
            fact = num * self.__factorial(num - 1)
            return fact
        else:
            return 'Inválido!, ingrese solo números enteros'
        
        
# Excepcion
if __name__ == "__main__":
    try:
        Mate1 = Op_Mates([1, 2, 3, 4, 5])  # Esto generará un error y mostrará un mensaje de excepción
    except Exception as e:
        print(f"Se produjo un error: {e}")
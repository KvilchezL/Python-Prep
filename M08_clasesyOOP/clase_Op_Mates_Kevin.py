class Op_Mates:
    def __init__(self, lista):
        if not isinstance(lista,list):
            #self.lista=[]
            raise ValueError('Los datos ingresados son inválidos, debe ingresar una lista de numeros enteros')
        
        for num  in lista:
            if not isinstance(num,int):
                #self.lista=[]
                raise TypeError('La lista debe contener números enteros')
        
        self.lista = lista

    def hallar_primo(self):
        resultados = []
        mensajes = []
        for i in self.lista:
            es_primo = self.__hallar_primo(i)
            resultados.append(es_primo)  # Agregar True o False a la lista
            if es_primo:
                mensajes.append(f'El elemento {i} SI es un número primo')
            else:
                mensajes.append(f'El elemento {i} NO es un número primo')
        return resultados, mensajes
    
    def conv_grados(self, medidai, medidaf):
        
        try:
            if not (medidai in ('c', 'C', 'f', 'F', 'k', 'K')) or not (medidaf in ('c', 'C', 'f', 'F', 'k', 'K')):
                raise ValueError("No se puede convertir!, ingrese 'c' o 'C' para celsius, 'f' o 'F' para farenheit y 'k' o 'K' para kelvin.")
                
            grados = []
            mensajes = []
            for i in self.lista:
                grado=self.__conv_grados(i, medidai, medidaf)
                grados.append(grado)
                mensaje = f"{i} ° {medidai} son {grado} ° {medidaf}"
                mensajes.append(mensaje)
                #print(i, '°', medidai, 'son', self.__conv_grados(i, medidai, medidaf), '°', medidaf)
            return grados, mensajes
        except ValueError as e:
            print(e)  # Imprimir solo el mensaje personalizado de la excepción

    def factorial(self):
        factoriales = []
        mensajes = []
        for i in self.lista:
            factorial = self.__factorial(i)
            factoriales.append(factorial)
            mensaje = f'El factorial de {i} es {factorial}'
            mensajes.append(mensaje)
            #print('El factorial de', i, 'es', self.__factorial(i))
        return factoriales, mensajes

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
        
        
# Excepciones

if __name__ == "__main__":
    try:
        Mate1 = Op_Mates([1, 2, 3, 4, 5])  # Esto generará un error y mostrará un mensaje de excepción
        
    except TypeError as e:
        print("Se produjo un error: {e}")


class Controlador():
    def __init__(self):
        self.direccion=''
        self.k=0
        self.coordenadaX=0
        self.coordenadaY=0

    def obtenerDatos(self,direccion):
        self.direccion=direccion
    
    def obtenerK(self,k):
        self.k=k
    
    def limpiarDatos(self):
        self.direccion=''
        self.k=0
        self.coordenadaX=0
        self.coordenadaY=0
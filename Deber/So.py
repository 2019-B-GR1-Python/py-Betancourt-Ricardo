import sys
import csv
import os



class Sistemas_Operativos:    

    Lista_Sistema_Operativo=[]
    Sistema_Operativo={}
    
    SO_TABLE = 'C:/Users/Asus/Documents/GitHub/py-Betancourt-Ricardo/Deber/SO.csv'
    SO_SCHEMA = ['id','Nombre','Version']


    def __init__(self):
        self.Sistema_Operativo = {'id':'','Nombre':'','Version':''}
        self.abrir_archivo()
        
    def abrir_archivo(self):
        del self.Lista_Sistema_Operativo[:]
        with open(self.SO_TABLE, mode='r') as f:
            reader = csv.DictReader(f,fieldnames= self.SO_SCHEMA)

            for row in reader:
                self.Lista_Sistema_Operativo.append(row)
        

    def guardar_SO(self):
        tmp_SO ='{}.tmp'.format(self.SO_TABLE)
        with open(tmp_SO, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames = self.SO_SCHEMA)
            writer.writerows(self.Lista_Sistema_Operativo)

        os.remove(self.SO_TABLE)
        os.rename(tmp_SO,self.SO_TABLE)

    def crear_Sistema_Operativo(self):
        self.abrir_archivo()
        control = input("Ingrese el id del SO: ")
        if control != None:
            self.Sistema_Operativo['id'] = control
        control = input("Ingrese el Nombre del SO: ")
        if control != None:
            self.Sistema_Operativo['Nombre'] = control
        control = input("Ingrese la Version del SO: ")
        if control != None:
            self.Sistema_Operativo['Version'] = control
        
        
        self.Lista_Sistema_Operativo.append(self.Sistema_Operativo)
        self.guardar_SO()
        
    def imprimir_SO(self):
        print(self.Sistema_Operativo)


    def impimir_ListaSO(self):
        print('         Lista SO      ')
        print(' id | Nombre | Version ')
        for SO in self.Lista_Sistema_Operativo:
            print(' {id} | {Nombre} | {Version} '.format(
                id = SO['id'],
                Nombre = SO['Nombre'],
                Version = SO['Version']))


    def buscar_SO(self):
         nombre_SO = input('Ingrese el Nombre del SO : ')
         
         for SO in self.Lista_Sistema_Operativo :
            if SO['Nombre'] != nombre_SO:
                continue

            else:
                print(' id | Nombre | Version ')
                print('{id}|{Nombre}|{Version}'.format(
                id = SO['id'],
                Nombre = SO['Nombre'],
                Version = SO['Version']))

    def buscar_SO_id(self,id):
           
            
            for SO in self.Lista_Sistema_Operativo :
                if SO['id'] != id:
                    continue

                else:
                    
                    return SO
            return None


    def eliminar_SO(self,num_aux=0):
        if num_aux != 0:
            print(num_aux)
            num = num_aux
        else:
            num=input("Ingrese el id del SO a eliminar: ")

        for  idx, SO in enumerate(self.Lista_Sistema_Operativo):
            if SO['id'] == num :
                del self.Lista_Sistema_Operativo[int(idx)] 

        
        self.guardar_SO()


    def actualizar_SO(self):
        num = input("Ingrese el id del SO a Actualizar: ")
        so_Aux = self.buscar_SO_id(num)
        self.eliminar_SO(num)
        if so_Aux != None:
            control = input("Actualizar el id del SO ("+so_Aux['id']+"): ")
            if control != "":
                self.Sistema_Operativo['id'] = control
            else:
                self.Sistema_Operativo['id'] = so_Aux['id']

            control = input("Actualizar el Nombre del SO ("+so_Aux['Nombre']+"): ")
            if control != "":
                self.Sistema_Operativo['Nombre'] = control
            else:
                self.Sistema_Operativo['Nombre'] = so_Aux['Nombre']

            control = input("Actualizar la Version del SO ("+so_Aux['Version']+"): ")
            if control != "":
                self.Sistema_Operativo['Version'] = control
            else:
                self.Sistema_Operativo['Version'] = so_Aux['Version']

            

            self.Lista_Sistema_Operativo.append(self.Sistema_Operativo)
            self.guardar_SO()
        else:
            print('No existe SO')
        
# def print_Menu_App():
    

class app:

    Lista_app=[]
    App = {}
    APP_TABLE = 'C:/Users/Asus/Documents/GitHub/py-Betancourt-Ricardo/Deber/APP.csv'
    APP_SCHEMA = ['idSO','idAPP','Nombre','Version']
    idSO= 0

    def __init__(self,idSO_Aux):
        self.App={'idSO':'','idAPP':'','Nombre':'','Version':''}
        self.idSO=idSO_Aux        
        self.abrir_archivo()

    def abrir_archivo(self):
            del self.Lista_app[:]
            with open(self.APP_TABLE, mode='r') as f:
                reader = csv.DictReader(f,fieldnames= self.APP_SCHEMA)

                for row in reader:
                    self.Lista_app.append(row)
                
                
        

    def guardar_APP(self):
        tmp_APP ='{}.tmp'.format(self.APP_TABLE)
        with open(tmp_APP, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames = self.APP_SCHEMA)
            writer.writerows(self.Lista_app)
            

        os.remove(self.APP_TABLE)
        os.rename(tmp_APP,self.APP_TABLE)
        

    def crear_APP(self):
        self.abrir_archivo()
        control = input("Ingrese el id del APP: ")
        if control != None:
            self.App['idAPP'] = control
        control = input("Ingrese el Nombre del APP: ")
        if control != None:
            self.App['Nombre'] = control
        control = input("Ingrese la Version del APP: ")
        if control != None:
            self.App['Version'] = control
        
        self.App['idSO'] = self.idSO
        self.Lista_app.append(self.App)
        self.guardar_APP()

    def listar_APP(self):
        print('          Lista APP           ')
        print(' idSO | id | Nombre | Version ')
        for app in self.Lista_app :
            if app['idSO'] == self.idSO:
                print(' {idSO} | {idAPP} | {Nombre} | {Version} '.format(
                    idSO = app['idSO'],
                    idAPP = app['idAPP'],
                    Nombre = app['Nombre'],
                    Version = app['Version']))

    def eliminar_APP(self,num_aux=0):
        if num_aux != 0:
            print(num_aux)
            num = num_aux
        else:
            num=input("Ingrese el id del APP a eliminar: ")

        for  idx, APP in enumerate(self.Lista_app):
            if APP['idAPP'] == num   and  APP['idSO'] == self.idSO:
                del self.Lista_app[int(idx)] 

        
        self.guardar_APP()


def print_Menu_App(SO):
    idSO_Aux= input("Ingrese el id del SO para ver sus APPs: ")
    SO_AUX = SO.buscar_SO_id(idSO_Aux)
    if SO_AUX == None:
        print('No existe ese SO')
    else:
        print(f"Aplicaciones del SO: {SO_AUX['Nombre']} {SO_AUX['Version']}")
        APP= app(idSO_Aux)
        print("[L] Listar APP")
        print("[C] Crear APP")
        print("[D] Eliminar APP")
        print("[M] Ver Menu")
        print("[X] Salir")

        while True:
            command = input('APP  >> ¿Escoja una Opción?')
            command = command.upper()

            if command == 'L':
                APP.listar_APP()
            elif command == 'C':
                APP.crear_APP()
            elif command == 'D':
                APP.eliminar_APP()
            elif command == 'X':
                break
            elif  command =='M':
                print(f"Aplicaciones del SO: {SO_AUX['Nombre']} {SO_AUX['Version']}")
                print("[L] Listar APP")
                print("[C] Crear APP")
                print("[D] Eliminar APP")
                print("[M] Ver Menu")
                print("[X] Salir")




def print_Menu():
    SO = Sistemas_Operativos()
    print("CRUD SO Y APLICACIONES")
    print('*'*50)
    print("[L] Listar SO")
    print("[C] Crear SO")
    print("[S] Buscar SO")
    print("[D] Eliminar SO")
    print("[U] Actualizar SO")
    print("[A] Aplicaciones")
    print("[M] Ver Menu")
    print("[X] Salir")

    while True:      

        command = input('SO >> ¿Escoja una Opción?')
        command = command.upper()

        if command == 'C':
            SO.crear_Sistema_Operativo()
        elif command == 'L':
            SO.impimir_ListaSO()
        elif command == 'X':
            break
        elif command == 'S':
            SO.buscar_SO()
        elif command == 'D':
            SO.eliminar_SO()
        elif command == 'U':
            SO.actualizar_SO()
        elif command == 'A':
            print_Menu_App(SO)
        elif command == 'M':
            print("CRUD SO Y APLICACIONES")
            print('*'*50)
            print("[L] Listar SO")
            print("[C] Crear SO")
            print("[S] Buscar SO")
            print("[D] Eliminar SO")
            print("[U] Actualizar SO")
            print("[A] Aplicaciones")
            print("[M] Ver Menu")
            print("[X] Salir")
            


    
if __name__ == "__main__":
    print_Menu()
    
    
        

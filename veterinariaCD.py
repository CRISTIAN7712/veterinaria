

class Cliente: 
    def _init_(self,nomCliente,telefono,direccion,ticket,mascota):
        self.nombre = nomCliente
        self.tel = telefono
        self.direccion = direccion
        self.ticket = ticket
        self.nomMascota=mascota


    def CrearCliente():
        return "Cliente Creado"


    def buscarCliente (pNombre):
        return "Cliente Creado" +pNombre

    def ticketCliente(pNombre):
        return "Facturacion a nombre de: " +pNombre+"$256556"
    
    
class Mascota (Cliente):
    def _init_(self,nomCliente,telefono,direccion,ticket,mascota,nomMascota,sintomas,comida,medicamentos,veterenario):
        super().__init__(nomCliente,telefono,direccion,ticket,mascota)
        self.nombreMasc=nomMascota
        self.sintomas=sintomas
        self.comida=comida
        self.medicamentos=medicamentos
        self.veterenario=veterenario
        
    def crearMascota():
        return "Mascota creada"


    def buscarMascota (pNombreMasc):
        return "Mascota encontrada" +pNombreMasc

    def alimentoMasctoa(pNombreMasc,pComida,pNumero):
        return "Useted ha ingresado" + pNombreMasc + "Comida:" + pComida + " a la mascota"  + pNumero  
    
class Medicamentos(Mascota):
    def _init_(self,nomMascota,sintomas,comida,medicamentos,veterenario,nomMedicamento,marcaMedicamento,puntajeMedicament,descripcion,valorMedicamento):
        super().__init__(nomMascota,sintomas,comida,medicamentos,veterenario)
        self.nombreMedicamento=nomMedicamento
        self.marcaMedicamento=marcaMedicamento
        self.puntaje=puntajeMedicament
        self.descripcion=descripcion
        self.valor= valorMedicamento
        
    def tenerMedicamento():
    insert = int(input("Inserte el valor del medicamento: ").strip())


    medicamento = 50
    total = medicamento- insert

    while insert < medicamento:
        print("La deuda es de: ", total)
        return
    if insert == medicamento:
        print("El sobrante de dinero es: ", total)
        return
    else:
        print("Inserte el descuento: ", medicamento)   
        
    
    def crearMedicamento():
        return "Medicamento creado"


    def buscarMedicamento (pNomMedicamento):
        return "Antribitic:" +pNomMedicamento

class Veterinaria(Mascota):
    def _init_(self,nomMascota,sintomas,comida,medicamento,veterenario,nomVeterinario,consultorioVeterinario,espVeterinario,telVeterinario,idVeterinario):    
     super().__init__(nomMascota,sintomas,comida,medicamento,veterenario)
     self.veterenaryName = nomVeterinario
     self.veterenaryRoom = consultorioVeterinario
     self.veterenaryEspeciality = espVeterinario
     self.veterenaryCellphone = telVeterinario
     self.veterenarySchedule = idVeterinario
       
    def crearVeterinario():
        return "Veterenario creado"


    def buscarVeterinario (pNomVeterinario):
        return "Veterenario:" + pNomVeterinario
    
    def llamarVeterinario(pNomVeterinario,pConsultorio)
        return "Urgencia en: " + pConsultorio+ "DR" +pNomVeterinario
            
            
      

class Comida(Mascota):
    def _init_(self,nomMascota,sintomas,comida,medicamento,veterenario,nomComida,marcaComida,datoNutricional,valorAlimento,tipoAlimento):
     super().__init__(nomMascota,sintomas,comida,medicamento,veterenario)  
     self.foodName = nomComida
     self.foodBrand = marcaComida
     self.foodConsume = datoNutricional 
     self.foodAvailable = valorAlimento
     self.foodPetType = tipoAlimento 
    
    def crearComida():
        return "Comida creada"


    def buscarComida (pNomComida):
        return "La comida es:" + pNomComida
            
    def giveFood():
    insert = int(input("Inserte dinero para el alimento: ").strip())


    comidaPerro = 50
    total = comidaPerro- insert

    while insert < comidaPerro:
        print("Valor adeudado: ", total)
        return
    if insert == comidaPerro:
        print("El cambio es de: ", total)
        return
    else:
        print("Inserte un valor para el alimento: ", comidaPerro)   
        
from paciente import Paciente
from medico import Medico

class Cita:
    def __init__(self, codigo, paciente, medico, fecha):
        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha

    #Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico

    @property
    def fecha(self):
        return self._fecha

    #Setters
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @paciente.setter
    def paciente(self, valor):
        self._paciente = valor

    @medico.setter
    def medico(self, valor):
        self._medico = valor

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    def resumen(self):
        return (
            f"Cita: C-{self._codigo}\n"
            "--------------------\n"
            f"Paciente: {self._paciente.nombre} (P-{self._paciente.codigo})\n"
            f"Edad: {self._paciente.edad}\n"
            "--------------------\n"
            f"Medico: Dr. {self._medico.nombre} (M-{self._medico.codigo})\n"
            f"Especialidad: {self._medico.especialidad}\n"
            f"Fecha de la cita: {self._fecha}\n"

        )

pacientes = []
citas = []

medicos = [
    Medico("001", "Manuel Torres", "Dermatologia"),
    Medico("002", "Jose Ugarte", "Cardiologia"),
    Medico("003", "Franchesco Ayala", "Ginecologia"),
    Medico("004", "Fabiana Bellavista", "Ginecologia"),
    Medico("005", "Felipe Huaman", "Neurologia"),
    Medico("006", "Michael Tacslluisa", "Neurologia"),
    Medico("007", "Fernando Gonzales", "Traumatologia"),
    Medico("008", "Claudia Montenegro", "Psiquiatria"),
    Medico("009", "Jason Brody", "Cirugia General"),
    Medico("010", "Jhon Price", "Medicina Interna"),
    Medico("011", "Eduardo Flores", "Pediatria"),
    
]

def registrar_medico():
    print("--- REGISTRAR NUEVO MÉDICO ---")
    nombre_m = input("Ingrese nombre del médico: ")
    especialidad_m = input("Ingrese especialidad médica (ej. Cardiologia, Pediatria): ")

    num_m = len(medicos) + 1
    codigo_m = f"{num_m:03d}"

    nuevo_medico = Medico(codigo_m, nombre_m, especialidad_m)
    medicos.append(nuevo_medico)
    print(f"-> Médico registrado con éxito con código: M-{codigo_m}")


def buscar_especialidad(especialidad_buscada):
    return list(filter(lambda medico: medico.especialidad.lower() == especialidad_buscada.lower(), medicos))

def registrar_cita():
    if not medicos:
        print("No hay médicos registrados en el sistema. Registre uno primero.")
        return

    print("--- REGISTRAR CITA ---")
    nombre_p = input("Ingrese nombre del paciente:")

    try:
        edad_p = int(input("Ingrese edad del paciente: "))
        if edad_p < 0 or edad_p > 120:
            print("Error: La edad debe estar en un rango de 0 a 120 años.")
            return
    except ValueError:
        print("La edad debe ser un valor numerico")
        return

    num_p = len(pacientes) + 1
    codigo_p = f"{num_p:03d}"

    paciente = Paciente(codigo_p, nombre_p, edad_p)
    pacientes.append(paciente)
    print(f"-> Paciente asignado con código: P-{codigo_p}")

    especialidades_disponibles = sorted(list(set(medico.especialidad for medico in medicos)))
    print("\n=== SELECCIONE EL ÁREA O ESPECIALIDAD ===")
    for i, especialidad in enumerate(especialidades_disponibles, start=1):
        print(f"{i}._ {especialidad}")
    try:
        opcion_especialidad = int(input("Elija una opción de especialidad: "))
        if opcion_especialidad < 1 or opcion_especialidad > len(especialidades_disponibles):
            print("Opción de especialidad no válida.")
            return
        especialidad_seleccionada = especialidades_disponibles[opcion_especialidad - 1]
    except ValueError:
        print("Error: Ingrese un número válido.")
        return
    
    medicos_filtrados = buscar_especialidad(especialidad_seleccionada)

    if not medicos_filtrados:
        print(f"No hay médicos disponibles para la especialidad '{especialidad_seleccionada}'.")
        return
    
    print(f"\n=== MÉDICOS DISPONIBLES EN {especialidad_seleccionada.upper()} ===")
    for i, medico in enumerate(medicos_filtrados, start=1):
        print(f"{i}._ Dr. {medico.nombre} (Código: M-{medico.codigo})")
    
    try:
        opcion_medico = int(input("Elija una opción de médico: "))
        if opcion_medico < 1 or opcion_medico > len(medicos_filtrados):
            print("Opción de médico no válida.")
            return
        medico = medicos_filtrados[opcion_medico - 1]
    except ValueError:
        print("Error: Ingrese un número válido.")
        return
    
    fecha = input("Ingrese fecha de la cita (DD/MM/AAAA): ")

    num_c = len(citas) + 1
    codigo_c = f"{num_c:03d}"

    cita = Cita(codigo_c, paciente, medico, fecha)
    citas.append(cita)

    print("\nCita registrada con éxito")

def mostrar_citas():
    print("\n--- DATOS DE CITAS REGISTRADAS ---")
    if len(citas) == 0:
        print("No hay citas registradas aún.")
    else:
        for c in citas:
            print(c.resumen())
            print("-" * 35)

def buscar_codigo_cita(codigo_buscado):
    resultado = list(filter(lambda c: c.codigo == codigo_buscado, citas))
    if resultado:
        return resultado[0].resumen()
    return "Cita no encontrada."
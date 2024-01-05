class Persona:
    def __init__(self, nombre, apellido, telefono, correo, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento

    def formato_doc(self):
        return{
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'correo': self.correo,
            'fecha_nacimiento': self.fecha_nacimiento
        }
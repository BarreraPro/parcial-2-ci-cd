class Vaso:
    def __init__(self, cantidad_vasos, contenido):
        self.cantidad_vasos = cantidad_vasos
        self.contenido = contenido  # oz de café

    def hay_vasos(self, cantidad):
        return self.cantidad_vasos >= cantidad

    def dar_vasos(self, cantidad):
        if self.hay_vasos(cantidad):
            self.cantidad_vasos -= cantidad

    def get_contenido(self):
        return self.contenido


class Cafetera:
    def __init__(self, cantidad_cafe):
        self.cantidad_cafe = cantidad_cafe

    def hay_cafe(self, cantidad):
        return self.cantidad_cafe >= cantidad

    def dar_cafe(self, cantidad):
        if self.hay_cafe(cantidad):
            self.cantidad_cafe -= cantidad


class Azucarero:
    def __init__(self, cantidad_azucar):
        self.cantidad_azucar = cantidad_azucar

    def hay_azucar(self, cantidad):
        return self.cantidad_azucar >= cantidad

    def dar_azucar(self, cantidad):
        if self.hay_azucar(cantidad):
            self.cantidad_azucar -= cantidad


class MaquinaCafe:
    def __init__(self, vaso_pequeno, vaso_mediano, vaso_grande, cafetera, azucarero):
        self.vaso_pequeno = vaso_pequeno
        self.vaso_mediano = vaso_mediano
        self.vaso_grande = vaso_grande
        self.cafetera = cafetera
        self.azucarero = azucarero

    def get_tipo_vaso(self, tipo):
        if tipo == "pequeno":
            return self.vaso_pequeno
        elif tipo == "mediano":
            return self.vaso_mediano
        elif tipo == "grande":
            return self.vaso_grande
        return None

    def servir_cafe(self, tipo_vaso, azucar):
        vaso = self.get_tipo_vaso(tipo_vaso)

        if vaso is None:
            return "Tipo de vaso invalido"

        if not vaso.hay_vasos(1):
            return "No hay vasos"

        cantidad_cafe = vaso.get_contenido()

        if not self.cafetera.hay_cafe(cantidad_cafe):
            return "No hay cafe"

        if not self.azucarero.hay_azucar(azucar):
            return "No hay azucar"

        vaso.dar_vasos(1)
        self.cafetera.dar_cafe(cantidad_cafe)
        self.azucarero.dar_azucar(azucar)

        return "Cafe servido"
from maquina_cafe import Vaso, Cafetera, Azucarero, MaquinaCafe


def crear_maquina():
    vaso_pequeno = Vaso(5, 3)   # 3 oz
    vaso_mediano = Vaso(5, 5)   # 5 oz
    vaso_grande = Vaso(5, 7)    # 7 oz

    cafetera = Cafetera(50)
    azucarero = Azucarero(20)

    return MaquinaCafe(vaso_pequeno, vaso_mediano, vaso_grande, cafetera, azucarero)


def test_servir_cafe_pequeno():
    maquina = crear_maquina()
    resultado = maquina.servir_cafe("pequeno", 2)

    assert resultado == "Cafe servido"


def test_sin_vasos():
    vaso_pequeno = Vaso(0, 3)
    vaso_mediano = Vaso(5, 5)
    vaso_grande = Vaso(5, 7)

    cafetera = Cafetera(50)
    azucarero = Azucarero(20)

    maquina = MaquinaCafe(vaso_pequeno, vaso_mediano, vaso_grande, cafetera, azucarero)

    resultado = maquina.servir_cafe("pequeno", 2)

    assert resultado == "No hay vasos"


def test_sin_cafe():
    maquina = crear_maquina()
    maquina.cafetera = Cafetera(0)

    resultado = maquina.servir_cafe("mediano", 2)

    assert resultado == "No hay cafe"


def test_sin_azucar():
    maquina = crear_maquina()
    maquina.azucarero = Azucarero(0)

    resultado = maquina.servir_cafe("grande", 2)

    assert resultado == "No hay azucar"
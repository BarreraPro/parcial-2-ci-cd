# Parcial 2 - CI/CD con GitHub Actions

##  Descripción
Este proyecto consiste en la implementación de una máquina de café en Python utilizando la metodología TDD (Test Driven Development).

Se desarrolló primero un conjunto de pruebas automatizadas y luego se implementó la lógica necesaria para que dichas pruebas pasaran correctamente.

Además, se configuró un flujo de integración continua (CI/CD) utilizando GitHub Actions para ejecutar automáticamente las pruebas en cada actualización del código.

---

##  Funcionalidades
La máquina de café permite:

- Seleccionar el tamaño del vaso (pequeño, mediano, grande)
- Verificar disponibilidad de vasos
- Verificar disponibilidad de café
- Verificar disponibilidad de azúcar
- Mostrar mensajes cuando no hay recursos disponibles

---

##  Pruebas (TDD)
Se implementaron pruebas automatizadas con `pytest` para validar el comportamiento del sistema.

Ejemplos de pruebas:
- Sin vasos → "No hay vasos"
- Sin café → "No hay café"
- Sin azúcar → "No hay azúcar"

Las pruebas se ejecutan con:

```bash
python -m pytest
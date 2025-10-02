# 🧩 Mejoras implementadas

## 📄 1. Creación del archivo `report.md`
Se ha añadido un nuevo archivo llamado **`report.md`**, destinado exclusivamente a registrar los **tests realizados**.  
Este archivo contendrá únicamente la información de las pruebas ejecutadas, manteniendo un registro separado y limpio.

---

## 🔁 2. Cambio en el método de escritura
El comportamiento original sobrescribía el contenido del archivo en cada ejecución.  
Ahora, el sistema ha sido modificado para que los **nuevos tests se añadan al principio del archivo**, mientras que los **más antiguos permanezcan al final**.  
De esta forma, siempre se muestran primero las pruebas más recientes.

---

## 🕒 3. Inclusión de la fecha en las pruebas
En ambos archivos, **`README.md`** y **`report.md`**, se ha añadido la **fecha y hora de cada ejecución de prueba**.  
Esto permite llevar un control cronológico y una trazabilidad más precisa de los resultados.
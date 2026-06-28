# Gestión de Restaurante con POO — Semana 5

**Estudiante:** Cristian Omar Garcia Aguilar  
**Materia:** Programación Orientada a Objetos  
**Entrega:** Semana 5 — Identificadores, tipos de datos y proyecto Python modular

---

## ¿Qué hace este sistema?

El proyecto implementa un **sistema de gestión para un restaurante** aplicando los principios de Programación Orientada a Objetos en Python. Se modelan tres entidades clave —`Producto`, `Cliente` y `Restaurante`— organizadas en módulos independientes según su responsabilidad.

El restaurante de referencia es **"Sabores del Pacífico"**, ubicado en Esmeraldas. El sistema permite registrar los ítems del menú, dar de alta clientes y consultar el estado general del local desde un único punto de arranque.

---

## Organización del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py        → registra las clases exportadas del paquete
│   ├── producto.py        → clase Producto (ítem del menú)
│   └── cliente.py         → clase Cliente (persona registrada)
├── servicios/
│   ├── __init__.py        → registra las clases exportadas del paquete
│   └── restaurante.py     → clase Restaurante (servicio central)
└── main.py                → punto de arranque del programa
```

---

## Rol de cada módulo

**`modelos/producto.py`**  
Contiene la clase `Producto`. Define los atributos que describen un ítem del menú —nombre, detalle, precio, tipo de plato, stock y disponibilidad— junto con métodos para descontar stock, reponer inventario y retirarlo de la carta.

**`modelos/cliente.py`**  
Contiene la clase `Cliente`. Almacena los datos de cada persona registrada y expone métodos para sumar visitas, acumular consumo y determinar el nivel de fidelidad del cliente.

**`servicios/restaurante.py`**  
Contiene la clase `Restaurante`. Actúa como servicio central: administra las listas `productos_en_menu` y `clientes_activos`, y ofrece métodos para incorporar, listar y buscar objetos.

**`main.py`**  
Punto de entrada del programa. Crea los objetos de cada modelo, los registra en el servicio central y demuestra el funcionamiento de los métodos con salida organizada en consola.

---

## Tipos de datos aplicados

| Tipo | Atributos donde se usa |
|---|---|
| `str` | `nombre_producto`, `detalle`, `tipo_plato`, `nombre_cliente`, `numero_contacto`, `email`, `nombre_local`, `ciudad` |
| `int` | `stock`, `total_visitas`, `aforo` |
| `float` | `precio_unitario`, `consumo_acumulado` |
| `bool` | `en_carta`, `es_preferencial`, `operativo` |
| `list` | `productos_en_menu`, `clientes_activos` |

---

## Convenciones seguidas

- Nombres de clases en **PascalCase**: `Producto`, `Cliente`, `Restaurante`
- Nombres de atributos, métodos, variables y archivos en **snake_case**: `precio_unitario`, `sumar_visita`, `listar_menu`, `producto.py`
- Anotaciones de tipo en todos los parámetros y atributos
- Identificadores que describen el dato sin ambigüedad; ningún nombre genérico como `x`, `val` o `obj`

---

## Cómo ejecutar

Requiere Python 3.10 o superior. Desde la raíz del repositorio:

```bash
python restaurante_app/main.py
```

---

## Reflexión personal

Trabajar con **identificadores descriptivos** cambia la forma de leer el código: al ver `consumo_acumulado` o `es_preferencial` queda inmediatamente claro qué se guarda ahí, sin necesidad de buscar dónde se definió la variable. Eso reduce errores y acelera cualquier corrección futura.

Elegir el **tipo de dato correcto** también tiene un efecto práctico: si `stock` fuera `float`, operaciones como comparar unidades disponibles devolverían resultados inesperados. Asignar `int` o `bool` donde corresponde hace que el programa se comporte de forma predecible.

Finalmente, la **estructura modular** permite que cada archivo tenga una sola razón para cambiar. Si el modelo de cliente evoluciona, solo se modifica `cliente.py`; si la lógica de negocio cambia, se ajusta `restaurante.py`. Ese aislamiento es la base de cualquier sistema mantenible a mediano plazo.

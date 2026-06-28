# servicios/restaurante.py
# Clase de servicio central del sistema.
# Gestiona el registro y consulta de productos y clientes mediante listas.

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Núcleo del sistema de gestión del restaurante.
    Coordina las listas de productos en carta y clientes activos.

    nombre_local       str   -- nombre comercial del restaurante
    ciudad             str   -- ciudad donde opera el local
    aforo              int   -- capacidad máxima de personas simultáneas
    operativo          bool  -- True si el local está abierto al público
    productos_en_menu  list  -- colección de objetos Producto registrados
    clientes_activos   list  -- colección de objetos Cliente registrados
    """

    def __init__(
        self,
        nombre_local: str,
        ciudad: str,
        aforo: int,
        operativo: bool,
    ) -> None:
        self.nombre_local: str = nombre_local
        self.ciudad: str = ciudad
        self.aforo: int = aforo
        self.operativo: bool = operativo
        # Listas como tipo compuesto para administrar múltiples objetos
        self.productos_en_menu: list = []
        self.clientes_activos: list = []

    # ── Gestión de productos ──────────────────────────────

    def incluir_producto(self, producto: Producto) -> None:
        """Incorpora un producto a la lista del menú."""
        self.productos_en_menu.append(producto)
        print(f"  + '{producto.nombre_producto}' incorporado al menú.")

    def listar_menu(self) -> None:
        """Imprime en consola todos los productos del menú."""
        linea: str = "─" * 58
        print(f"\n{linea}")
        print(f"  MENÚ  ·  {self.nombre_local}  ·  {self.ciudad}")
        print(linea)
        if not self.productos_en_menu:
            print("  Sin productos registrados.")
        else:
            for pos, item in enumerate(self.productos_en_menu, start=1):
                print(f"\n  {pos}. {item}")
        print(linea)

    def encontrar_producto(self, nombre_producto: str) -> Producto | None:
        """Retorna el objeto Producto cuyo nombre coincida; None si no existe."""
        for item in self.productos_en_menu:
            if item.nombre_producto.lower() == nombre_producto.lower():
                return item
        return None

    # ── Gestión de clientes ───────────────────────────────

    def dar_alta_cliente(self, cliente: Cliente) -> None:
        """Da de alta a un cliente en el sistema del restaurante."""
        self.clientes_activos.append(cliente)
        print(f"  + Cliente '{cliente.nombre_cliente}' dado de alta.")

    def listar_clientes(self) -> None:
        """Imprime en consola todos los clientes registrados."""
        linea: str = "─" * 58
        print(f"\n{linea}")
        print(f"  CLIENTES  ·  {self.nombre_local}")
        print(linea)
        if not self.clientes_activos:
            print("  Sin clientes registrados.")
        else:
            for pos, cliente in enumerate(self.clientes_activos, start=1):
                print(f"\n  {pos}. {cliente}")
        print(linea)

    def encontrar_cliente(self, nombre_cliente: str) -> Cliente | None:
        """Retorna el objeto Cliente cuyo nombre coincida; None si no existe."""
        for cliente in self.clientes_activos:
            if cliente.nombre_cliente.lower() == nombre_cliente.lower():
                return cliente
        return None

    # ── Resumen general ───────────────────────────────────

    def estado_general(self) -> None:
        """Muestra un panel con los datos generales del restaurante."""
        estado: str = "Operativo" if self.operativo else "Cerrado"
        linea: str = "═" * 58
        print(f"\n{linea}")
        print(f"  PANEL DE CONTROL — {self.nombre_local}")
        print(linea)
        print(f"  Ciudad       : {self.ciudad}")
        print(f"  Aforo        : {self.aforo} personas")
        print(f"  Estado       : {estado}")
        print(f"  Productos    : {len(self.productos_en_menu)}")
        print(f"  Clientes     : {len(self.clientes_activos)}")
        print(linea)

    def __str__(self) -> str:
        estado: str = "Operativo" if self.operativo else "Cerrado"
        return (
            f"{self.nombre_local} | {self.ciudad} | "
            f"Aforo: {self.aforo} | {estado}"
        )

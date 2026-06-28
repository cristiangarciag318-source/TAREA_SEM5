# modelos/producto.py
# Define la clase Producto para el sistema del restaurante.
# Cada instancia representa un ítem del menú: entrada, plato fuerte o bebida.


class Producto:
    """
    Modela un ítem ofrecido dentro del menú del restaurante.

    nombre_producto   str   -- denominación del ítem en el menú
    detalle           str   -- descripción corta del ítem
    precio_unitario   float -- valor en dólares por unidad
    tipo_plato        str   -- clasificación: 'entrada', 'fuerte', 'postre', 'bebida'
    stock             int   -- unidades en bodega disponibles para servir
    en_carta          bool  -- True si el ítem aparece actualmente en el menú
    """

    def __init__(
        self,
        nombre_producto: str,
        detalle: str,
        precio_unitario: float,
        tipo_plato: str,
        stock: int,
        en_carta: bool,
    ) -> None:
        self.nombre_producto: str = nombre_producto
        self.detalle: str = detalle
        self.precio_unitario: float = precio_unitario
        self.tipo_plato: str = tipo_plato
        self.stock: int = stock
        self.en_carta: bool = en_carta

    def retirar_de_carta(self) -> None:
        """Marca el producto como no disponible en el menú activo."""
        self.en_carta = False

    def reponer_stock(self, unidades: int) -> None:
        """Suma unidades al stock del producto cuando llega nuevo inventario."""
        self.stock += unidades

    def descontar_stock(self, unidades: int) -> bool:
        """
        Descuenta unidades del stock al registrar un pedido.
        Retorna True si la operación fue exitosa, False si no hay suficiente stock.
        """
        if unidades <= self.stock:
            self.stock -= unidades
            return True
        return False

    def __str__(self) -> str:
        carta: str = "En carta" if self.en_carta else "Fuera de carta"
        return (
            f"{self.nombre_producto}  [{self.tipo_plato}]  "
            f"${self.precio_unitario:.2f}  |  Stock: {self.stock}  |  {carta}\n"
            f"    {self.detalle}"
        )

# modelos/cliente.py
# Define la clase Cliente para el sistema del restaurante.
# Almacena los datos de cada persona registrada y su historial de consumo.


class Cliente:
    """
    Representa a una persona registrada como cliente del restaurante.

    nombre_cliente     str   -- nombre y apellido del cliente
    numero_contacto    str   -- teléfono celular de contacto
    email              str   -- dirección de correo electrónico
    total_visitas      int   -- número de veces que ha asistido al local
    consumo_acumulado  float -- suma total en dólares de todos sus pedidos
    es_preferencial    bool  -- True cuando el cliente tiene trato preferencial
    """

    def __init__(
        self,
        nombre_cliente: str,
        numero_contacto: str,
        email: str,
        total_visitas: int,
        consumo_acumulado: float,
        es_preferencial: bool,
    ) -> None:
        self.nombre_cliente: str = nombre_cliente
        self.numero_contacto: str = numero_contacto
        self.email: str = email
        self.total_visitas: int = total_visitas
        self.consumo_acumulado: float = consumo_acumulado
        self.es_preferencial: bool = es_preferencial

    def sumar_visita(self, valor_pedido: float) -> None:
        """Registra una nueva visita y acumula el valor del pedido realizado."""
        self.total_visitas += 1
        self.consumo_acumulado += valor_pedido
        # Ascender a preferencial a partir de la quinta visita
        if self.total_visitas >= 5 and not self.es_preferencial:
            self.es_preferencial = True
            print(f"    ★ {self.nombre_cliente} ahora es cliente preferencial.")

    def nivel_fidelidad(self) -> str:
        """Clasifica al cliente según su historial de visitas."""
        if self.total_visitas >= 10:
            return "Oro"
        elif self.total_visitas >= 5:
            return "Plata"
        else:
            return "Bronce"

    def __str__(self) -> str:
        tipo: str = "Preferencial" if self.es_preferencial else "Regular"
        return (
            f"{self.nombre_cliente}  ({tipo})  |  "
            f"Tel: {self.numero_contacto}  |  "
            f"Email: {self.email}\n"
            f"    Visitas: {self.total_visitas}  |  "
            f"Consumo acumulado: ${self.consumo_acumulado:.2f}  |  "
            f"Nivel: {self.nivel_fidelidad()}"
        )

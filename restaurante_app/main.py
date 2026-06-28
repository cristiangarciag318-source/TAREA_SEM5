# main.py
# Archivo de arranque del sistema de gestión para el restaurante.
# Instancia los modelos, los registra en el servicio central
# y presenta la información resultante en consola.

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main() -> None:
    """Ejecuta la demostración completa del sistema de gestión de restaurante."""

    separador: str = "═" * 58
    print(f"\n{separador}")
    print("  GESTIÓN DE RESTAURANTE — POO  |  Semana 5")
    print(separador)

    # ── 1. Crear el servicio central ─────────────────────
    local = Restaurante(
        nombre_local="Sabores del Pacífico",
        ciudad="Esmeraldas",
        aforo=45,
        operativo=True,
    )

    # ── 2. Crear productos del menú ───────────────────────
    ceviche_mixto = Producto(
        nombre_producto="Ceviche Mixto",
        detalle="Combinación de camarón, concha y pescado en marinada de limón con cebolla y cilantro.",
        precio_unitario=9.00,
        tipo_plato="entrada",
        stock=18,
        en_carta=True,
    )

    encocado_camaron = Producto(
        nombre_producto="Encocado de Camarón",
        detalle="Camarones frescos cocinados en salsa de coco con especias del Pacífico, acompañado de arroz.",
        precio_unitario=11.50,
        tipo_plato="fuerte",
        stock=12,
        en_carta=True,
    )

    arroz_concha = Producto(
        nombre_producto="Arroz con Concha",
        detalle="Arroz negro con conchas al ajillo, pimiento y culantro, estilo esmeraldeño.",
        precio_unitario=10.00,
        tipo_plato="fuerte",
        stock=10,
        en_carta=True,
    )

    jugo_coco = Producto(
        nombre_producto="Agua de Coco Natural",
        detalle="Coco fresco partido al momento, servido con sorbete.",
        precio_unitario=2.50,
        tipo_plato="bebida",
        stock=0,
        en_carta=False,
    )

    # ── 3. Registrar productos en el servicio central ─────
    print("\n  >> Incorporando productos al menú...")
    local.incluir_producto(ceviche_mixto)
    local.incluir_producto(encocado_camaron)
    local.incluir_producto(arroz_concha)
    local.incluir_producto(jugo_coco)

    # ── 4. Crear clientes ─────────────────────────────────
    cliente_ana = Cliente(
        nombre_cliente="Ana Beatriz Quiñónez Palma",
        numero_contacto="0981112233",
        email="ana.quinonez@correo.com",
        total_visitas=11,
        consumo_acumulado=198.75,
        es_preferencial=True,
    )

    cliente_julio = Cliente(
        nombre_cliente="Julio Marcelo Bone Caicedo",
        numero_contacto="0964445566",
        email="jbone@correo.com",
        total_visitas=3,
        consumo_acumulado=35.50,
        es_preferencial=False,
    )

    cliente_rosa = Cliente(
        nombre_cliente="Rosa Elena Mina Cortez",
        numero_contacto="0997778899",
        email="rmina@correo.com",
        total_visitas=6,
        consumo_acumulado=91.00,
        es_preferencial=True,
    )

    # ── 5. Dar de alta a los clientes ─────────────────────
    print("\n  >> Registrando clientes en el sistema...")
    local.dar_alta_cliente(cliente_ana)
    local.dar_alta_cliente(cliente_julio)
    local.dar_alta_cliente(cliente_rosa)

    # ── 6. Panel de control general ───────────────────────
    local.estado_general()

    # ── 7. Mostrar menú completo ──────────────────────────
    local.listar_menu()

    # ── 8. Mostrar clientes registrados ──────────────────
    local.listar_clientes()

    # ── 9. Operaciones adicionales sobre los objetos ──────
    print("\n  >> Operaciones adicionales...")

    # Registrar una nueva visita para cliente_julio
    cliente_julio.sumar_visita(valor_pedido=28.00)
    print(f"\n  Visita registrada — {cliente_julio.nombre_cliente}:")
    print(f"  {cliente_julio}")

    # Descontar stock del encocado de camarón
    exito: bool = encocado_camaron.descontar_stock(4)
    if exito:
        print(f"\n  Stock actualizado — {encocado_camaron.nombre_producto}: {encocado_camaron.stock} unidades restantes.")

    # Reponer agua de coco y reactivar en carta
    jugo_coco.reponer_stock(20)
    jugo_coco.en_carta = True
    print(f"\n  '{jugo_coco.nombre_producto}' reabastecido — Stock: {jugo_coco.stock}  |  En carta: {jugo_coco.en_carta}")

    # Buscar cliente por nombre
    encontrado = local.encontrar_cliente("Ana Beatriz Quiñónez Palma")
    if encontrado:
        print(f"\n  Búsqueda exitosa → Nivel de fidelidad: {encontrado.nivel_fidelidad()}")

    print(f"\n{separador}")
    print("  Ejecución finalizada sin errores.")
    print(f"{separador}\n")


if __name__ == "__main__":
    main()

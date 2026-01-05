import streamlit as st

# ---------------------------
# Configuración de la página
# ---------------------------
st.set_page_config(
    page_title="Recomendador de Perfumes",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Inicialización de estado
# ---------------------------
if "historial_ph" not in st.session_state:
    st.session_state.historial_ph = []

if "perfumes_favoritos" not in st.session_state:
    st.session_state.perfumes_favoritos = []

# ---------------------------
# Función para aplicar color de fondo
# ---------------------------
def set_background(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
            transition: background-color 0.5s;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------------------------
# Encabezado principal
# ---------------------------
st.markdown(
    "<h1 style='text-align:center; color:#4B0082;'>Recomendador de Perfumes</h1>",
    unsafe_allow_html=True
)
st.write(
    "Descubre la fragancia ideal según el pH de tu piel, la ocasión de uso y el lugar de aplicación recomendado."
)

# ---------------------------
# Barra lateral
# ---------------------------
with st.sidebar:
    st.markdown("### Preferencias Guardadas")

    if st.session_state.historial_ph:
        st.markdown("**Últimos valores de pH consultados:**")
        for ph_hist in st.session_state.historial_ph[-5:]:
            st.text(f"pH {ph_hist}")

    if st.session_state.perfumes_favoritos:
        st.markdown("**Perfumes Favoritos:**")
        for fav in st.session_state.perfumes_favoritos:
            st.text(f"- {fav}")

        if st.button("Eliminar favoritos"):
            st.session_state.perfumes_favoritos.clear()
            st.experimental_rerun()

# ---------------------------
# Selector de pH
# ---------------------------
ph = st.slider("Selecciona el pH de tu piel", 0.0, 14.0, 5.5, 0.1)

if ph not in st.session_state.historial_ph:
    st.session_state.historial_ph.append(ph)

# ---------------------------
# Clasificación y recomendaciones
# ---------------------------
if ph <= 3.0:
    color = "#87CEEB"
    tipo = "Fragancias frescas y acuáticas"
    descripcion = "La piel muy ácida favorece aromas frescos y ligeros, con buena duración."
    estacion = "Primavera / Verano"
    perfumes = [
        {
            "nombre": "Acqua di Gio - Giorgio Armani",
            "ocasión": "Uso diario",
            "lugar": "Muñecas y cuello",
            "notas_top": "Bergamota, neroli, mandarina",
            "notas_corazon": "Jazmín, calone, romero",
            "notas_base": "Ámbar, cedro, almizcle",
            "precio": "$95 USD"
        },
        {
            "nombre": "Nautica Voyage",
            "ocasión": "Climas cálidos",
            "lugar": "Cuello y pecho",
            "notas_top": "Manzana verde, hoja de loto",
            "notas_corazon": "Mimosa, menta acuática",
            "notas_base": "Cedro, almizcle, ámbar",
            "precio": "$25 USD"
        },
        {
            "nombre": "Issey Miyake L'Eau d'Issey",
            "ocasión": "Oficina o citas",
            "lugar": "Muñecas y cuello",
            "notas_top": "Limón, bergamota, yuzu",
            "notas_corazon": "Lirio, nuez moscada",
            "notas_base": "Sándalo, cedro, almizcle",
            "precio": "$75 USD"
        }
    ]
elif ph <= 7.0:
    color = "#FFFACD"
    tipo = "Fragancias suaves y florales"
    descripcion = "La piel neutra se adapta a fragancias equilibradas y delicadas."
    estacion = "Todo el año"
    perfumes = [
        {
            "nombre": "Chanel Chance Eau Tendre",
            "ocasión": "Uso diario y ocasiones especiales",
            "lugar": "Muñecas y cuello",
            "notas_top": "Pomelo, membrillo",
            "notas_corazon": "Jazmín, jacinto",
            "notas_base": "Almizcle blanco",
            "precio": "$110 USD"
        }
    ]
else:
    color = "#FFB6C1"
    tipo = "Fragancias cálidas y amaderadas"
    descripcion = "La piel alcalina se beneficia de aromas intensos y duraderos."
    estacion = "Otoño / Invierno"
    perfumes = [
        {
            "nombre": "Tom Ford Oud Wood",
            "ocasión": "Eventos nocturnos",
            "lugar": "Cuello y pecho",
            "notas_top": "Cardamomo, pimienta",
            "notas_corazon": "Oud, sándalo",
            "notas_base": "Vainilla, ámbar",
            "precio": "$250 USD"
        }
    ]

# ---------------------------
# Aplicar fondo
# ---------------------------
set_background(color)

# ---------------------------
# Panel principal
# ---------------------------
st.markdown(
    f"""
    <div style='background-color:rgba(255,255,255,0.85);
                padding:30px;
                border-radius:20px;
                margin-bottom:20px;'>
        <h3>Tipo de fragancia recomendada: {tipo}</h3>
        <p>{descripcion}</p>
        <p><b>Temporada ideal:</b> {estacion}</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Perfumes recomendados
# ---------------------------
st.markdown("### Perfumes sugeridos")
cols = st.columns(3)

for i, p in enumerate(perfumes):
    with cols[i]:
        st.markdown(
            f"""
            <div style='background-color:rgba(255,255,255,0.95);
                        padding:20px;
                        border-radius:15px;
                        box-shadow:0 4px 6px rgba(0,0,0,0.1);
                        margin-bottom:10px;'>
                <h4>{p['nombre']}</h4>
                <p><b>Precio:</b> {p['precio']}</p>
                <p><b>Ocasión:</b> {p['ocasión']}</p>
                <p><b>Aplicación recomendada:</b> {p['lugar']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.expander("Notas de la fragancia"):
            st.markdown(f"**Notas superiores:** {p['notas_top']}")
            st.markdown(f"**Notas de corazón:** {p['notas_corazon']}")
            st.markdown(f"**Notas de base:** {p['notas_base']}")

        st.markdown("**Tiendas disponibles:**")
        st.markdown(
            f"[Amazon](https://www.amazon.com/s?k={p['nombre'].replace(' ', '+')}) | "
            f"[Sephora](https://www.sephora.com/search?keyword={p['nombre'].replace(' ', '+')}) | "
            f"[Ulta](https://www.ulta.com/search?q={p['nombre'].replace(' ', '+')})"
        )

        if p["nombre"] not in st.session_state.perfumes_favoritos:
            if st.button("Agregar a favoritos", key=f"fav_{i}"):
                st.session_state.perfumes_favoritos.append(p["nombre"])
                st.experimental_rerun()
        else:
            st.success("Este perfume está en tus favoritos")

# ---------------------------
# Consejos finales
# ---------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### Consejos de aplicación")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style='background-color:rgba(255,255,255,0.85);
                    padding:20px;
                    border-radius:10px;'>
        <h4>Puntos de pulso recomendados</h4>
        <ul>
            <li>Detrás de las orejas</li>
            <li>Muñecas</li>
            <li>Interior de los codos</li>
            <li>Detrás de las rodillas</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style='background-color:rgba(255,255,255,0.85);
                    padding:20px;
                    border-radius:10px;'>
        <h4>Buenas prácticas</h4>
        <ul>
            <li>Aplicar después de la ducha</li>
            <li>Usar sobre piel hidratada</li>
            <li>No frotar la fragancia</li>
            <li>Evitar contacto directo con joyería</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align:center;'>La fragancia adecuada complementa tu identidad</h3>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; color:#666;'>Cada piel reacciona de forma distinta. Prueba siempre antes de comprar.</p>",
    unsafe_allow_html=True
)

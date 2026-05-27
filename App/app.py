"""
🩰 Pilates & Yoga Studio - Sistema de Gestión
Proyecto Final - Manuela Giraldo & Sophia Mateus
"""

import streamlit as st
import pandas as pd
from datetime import date, timedelta
from connection import run_query, run_dml

st.set_page_config(page_title="✨ Pilates & Yoga Studio", page_icon="🩰", layout="wide")
SCHEMA = "G06_E02"

# ══════════════════════════════════════════════
# CSS
# ══════════════════════════════════════════════
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Quicksand:wght@300;400;500;600;700&display=swap');
    .stApp { background: linear-gradient(170deg, #FFF5F7 0%, #FDE8EE 30%, #FCE4EC 60%, #FFF0F3 100%); }
    .stApp, .stApp p, .stApp span, .stApp label, .stApp div, .stMarkdown {
        color: #5A2040 !important; font-family: 'Quicksand', sans-serif !important; }
    .stApp h1, .stApp h2, .stApp h3 {
        font-family: 'Cormorant Garamond', serif !important; color: #7A2E50 !important; font-weight: 400 !important; }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FAD0DB 0%, #F4B8C8 100%) !important; border-right: 1px solid #EEA0B5; }
    section[data-testid="stSidebar"] * { color: #7A2E50 !important; font-family: 'Quicksand', sans-serif !important; }
    section[data-testid="stSidebar"] .stButton button {
        background: rgba(255,255,255,0.65) !important; color: #7A2E50 !important;
        border: 1px solid #E8A0B5 !important; border-radius: 14px !important;
        font-weight: 600 !important; font-size: 0.9rem !important;
        padding: 0.5rem 1rem !important; margin-bottom: 4px !important; transition: all 0.25s ease !important; }
    section[data-testid="stSidebar"] .stButton button:hover {
        background: rgba(255,255,255,0.9) !important; border-color: #D0708A !important;
        box-shadow: 0 4px 15px rgba(200,100,140,0.15) !important; transform: translateX(3px) !important; }
    .main-title { font-family: 'Cormorant Garamond', serif; font-size: 2.8rem; font-weight: 300;
        color: #7A2E50; text-align: center; margin-bottom: 0; letter-spacing: 2px; }
    .subtitle { font-family: 'Quicksand', sans-serif; font-size: 0.8rem; color: #B8708A;
        text-align: center; letter-spacing: 5px; text-transform: uppercase; margin-top: 5px; font-weight: 500; }
    .pink-divider { height: 1px; background: linear-gradient(90deg, transparent, #E8A0B5, transparent);
        margin: 1.5rem 0; border: none; }
    .section-header { font-family: 'Cormorant Garamond', serif; font-size: 1.8rem;
        font-weight: 400; color: #7A2E50; margin-bottom: 0.3rem; }
    .section-sub { font-family: 'Quicksand', sans-serif; font-size: 0.75rem; color: #B8708A;
        letter-spacing: 3px; text-transform: uppercase; margin-bottom: 1.5rem; font-weight: 500; }
    .hero-container { background: linear-gradient(135deg, rgba(255,255,255,0.7), rgba(250,208,219,0.4));
        border-radius: 24px; padding: 2.5rem 2rem; text-align: center; border: 1px solid #F0C8D5;
        box-shadow: 0 8px 32px rgba(200,100,140,0.1); margin-bottom: 2rem; backdrop-filter: blur(10px); }
    .hero-emoji { font-size: 3rem; margin-bottom: 0.5rem; }
    .hero-title { font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 300;
        color: #7A2E50; margin: 0.5rem 0; letter-spacing: 1px; }
    .hero-text { font-family: 'Quicksand', sans-serif; font-size: 0.95rem; color: #9A5070;
        line-height: 1.8; max-width: 600px; margin: 0 auto; }
    .hero-quote { font-family: 'Cormorant Garamond', serif; font-size: 1.3rem; font-style: italic;
        color: #B8708A; margin-top: 1.5rem; letter-spacing: 0.5px; }
    .metric-card { background: rgba(255,255,255,0.75); border-radius: 20px; padding: 1.8rem 1.2rem;
        text-align: center; border: 1px solid #F0C8D5; box-shadow: 0 4px 20px rgba(200,100,140,0.08);
        transition: transform 0.3s ease; backdrop-filter: blur(10px); }
    .metric-card:hover { transform: translateY(-3px); box-shadow: 0 8px 30px rgba(200,100,140,0.15); }
    .metric-icon { font-size: 1.8rem; margin-bottom: 0.5rem; }
    .metric-value { font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; font-weight: 700;
        color: #7A2E50; line-height: 1; }
    .metric-label { font-family: 'Quicksand', sans-serif; font-size: 0.7rem; color: #B8708A;
        text-transform: uppercase; letter-spacing: 3px; margin-top: 0.5rem; font-weight: 600; }
    .chart-card { background: rgba(255,255,255,0.75); border-radius: 20px; padding: 1.5rem;
        border: 1px solid #F0C8D5; box-shadow: 0 4px 20px rgba(200,100,140,0.08);
        margin-bottom: 1rem; backdrop-filter: blur(10px); }
    .chart-title { font-family: 'Cormorant Garamond', serif; font-size: 1.2rem; font-weight: 600;
        color: #7A2E50; margin-bottom: 0.8rem; text-align: center; }
    .profile-card { background: rgba(255,255,255,0.75); border-radius: 20px; padding: 1.5rem;
        border: 1px solid #F0C8D5; box-shadow: 0 4px 20px rgba(200,100,140,0.08);
        margin-bottom: 1rem; backdrop-filter: blur(10px); }
    .profile-name { font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; font-weight: 600;
        color: #7A2E50; margin-bottom: 0.3rem; }
    .profile-detail { font-family: 'Quicksand', sans-serif; font-size: 0.85rem; color: #9A5070; margin: 0.2rem 0; }
    .profile-badge-activo { display: inline-block; background: #E8F5E9; color: #388E3C;
        padding: 3px 14px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; }
    .profile-badge-inactivo { display: inline-block; background: #FCE4EC; color: #C62828;
        padding: 3px 14px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; }
    .profile-badge-potencial { display: inline-block; background: #FFF3E0; color: #EF6C00;
        padding: 3px 14px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; }
    .profile-badge-pagada { display: inline-block; background: #E8F5E9; color: #388E3C;
        padding: 3px 14px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; }
    .profile-badge-parcial { display: inline-block; background: #FFF3E0; color: #EF6C00;
        padding: 3px 14px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; }
    .profile-badge-nopagada { display: inline-block; background: #FCE4EC; color: #C62828;
        padding: 3px 14px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; }
    .stSelectbox > div > div { background: rgba(255,255,255,0.8) !important;
        border: 1px solid #F0C8D5 !important; border-radius: 12px !important; color: #5A2040 !important; }
    .stSelectbox label { color: #7A2E50 !important; font-weight: 600 !important; }
    .stTextInput > div > div > input { background: rgba(255,255,255,0.8) !important;
        border: 1px solid #F0C8D5 !important; border-radius: 12px !important; color: #5A2040 !important; }
    .stTextInput > div > div > input:focus { border-color: #E8809A !important; box-shadow: 0 0 0 1px #E8809A !important; }
    .stTextInput label { color: #7A2E50 !important; font-weight: 600 !important; }
    .stNumberInput > div > div > input { background: rgba(255,255,255,0.8) !important;
        border: 1px solid #F0C8D5 !important; border-radius: 12px !important; color: #5A2040 !important; }
    .stNumberInput label { color: #7A2E50 !important; font-weight: 600 !important; }
    .stDateInput > div > div > input { background: rgba(255,255,255,0.8) !important;
        border: 1px solid #F0C8D5 !important; border-radius: 12px !important; color: #5A2040 !important; }
    .stDateInput label { color: #7A2E50 !important; font-weight: 600 !important; }
    .stFormSubmitButton button { background: linear-gradient(135deg, #E8809A, #D8608A) !important;
        color: white !important; border: none !important; border-radius: 25px !important;
        font-family: 'Quicksand', sans-serif !important; font-weight: 600 !important;
        letter-spacing: 1px !important; padding: 0.6rem 2rem !important; }
    .stFormSubmitButton button:hover { background: linear-gradient(135deg, #D06080, #C04070) !important;
        box-shadow: 0 6px 20px rgba(200,80,120,0.3) !important; }
    .stDataFrame { border-radius: 16px !important; overflow: hidden; border: 1px solid #F0C8D5 !important; }
    .success-msg { background: linear-gradient(135deg, #F0FFF0, #E8F5E9); border-left: 4px solid #A5D6A7;
        padding: 1rem 1.5rem; border-radius: 0 16px 16px 0; color: #2E7D32; font-weight: 500; }
    .error-msg { background: linear-gradient(135deg, #FFF5F7, #FCE4EC); border-left: 4px solid #E8809A;
        padding: 1rem 1.5rem; border-radius: 0 16px 16px 0; color: #8B2252; font-weight: 500; }
    [data-testid="stMetricValue"] { font-family: 'Cormorant Garamond', serif !important; color: #7A2E50 !important; }
    [data-testid="stMetricLabel"] { color: #B8708A !important; }
    .stCaption, small { color: #B8708A !important; }
    .footer { text-align: center; color: #C8909A; font-size: 0.75rem;
        font-family: 'Quicksand', sans-serif; letter-spacing: 2px; margin-top: 2rem; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════
st.markdown('<p class="main-title">🩰 Pilates & Yoga Studio</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">wellness · balance · glow</p>', unsafe_allow_html=True)
st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════
st.sidebar.markdown("### 🌸 Menú")
opciones = [
    ("🏠", "Dashboard"), ("👤", "Mi Perfil"), ("👥", "Miembros"), ("💳", "Membresías"),
    ("🧘", "Clases"), ("📝", "Inscripciones"), ("💰", "Pagos"),
    ("✨", "Nuevo Miembro"), ("💳+", "Nueva Membresía"), ("🩰", "Nueva Inscripción"),
    ("💸", "Registrar Pago"), ("✅", "Tomar Asistencia")
]
if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"
for icon, label in opciones:
    if st.sidebar.button(f"{icon}  {label}", key=label, use_container_width=True):
        st.session_state.menu = label
menu = st.session_state.menu

def estado_badge(e):
    e = e.upper()
    if e == "ACTIVO": return '<span class="profile-badge-activo">ACTIVO</span>'
    if e == "INACTIVO": return '<span class="profile-badge-inactivo">INACTIVO</span>'
    if e == "POTENCIAL": return '<span class="profile-badge-potencial">POTENCIAL</span>'
    return f'<span>{e}</span>'

def pago_badge(e):
    e = e.upper()
    if e == "PAGADA": return '<span class="profile-badge-pagada">PAGADA</span>'
    if e == "PAGO PARCIAL": return '<span class="profile-badge-parcial">PAGO PARCIAL</span>'
    if e == "NO PAGADA": return '<span class="profile-badge-nopagada">NO PAGADA</span>'
    return f'<span>{e}</span>'


# ══════════════════════════════════════════════
# 🏠 DASHBOARD
# ══════════════════════════════════════════════
if menu == "Dashboard":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-emoji">🧘‍♀️✨🩰</div>
        <div class="hero-title">Bienvenida al Studio</div>
        <div class="hero-text">Tu espacio para gestionar membresías, clases e inscripciones
            de nuestro club de Pilates & Yoga. Todo en un solo lugar, diseñado con amor y buena energía.</div>
        <div class="hero-quote">"Inhale confidence, exhale doubt"</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<p class="section-header">📊 Resumen General</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Números del studio en tiempo real</p>', unsafe_allow_html=True)

    try:
        import plotly.graph_objects as go

        c1, c2, c3, c4 = st.columns(4)
        tm = run_query(f"SELECT COUNT(*) AS total FROM {SCHEMA}.py_miembros")[0]['TOTAL']
        ta = run_query(f"SELECT COUNT(*) AS total FROM {SCHEMA}.py_miembros WHERE estado='ACTIVO'")[0]['TOTAL']
        tc = run_query(f"SELECT COUNT(*) AS total FROM {SCHEMA}.py_clases")[0]['TOTAL']
        ti = run_query(f"SELECT COUNT(*) AS total FROM {SCHEMA}.py_inscripciones")[0]['TOTAL']
        with c1: st.markdown(f'<div class="metric-card"><div class="metric-icon">🌸</div><div class="metric-value">{tm}</div><div class="metric-label">Miembros</div></div>', unsafe_allow_html=True)
        with c2: st.markdown(f'<div class="metric-card"><div class="metric-icon">💖</div><div class="metric-value">{ta}</div><div class="metric-label">Activos</div></div>', unsafe_allow_html=True)
        with c3: st.markdown(f'<div class="metric-card"><div class="metric-icon">🧘</div><div class="metric-value">{tc}</div><div class="metric-label">Clases</div></div>', unsafe_allow_html=True)
        with c4: st.markdown(f'<div class="metric-card"><div class="metric-icon">📋</div><div class="metric-value">{ti}</div><div class="metric-label">Inscripciones</div></div>', unsafe_allow_html=True)

        st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)

        # ── GRÁFICAS EN EL DASHBOARD ──
        col_left, col_right = st.columns(2)

        # Clases más populares — TOP 3 en cards
        with col_left:
            st.markdown('<div class="chart-card"><div class="chart-title">🧘 Top 3 Clases Más Populares</div>',
                        unsafe_allow_html=True)
            pop = run_query(f"""SELECT c.disciplina AS disc, COUNT(i.inscripcion_id) AS total
                        FROM {SCHEMA}.py_clases c LEFT JOIN {SCHEMA}.py_inscripciones i ON c.clase_id=i.clase_id
                        GROUP BY c.disciplina ORDER BY total DESC""")
            if pop:
                top = pop[:3]
                medallas = ["🥇", "🥈", "🥉"]
                sizes = ["1.8rem", "1.4rem", "1.2rem"]
                for idx, t in enumerate(top):
                    st.markdown(f"""
                            <div style="background: linear-gradient(135deg, rgba(255,255,255,0.8), rgba(250,208,219,0.3));
                                border-radius: 16px; padding: 1rem 1.2rem; margin-bottom: 0.6rem;
                                border: 1px solid #F0C8D5; display: flex; align-items: center; gap: 1rem;">
                                <span style="font-size: 2rem;">{medallas[idx]}</span>
                                <div>
                                    <div style="font-family: 'Cormorant Garamond', serif; font-size: {sizes[idx]};
                                        font-weight: 600; color: #7A2E50;">{t['DISC']}</div>
                                    <div style="font-family: 'Quicksand', sans-serif; font-size: 0.8rem;
                                        color: #B8708A;">{t['TOTAL']} inscripciones</div>
                                </div>
                            </div>""", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Distribución membresías
        with col_right:
            st.markdown('<div class="chart-card"><div class="chart-title">💳 Tipos de Membresía</div>', unsafe_allow_html=True)
            dist = run_query(f"SELECT tipo_pase AS tp, COUNT(*) AS total FROM {SCHEMA}.py_membresias GROUP BY tipo_pase")
            if dist:
                fig2 = go.Figure(go.Pie(
                    labels=[d['TP'] for d in dist], values=[d['TOTAL'] for d in dist],
                    hole=0.45, marker=dict(colors=['#E8809A','#F48FB1','#F8BBD0','#B8708A','#7A2E50']),
                    textfont=dict(family='Quicksand', color='#7A2E50', size=12)))
                fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(family='Quicksand', color='#7A2E50', size=12),
                    margin=dict(l=20,r=20,t=10,b=10), height=280, showlegend=True,
                    legend=dict(font=dict(size=10, color='#7A2E50')))
                st.plotly_chart(fig2, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        col_left2, col_right2 = st.columns(2)

        # Estado de pagos
        # Estado de pagos — cards
        with col_left2:
            st.markdown('<div class="chart-card"><div class="chart-title">💰 Estado de Pagos</div>',
                        unsafe_allow_html=True)
            epago = run_query(
                f"SELECT estado_pago AS ep, COUNT(*) AS total FROM {SCHEMA}.py_membresias GROUP BY estado_pago")
            if epago:
                iconos = {'PAGADA': '✅', 'PAGO PARCIAL': '⏳', 'NO PAGADA': '❌'}
                colores_bg = {'PAGADA': '#E8F5E9', 'PAGO PARCIAL': '#FFF3E0', 'NO PAGADA': '#FCE4EC'}
                colores_txt = {'PAGADA': '#388E3C', 'PAGO PARCIAL': '#EF6C00', 'NO PAGADA': '#C62828'}
                for e in epago:
                    st.markdown(f"""
                            <div style="background: {colores_bg.get(e['EP'], '#FFF5F7')};
                                border-radius: 16px; padding: 1rem 1.2rem; margin-bottom: 0.6rem;
                                border: 1px solid #F0C8D5; display: flex; align-items: center; gap: 1rem;">
                                <span style="font-size: 2rem;">{iconos.get(e['EP'], '📌')}</span>
                                <div>
                                    <div style="font-family: 'Quicksand', sans-serif; font-size: 1.1rem;
                                        font-weight: 700; color: {colores_txt.get(e['EP'], '#5A2040')};">{e['EP']}</div>
                                    <div style="font-family: 'Quicksand', sans-serif; font-size: 0.8rem;
                                        color: #B8708A;">{e['TOTAL']} membresía(s)</div>
                                </div>
                            </div>""", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Asistencia
        with col_right2:
            st.markdown('<div class="chart-card"><div class="chart-title">✅ Resumen de Asistencia</div>', unsafe_allow_html=True)
            asist = run_query(f"SELECT estado_asist AS ea, COUNT(*) AS total FROM {SCHEMA}.py_inscripciones GROUP BY estado_asist")
            if asist:
                fig4 = go.Figure(go.Pie(
                    labels=[a['EA'] for a in asist], values=[a['TOTAL'] for a in asist],
                    hole=0.45, marker=dict(colors=['#F48FB1','#E8809A','#F8BBD0']),
                    textfont=dict(family='Quicksand', color='#7A2E50', size=12)))
                fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(family='Quicksand', color='#7A2E50', size=12),
                    margin=dict(l=20,r=20,t=10,b=10), height=280, showlegend=True,
                    legend=dict(font=dict(size=10, color='#7A2E50')))
                st.plotly_chart(fig4, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)

        # Ingresos totales
        ingresos = run_query(f"SELECT SUM(monto_pago) AS total FROM {SCHEMA}.py_pagos")
        if ingresos and ingresos[0]['TOTAL']:
            st.markdown(f"""
            <div class="metric-card" style="max-width:350px; margin: 0 auto;">
                <div class="metric-icon">💵</div>
                <div class="metric-value">${ingresos[0]['TOTAL']:,.0f}</div>
                <div class="metric-label">Total Recaudado</div>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)

        # Membresías pendientes
        st.markdown('<p class="section-header">⚠️ Membresías con Saldo Pendiente</p>', unsafe_allow_html=True)
        pend = run_query(f"""SELECT m.nombre AS "Nombre", mem.tipo_pase AS "Plan", mem.valor_pase AS "Valor",
            mem.saldo_pendiente AS "Saldo Pendiente", mem.estado_pago AS "Estado", mem.fecha_corte AS "Vence"
            FROM {SCHEMA}.py_membresias mem JOIN {SCHEMA}.py_miembros m ON mem.miembro_id=m.miembro_id
            WHERE mem.estado_pago!='PAGADA' ORDER BY mem.saldo_pendiente DESC""")
        if pend: st.dataframe(pd.DataFrame(pend), use_container_width=True, hide_index=True)
        else: st.markdown('<div class="success-msg">✨ Todas las membresías están al día</div>', unsafe_allow_html=True)

    except Exception as e:
        st.markdown(f'<div class="error-msg">Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# 👤 MI PERFIL
# ══════════════════════════════════════════════
elif menu == "Mi Perfil":
    st.markdown('<p class="section-header">👤 Portal del Miembro</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Consulta tu información completa</p>', unsafe_allow_html=True)
    try:
        miembros = run_query(f"SELECT miembro_id, nombre FROM {SCHEMA}.py_miembros ORDER BY nombre")
        if not miembros: st.warning("No hay miembros registrados.")
        else:
            opc = {m['NOMBRE']: m['MIEMBRO_ID'] for m in miembros}
            sel = st.selectbox("Selecciona tu nombre 🌸", list(opc.keys()))
            mid = opc[sel]
            info = run_query(f"SELECT * FROM {SCHEMA}.py_miembros WHERE miembro_id=:m", {"m": mid})
            if info:
                m = info[0]
                st.markdown(f"""<div class="profile-card">
                    <div class="profile-name">🌸 {m['NOMBRE']}</div>
                    <div class="profile-detail">📄 {m['TIPO_DOC']} {m['NUM_DOC']}</div>
                    <div class="profile-detail">📧 {m['EMAIL'] or 'Sin email'}</div>
                    <div class="profile-detail">📅 Miembro desde: {m['FECHA_REGISTRO']}</div>
                    <div class="profile-detail">Estado: {estado_badge(m['ESTADO'])}</div>
                </div>""", unsafe_allow_html=True)
            st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)
            st.markdown('<p class="section-header">💳 Membresías</p>', unsafe_allow_html=True)
            mems = run_query(f"SELECT * FROM {SCHEMA}.py_membresias WHERE miembro_id=:m ORDER BY fecha_inicio DESC", {"m": mid})
            if mems:
                for mm in mems:
                    saldo_txt = f"${mm['SALDO_PENDIENTE']:,.0f}" if mm['SALDO_PENDIENTE'] > 0 else "✅ $0"
                    st.markdown(f"""<div class="profile-card">
                        <div class="profile-name">🎫 {mm['TIPO_PASE']}</div>
                        <div class="profile-detail">💰 Valor: ${mm['VALOR_PASE']:,.0f}</div>
                        <div class="profile-detail">📅 {mm['FECHA_INICIO']} → {mm['FECHA_CORTE']}</div>
                        <div class="profile-detail">Estado: {pago_badge(mm['ESTADO_PAGO'])}</div>
                        <div class="profile-detail">Saldo pendiente: {saldo_txt}</div>
                    </div>""", unsafe_allow_html=True)
            else: st.info("No tiene membresías.")
            st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)
            st.markdown('<p class="section-header">🧘 Clases Reservadas</p>', unsafe_allow_html=True)
            cls = run_query(f"""SELECT c.disciplina AS "Disciplina", c.fecha_clase AS "Fecha",
                c.horario AS "Horario", i.estado_asist AS "Estado"
                FROM {SCHEMA}.py_inscripciones i JOIN {SCHEMA}.py_clases c ON i.clase_id=c.clase_id
                WHERE i.miembro_id=:m ORDER BY c.fecha_clase DESC""", {"m": mid})
            if cls: st.dataframe(pd.DataFrame(cls), use_container_width=True, hide_index=True)
            else: st.info("No tiene clases reservadas.")
            st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)
            st.markdown('<p class="section-header">💰 Historial de Pagos</p>', unsafe_allow_html=True)
            pgs = run_query(f"""SELECT p.fecha_pago AS "Fecha", p.monto_pago AS "Monto",
                p.canal_pago AS "Canal", p.referencia AS "Ref", mem.tipo_pase AS "Plan"
                FROM {SCHEMA}.py_pagos p JOIN {SCHEMA}.py_membresias mem ON p.membresia_id=mem.membresia_id
                WHERE mem.miembro_id=:m ORDER BY p.fecha_pago DESC""", {"m": mid})
            if pgs:
                st.dataframe(pd.DataFrame(pgs), use_container_width=True, hide_index=True)
                st.metric("💵 Total Pagado", f"${sum(p['Monto'] for p in pgs):,.0f}")
            else: st.info("No tiene pagos.")
    except Exception as e:
        st.markdown(f'<div class="error-msg">Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# 👥 MIEMBROS
# ══════════════════════════════════════════════
elif menu == "Miembros":
    st.markdown('<p class="section-header">👥 Nuestras Miembros</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Comunidad del studio</p>', unsafe_allow_html=True)
    try:
        f = st.selectbox("Filtrar por estado:", ["TODOS", "ACTIVO", "INACTIVO", "POTENCIAL"])
        if f == "TODOS":
            d = run_query(f'SELECT miembro_id AS "ID", tipo_doc AS "Doc", num_doc AS "Número", nombre AS "Nombre", email AS "Email", fecha_registro AS "Registro", estado AS "Estado" FROM {SCHEMA}.py_miembros ORDER BY miembro_id')
        else:
            d = run_query(f'SELECT miembro_id AS "ID", tipo_doc AS "Doc", num_doc AS "Número", nombre AS "Nombre", email AS "Email", fecha_registro AS "Registro", estado AS "Estado" FROM {SCHEMA}.py_miembros WHERE estado=:e ORDER BY miembro_id', {"e": f})
        if d:
            st.dataframe(pd.DataFrame(d), use_container_width=True, hide_index=True)
            st.caption(f"🌸 Total: {len(d)} miembro(s)")
        else: st.info("No se encontraron miembros.")
    except Exception as e:
        st.markdown(f'<div class="error-msg">Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# 💳 MEMBRESÍAS
# ══════════════════════════════════════════════
elif menu == "Membresías":
    st.markdown('<p class="section-header">💳 Membresías</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Planes activos del studio</p>', unsafe_allow_html=True)
    try:
        f = st.selectbox("Filtrar por estado de pago:", ["TODOS", "PAGADA", "PAGO PARCIAL", "NO PAGADA"])
        q = f"""SELECT mem.membresia_id AS "ID", m.nombre AS "Nombre", mem.tipo_pase AS "Plan",
            mem.valor_pase AS "Valor", mem.fecha_inicio AS "Inicio", mem.fecha_corte AS "Vence",
            mem.estado_pago AS "Estado", mem.saldo_pendiente AS "Saldo"
            FROM {SCHEMA}.py_membresias mem JOIN {SCHEMA}.py_miembros m ON mem.miembro_id=m.miembro_id"""
        if f == "TODOS": d = run_query(q + " ORDER BY mem.membresia_id")
        else: d = run_query(q + " WHERE mem.estado_pago=:e ORDER BY mem.membresia_id", {"e": f})
        if d: st.dataframe(pd.DataFrame(d), use_container_width=True, hide_index=True)
        else: st.info("No se encontraron membresías.")
    except Exception as e:
        st.markdown(f'<div class="error-msg">Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# 🧘 CLASES
# ══════════════════════════════════════════════
elif menu == "Clases":
    st.markdown('<p class="section-header">🧘 Clases del Studio</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Agenda y disponibilidad</p>', unsafe_allow_html=True)
    try:
        f = st.selectbox("Filtrar por disciplina:", ["TODAS", "REFORMER PILATES", "MAT PILATES", "MAT YOGA", "HOT YOGA", "PUPPY YOGA"])
        q = f"""SELECT c.clase_id AS "ID", c.disciplina AS "Disciplina", c.fecha_clase AS "Fecha",
            c.horario AS "Horario", c.cupo_maximo AS "Cupo", c.cargo_inasist AS "Cargo Inasist.",
            (c.cupo_maximo - COUNT(i.inscripcion_id)) AS "Cupos Libres"
            FROM {SCHEMA}.py_clases c LEFT JOIN {SCHEMA}.py_inscripciones i ON c.clase_id=i.clase_id"""
        grp = " GROUP BY c.clase_id, c.disciplina, c.fecha_clase, c.horario, c.cupo_maximo, c.cargo_inasist ORDER BY c.fecha_clase"
        if f == "TODAS": d = run_query(q + grp)
        else: d = run_query(q + f" WHERE c.disciplina=:disc" + grp, {"disc": f})
        if d: st.dataframe(pd.DataFrame(d), use_container_width=True, hide_index=True)
        else: st.info("No se encontraron clases.")
    except Exception as e:
        st.markdown(f'<div class="error-msg">Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# 📝 INSCRIPCIONES
# ══════════════════════════════════════════════
elif menu == "Inscripciones":
    st.markdown('<p class="section-header">📝 Inscripciones</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Registro de reservas</p>', unsafe_allow_html=True)
    try:
        d = run_query(f"""SELECT i.inscripcion_id AS "ID", m.nombre AS "Nombre", c.disciplina AS "Clase",
            c.fecha_clase AS "Fecha", c.horario AS "Horario", i.estado_asist AS "Asistencia"
            FROM {SCHEMA}.py_inscripciones i JOIN {SCHEMA}.py_miembros m ON i.miembro_id=m.miembro_id
            JOIN {SCHEMA}.py_clases c ON i.clase_id=c.clase_id ORDER BY c.fecha_clase, c.horario""")
        if d: st.dataframe(pd.DataFrame(d), use_container_width=True, hide_index=True)
        else: st.info("No hay inscripciones.")
    except Exception as e:
        st.markdown(f'<div class="error-msg">Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# 💰 PAGOS
# ══════════════════════════════════════════════
elif menu == "Pagos":
    st.markdown('<p class="section-header">💰 Historial de Pagos</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Transacciones registradas</p>', unsafe_allow_html=True)
    try:
        d = run_query(f"""SELECT p.pago_id AS "ID", m.nombre AS "Nombre", mem.tipo_pase AS "Plan",
            p.fecha_pago AS "Fecha", p.monto_pago AS "Monto", p.canal_pago AS "Canal", p.referencia AS "Ref"
            FROM {SCHEMA}.py_pagos p JOIN {SCHEMA}.py_membresias mem ON p.membresia_id=mem.membresia_id
            JOIN {SCHEMA}.py_miembros m ON mem.miembro_id=m.miembro_id ORDER BY p.fecha_pago DESC""")
        if d:
            st.dataframe(pd.DataFrame(d), use_container_width=True, hide_index=True)
            st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)
            st.metric("💵 Total Recaudado", f"${sum(r['Monto'] for r in d):,.0f}")
        else: st.info("No hay pagos.")
    except Exception as e:
        st.markdown(f'<div class="error-msg">Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# ✨ NUEVO MIEMBRO
# ══════════════════════════════════════════════
elif menu == "Nuevo Miembro":
    st.markdown('<p class="section-header">✨ Registrar Nueva Miembro</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Bienvenida al studio</p>', unsafe_allow_html=True)
    with st.form("form_miembro"):
        c1, c2 = st.columns(2)
        with c1:
            tipo_doc = st.selectbox("Tipo de Documento", ["CC", "TI", "CE", "PP"])
            num_doc = st.text_input("Número de Documento")
            nombre = st.text_input("Nombre Completo")
        with c2:
            email = st.text_input("Email")
            estado = st.selectbox("Estado", ["ACTIVO", "INACTIVO", "POTENCIAL"])
        sub = st.form_submit_button("🌸 Registrar Miembro", use_container_width=True)
        if sub:
            if not num_doc or not nombre:
                st.markdown('<div class="error-msg">⚠️ Documento y nombre son obligatorios.</div>', unsafe_allow_html=True)
            else:
                try:
                    run_dml(f"""INSERT INTO {SCHEMA}.py_miembros (tipo_doc,num_doc,nombre,email,estado)
                        VALUES (:td,:nd,:n,:e,:es)""",
                        {"td":tipo_doc,"nd":num_doc,"n":nombre.upper(),"e":email.lower() if email else None,"es":estado})
                    st.markdown('<div class="success-msg">✨ ¡Miembro registrada! Welcome to the studio 🩰</div>', unsafe_allow_html=True)
                except Exception as e:
                    if "UQ_PY_MIEMBRO_DOC" in str(e).upper():
                        st.markdown('<div class="error-msg">⚠️ Ya existe un miembro con ese documento.</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="error-msg">❌ Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# 💳+ NUEVA MEMBRESÍA
# ══════════════════════════════════════════════
elif menu == "Nueva Membresía":
    st.markdown('<p class="section-header">💳 Crear Membresía</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Asignar plan a un miembro</p>', unsafe_allow_html=True)
    try:
        miembros = run_query(f"SELECT miembro_id, nombre FROM {SCHEMA}.py_miembros ORDER BY nombre")
        if not miembros: st.warning("No hay miembros.")
        else:
            precios = {"PILATES MENSUAL":180000,"YOGA MENSUAL":150000,"VIP ANUAL":1600000,"DAILY PASS":35000,"CORTESIA":0}
            with st.form("form_membresia"):
                opc_m = {m['NOMBRE']: m['MIEMBRO_ID'] for m in miembros}
                miembro_sel = st.selectbox("Seleccionar Miembro 🌸", list(opc_m.keys()))
                tipo_pase = st.selectbox("Tipo de Pase", list(precios.keys()))
                c1, c2 = st.columns(2)
                with c1:
                    valor = st.number_input("Valor ($)", min_value=0, value=precios[tipo_pase], step=1000)
                    fecha_inicio = st.date_input("Fecha Inicio", value=date.today())
                with c2:
                    if "MENSUAL" in tipo_pase: corte_d = date.today() + timedelta(days=30)
                    elif "ANUAL" in tipo_pase: corte_d = date.today() + timedelta(days=365)
                    else: corte_d = date.today()
                    fecha_corte = st.date_input("Fecha Corte", value=corte_d)
                    estado_pago = st.selectbox("Estado de Pago", ["NO PAGADA", "PAGADA", "PAGO PARCIAL"])
                saldo = valor if estado_pago == "NO PAGADA" else (0 if estado_pago == "PAGADA" else valor)
                if estado_pago == "PAGO PARCIAL":
                    saldo = st.number_input("Saldo Pendiente ($)", min_value=0, max_value=valor, value=valor, step=1000)
                sub = st.form_submit_button("💳 Crear Membresía", use_container_width=True)
                if sub:
                    try:
                        run_dml(f"""INSERT INTO {SCHEMA}.py_membresias
                            (miembro_id,tipo_pase,valor_pase,fecha_inicio,fecha_corte,estado_pago,saldo_pendiente)
                            VALUES (:mid,:tp,:vp,:fi,:fc,:ep,:sp)""",
                            {"mid":opc_m[miembro_sel],"tp":tipo_pase,"vp":valor,"fi":fecha_inicio,
                             "fc":fecha_corte,"ep":estado_pago,"sp":saldo})
                        st.markdown(f'<div class="success-msg">✨ ¡Membresía {tipo_pase} creada!</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.markdown(f'<div class="error-msg">❌ Error: {e}</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="error-msg">Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# 🩰 NUEVA INSCRIPCIÓN
# ══════════════════════════════════════════════
elif menu == "Nueva Inscripción":
    st.markdown('<p class="section-header">🩰 Inscribir a Clase</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Reserva tu spot</p>', unsafe_allow_html=True)
    try:
        miembros = run_query(f"SELECT miembro_id, nombre FROM {SCHEMA}.py_miembros WHERE estado='ACTIVO' ORDER BY nombre")
        clases = run_query(f"""SELECT c.clase_id, c.disciplina, c.fecha_clase, c.horario,
            (c.cupo_maximo - COUNT(i.inscripcion_id)) AS cupos
            FROM {SCHEMA}.py_clases c LEFT JOIN {SCHEMA}.py_inscripciones i ON c.clase_id=i.clase_id
            GROUP BY c.clase_id, c.disciplina, c.fecha_clase, c.horario, c.cupo_maximo
            HAVING (c.cupo_maximo - COUNT(i.inscripcion_id)) > 0 ORDER BY c.fecha_clase""")
        if not miembros: st.warning("No hay miembros activos.")
        elif not clases: st.warning("No hay clases con cupos.")
        else:
            with st.form("form_insc"):
                opc_m = {m['NOMBRE']: m['MIEMBRO_ID'] for m in miembros}
                ms = st.selectbox("Seleccionar Miembro 🌸", list(opc_m.keys()))
                opc_c = {f"{c['DISCIPLINA']} — {c['FECHA_CLASE']} {c['HORARIO']} ({c['CUPOS']} cupos)": c['CLASE_ID'] for c in clases}
                cs = st.selectbox("Seleccionar Clase 🧘", list(opc_c.keys()))
                sub = st.form_submit_button("🩰 Reservar Spot", use_container_width=True)
                if sub:
                    try:
                        run_dml(f"""INSERT INTO {SCHEMA}.py_inscripciones (miembro_id,clase_id,estado_asist)
                            VALUES (:m,:c,'RESERVADO')""", {"m":opc_m[ms],"c":opc_c[cs]})
                        st.markdown('<div class="success-msg">✨ ¡Inscripción exitosa! See you in class 🩰</div>', unsafe_allow_html=True)
                    except Exception as e:
                        if "UQ_PY_INSC_MIEMBRO_CLASE" in str(e).upper():
                            st.markdown('<div class="error-msg">⚠️ Ya está inscrita en esa clase.</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="error-msg">❌ Error: {e}</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="error-msg">Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# 💸 REGISTRAR PAGO
# ══════════════════════════════════════════════
elif menu == "Registrar Pago":
    st.markdown('<p class="section-header">💸 Registrar Pago</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Abonar a una membresía</p>', unsafe_allow_html=True)
    try:
        membresias = run_query(f"""SELECT mem.membresia_id, m.nombre, mem.tipo_pase, mem.valor_pase,
            mem.saldo_pendiente, mem.estado_pago
            FROM {SCHEMA}.py_membresias mem JOIN {SCHEMA}.py_miembros m ON mem.miembro_id=m.miembro_id ORDER BY m.nombre""")
        if not membresias: st.warning("No hay membresías.")
        else:
            pend = [m for m in membresias if m['ESTADO_PAGO'] != 'PAGADA']
            if pend:
                st.markdown("**Membresías con saldo pendiente:**")
                for p in pend:
                    st.markdown(f"""<div class="profile-card">
                        <div class="profile-detail"><strong>{p['NOMBRE']}</strong> — {p['TIPO_PASE']}</div>
                        <div class="profile-detail">Valor: ${p['VALOR_PASE']:,.0f} · Saldo: ${p['SALDO_PENDIENTE']:,.0f} · {pago_badge(p['ESTADO_PAGO'])}</div>
                    </div>""", unsafe_allow_html=True)
            st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)
            with st.form("form_pago"):
                opc = {f"{m['NOMBRE']} — {m['TIPO_PASE']} (Saldo: ${m['SALDO_PENDIENTE']:,.0f})": m['MEMBRESIA_ID'] for m in membresias}
                ms = st.selectbox("Seleccionar Membresía 💳", list(opc.keys()))
                c1, c2 = st.columns(2)
                with c1:
                    monto = st.number_input("Monto ($)", min_value=0, step=1000, value=0)
                    canal = st.selectbox("Canal", ["TRANSFERENCIA", "EFECTIVO", "TARJETA"])
                with c2:
                    fecha = st.date_input("Fecha", value=date.today())
                    ref = st.text_input("Referencia (opcional)")
                sub = st.form_submit_button("💸 Registrar Pago", use_container_width=True)
                if sub:
                    if monto <= 0:
                        st.markdown('<div class="error-msg">⚠️ Monto debe ser mayor a $0.</div>', unsafe_allow_html=True)
                    else:
                        try:
                            mid = opc[ms]
                            run_dml(f"""INSERT INTO {SCHEMA}.py_pagos (membresia_id,fecha_pago,monto_pago,canal_pago,referencia)
                                VALUES (:m,:f,:mo,:c,:r)""", {"m":mid,"f":fecha,"mo":monto,"c":canal,"r":ref if ref else None})
                            mi = run_query(f"SELECT saldo_pendiente FROM {SCHEMA}.py_membresias WHERE membresia_id=:m", {"m":mid})
                            if mi:
                                ns = max(0, mi[0]['SALDO_PENDIENTE'] - monto)
                                ne = 'PAGADA' if ns == 0 else 'PAGO PARCIAL'
                                run_dml(f"UPDATE {SCHEMA}.py_membresias SET saldo_pendiente=:s, estado_pago=:e WHERE membresia_id=:m",
                                    {"s":ns,"e":ne,"m":mid})
                            st.markdown(f'<div class="success-msg">✨ ¡Pago de ${monto:,.0f} registrado!</div>', unsafe_allow_html=True)
                        except Exception as e:
                            st.markdown(f'<div class="error-msg">❌ Error: {e}</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="error-msg">Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# ✅ TOMAR ASISTENCIA
# ══════════════════════════════════════════════
elif menu == "Tomar Asistencia":
    st.markdown('<p class="section-header">✅ Tomar Asistencia</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Actualizar estado de asistencia</p>', unsafe_allow_html=True)
    try:
        clases = run_query(f"SELECT clase_id, disciplina, fecha_clase, horario FROM {SCHEMA}.py_clases ORDER BY fecha_clase DESC")
        if not clases: st.warning("No hay clases.")
        else:
            opc_c = {f"{c['DISCIPLINA']} — {c['FECHA_CLASE']} {c['HORARIO']}": c['CLASE_ID'] for c in clases}
            clase_sel = st.selectbox("Seleccionar Clase 🧘", list(opc_c.keys()))
            clase_id = opc_c[clase_sel]
            inscritos = run_query(f"""SELECT i.inscripcion_id, m.nombre, i.estado_asist
                FROM {SCHEMA}.py_inscripciones i JOIN {SCHEMA}.py_miembros m ON i.miembro_id=m.miembro_id
                WHERE i.clase_id=:cid ORDER BY m.nombre""", {"cid": clase_id})
            if not inscritos: st.info("No hay inscripciones para esta clase.")
            else:
                st.markdown(f"**{len(inscritos)} miembro(s) inscrito(s):**")
                st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)
                with st.form("form_asistencia"):
                    nuevos = {}
                    for ins in inscritos:
                        estados = ["RESERVADO", "ASISTIÓ", "NO ASISTIÓ"]
                        idx = estados.index(ins['ESTADO_ASIST']) if ins['ESTADO_ASIST'] in estados else 0
                        nuevo = st.selectbox(f"🌸 {ins['NOMBRE']} (actual: {ins['ESTADO_ASIST']})", estados, index=idx, key=f"a_{ins['INSCRIPCION_ID']}")
                        nuevos[ins['INSCRIPCION_ID']] = nuevo
                    sub = st.form_submit_button("✅ Guardar Asistencia", use_container_width=True)
                    if sub:
                        try:
                            cambios = 0
                            for iid, est in nuevos.items():
                                orig = next(i['ESTADO_ASIST'] for i in inscritos if i['INSCRIPCION_ID'] == iid)
                                if est != orig:
                                    run_dml(f"UPDATE {SCHEMA}.py_inscripciones SET estado_asist=:e WHERE inscripcion_id=:i", {"e":est,"i":iid})
                                    cambios += 1
                            if cambios: st.markdown(f'<div class="success-msg">✨ ¡{cambios} asistencia(s) actualizada(s)!</div>', unsafe_allow_html=True)
                            else: st.info("No hubo cambios.")
                        except Exception as e:
                            st.markdown(f'<div class="error-msg">❌ Error: {e}</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="error-msg">Error: {e}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════
st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="footer">🩰 Pilates & Yoga Studio — Proyecto Final BI · Manuela Giraldo & Sophia Mateus · 2026-I</p>', unsafe_allow_html=True)
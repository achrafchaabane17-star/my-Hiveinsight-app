import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time

# --- 1. إعدادات الاستوديو الاحترافي ---
st.set_page_config(page_title="HiveInsight Studio", page_icon="📊", layout="wide")

# تصميم مخصص لواجهة الاستوديو
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; background-color: #ffffff;
        border-radius: 10px 10px 0px 0px; gap: 1px; padding: 10px;
    }
    .status-card {
        background-color: white; border-radius: 15px; padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-left: 5px solid #1E88E5;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. القائمة الجانبية (نظام التحكم) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=70)
    st.title("HiveInsight Studio")
    st.markdown("---")
    st.subheader("⚙️ Paramètres d'analyse")
    engine = st.selectbox("Moteur d'exécution", ["Tez", "MapReduce", "Spark"])
    sampling = st.checkbox("Activer le Sampling (Data)", value=True)
    st.markdown("---")
    st.info("💡 **Objectif:** Identifier les opérations coûteuses et optimiser les performances.")

# --- 3. الهيدر الرئيسي للمشروع ---
st.title("🛡️ HiveInsight: Profiling & Optimization Studio")
st.write("Plateforme d'analyse avancée pour l'écosystème Apache Hive")

# --- 4. منطقة العمل الأساسية (Tabs حسب أهداف المشروع) ---
tab_query, tab_profile, tab_recommandation = st.tabs([
    "🔍 Analyseur de Requête", "📈 Profiling de Performance", "💡 Recommandations"
])

with tab_query:
    col_input, col_info = st.columns([2, 1])
    with col_input:
        query_input = st.text_area("✍️ Saisie de la requête HQL :", height=200, 
                                 placeholder="SELECT a.id, b.name FROM sales a JOIN users b ON a.user_id = b.id...")
        analyze_btn = st.button("🚀 Lancer l'Analyse Studio", use_container_width=True)
    
    with col_info:
        st.markdown("""
        <div class="status-card">
            <h4>📋 Aide au Profilage</h4>
            <ul>
                <li>Vérification de la syntaxe</li>
                <li>Détection des Jointures lourdes</li>
                <li>Analyse du Predicate Pushdown</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

if analyze_btn:
    if not query_input.strip():
        st.error("Veuillez entrer une requête pour le profilage.")
    else:
        with st.spinner("Génération du plan d'exécution et calcul des métriques..."):
            time.sleep(2)
        
        # محاكاة البيانات بناءً على أهداف المشروع
        with tab_profile:
            st.subheader("📊 Métriques d'exécution (Simulation)")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("CPU Time", "124 ms", "-12%")
            m2.metric("Memory HDFS", "1.4 GB", "Stable")
            m3.metric("Data Skew", "Low", "Optimized")
            m4.metric("Stages YARN", "3 Tasks", "Tez")

            # رسم بياني لمراحل التنفيذ (Execution Steps)
            st.markdown("---")
            col_viz1, col_viz2 = st.columns(2)
            
            with col_viz1:
                st.write("🕒 **Distribution du temps par étape**")
                steps = pd.DataFrame({
                    'Étape': ['Scan Table', 'Map Join', 'Shuffle', 'Reduce'],
                    'Temps (s)': [15, 45, 20, 30]
                })
                fig_bar = px.bar(steps, x='Étape', y='Temps (s)', color='Étape', text_auto=True)
                st.plotly_chart(fig_bar, use_container_width=True)

            with col_viz2:
                st.write("📉 **Consommation des ressources**")
                fig_gauge = go.Figure(go.Indicator(
                    mode = "gauge+number", value = 65,
                    title = {'text': "Efficacité Globale (%)"},
                    gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': "#1E88E5"}}
                ))
                st.plotly_chart(fig_gauge, use_container_width=True)

        with tab_recommandation:
            st.subheader("🎯 Pistes d'amélioration")
            
            # منطق التوصيات الذكي
            if "JOIN" in query_input.upper():
                st.success("✅ **MapJoin Optimisé:** Votre jointure peut être convertie en MapJoin pour plus de rapidité.")
            
            if "*" in query_input:
                st.error("🚨 **Avertissement:** L'utilisation de `SELECT *` augmente le Data Scanning. Spécifiez vos colonnes.")
            
            with st.expander("📝 Détails des optimisations proposées"):
                st.write("1. **Partitioning:** Ajoutez un filtre sur la colonne de date.")
                st.write("2. **Format de fichier:** Utilisez ORC avec compression ZLIB.")
                st.write("3. **Vectorization:** Activez `hive.vectorized.execution.enabled`.")

# --- 5. الفوتر (المعلومات التقنية) ---
st.markdown("---")
st.caption("HiveInsight Studio v2.5 | Analyseur interactif pour environnements Big Data")
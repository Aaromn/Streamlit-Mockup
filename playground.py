import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import date, timedelta
from utils import load_css

st.set_page_config(layout="wide", page_title="OAM Widgets", page_icon="📊")


load_css()

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📊 OAM Dashboard")
    st.markdown("---")
    selected_oam = st.selectbox(
        "Select OAM",
        ["All OAMs", "J. Lorem", "A. Ipsum", "D. Dolor", "S. Amet", "C. Consec"]
    )
    st.markdown("---")
    st.markdown("**Date Range**")
    start_date = st.date_input("From", value=date(2025, 4, 1))
    end_date   = st.date_input("To",   value=date.today())
    st.markdown("---")
    st.caption("Last refreshed: Jul 11, 2025 · 8:00 AM EST")

st.markdown(f"## OAM Widgets — {selected_oam}")
st.markdown("Placeholder data shown. Connect to live data source to populate.")
st.markdown("---")




# ═════════════════════════════════════════════════════════════════════════════
# ROW 2: AI Evaluation (Future)  |  Patient Tracker
# ═════════════════════════════════════════════════════════════════════════════
col3, col4 = st.columns(2)

# ── WIDGET 3: AI Tool — Account Plan Evaluation (Future) ─────────────────────
with col3:
    st.markdown("""
    <div class="widget-card">
      <div class="widget-title">🤖 AI Evaluation — Account Plans
        <span class="widget-subtitle">— Coming Soon</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="future-badge">
        <div style="font-size:28px; margin-bottom:8px;">🤖</div>
        <div style="font-weight:700; font-size:15px; color:#4527a0; margin-bottom:6px;">AI-Powered Account Plan Evaluator</div>
        <div style="font-size:13px; color:#555; margin-bottom:12px;">
            This widget will automatically analyze each OAM's account plans and score them on:<br><br>
            <b>• Completeness</b> — Are all required fields filled?<br>
            <b>• Recency</b> — Has the plan been updated within the target window?<br>
            <b>• Quality Score</b> — AI-generated 1–10 rating based on strategic depth<br>
            <b>• Recommended Actions</b> — Suggested next steps per account
        </div>
        <div style="background:#d1c4e9; border-radius:6px; padding:8px 14px; font-size:12px; color:#4527a0; font-weight:600;">
            🔒 Feature in Development — Available Q4 2025
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.button("🔔 Notify Me When Available", key="ai_notify", use_container_width=True)










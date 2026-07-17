import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utils import load_css
from datetime import date

load_css()




# ═════════════════════════════════════════════════════════════════════════════
# ROW 1: Account Plans  |  Calls/Day
# ═════════════════════════════════════════════════════════════════════════════
col1, col2 = st.columns(2)

# ── WIDGET 1: Account Plans ───────────────────────────────────────────────────
with col1:
    st.markdown("""
    <div class="widget-card">
      <div class="widget-title">📋 Account Plans
        <span class="widget-subtitle">— Last update date on OAM's Top 10 Accounts</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    account_data = {
        "Account":      ["Ipsum Medical Grp", "Lorem Health", "Dolor Clinic", "Amet Partners",
                         "Consec Institute", "Adipis Center", "Elit Hospital", "Sed Practice",
                         "Do Eiusmod Clinic", "Tempor Health"],
        "Last Updated": ["Jul 8, 2025",  "Jun 30, 2025", "Jun 15, 2025", "Jul 10, 2025",
                         "May 28, 2025", "Jul 3, 2025",  "Jun 22, 2025", "Apr 30, 2025",
                         "Jul 9, 2025",  "Jun 5, 2025"],
        "Days Since":   [3, 11, 26, 1, 44, 8, 19, 72, 2, 36],
        "Tier":         ["T1","T1","T2","T1","T2","T3","T2","T1","T3","T2"],
    }
    df_acct = pd.DataFrame(account_data)

    def acct_status(days):
        if days <= 14:  return "🟢 Current"
        if days <= 30:  return "🟡 Due Soon"
        return          "🔴 Overdue"

    df_acct["Status"] = df_acct["Days Since"].apply(acct_status)

    overdue  = (df_acct["Days Since"] > 30).sum()
    due_soon = ((df_acct["Days Since"] > 14) & (df_acct["Days Since"] <= 30)).sum()
    current  = (df_acct["Days Since"] <= 14).sum()

    m1, m2, m3 = st.columns(3)
    m1.metric("🟢 Current",  current)
    m2.metric("🟡 Due Soon", due_soon)
    m3.metric("🔴 Overdue",  overdue)

    st.dataframe(
        df_acct[["Account","Tier","Last Updated","Days Since","Status"]],
        hide_index=True, use_container_width=True, height=230
    )
    st.button("✏️ Update Account Plan", key="update_acct", use_container_width=True)


# ── WIDGET 2: Calls/Day ───────────────────────────────────────────────────────
with col2:
    st.markdown("""
    <div class="widget-card">
      <div class="widget-title">📞 Calls / Day
        <span class="widget-subtitle">— Adjust for days out of territory</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        total_days    = st.number_input("Total Working Days", min_value=1, max_value=30, value=20)
        days_out      = st.number_input("Days Out of Territory", min_value=0, max_value=30, value=3)
    with c2:
        total_calls   = st.number_input("Total Calls Made", min_value=0, max_value=500, value=34)

    adj_days      = max(total_days - days_out, 1)
    calls_per_day = round(total_calls / adj_days, 2)
    target        = 1.4

    status_color  = "#2e7d32" if calls_per_day >= target else ("#e65100" if calls_per_day >= target * 0.8 else "#c62828")

    st.markdown(f"""
    <div style="text-align:center; margin:10px 0;">
        <div class="metric-label">Adjusted Calls/Day ({adj_days} field days)</div>
        <div style="font-size:40px; font-weight:800; color:{status_color};">{calls_per_day}</div>
        <div class="metric-label">Target: {target} calls/day</div>
    </div>
    """, unsafe_allow_html=True)

    # Mini bar chart: calls per day over recent weeks (dummy)
    weeks_cd  = ["Wk 1","Wk 2","Wk 3","Wk 4"]
    cpd_vals  = [1.2, 1.5, 1.3, calls_per_day]
    colors_cd = ["#2e6db4" if v >= target else "#e65100" for v in cpd_vals]

    fig_cd = go.Figure(go.Bar(x=weeks_cd, y=cpd_vals, marker_color=colors_cd, text=[f"{v}" for v in cpd_vals], textposition="outside"))
    fig_cd.add_hline(y=target, line_dash="dash", line_color="#c62828", annotation_text="Target")
    fig_cd.update_layout(
        height=180, margin=dict(l=10,r=10,t=10,b=10),
        plot_bgcolor="white", paper_bgcolor="white",
        yaxis=dict(range=[0, 2.2], showgrid=True, gridcolor="#eee"),
        xaxis=dict(showgrid=False),
        showlegend=False
    )
    st.plotly_chart(fig_cd, use_container_width=True)


# ═════════════════════════════════════════════════════════════════════════════
# ROW 2: AI Evaluation (Future)  |  Patient Tracker
# ═════════════════════════════════════════════════════════════════════════════
col3, col4 = st.columns(2)

# ── WIDGET 5: Check-Out Files to Patients Chart ───────────────────────────────
with col3:
    st.markdown("""
    <div class="widget-card">
      <div class="widget-title">📁 Files Checked Out to Patients
        <span class="widget-subtitle">— By file type over time</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    weeks_fo  = ["Wk 1","Wk 2","Wk 3","Wk 4","Wk 5","Wk 6"]
    brochures = [8, 11, 7, 14, 10, 13]
    fact_shts = [5, 6, 9, 7, 8, 11]
    guides    = [3, 4, 3, 6, 5, 7]

    fig_fo = go.Figure()
    fig_fo.add_trace(go.Bar(name="Brochures",   x=weeks_fo, y=brochures, marker_color="#1a3a6b"))
    fig_fo.add_trace(go.Bar(name="Fact Sheets", x=weeks_fo, y=fact_shts, marker_color="#2e6db4"))
    fig_fo.add_trace(go.Bar(name="Pat. Guides", x=weeks_fo, y=guides,    marker_color="#90caf9"))
    fig_fo.update_layout(
        barmode="stack", height=220,
        margin=dict(l=10,r=10,t=10,b=10),
        plot_bgcolor="white", paper_bgcolor="white",
        legend=dict(orientation="h", y=-0.25, font=dict(size=10)),
        xaxis=dict(showgrid=False, tickfont=dict(size=10)),
        yaxis=dict(showgrid=True, gridcolor="#eee", tickfont=dict(size=10)),
    )
    st.plotly_chart(fig_fo, use_container_width=True)

    tot1, tot2, tot3 = st.columns(3)
    tot1.metric("Brochures",   sum(brochures))
    tot2.metric("Fact Sheets", sum(fact_shts))
    tot3.metric("Pat. Guides", sum(guides))
    st.button("📤 Log File Check-Out", key="log_file", use_container_width=True)

# ── WIDGET 4: Patient Tracker — Update Date ───────────────────────────────────
with col4:
    st.markdown("""
    <div class="widget-card">
      <div class="widget-title">🧑‍⚕️ Patient Tracker
        <span class="widget-subtitle">— Last update date per account</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    pt_data = {
        "Account":       ["Ipsum Medical Grp", "Lorem Health", "Dolor Clinic", "Amet Partners", "Consec Institute"],
        "Active Pts":    [14, 9, 21, 6, 17],
        "New This Wk":   [2, 0, 3, 1, 2],
        "Last Updated":  ["Jul 10, 2025","Jul 7, 2025","Jul 9, 2025","Jun 28, 2025","Jul 11, 2025"],
        "Days Since":    [1, 4, 2, 13, 0],
    }
    df_pt = pd.DataFrame(pt_data)

    p1, p2, p3 = st.columns(3)
    p1.metric("Total Active Patients", df_pt["Active Pts"].sum())
    p2.metric("New This Week",         df_pt["New This Wk"].sum())
    p3.metric("Accounts Updated Today",int((df_pt["Days Since"] == 0).sum()))

    st.dataframe(df_pt, hide_index=True, use_container_width=True, height=200)

    st.markdown("**Log a Patient Update:**")
    pu1, pu2 = st.columns(2)
    with pu1:
        st.selectbox("Account", df_pt["Account"].tolist(), key="pt_acct")
    with pu2:
        st.date_input("Update Date", value=date.today(), key="pt_date")
    st.button("✅ Save Patient Update", key="save_pt", type="primary", use_container_width=True)
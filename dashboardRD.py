import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from utils import load_css
from datetime import date

load_css()

# ═════════════════════════════════════════════════════════════════════════════
# ROW 4: P2P Adherence  |  Triggers Received & % Actioned
# ═════════════════════════════════════════════════════════════════════════════
col7, col8 = st.columns(2)

# ── WIDGET 7: P2P Adherence ───────────────────────────────────────────────────
with col7:
    st.markdown("""
    <div class="widget-card">
      <div class="widget-title">🤝 P2P Adherence
        <span class="widget-subtitle">— Peer-to-Peer program participation per OAM</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.info("ℹ️ **P2P Definition Pending** — This widget will track peer-to-peer engagement metrics once the P2P program definition and data source are confirmed. Placeholder structure shown below.", icon="📌")

    p2p_data = {
        "OAM":            ["J. Lorem", "A. Ipsum", "D. Dolor", "S. Amet", "C. Consec"],
        "P2P Events":     [3, 5, 1, 4, 2],
        "Target Events":  [4, 4, 4, 4, 4],
        "Adherence %":    ["75%", "100%+", "25%", "100%", "50%"],
        "Last P2P":       ["Jul 1, 2025","Jul 8, 2025","May 15, 2025","Jul 5, 2025","Jun 20, 2025"],
    }
    df_p2p = pd.DataFrame(p2p_data)

    p2p_vals   = [3, 5, 1, 4, 2]
    p2p_target = [4, 4, 4, 4, 4]
    p2p_colors = ["#2e7d32" if v >= t else ("#e65100" if v >= t * 0.5 else "#c62828")
                  for v, t in zip(p2p_vals, p2p_target)]

    fig_p2p = go.Figure()
    fig_p2p.add_trace(go.Bar(name="Actual",  x=df_p2p["OAM"], y=p2p_vals,   marker_color=p2p_colors))
    fig_p2p.add_trace(go.Scatter(name="Target", x=df_p2p["OAM"], y=p2p_target,
                                  mode="lines+markers", line=dict(color="#c62828", dash="dash"), marker=dict(size=8)))
    fig_p2p.update_layout(
        height=200, margin=dict(l=10,r=10,t=10,b=10),
        plot_bgcolor="white", paper_bgcolor="white",
        legend=dict(orientation="h", y=-0.3, font=dict(size=10)),
        xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="#eee", range=[0, 7]),
    )
    st.plotly_chart(fig_p2p, use_container_width=True)
    st.dataframe(df_p2p, hide_index=True, use_container_width=True, height=150)


# ── WIDGET 8: Triggers Received & % Actioned ─────────────────────────────────
with col8:
    st.markdown("""
    <div class="widget-card">
      <div class="widget-title">🔔 Triggers Received & % Actioned
        <span class="widget-subtitle">— Per OAM · Confirmed via call log or manual button</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    trig_data = {
        "OAM":           ["J. Lorem", "A. Ipsum", "D. Dolor", "S. Amet", "C. Consec"],
        "Triggers Recv": [8, 12, 6, 10, 7],
        "Actioned":      [6, 10, 3, 9, 5],
        "% Actioned":    [75, 83, 50, 90, 71],
    }
    df_trig = pd.DataFrame(trig_data)

    nation_pct = int(df_trig["Actioned"].sum() / df_trig["Triggers Recv"].sum() * 100)

    t1, t2, t3 = st.columns(3)
    t1.metric("Total Triggers",   df_trig["Triggers Recv"].sum())
    t2.metric("Total Actioned",   df_trig["Actioned"].sum())
    t3.metric("Nation % Actioned", f"{nation_pct}%")

    # Progress bars per OAM
    st.markdown("**Actioned Rate by OAM:**")
    for _, row in df_trig.iterrows():
        pct   = row["% Actioned"]
        color = "#2e7d32" if pct >= 80 else ("#e65100" if pct >= 60 else "#c62828")
        st.markdown(f"""
        <div style="margin-bottom:8px;">
            <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:2px;">
                <span><b>{row['OAM']}</b></span>
                <span style="color:{color}; font-weight:700;">{row['Actioned']}/{row['Triggers Recv']} &nbsp;({pct}%)</span>
            </div>
            <div style="background:#eee; border-radius:4px; height:10px;">
                <div style="background:{color}; width:{pct}%; height:10px; border-radius:4px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Mark a Trigger as Actioned:**")
    ta1, ta2 = st.columns(2)
    with ta1:
        st.selectbox("OAM",     df_trig["OAM"].tolist(), key="trig_oam")
    with ta2:
        st.selectbox("Trigger", ["Trigger #1042 — Low call freq.",
                                  "Trigger #1043 — No email last 2wks",
                                  "Trigger #1044 — Account plan overdue"], key="trig_id")
    tb1, tb2 = st.columns(2)
    with tb1:
        st.button("✅ Mark Actioned (Manual)",      key="trig_manual", type="primary",  use_container_width=True)
    with tb2:
        st.button("🔍 Auto-Check Call Logs",        key="trig_auto",                    use_container_width=True)

# ═════════════════════════════════════════════════════════════════════════════
# ROW 3: Check-Out Files to Patients  |  Field Coaching Report
# ═════════════════════════════════════════════════════════════════════════════
col5, col6 = st.columns(2)




# ── WIDGET 6: Field Coaching Report ──────────────────────────────────────────
with col5:
    st.markdown("""
    <div class="widget-card">
      <div class="widget-title">🏫 Field Coaching Report
        <span class="widget-subtitle">— Last coaching session date per OAM</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    fcr_data = {
        "OAM":            ["J. Lorem", "A. Ipsum", "D. Dolor", "S. Amet", "C. Consec"],
        "Last FCR Date":  ["Jun 30, 2025","Jul 7, 2025","May 19, 2025","Jul 2, 2025","Jun 10, 2025"],
        "Days Since":     [11, 4, 53, 9, 31],
        "Coach":          ["Mgr. Alpha","Mgr. Alpha","Mgr. Beta","Mgr. Beta","Mgr. Alpha"],
        "Score":          ["4.2 / 5","4.7 / 5","3.9 / 5","4.5 / 5","4.1 / 5"],
    }
    df_fcr = pd.DataFrame(fcr_data)

    def fcr_status(days):
        if days <= 30: return "🟢 On Track"
        if days <= 60: return "🟡 Due Soon"
        return               "🔴 Overdue"

    df_fcr["Status"] = df_fcr["Days Since"].apply(fcr_status)

    overdue_fcr = (df_fcr["Days Since"] > 60).sum()
    avg_days    = int(df_fcr["Days Since"].mean())

    f1, f2 = st.columns(2)
    f1.metric("Avg Days Since Last FCR", avg_days)
    f2.metric("OAMs Overdue for FCR",    overdue_fcr)

    st.dataframe(df_fcr[["OAM","Coach","Last FCR Date","Days Since","Score","Status"]],
                 hide_index=True, use_container_width=True, height=180)

    st.markdown("**Schedule a New FCR:**")
    sc1, sc2, sc3 = st.columns(3)
    with sc1: st.selectbox("OAM",   df_fcr["OAM"].tolist(), key="fcr_oam")
    with sc2: st.selectbox("Coach", ["Mgr. Alpha","Mgr. Beta"], key="fcr_coach")
    with sc3: st.date_input("Date", value=date.today(), key="fcr_date")
    st.button("📅 Schedule FCR", key="sched_fcr", type="primary", use_container_width=True)


# ═════════════════════════════════════════════════════════════════════════════
# ROW 5: PEQ Adherence (full width)
# ═════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="widget-card">
  <div class="widget-title">📊 PEQ Call Adherence
    <span class="widget-subtitle">— Query per OAM · Target: ≥ 30%</span>
  </div>
</div>
""", unsafe_allow_html=True)

peq_data = {
    "OAM":             ["J. Lorem", "A. Ipsum", "D. Dolor", "S. Amet", "C. Consec"],
    "Total Calls":     [34, 41, 28, 38, 31],
    "PEQ Calls":       [11, 17, 7,  14, 9 ],
    "PEQ Adherence %": [32.4, 41.5, 25.0, 36.8, 29.0],
    "Target":          [30.0, 30.0, 30.0, 30.0, 30.0],
    "vs Target":       ["+2.4%", "+11.5%", "-5.0%", "+6.8%", "-1.0%"],
}
df_peq = pd.DataFrame(peq_data)

peq_colors = ["#2e7d32" if v >= 30 else "#c62828" for v in df_peq["PEQ Adherence %"]]

# Gauge-style bar chart
fig_peq = go.Figure()
fig_peq.add_trace(go.Bar(
    x=df_peq["OAM"],
    y=df_peq["PEQ Adherence %"],
    marker_color=peq_colors,
    text=[f"{v}%" for v in df_peq["PEQ Adherence %"]],
    textposition="outside",
    name="PEQ Adherence %"
))
fig_peq.add_hline(y=30, line_dash="dash", line_color="#c62828", line_width=2,
                  annotation_text="30% Target", annotation_position="top right")
fig_peq.update_layout(
    height=250, margin=dict(l=10,r=10,t=30,b=10),
    plot_bgcolor="white", paper_bgcolor="white",
    yaxis=dict(range=[0, 55], showgrid=True, gridcolor="#eee", ticksuffix="%"),
    xaxis=dict(showgrid=False),
    showlegend=False
)

pc1, pc2 = st.columns([2, 1])
with pc1:
    st.plotly_chart(fig_peq, use_container_width=True)
with pc2:
    st.markdown("**OAM Breakdown:**")
    st.dataframe(
        df_peq[["OAM","Total Calls","PEQ Calls","PEQ Adherence %","vs Target"]],
        hide_index=True, use_container_width=True, height=220
    )

# PEQ query selector
st.markdown("**Run a Custom PEQ Query:**")
qc1, qc2, qc3, qc4 = st.columns([1.5, 1.5, 1.5, 1])
with qc1: st.selectbox("OAM",         ["All OAMs","J. Lorem","A. Ipsum","D. Dolor","S. Amet","C. Consec"], key="peq_oam")
with qc2: st.selectbox("Time Period",  ["R13W","R26W","QTD","Custom"], key="peq_period")
with qc3: st.selectbox("Region",       ["All","Alpha","Beta","Gamma"], key="peq_region")
with qc4:
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🔍 Run Query", key="run_peq", type="primary", use_container_width=True)



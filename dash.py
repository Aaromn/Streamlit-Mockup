import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import date

st.set_page_config(layout="wide", page_title="Sales Dashboard")

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
.main { background-color: #f5f5f5; }
.stButton > button {
    border-radius: 4px;
    font-weight: 600;
    font-size: 13px;
}
/* Sidebar nav */
[data-testid="stSidebar"] {
    background-color: #1a3a6b;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
[data-testid="stSidebar"] .stRadio label {
    font-size: 15px;
    font-weight: 600;
}
/* Report cards */
.report-card {
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 12px;
    border-left: 5px solid #2c4a7c;
}
.report-card-new {
    border-left: 5px solid #e8a000;
}
.report-title {
    font-size: 15px;
    font-weight: 700;
    color: #1a3a6b;
    margin-bottom: 4px;
}
.report-meta {
    font-size: 12px;
    color: #666;
    margin-bottom: 10px;
}
.badge-new {
    background: #e8a000;
    color: white;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 10px;
    margin-left: 8px;
}
.badge-viewed {
    background: #aaa;
    color: white;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 10px;
    margin-left: 8px;
}
.insight-bullet {
    font-size: 13px;
    color: #333;
    margin: 3px 0;
}
.insight-positive { color: #e6ffe6; font-weight: 600; }
.insight-negative { color: #ffe6e6; font-weight: 600; }
.insight-neutral  { color: #e6ffff; font-weight: 600; }
.section-header {
    font-size: 20px;
    font-weight: 700;
    color: #1a3a6b;
    border-bottom: 2px solid #2c4a7c;
    padding-bottom: 6px;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR NAVIGATION ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📊 Sales Dashboard")
    st.markdown("---")
    page = st.radio("Navigate", ["🏠  Dashboard", "📋  Triggers / Reports"], label_visibility="collapsed")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
if page == "🏠  Dashboard":

    # ── FILTER BAR ────────────────────────────────────────────────────────────
    with st.container():
        f1, f2, f3, f4, f5, f6, f7 = st.columns([1.2, 1.2, 1, 1, 1, 0.7, 0.7])
        with f1:
            st.selectbox("Time Period ⓘ", ["R13W", "R26W", "R52W", "QTD"])
        with f2:
            st.text_input("Custom Date ⓘ", placeholder="Start – End")
        with f3:
            st.selectbox("Region", ["All", "East", "West", "South/Central"])
        with f4:
            st.selectbox("Territory", ["All", "Territory 1", "Territory 2"])
        with f5:
            st.selectbox("State", ["All", "CA", "TX", "NY"])
        with f6:
            st.markdown("<br>", unsafe_allow_html=True)
            st.button("Vials", type="primary", use_container_width=True)
        with f7:
            st.markdown("<br>", unsafe_allow_html=True)
            st.button("Calls", use_container_width=True)

    # ── CHART DATA ────────────────────────────────────────────────────────────
    weeks = ["04/18","04/25","05/02","05/09","05/16","05/23","05/30",
             "06/06","06/13","06/20","06/27","07/04","07/11"]
    east       = [128, 102, 123, 115, 132, 109, 103, 104, 139, 115, 144,  97, 139]
    south_cent = [ 84,  84,  91,  81, 106,  97,  84,  77,  85,  88,  80,  77,  92]
    unassigned = [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
    west       = [ 88,  88, 104, 110,  84,  88,  81,  76,  94,  82, 101,  86,  92]
    totals     = [300, 274, 318, 306, 322, 294, 268, 257, 318, 285, 325, 260, 323]

    fig = go.Figure()
    fig.add_trace(go.Bar(name="East",             x=weeks, y=east,       marker_color="#1a3a6b", text=east,       textposition="inside", textfont=dict(color="white", size=10)))
    fig.add_trace(go.Bar(name="South /Central",   x=weeks, y=south_cent, marker_color="#2e6db4", text=south_cent, textposition="inside", textfont=dict(color="white", size=10)))
    fig.add_trace(go.Bar(name="Unassigned Region",x=weeks, y=unassigned, marker_color="#f5c842"))
    fig.add_trace(go.Bar(name="West",             x=weeks, y=west,       marker_color="#b0bec5", text=west,       textposition="inside", textfont=dict(color="#333",   size=10)))
    fig.add_trace(go.Scatter(x=weeks, y=[t + 14 for t in totals], mode="text", text=totals, textfont=dict(size=11, color="#222"), showlegend=False))
    fig.update_layout(
        barmode="stack",
        title=dict(text="Vials by Region", x=0.42, font=dict(size=15, color="#1a1a2e")),
        plot_bgcolor="white", paper_bgcolor="white",
        legend=dict(orientation="v", x=1.01, y=0.9, font=dict(size=11)),
        margin=dict(l=30, r=10, t=50, b=30),
        height=340,
        xaxis=dict(showgrid=False, tickfont=dict(size=10)),
        yaxis=dict(showgrid=True, gridcolor="#eee", tickfont=dict(size=10), range=[0, 380]),
    )

    # ── TOP SECTION ───────────────────────────────────────────────────────────
    chart_col, haid_col = st.columns([2.6, 1])
    with chart_col:
        tb1, tb2, tb3 = st.columns([4, 0.7, 0.7])
        with tb2: st.button("Line Chart", key="linechart")
        with tb3: st.button("Bar Chart",  key="barchart", type="primary")
        st.plotly_chart(fig, use_container_width=True)

    with haid_col:
        st.markdown("""
        <div style="background:white; border:1px solid #ddd; border-radius:6px; padding:16px; height:340px; overflow:auto;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:15px; font-weight:700; color:#1a1a2e;">ⓘ &nbsp; How am I doing?</span>
            <span style="color:#2e6db4; font-weight:700; font-size:14px;">→</span>
          </div>
          <div style="font-size:13px; font-weight:700; color:#1a1a2e; border-bottom:1px solid #eee; padding-bottom:3px; margin:10px 0 4px 0;">Attainment</div>
          <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Territory QTD</span><span style="font-weight:600; color:#1a3a6b;">11.9%</span></div>
          <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Region QTD</span><span style="font-weight:600; color:#1a3a6b;">11.9%</span></div>
          <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Nation QTD</span><span style="font-weight:600; color:#1a3a6b;">11.9%</span></div>
          <div style="font-size:13px; font-weight:700; color:#1a1a2e; border-bottom:1px solid #eee; padding-bottom:3px; margin:10px 0 4px 0;">Growth</div>
          <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Territory R13</span><span style="font-weight:600; color:#1a3a6b;">1.5%</span></div>
          <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Region R13</span><span style="font-weight:600; color:#1a3a6b;">1.5%</span></div>
          <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Nation R13</span><span style="font-weight:600; color:#1a3a6b;">1.5%</span></div>
          <div style="font-size:13px; font-weight:700; color:#1a1a2e; border-bottom:1px solid #eee; padding-bottom:3px; margin:10px 0 4px 0;">PEQ Adherence ⓘ</div>
          <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Territory R3M</span><span style="font-weight:600; color:#1a3a6b;">31.2%</span></div>
          <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Region R3M</span><span style="font-weight:600; color:#1a3a6b;">31.2%</span></div>
          <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Nation R3M</span><span style="font-weight:600; color:#1a3a6b;">31.2%</span></div>
        </div>
        """, unsafe_allow_html=True)

    # ── DATA TABLE ────────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    table_data = {
        "Nation":                  ["Nation", "East", "West", "South /Central", "Unassigned Region"],
        "Vials":                   [3850, 1550, 1174, 1126, ""],
        "Run Rate ⓘ":              [296.2, 119.2, 90.3, 86.6, ""],
        "Goals":                   [3800, 1537, 1136, 1127, ""],
        "Projected Quarter Sales": [3789, 1539, 1196, 1054, ""],
        "Projected Attainment ⓘ":  ["99.7%", "100.1%", "105.3%", "93.5%", ""],
        "C13W/P13W Growth%":       ["1.5%", "5.7%", "3.3%", "-5.4%", ""],
        "C26W/P26W Growth%":       ["1.0%", "1.4%", "-2.0%", "3.6%", ""],
        "C52W/P52W Growth%":       ["4.4%", "5.1%", "-1.2%", "9.7%", ""],
        "Avg HCP Calls/Day ⓘ":     [1.3, 1.1, 1.3, 1.1, 5.3],
        "HCPs Reached":            [1451, 384, 398, 378, 291],
        "Calls by Initiators":     [451, 153, 147, 142, 9],
        "Total Emails Sent":       [3778, 1141, 952, 1432, 253],
        "PEQ Call Adherence % ⓘ":  ["31.3%", "41.2%", "24.2%", "32.1%", "6.5%"],
    }
    df = pd.DataFrame(table_data)
    row_colors = ["#fff9e6", "#ffffff", "#fff9e6", "#ffe8b0", "#ffffff"]
    html = '<div style="background:white; border:1px solid #ddd; border-radius:6px; overflow-x:auto; padding:0;">'
    html += '<table style="width:100%; border-collapse:collapse; font-size:12px;">'
    for col in df.columns:
        html += f'<th style="background:#2c4a7c; color:white; font-weight:700; font-size:11px; text-align:center; padding:7px 5px; border:1px solid #4a6a9c; white-space:nowrap;">{col}</th>'
    html += '</tr>'
    for i, row in df.iterrows():
        bg = row_colors[i]
        html += f'<tr style="background:{bg}; color:black;">'
        for j, val in enumerate(row):
            align = "left" if j == 0 else "center"
            bold  = "font-weight:700;" if j == 0 else ""
            html += f'<td style="padding:6px 5px; border:1px solid #ddd; {bold} text-align:{align}; white-space:nowrap; color:black;">'
            if j == 0:
                html += f'<span style="color:#aaa; margin-right:4px;">□</span>{val}'
            else:
                html += str(val) if str(val) != "" else "&nbsp;"
            html += '</td>'
        html += '</tr>'
    html += '</table></div>'
    st.markdown(html, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — TRIGGERS / REPORTS
# ══════════════════════════════════════════════════════════════════════════════
else:
    # ── Mock report history data ──────────────────────────────────────────────
    reports = [
        {
            "week": "Week of Jul 7, 2025",
            "generated": "Jul 11, 2025",
            "region": "All Regions",
            "status": "New",
            "summary": "Nation vials hit 323 — highest in 13 weeks. East region continues to lead growth.",
            "insights": [
                ("positive", "✅ East region exceeded weekly vial goal by 8.3% (139 vs. 128 target)."),
                ("positive", "✅ Nation C13W/P13W growth held steady at +1.5% for the third consecutive week."),
                ("negative", "⚠️ South/Central PEQ Call Adherence dropped to 28.4% — below the 30% threshold."),
                ("negative", "⚠️ West region projected attainment fell to 101.2%, narrowing the buffer."),
                ("neutral",  "ℹ️ Unassigned Region avg HCP calls/day increased to 5.3 — monitor for territory assignment."),
            ],
            "top_performers": ["J. Smith (East) — 18 vials", "A. Torres (East) — 15 vials", "M. Lee (West) — 14 vials"],
            "action_items": ["Follow up with South/Central reps on PEQ adherence protocol.", "Review West territory goal calibration for Q3."],
        },
        {
            "week": "Week of Jun 30, 2025",
            "generated": "Jul 4, 2025",
            "region": "All Regions",
            "status": "Viewed",
            "summary": "Vial output dipped to 260 nationally. West and South/Central underperformed vs. prior week.",
            "insights": [
                ("negative", "⚠️ Nation weekly vials down 20% vs. prior week (260 vs. 325)."),
                ("negative", "⚠️ West C26W/P26W growth turned negative at -2.0%."),
                ("positive", "✅ East maintained strong HCP reach with 384 HCPs contacted."),
                ("neutral",  "ℹ️ Total emails sent nationally dropped by 12% — verify CRM sync."),
                ("positive", "✅ South/Central C52W/P52W growth remains strong at +9.7%."),
            ],
            "top_performers": ["R. Patel (South/Central) — 16 vials", "J. Smith (East) — 14 vials", "C. Brown (West) — 11 vials"],
            "action_items": ["Investigate West region growth decline — schedule regional call.", "Audit CRM email sync for missing records."],
        },
        {
            "week": "Week of Jun 23, 2025",
            "generated": "Jun 27, 2025",
            "region": "All Regions",
            "status": "Viewed",
            "summary": "Best performing week in Q2 — 325 vials nationally. Projected attainment at 99.7% on track.",
            "insights": [
                ("positive", "✅ Nation vials reached 325 — highest single-week output this quarter."),
                ("positive", "✅ East projected attainment at 100.1%, surpassing quarterly goal."),
                ("positive", "✅ West region rebounded with 101 vials after two consecutive down weeks."),
                ("neutral",  "ℹ️ PEQ Call Adherence nationally at 31.3% — marginally above 30% floor."),
                ("negative", "⚠️ South/Central run rate (86.6) remains the lowest across all regions."),
            ],
            "top_performers": ["A. Torres (East) — 19 vials", "M. Lee (West) — 17 vials", "K. Nguyen (East) — 16 vials"],
            "action_items": ["Recognize top East performers in weekly all-hands.", "Coach South/Central reps on run rate improvement strategies."],
        },
        {
            "week": "Week of Jun 16, 2025",
            "generated": "Jun 20, 2025",
            "region": "All Regions",
            "status": "Viewed",
            "summary": "Moderate week nationally at 285 vials. HCP reach remains strong across all regions.",
            "insights": [
                ("neutral",  "ℹ️ Nation vials at 285 — 4% below prior week but within seasonal expectations."),
                ("positive", "✅ HCPs Reached nationally at 1,451 — consistent with 13-week average."),
                ("negative", "⚠️ Calls by Initiators declined 6% week-over-week (451 vs. 479)."),
                ("positive", "✅ East C13W growth at 5.7% — strongest region for short-term growth."),
                ("neutral",  "ℹ️ South/Central email volume (1,432) highest of all regions — good digital engagement."),
            ],
            "top_performers": ["J. Smith (East) — 15 vials", "R. Patel (South/Central) — 14 vials", "D. Kim (West) — 13 vials"],
            "action_items": ["Analyze initiator call decline — identify reps below threshold.", "Share South/Central email best practices cross-regionally."],
        },
        {
            "week": "Week of Jun 9, 2025",
            "generated": "Jun 13, 2025",
            "region": "All Regions",
            "status": "Viewed",
            "summary": "Strong rebound week — 318 vials. East and West both outperformed weekly targets.",
            "insights": [
                ("positive", "✅ Nation vials at 318 — up 24% vs. prior week (257)."),
                ("positive", "✅ West region vials at 94 — highest in 6 weeks."),
                ("positive", "✅ Projected attainment for West climbed to 105.3% for the first time this quarter."),
                ("negative", "⚠️ South/Central PEQ adherence at 32.1% — only marginally above threshold."),
                ("neutral",  "ℹ️ Avg HCP Calls/Day nationally stable at 1.3."),
            ],
            "top_performers": ["M. Lee (West) — 20 vials", "A. Torres (East) — 17 vials", "J. Smith (East) — 16 vials"],
            "action_items": ["Replicate West region strategies in South/Central.", "Set stretch goals for East reps nearing quota ceiling."],
        },
        {
            "week": "Week of Jun 2, 2025",
            "generated": "Jun 6, 2025",
            "region": "All Regions",
            "status": "Viewed",
            "summary": "Slowest week of the quarter at 257 vials. Multiple regions flagged for follow-up.",
            "insights": [
                ("negative", "⚠️ Nation vials at 257 — lowest of the quarter, likely due to holiday impact."),
                ("negative", "⚠️ West region C26W growth turned negative at -2.0%."),
                ("negative", "⚠️ Calls by Initiators at 451 — declined for second consecutive week."),
                ("neutral",  "ℹ️ East maintained relative stability at 103 vials despite national dip."),
                ("positive", "✅ Email engagement remained high across all regions."),
            ],
            "top_performers": ["J. Smith (East) — 13 vials", "R. Patel (South/Central) — 12 vials", "C. Brown (West) — 10 vials"],
            "action_items": ["Account for holiday week in monthly reporting.", "Schedule call with West regional manager to address growth trend."],
        },
    ]

    # ── Page Header ───────────────────────────────────────────────────────────
    hdr_col, btn_col = st.columns([4, 1])
    with hdr_col:
        st.markdown('<div class="section-header">📋 Triggers / Reports — Weekly Archive</div>', unsafe_allow_html=True)
    with btn_col:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("＋ Generate & Send Report", type="primary", use_container_width=True)

    # ── How it works banner ───────────────────────────────────────────────────
    st.markdown("""
    <div style="background:#e8f0fb; border:1px solid #b3c8f0; border-radius:8px; padding:12px 18px; margin-bottom:16px; font-size:13px; color:#1a3a6b;">
        <b>🔄 Automated Weekly Workflow:</b> &nbsp; Every <b>Monday morning</b>, a new Triggers/Report is automatically 
        generated from the latest sales data and <b>emailed directly to all Sales Managers</b>. 
        It is then archived here for reference. All historical reports are stored below.
    </div>
    """, unsafe_allow_html=True)

    # ── Next send info ────────────────────────────────────────────────────────
    nc1, nc2, nc3 = st.columns(3)
    with nc1:
        st.markdown("""
        <div style="background:white; border:1px solid #ddd; border-radius:8px; padding:12px 16px; text-align:center;">
            <div style="font-size:11px; color:#888; text-transform:uppercase; letter-spacing:1px;">Next Scheduled Send</div>
            <div style="font-size:18px; font-weight:700; color:#1a3a6b; margin-top:4px;">Mon, Jul 20, 2026</div>
            <div style="font-size:12px; color:#666;">8:00 AM EST</div>
        </div>
        """, unsafe_allow_html=True)
    with nc2:
        st.markdown("""
        <div style="background:white; border:1px solid #ddd; border-radius:8px; padding:12px 16px; text-align:center;">
            <div style="font-size:11px; color:#888; text-transform:uppercase; letter-spacing:1px;">Recipients</div>
            <div style="font-size:18px; font-weight:700; color:#1a3a6b; margin-top:4px;">3 RDs</div>
            <div style="font-size:12px; color:#666;">All Regions</div>
        </div>
        """, unsafe_allow_html=True)
    with nc3:
        st.markdown("""
        <div style="background:white; border:1px solid #ddd; border-radius:8px; padding:12px 16px; text-align:center;">
            <div style="font-size:11px; color:#888; text-transform:uppercase; letter-spacing:1px;">Total Reports Sent</div>
            <div style="font-size:18px; font-weight:700; color:#1a3a6b; margin-top:4px;">6 Reports</div>
            <div style="font-size:12px; color:#666;">Since Apr 18, 2026</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # ── Filters ───────────────────────────────────────────────────────────────
    fc1, fc2, fc3, _ = st.columns([1.5, 1.5, 1.5, 2])
    with fc1:
        st.selectbox("Filter by Region", ["All Regions", "East", "West", "South/Central"])
    with fc2:
        st.selectbox("Filter by Status", ["All", "New", "Viewed"])
    with fc3:
        st.selectbox("Sort by", ["Newest First", "Oldest First"])

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Email metadata per report (dummy) ─────────────────────────────────────
    email_meta = [
        {"sent": "Jul 11, 2025 · 8:02 AM EST", "delivered": 12, "opened": 9,  "open_rate": "75%"},
        {"sent": "Jul 4, 2025 · 8:01 AM EST",  "delivered": 12, "opened": 11, "open_rate": "92%"},
        {"sent": "Jun 27, 2025 · 8:00 AM EST", "delivered": 12, "opened": 12, "open_rate": "100%"},
        {"sent": "Jun 20, 2025 · 8:03 AM EST", "delivered": 12, "opened": 10, "open_rate": "83%"},
        {"sent": "Jun 13, 2025 · 8:00 AM EST", "delivered": 12, "opened": 8,  "open_rate": "67%"},
        {"sent": "Jun 6, 2025 · 8:01 AM EST",  "delivered": 12, "opened": 7,  "open_rate": "58%"},
    ]

    # ── Report Cards ──────────────────────────────────────────────────────────
    for i, r in enumerate(reports):
        is_new = r["status"] == "New"
        em     = email_meta[i]
        icon   = "🔔" if is_new else "📄"
        label  = f"{icon}  {r['week']}  |  {r['region']}  |  📧 Emailed: {em['sent']}"

        with st.expander(label, expanded=is_new):

            # ── Email delivery status bar ──────────────────────────────────
            st.markdown(f"""
            <div style="background:#f0f7ff; border:1px solid #c0d8f5; border-radius:6px; padding:10px 16px; margin-bottom:12px; font-size:12px; display:flex; gap:32px; align-items:center;">
                <span>📧 <b>Email sent:</b> {em['sent']}</span>
                <span>✅ <b>Delivered:</b> {em['delivered']} / 12 managers</span>
                <span>👁️ <b>Opened:</b> {em['opened']} &nbsp;(<b style="color:#2e7d32">{em['open_rate']}</b>)</span>
                <span style="margin-left:auto; background:#2e7d32; color:white; padding:2px 10px; border-radius:10px; font-weight:700;">✔ Email Delivered</span>
            </div>
            """, unsafe_allow_html=True)

            col_left, col_right = st.columns([2, 1])

            with col_left:
                st.markdown(f"**Summary:** {r['summary']}")
                st.markdown("**Key Insights:**")
                for kind, text in r["insights"]:
                    color = "#f2fff3" if kind == "positive" else ("#ffe6e6" if kind == "negative" else "#e6ffff")
                    st.markdown(f'<p style="font-size:13px; color:{color}; margin:3px 0;">{text}</p>', unsafe_allow_html=True)

            with col_right:
                st.markdown("**🏆 Top Performers This Week:**")
                for p in r["top_performers"]:
                    st.markdown(f'<p style="font-size:13px; color:#ffffff; margin:2px 0;">• {p}</p>', unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown("**📌 Action Items:**")
                for a in r["action_items"]:
                    st.markdown(f'<p style="font-size:13px; color:#ffffff; margin:2px 0;">→ {a}</p>', unsafe_allow_html=True)

            st.markdown("---")
            dl1, dl2, dl3 = st.columns([1.2, 1.2, 4])
            with dl1:
                st.button("📥 Export PDF", key=f"pdf_{i}")
            with dl2:
                st.button("📧 Resend Email", key=f"email_{i}")

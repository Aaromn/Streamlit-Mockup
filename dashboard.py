import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ── FILTER BAR ────────────────────────────────────────────────────────────
f1, f2, f3, f4, f5, f6, f7 = st.columns([1.2, 1.2, 1, 1, 1, 0.7, 0.7])
with f1: st.selectbox("Time Period ⓘ", ["R13W", "R26W", "R52W", "QTD"])
with f2: st.text_input("Custom Date ⓘ", placeholder="Start – End")
with f3: st.selectbox("Region", ["All", "Alpha", "Beta", "Gamma"])
with f4: st.selectbox("Territory", ["All", "Territory A", "Territory B"])
with f5: st.selectbox("State", ["All", "State X", "State Y", "State Z"])
with f6:
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("Units", type="primary", use_container_width=True)
with f7:
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("Calls", use_container_width=True)

# ── CHART DATA (scrambled) ────────────────────────────────────────────────
weeks = ["04/18","04/25","05/02","05/09","05/16","05/23","05/30",
            "06/06","06/13","06/20","06/27","07/04","07/11"]

alpha   = [112, 95, 130, 108, 125, 117, 99, 121, 134, 110, 140, 103, 127]
gamma   = [78,  91, 85,  94,  102, 88,  80, 73,  90,  82,  76,  80,  88 ]
unassig = [0,   0,  0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0  ]
beta    = [92,  80, 99,  104, 88,  95,  85, 79,  98,  86,  105, 89,  95 ]
totals  = [282, 266, 314, 306, 315, 300, 264, 273, 322, 278, 321, 272, 310]

fig = go.Figure()
fig.add_trace(go.Bar(name="Alpha",            x=weeks, y=alpha,   marker_color="#1a3a6b", text=alpha,   textposition="inside", textfont=dict(color="white", size=10)))
fig.add_trace(go.Bar(name="Gamma",            x=weeks, y=gamma,   marker_color="#2e6db4", text=gamma,   textposition="inside", textfont=dict(color="white", size=10)))
fig.add_trace(go.Bar(name="Unassigned Region",x=weeks, y=unassig, marker_color="#f5c842"))
fig.add_trace(go.Bar(name="Beta",             x=weeks, y=beta,    marker_color="#b0bec5", text=beta,    textposition="inside", textfont=dict(color="#333",   size=10)))
fig.add_trace(go.Scatter(x=weeks, y=[t + 14 for t in totals], mode="text", text=totals, textfont=dict(size=11, color="#222"), showlegend=False))
fig.update_layout(
    barmode="stack",
    title=dict(text="Units by Region", x=0.42, font=dict(size=15, color="#1a1a2e")),
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
        <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Territory QTD</span><span style="font-weight:600; color:#1a3a6b;">14.2%</span></div>
        <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Region QTD</span><span style="font-weight:600; color:#1a3a6b;">13.7%</span></div>
        <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Nation QTD</span><span style="font-weight:600; color:#1a3a6b;">12.9%</span></div>
        <div style="font-size:13px; font-weight:700; color:#1a1a2e; border-bottom:1px solid #eee; padding-bottom:3px; margin:10px 0 4px 0;">Growth</div>
        <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Territory R13</span><span style="font-weight:600; color:#1a3a6b;">2.1%</span></div>
        <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Region R13</span><span style="font-weight:600; color:#1a3a6b;">1.8%</span></div>
        <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Nation R13</span><span style="font-weight:600; color:#1a3a6b;">1.6%</span></div>
        <div style="font-size:13px; font-weight:700; color:#1a1a2e; border-bottom:1px solid #eee; padding-bottom:3px; margin:10px 0 4px 0;">PEQ Adherence ⓘ</div>
        <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Territory R3M</span><span style="font-weight:600; color:#1a3a6b;">33.5%</span></div>
        <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Region R3M</span><span style="font-weight:600; color:#1a3a6b;">34.1%</span></div>
        <div style="display:flex; justify-content:space-between; font-size:13px; padding:2px 0;"><span>Nation R3M</span><span style="font-weight:600; color:#1a3a6b;">32.8%</span></div>
    </div>
    """, unsafe_allow_html=True)

# ── DATA TABLE (scrambled) ────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
table_data = {
    "Region":                  ["Nation", "Alpha", "Beta", "Gamma", "Unassigned Region"],
    "Units":                   [4120, 1680, 1254, 1186, ""],
    "Run Rate ⓘ":              [317.0, 129.2, 96.5, 91.3, ""],
    "Goals":                   [4050, 1620, 1210, 1220, ""],
    "Projected Quarter Sales": [4031, 1645, 1278, 1108, ""],
    "Projected Attainment ⓘ":  ["99.5%", "101.5%", "105.6%", "90.8%", ""],
    "C13W/P13W Growth%":       ["2.1%", "6.3%", "3.8%", "-4.9%", ""],
    "C26W/P26W Growth%":       ["1.3%", "1.9%", "-1.7%", "4.2%", ""],
    "C52W/P52W Growth%":       ["4.8%", "5.5%", "-0.9%", "10.3%", ""],
    "Avg HCP Calls/Day ⓘ":     [1.4, 1.2, 1.4, 1.2, 5.7],
    "HCPs Reached":            [1532, 412, 421, 399, 307],
    "Calls by Initiators":     [478, 162, 155, 151, 11],
    "Total Emails Sent":       [3994, 1208, 1014, 1512, 270],
    "PEQ Call Adherence % ⓘ":  ["33.5%", "43.1%", "25.6%", "33.8%", "7.2%"],
}
df = pd.DataFrame(table_data)
row_colors = ["#fff9e6", "#ffffff", "#fff9e6", "#ffe8b0", "#ffffff"]

html = '<div style="background:white; border:1px solid #ddd; border-radius:6px; overflow-x:auto; padding:0;">'
html += '<table style="width:100%; border-collapse:collapse; font-size:12px;"><tr>'
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
        html += (f'<span style="color:#aaa; margin-right:4px;">□</span>{val}' if j == 0 else (str(val) if str(val) != "" else "&nbsp;"))
        html += '</td>'
    html += '</tr>'
html += '</table></div>'
st.markdown(html, unsafe_allow_html=True)
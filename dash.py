import streamlit as st

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
.report-card { background: white; border: 1px solid #ddd; border-radius: 8px; padding: 16px 20px; margin-bottom: 12px; border-left: 5px solid #2c4a7c; }
.report-card-new { border-left: 5px solid #e8a000; }
.report-title { font-size: 15px; font-weight: 700; color: #1a3a6b; margin-bottom: 4px; }
.report-meta { font-size: 12px; color: #666; margin-bottom: 10px; }
.badge-new { background: #e8a000; color: white; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-left: 8px; }
.badge-viewed { background: #aaa; color: white; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-left: 8px; }
.section-header { font-size: 20px; font-weight: 700; color: #1a3a6b; border-bottom: 2px solid #2c4a7c; padding-bottom: 6px; margin-bottom: 16px; }
</style>
""", unsafe_allow_html=True)


# Define the pages
dashboard = st.Page("dashboard.py", title="Dashboard", icon="🎯")
reports = st.Page("reports.py", title="Reports", icon="🚨")
playground = st.Page("playground.py", title="Playground", icon="🛝")
dashboardRD = st.Page("dashboardRD.py", title="RD Dashboard", icon="🗿")
dashboardOAM = st.Page("dashboardOAM.py", title="OAM Dashboard", icon="🕴")

# Set up navigation
pg = st.navigation([dashboard, reports, playground, dashboardRD, dashboardOAM])

# Run the selected page
pg.run()

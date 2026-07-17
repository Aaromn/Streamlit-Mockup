import streamlit as st
from utils import load_css


load_css()

st.set_page_config(layout="wide", page_title="Sales Dashboard")




# Define the pages
dashboard = st.Page("dashboard.py", title="Dashboard", icon="🎯")
reports = st.Page("reports.py", title="Reports", icon="🚨")
playground = st.Page("playground.py", title="Playground", icon="🛝")
dashboardRD = st.Page("rd.py", title="RD Dashboard", icon="🗿")
dashboardOAM = st.Page("oam.py", title="OAM Dashboard", icon="💼")

# Set up navigation
pg = st.navigation([dashboard, reports, dashboardRD, dashboardOAM])

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
def create_territories():
    territories = []
    selected_regions = st.session_state.get("selected_regions", [])

    if "East" in selected_regions:
        territories.extend(["East PA/Maryland", "Indiana/Kentucky", "Michigan", "New England", "NYC", "Ohio", "Upstate NY/West PA",])

    if "South/Central" in selected_regions:
        territories.extend(["Central Florida", "Georgia", "Gulf Coast", "Mid-America", "North Texas", "South Florida",])

    if "West" in selected_regions:
        territories.extend(["Great Plains", "Midwest", "Mountain", "NorCal", "Northwest", "SoCal", "Southwest",])

    return territories

with st.sidebar:
    st.multiselect(
        "Select Regions",
        ["East", "South/Central", "West"],
        key="selected_regions",
        placeholder="Select",
        default=None,
    )
    st.markdown("---")
    st.multiselect(
        "Select Territory",
        create_territories(),
        key="selected_territories",
        placeholder="Select",
        default=None,
    )




# Run the selected page
pg.run()

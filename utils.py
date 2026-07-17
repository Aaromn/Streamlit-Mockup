# utils.py
import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    .widget-card {
        background: white;
        border: 1px solid #dde3ed;
        border-radius: 10px;
        padding: 18px 20px;
        margin-bottom: 18px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .widget-title {
        font-size: 14px;
        font-weight: 700;
        color: #1a3a6b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .widget-subtitle {
        font-size: 11px;
        color: #888;
        font-weight: 400;
        text-transform: none;
        letter-spacing: 0;
    }
    .metric-big {
        font-size: 28px;
        font-weight: 800;
        color: #1a3a6b;
        margin: 4px 0;
    }
    .metric-label {
        font-size: 11px;
        color: #888;
        margin-bottom: 2px;
    }
    .status-ok    { color: #2e7d32; font-weight: 700; font-size: 12px; }
    .status-warn  { color: #e65100; font-weight: 700; font-size: 12px; }
    .status-bad   { color: #c62828; font-weight: 700; font-size: 12px; }
    .pill-ok   { background:#e8f5e9; color:#2e7d32; border-radius:10px; padding:2px 10px; font-size:11px; font-weight:700; }
    .pill-warn { background:#fff3e0; color:#e65100; border-radius:10px; padding:2px 10px; font-size:11px; font-weight:700; }
    .pill-bad  { background:#ffebee; color:#c62828; border-radius:10px; padding:2px 10px; font-size:11px; font-weight:700; }
    .pill-grey { background:#f0f0f0; color:#555;    border-radius:10px; padding:2px 10px; font-size:11px; font-weight:700; }
    .divider { border:none; border-top:1px solid #eee; margin:10px 0; }
    .future-badge {
        background: #ede7f6;
        color: #4527a0;
        border: 1px dashed #7c4dff;
        border-radius: 8px;
        padding: 14px 18px;
        font-size: 13px;
        text-align: center;
    }
    [data-testid="stSidebar"] { background-color: #1a3a6b; }
    [data-testid="stSidebar"] * { color: white !important; }
    </style>
    """, unsafe_allow_html=True)
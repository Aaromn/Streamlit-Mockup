import streamlit as st

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

selected_regions = st.session_state.get("selected_regions", [])
region_label = ", ".join(selected_regions) if selected_regions else "No Regions"

selected_territories = st.session_state.get("selected_territories", [])
territories_label = ", ".join(selected_territories) if selected_territories else "No Territories"


with hdr_col:
    st.markdown('<div class="section-header">📋 Triggers / Reports — Weekly Archive — </div>', unsafe_allow_html=True)
    st.markdown(f'<div>{region_label}</div>', unsafe_allow_html=True)
    st.markdown(f'<div>{territories_label}</div>', unsafe_allow_html=True)
    
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
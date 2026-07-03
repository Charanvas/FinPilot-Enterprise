import streamlit as st
import requests
import plotly.express as px
import pandas as pd

API_URL = "http://127.0.0.1:8000"


def dashboard_page():

    st.title("💰 FinPilot Enterprise")
    st.caption("AI Financial Operations Platform")

    analytics = requests.get(f"{API_URL}/analytics")

    if analytics.status_code != 200:
        st.error("Unable to load analytics.")
        return

    stats = analytics.json()

    # ======================================
    # KPI Cards
    # ======================================

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "💰 Money Audited",
        f"₹{stats['money_audited']:,.2f}"
    )

    c2.metric(
        "📄 Highest Invoice",
        f"₹{stats['highest_invoice']:,.2f}"
    )

    c3.metric(
        "📊 Average Invoice",
        f"₹{stats['average_invoice']:,.2f}"
    )

    st.divider()

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "🏢 Vendors",
        stats["vendors"]
    )

    c5.metric(
        "🎫 Tickets",
        stats["tickets_raised"]
    )

    c6.metric(
        "✅ Auto Correct %",
        f"{stats['success_rate']}%"
    )

    # ======================================
    # Charts
    # ======================================

    left, right = st.columns([2,1])

    with left:

        response = requests.get(f"{API_URL}/invoices")

        if response.status_code == 200:

            invoices = response.json()

            if invoices:

                df = pd.DataFrame(invoices)

                if "created_at" in df.columns:

                    df["created_at"] = pd.to_datetime(df["created_at"])

                    trend = (
                        df.groupby(df["created_at"].dt.date)
                        .size()
                        .reset_index(name="Invoices")
                    )

                    fig = px.line(
                        trend,
                        x="created_at",
                        y="Invoices",
                        markers=True,
                        title="Invoice Trend"
                    )

                    fig.update_layout(
                        template="plotly_white",
                        height=400,
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

    with right:

        fig = px.pie(

            names=[
                "Auto Correct",
                "Tickets"
            ],

            values=[
                stats["auto_corrected"],
                stats["tickets_raised"]
            ],

            hole=0.6,

            title="Decision Distribution"

        )

        fig.update_layout(
            template="plotly_white",
            height=400,
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # ======================================
    # Recent Invoices
    # ======================================

    st.subheader("📄 Recent Invoices")

    response = requests.get(f"{API_URL}/invoices")

    if response.status_code == 200:

        st.dataframe(
            response.json(),
            use_container_width=True,
            hide_index=True,
        )

    st.divider()

    # ======================================
    # AI Summary
    # ======================================

    st.subheader("🤖 AI Summary")

    st.success(
        f"""
Invoices Processed : {stats["total_invoices"]}

Auto Corrected : {stats["auto_corrected"]}

Tickets Raised : {stats["tickets_raised"]}

System is operating normally.
"""
    )
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://127.0.0.1:8000"


def audit_logs_page():

    st.title("📈 Analytics")

    response = requests.get(f"{API_URL}/invoices")

    if response.status_code != 200:
        st.error("Unable to load invoices.")
        return

    invoices = response.json()

    if not invoices:
        st.info("No invoices found.")
        return

    df = pd.DataFrame(invoices)

    # ==============================
    # KPI Cards
    # ==============================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Invoices",
        len(df)
    )

    c2.metric(
        "Money Audited",
        f"₹{df['invoice_total'].sum():,.2f}"
    )

    c3.metric(
        "Average Invoice",
        f"₹{df['invoice_total'].mean():,.2f}"
    )

    c4.metric(
        "Vendors",
        df["vendor_name"].nunique()
    )

    st.divider()

    # ==============================
    # Charts
    # ==============================

    left, right = st.columns(2)

    with left:

        vendor_df = (
            df.groupby("vendor_name")["invoice_total"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            vendor_df,
            x="vendor_name",
            y="invoice_total",
            color="invoice_total",
            title="Vendor Spending"
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        fig = px.pie(
            df,
            names="status",
            title="Invoice Decisions",
            hole=0.55,
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # ==============================
    # Invoice Table
    # ==============================

    st.subheader("📄 Invoice Database")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )
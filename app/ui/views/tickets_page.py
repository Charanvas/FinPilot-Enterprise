import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"


def tickets_page():

    st.title("🎫 Ticket Center")
    st.caption("Monitor invoices requiring manual review")

    response = requests.get(f"{API_URL}/tickets")

    if response.status_code != 200:
        st.error("Unable to load tickets.")
        return

    tickets = response.json()

    if not tickets:
        st.success("🎉 No Open Tickets")
        return

    df = pd.DataFrame(tickets)

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Open Tickets",
        len(df)
    )

    c2.metric(
        "Critical",
        len(df)
    )

    c3.metric(
        "Resolved",
        0
    )

    st.divider()

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )
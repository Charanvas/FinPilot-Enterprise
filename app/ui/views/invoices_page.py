import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"


def invoices_page():

    st.title("📄 Invoice Center")
    st.caption("Upload • Audit • Track • Search")

    st.divider()

    # ==========================================
    # Upload Section
    # ==========================================

    col1, col2 = st.columns([2, 1])

    with col1:

        uploaded_file = st.file_uploader(
            "Upload Invoice",
            type=["pdf", "png", "jpg", "jpeg"],
        )

    with col2:

        expected_amount = st.number_input(
            "Expected Amount",
            min_value=0.0,
            value=400.0,
        )

    if st.button(
        "🚀 Audit Invoice",
        use_container_width=True,
    ):

        if uploaded_file is None:

            st.warning("Please upload an invoice.")

            return

        with st.spinner("Analyzing Invoice..."):

            response = requests.post(
                f"{API_URL}/audit",
                files={
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type,
                    )
                },
                data={
                    "expected_amount": expected_amount
                },
            )

        if response.status_code != 200:

            st.error(response.text)

            return

        result = response.json()

        st.success("✅ Invoice Processed Successfully")

        invoice = result["invoice"]
        decision = result["decision"]

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Vendor",
            invoice["vendor_name"],
        )

        c2.metric(
            "Invoice",
            invoice["invoice_number"],
        )

        c3.metric(
            "Amount",
            f"₹{invoice['invoice_total']}",
        )

        st.divider()

        st.subheader("🤖 AI Decision")

        if result["action"] == "AUTO_CORRECT":

            st.success("🟢 AUTO CORRECT")

        elif result["action"] == "RAISE_TICKET":

            st.error("🔴 TICKET RAISED")

        else:

            st.warning("🟡 HUMAN REVIEW")

        st.info(decision["reason"])

    st.divider()

    # ==========================================
    # Invoice History
    # ==========================================

    st.subheader("📜 Invoice History")

    response = requests.get(
        f"{API_URL}/invoices"
    )

    if response.status_code != 200:

        st.error("Unable to load invoices.")

        return

    invoices = response.json()

    if not invoices:

        st.info("No invoices available.")

        return

    df = pd.DataFrame(invoices)

    # ==========================================
    # Search
    # ==========================================

    search = st.text_input(
        "🔍 Search Invoice Number or Vendor"
    )

    if search:

        df = df[
            df["invoice_number"]
            .astype(str)
            .str.contains(
                search,
                case=False,
                na=False,
            )
            |
            df["vendor_name"]
            .astype(str)
            .str.contains(
                search,
                case=False,
                na=False,
            )
        ]

    # ==========================================
    # Status Icons
    # ==========================================

    if "status" in df.columns:

        def status_badge(status):

            if status == "AUTO_CORRECT":
                return "🟢 AUTO CORRECT"

            elif status == "RAISE_TICKET":
                return "🔴 TICKET"

            return "🟡 REVIEW"

        df["status"] = df["status"].apply(status_badge)

    # ==========================================
    # Download CSV
    # ==========================================

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download CSV",
        csv,
        "invoice_history.csv",
        "text/csv",
        use_container_width=True,
    )

    # ==========================================
    # Table
    # ==========================================

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )
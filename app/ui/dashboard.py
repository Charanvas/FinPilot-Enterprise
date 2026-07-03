import streamlit as st

from app.ui.components.sidebar import sidebar

from app.ui.views.dashboard_page import dashboard_page
from app.ui.views.invoices_page import invoices_page
from app.ui.views.tickets_page import tickets_page
from app.ui.views.audit_logs_page import audit_logs_page
from app.ui.views.about_page import about_page

st.set_page_config(
    page_title="FinPilot Enterprise",
    page_icon="💰",
    layout="wide",
)

page = sidebar()

if page == "🏠 Dashboard":

    dashboard_page()

elif page == "📄 Invoice Center":

    invoices_page()

elif page == "🎫 Tickets":

    tickets_page()

elif page == "📈 Analytics":

    audit_logs_page()

elif page == "⚙ Settings":

    about_page()

else:

    st.title("🚧 Coming Soon")

    st.info(
        "This module will be added in Phase 2."
    )
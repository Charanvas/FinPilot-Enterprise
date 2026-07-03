import streamlit as st


def metric_card(icon, title, value, footer):

    html = f"""
    <div class="metric-card">

        <div class="metric-icon">
            {icon}
        </div>

        <div class="metric-title">
            {title}
        </div>

        <div class="metric-value">
            {value}
        </div>

        <div class="metric-footer">
            {footer}
        </div>

    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True,
    )
import streamlit as st


def sidebar():

    st.sidebar.image(
        "https://img.icons8.com/fluency/96/money-bag.png",
        width=70,
    )

    st.sidebar.title("FinPilot")

    st.sidebar.caption(
        "Enterprise Edition"
    )

    st.sidebar.divider()

    page = st.sidebar.radio(

        "",

        [

            "🏠 Dashboard",

            "📄 Invoice Center",

            "📦 Purchase Orders",

            "🏢 Vendors",

            "🎫 Tickets",

            "📈 Analytics",

            "🤖 AI Copilot",

            "⚙ Settings",

        ],

    )

    st.sidebar.divider()

    st.sidebar.success(
        "Gemini Connected"
    )

    return page
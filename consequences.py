import streamlit as st

st.markdown("""
<style>
.node-box {
    width: 220px;
    padding: 0;
    margin: 12px auto;
    text-align: center;
    font-weight: 600;
    font-family: Arial, sans-serif;

    border-radius: 10px;
    border: 2px solid #b50000;
    background: linear-gradient(to bottom, #ff6666, #cc0000);
    box-shadow: 0 0 4px rgba(0,0,0,0.25);

    display: flex;
    flex-direction: column;
    overflow: hidden;
}

.node-inner {
    background: white;
    padding: 16px 12px;
    font-size: 16px;
}

.node-squares {
    display: flex;
    justify-content: center;
    padding: 8px 0;
    gap: 4px;
}

.node-square {
    width: 24px;
    height: 24px;
    background: #f2f2f2;
    border: 1px solid #c0c0c0;
    border-radius: 3px;
}
</style>
""", unsafe_allow_html=True)

consequences = [
    "Rear-end or multi-vehicle collision",
    "Vehicle roll-over",
    "Injury to driver or others"
]

for c in consequences:
    st.markdown(
        f"""
        <div class='node-box'>
            <div class='node-inner'>{c}</div>
            <div class='node-squares'>
                <div class='node-square'></div>
                <div class='node-square'></div>
                <div class='node-square'></div>
                <div class='node-square'></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

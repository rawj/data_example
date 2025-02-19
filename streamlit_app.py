import streamlit as st
import pandas as pd

# Streamlit-sovelluksen otsikko
st.title("Dataesityssovellus")

# Esimerkkidata
data = {
    "Nimi": ["Tuote A", "Tuote B", "Tuote C"],
    "Hinta (€)": [25, 40, 30],
    "Varasto": [100, 50, 75]
}
df = pd.DataFrame(data)

# Näytetään data taulukkona
st.subheader("Tuotetiedot")
st.dataframe(df, use_container_width=True)

# Ohje Frameriin upottamiseen
st.subheader("Upottaminen Frameriin")
iframe_code = """
<iframe src='YOUR_STREAMLIT_APP_URL' width='600' height='400' style='border:none;'></iframe>
"""
st.code(iframe_code, language="html")

st.markdown("Korvaa **YOUR_STREAMLIT_APP_URL** omalla Streamlit-palvelimesi URL-osoitteella.")

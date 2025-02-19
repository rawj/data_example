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

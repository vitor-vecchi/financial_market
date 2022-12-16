import streamlit as st

st.set_page_config(
    page_title="Página Principal",
    page_icon="📈",
)

st.markdown("# Página Principal")
st.image('logo.png', caption=None, width=800, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.write(
    """Este programa foi escrito em Python e visa facilitar a análise
    de ações listadas na B3, bem como comparar títulos de renda fixa.
    O desenvolvimento deste aplicativo teve por inspiração principais
    as ideias de Joel Greenblatt insculpidas no livro "The Little Book
    That Beats the Market", em suas ideias e análises históricas com a
    a utilizaçao do Earnings Yield do Ebit e Return on Employed Capital,
    como medidas exaustivamente testadas e que apresentaram excelentes
    resultados ao longo do tempo na seleção de bons ativos a preços 
    justos. As análises de risco se baseiam numa perspectiva básica do 
    risco, que utiliza beta como referência, com vistas a inaugurar a 
    construção de um Modelo de Precificação e Ativos Financeiros (CAPM)."""
)
st.write("\n")

st.write("""Agradecimentos especiais a Ran Aroussi pelo trabalho fantástico
    no desenvolvimento do pacote yfinance, que permite a extração de dados
    de ações listadas na B3. Também agradeço a todos os desenvolvedores
    do Streamlit, especialmente Thiago Teixeira (tvst) e Adrien Treuille, 
    que tornaram possível a criação deste aplicativo."""
)

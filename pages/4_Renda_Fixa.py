import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import datetime
from datetime import timedelta
from datetime import date
import streamlit as st

def main():
    st.image('logo.png', caption=None, width=600, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    aplicacao = st.sidebar.selectbox("Selecione a aplicação", ['Página Principal', 'Renda Fixa'])
    if aplicacao == 'Página Principal':
        st.title('Renda Fixa')
        st.markdown('Este aplicativo foi desenvolvido com a finalidade de simplificar a comparação da rentabilidade de ativos de renda fixa.')
    
    def rf():
        ativo = st.selectbox(
        'Selecione o ativo:',
        ( 'CDB', 'LCI/LCA'))
        if ativo == 'CDB':
            taxa = float(st.number_input("Digite a taxa de juros: "))
            vencimento = st.date_input("Selecione a data de vencimento: ")
            st.write("A data de vencimento escolhida é", vencimento)
            hoje = datetime.date.today()
            prazo = (vencimento - hoje).days
            st.write("O ativo será resgatado em ", prazo, " dias")
            if prazo >= 721:
                liq4 = taxa - (0.15 * taxa)
                st.write("A taxa de juros líquida é ", liq4,"%")
            if prazo >= 361 and prazo <= 720:
                liq3 = taxa - (0.175 * taxa)
                st.write("A taxa de juros líquida é ", liq3,"%")
            if prazo >= 181 and prazo <= 360:
                liq2 = taxa - (0.20 * taxa)
                st.write("A taxa de juros líquida é ", liq2,"%")
            if prazo > 0 and prazo <= 180:
                liq1 = taxa - (0.225 * taxa)
                st.write("A taxa de juros líquida é ", liq1,"%")
        if ativo == 'LCI/LCA':
            taxa_lc = float(st.number_input("Digite a taxa de juros: (%)"))
            vencimento = st.date_input("Selecione a data de vencimento: ")
            st.write("A data de vencimento escolhida é", vencimento)
            hoje = datetime.date.today()
            prazo = (vencimento - hoje).days
            st.write("O ativo será resgatado em ", prazo, " dias")
            if prazo >= 721:
                tx_percent_lc = taxa_lc / 100
                liq4 = tx_percent_lc / 0.85
                st.write("O ativo é equivalente a um CDB de ", liq4 * 100,"%")
            if prazo >= 361 and prazo <= 720:
                tx_percent_lc = taxa_lc / 100
                liq3 = tx_percent_lc / 0.825
                st.write("O ativo é equivalente a um CDB de ", liq3 * 100,"%")
            if prazo >= 181 and prazo <= 360:
                tx_percent_lc = taxa_lc / 100
                liq2 = tx_percent_lc / 0.8
                st.write("O ativo é equivalente a um CDB de ", liq2 * 100,"%")
            if prazo > 0 and prazo <= 180:
                tx_percent_lc = taxa_lc / 100
                liq1 = tx_percent_lc / 0.775
                st.write("O ativo é equivalente a um CDB de ", liq1 * 100,"%")
    if aplicacao == 'Renda Fixa':
        rf()
main()
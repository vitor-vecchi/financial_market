import streamlit as st
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd

st.title('Análise Fundamentalista de Ações')
st.subheader('Indicadores relevantes')

def main():
    stock = st.text_input('Informe o ticker da ação:', '')
    global stock_yf
    stock_yf = yf.Ticker(stock)
    
    if st.button('Enviar'):
        def calc():
            bs = stock_yf.balance_sheet
            long_term_Debt = bs.loc['Long Term Debt', '2021-12-31']
            fin = stock_yf.income_stmt
            ebit = fin.loc['EBIT']
            st.write(ebit)
            ebit_avg = ebit.mean()
            st.write("EBIT Médio - últimos 4 anos:", ebit_avg)
            st.write("\n")

            inf = stock_yf.info
            shares_Outs = float((inf['sharesOutstanding']))
            price = float((inf['regularMarketPrice']))
            est_fwd_EPS = float((inf['forwardEps']))
            est_earnings_Yield = (est_fwd_EPS / price) * 100
            earnings_yield_Ebit = ((ebit_avg / (shares_Outs * price)) * 100)
            est_price_to_Earnings = (price / est_fwd_EPS)

            st.write("Earnings Yield do EBIT:", "%.3f" % earnings_yield_Ebit + "%")
            st.write("LPA Estimado para 12 meses:", est_fwd_EPS)
            st.write("Earnings Yield Estimado:", "%.3f" % est_earnings_Yield + "%")
            st.write("PE Estimado:", "%.3f" % est_price_to_Earnings + "x")
            st.write("\n")

            # bs = stock_yf.balance_sheet
            total_Assets = bs.loc['Total Assets', '2021-12-31']
            current_Liabilities = bs.loc['Current Liabilities', '2021-12-31']

            roce = ((ebit_avg / (total_Assets - current_Liabilities)) * 100)
            net_assets = (total_Assets - current_Liabilities)

            st.write("Retorno sobre o Capital Empregado:", "%.3f" % roce + "%")
            st.write("Ativos Líquidos excl. Passivo Circulante:", net_assets)

            stockholders_Equity = bs.loc['Stockholders Equity', '2021-12-31']

            st.write("Patrimônio Líquido do Acionista:", stockholders_Equity)

            # long_term_Debt = bs.loc['Long Term Debt', '2021-12-31']

            st.write("Dívida de Longo Prazo:", long_term_Debt)

            alt_roce = ((ebit_avg / (stockholders_Equity - long_term_Debt)) * 100)
            net_equity = (stockholders_Equity - long_term_Debt)
            st.write("Retorno sobre o Capital Empregado - Alternativo:", "%.3f" % alt_roce + "%")

            st.write("Patrimônio excl. Dívida de Longo Prazo:", net_equity)
        calc()
main()
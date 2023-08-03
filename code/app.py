import streamlit as st
import pandas as pd

def aplicar_filtros(df, caracteristicas_filtro):
    return df[df['caracteristica'].isin(caracteristicas_filtro)][['coluna1', 'coluna2', 'coluna3']]

def main():
    st.title('FiltradorCSV: Simplificando a Análise de Dados em CSV')

    arquivo = st.file_uploader('Selecione os arquivos CSV:', type=['csv'], accept_multiple_files=True)

    if arquivo is not None:
        caracteristicas_filtro = st.multiselect('Selecione as características para filtrar:',
                                                ['caracteristica1', 'caracteristica2', 'caracteristica3'])

        dfs_filtrados = []
        for arquivo_csv in arquivo:
            df = pd.read_csv(arquivo_csv)
            df_filtrado = aplicar_filtros(df, caracteristicas_filtro)
            dfs_filtrados.append(df_filtrado)

        resultado_final = pd.concat(dfs_filtrados, ignore_index=True)

        st.write('Resultados filtrados:')
        st.write(resultado_final)

        # Gerar o arquivo final consolidado
        resultado_final_csv = resultado_final.to_csv(index=False)
        st.download_button(label='Download do arquivo final consolidado',
                           data=resultado_final_csv,
                           file_name='resultado_final.csv',
                           mime='text/csv')

if __name__ == "__main__":
    main()




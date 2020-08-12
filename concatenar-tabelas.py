import streamlit as st
import pandas as pd
import base64

def get_table_download_link(df):
    '''Essa função foi uma solução encontrada no fórum do StreamLit. Você pode encontrar a discussão aqui: https://discuss.streamlit.io/t/file-download-workaround-added-to-awesome-streamlit-org/1244
    '''
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a>'

    return href

def main():
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.image('https://media.giphy.com/media/IboGSjkXaOre0/giphy.gif', caption='imagem animada de uma esteira com mesas e uma boneca virando-as', use_column_width=True, format='gif')
    # Seleção tabelas
    st.title('Concatenador de tabelas')
    st.subheader('')
    st.subheader('Selecione as tabelas que você deseja concatenar')

    csv_1 = st.file_uploader('Tabela 1', type='csv')
    csv_2 = st.file_uploader('Tabela 2', type='csv')

    df_1 = pd.DataFrame()
    df_2 = pd.DataFrame()
    df_final = pd.DataFrame()

    if csv_1 is not None:
        df_1 = pd.read_csv(csv_1)

    if csv_2 is not None:
        df_2 = pd.read_csv(csv_2)

    # Tipo de concatenação
    st.subheader('')
    st.subheader('Tipo de concatenação')
    add_selectbox = st.selectbox(
        'Selecione o tipo de concatenação que você deseja realizar:', (['', 'Linhas no final'])
    )

    if add_selectbox == 'Linhas no final':
        df_final = pd.concat([df_1, df_2])
        st.subheader('')
        st.subheader('Faça download da tabela concatenada')
        st.markdown(get_table_download_link(df_final), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
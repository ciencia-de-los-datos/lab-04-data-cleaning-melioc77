
"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
    #df = dframe.copy()
    #df.set_index(df.columns[0], inplace = True) #establece la primera columna como índice
    df.dropna(inplace = True) #elimina las filas que contengan valores nulos
    #val_colum = df["barrio"].value_counts()
    df = df.apply(lambda x: x.astype(str))
    df = df.apply(lambda x: x.str.replace("$", "")) #elimina el signo de pesos
    df = df.apply(lambda x: x.str.replace(",", "")) #elimina las comas
    df = df.apply(lambda x: x.str.replace("¿", "")) 
    df = df.apply(lambda x: x.str.replace("_", " ")) 
    df = df.apply(lambda x: x.str.replace("-", " ")) 
    df = df.apply(lambda x: x.str.lower()) #convierte a minúsculasb
   # Convertir a float una columna
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)
    
    # Convertir a formato fecha
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst = True , format="mixed")
    
    df = df.drop_duplicates() #elimina duplicados

    return df

#print(clean_data().monto_del_credito.value_counts().to_list())
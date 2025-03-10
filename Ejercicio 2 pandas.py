import pandas as pd 

Tabla = {
        "Productos": ["Manzanas", "Naranjas", "Platanos", "Uvas", "Peras"],
        "Precio": [100,80,60,120,90],
        "Stock": [30,50,20,60,40]
}

df = pd.DataFrame(Tabla)
print (df)

df_nuevo = df.set_index("Productos")
print (df_nuevo)

df_nuevo2 = df.drop("Stock", axis=1, inplace=True)
print (df_nuevo2)

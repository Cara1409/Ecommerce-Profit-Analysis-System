import pandas as pd

# 1. Cargar nuestra data sucia
df = pd.read_csv('Data/ventas_suplementos_sucias.csv')

print(f"📊 Registros iniciales: {len(df)}")

# 2. Limpieza de Duplicados
df = df.drop_duplicates()
df = df.drop_duplicates(subset=['ID_Venta'], keep='first')
print(f"✅ Sin duplicados: {len(df)}")

# 3. Limpieza de Categorías (Normalización)
# Convertimos todo a Título (Ej: proteina -> Proteina) para que sea uniforme
df['Categoria'] = df['Categoria'].str.capitalize()

# 4. Manejo de Outliers (Precios locos)
# Filtramos precios razonables (por ejemplo, menores a 100.000)
# y mayores a 0
df = df[(df['Precio_Venta'] > 0) & (df['Precio_Venta'] < 100000)]

# 5. Manejo de Nulos (NaN)
# Si no hay canal o precio, esa venta no nos sirve para el análisis real
df = df.dropna(subset=['Canal', 'Precio_Venta'])

print(f"✨ Registros limpios finales: {len(df)}")

# Guardar el resultado limpio
df.to_csv('Data/ventas_suplementos_limpias.csv', index=False)
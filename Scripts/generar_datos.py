import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# 1. Configuración inicial del negocio
n_ventas = 1000
productos = {
    # PROTEÍNAS (Altos costos, márgenes ajustados)
    'Proteína Whey 1kg': {'costo': 25000, 'categoria': 'Proteínas'},
    'Proteína Isolate 1kg': {'costo': 32000, 'categoria': 'Proteínas'},
    'Proteína Vegana 900g': {'costo': 28000, 'categoria': 'Proteínas'},
    
    # CREATINAS (Mucha rotación)
    'Creatina Monohidrato 300g': {'costo': 18000, 'categoria': 'Creatinas'},
    'Creatina Monohidrato 500g': {'costo': 26000, 'categoria': 'Creatinas'},
    'Creatina Micronizada 300g': {'costo': 21000, 'categoria': 'Creatinas'},
    
    # AMINOÁCIDOS Y PRE-ENTRENOS
    'Aminoácidos BCAA 200g': {'costo': 12000, 'categoria': 'Suplementos'},
    'Pre-Entreno Explosive': {'costo': 15000, 'categoria': 'Suplementos'},
    'Glutamina 300g': {'costo': 14000, 'categoria': 'Suplementos'},
    
    # ACCESORIOS (Bajo costo, buen margen porcentual)
    'Shaker Pro': {'costo': 3500, 'categoria': 'Accesorios'},
    'Cinto de Cuero Gym': {'costo': 15000, 'categoria': 'Accesorios'},
    'Straps de Agarre': {'costo': 4500, 'categoria': 'Accesorios'}
}
canales = ['Instagram/Directo', 'ML_Clasico', 'ML_Premium']

# 2. Generación de datos base
data = []
fecha_inicio = datetime(2026, 1, 1)

for i in range(n_ventas):
    prod_nombre = random.choice(list(productos.keys()))
    costo_base = productos[prod_nombre]['costo']
    cat = productos[prod_nombre]['categoria']
    canal = random.choice(canales)
    
    # Lógica de precio de venta (Margen del 35% al 50%)
    precio_venta = costo_base * random.uniform(1.35, 1.50)
    
    # Comisiones según canal
    if canal == 'ML_Premium':
        comision = precio_venta * 0.30
    elif canal == 'ML_Clasico':
        comision = precio_venta * 0.15
    else: # Instagram
        comision = 0
        
    # Costo de envío (Gratis para cliente en compras > $30.000, lo paga el vendedor)
    envio = 3500 if precio_venta > 30000 else 0
    
    fecha = fecha_inicio + timedelta(days=random.randint(0, 120), hours=random.randint(0, 23))
    
    data.append([i+1, fecha, prod_nombre, cat, canal, round(precio_venta, 2), round(costo_base, 2), round(comision, 2), envio])

# 3. Crear DataFrame inicial
df = pd.DataFrame(data, columns=['ID_Venta', 'Fecha', 'Producto', 'Categoria', 'Canal', 'Precio_Venta', 'Costo_Repo', 'Comision_Plat', 'Costo_Envio'])

# --- INYECCIÓN DE ERRORES PARA ETAPA DE LIMPIEZA (ETL) ---

# A. Generar duplicados (5% de los datos) para practicar df.drop_duplicates()
df = pd.concat([df, df.sample(frac=0.05)], ignore_index=True)

# B. Meter valores nulos (NaN) en columnas críticas para practicar df.fillna() o dropna()
for col in ['Canal', 'Precio_Venta']:
    df.loc[df.sample(frac=0.02).index, col] = np.nan

# C. Inconsistencia de strings: Mezclar mayúsculas/minúsculas en Categorías
df['Categoria'] = df['Categoria'].apply(lambda x: x.upper() if random.random() > 0.8 else x.lower() if random.random() > 0.9 else x)

# D. Outliers: Precios erróneos por falla de sistema
df.loc[df.sample(n=3).index, 'Precio_Venta'] = 999999
df.loc[df.sample(n=2).index, 'Precio_Venta'] = 0

# ---------------------------------------------------------

# 4. Exportar a la carpeta Data (ruta relativa directa)
df.to_csv('Data/ventas_suplementos_sucias.csv', index=False)

print("--------------------------------------------------")
print("✅ ¡Dataset 'sucio' generado con éxito!")
print("📂 Buscalo en la carpeta /Data de tu proyecto.")
print(f"📊 Registros generados: {len(df)}")
print("--------------------------------------------------")
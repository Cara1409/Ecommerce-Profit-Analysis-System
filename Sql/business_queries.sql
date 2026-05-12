/* 
Análisis de Productos Estrella por Categoría
Objetivo: Identificar los 3 productos con mejor ROI por cada categoría de venta.
*/

WITH ResumenVentas AS (
    -- Paso 1: Limpiamos y calculamos métricas base
    SELECT 
        Producto,
        Categoria,
        Canal,
        SUM(Precio_Venta) AS Ingresos_Totales,
        SUM(Precio_Venta - Costo_Repo - Comision_Plat - Costo_Envio) AS Utilidad_Neta_Total,
        AVG((Precio_Venta - Costo_Repo - Comision_Plat - Costo_Envio) / NULLIF(Costo_Repo, 0)) * 100 AS ROI_Promedio
    FROM VentasSuplementos
    GROUP BY Producto, Categoria, Canal
),
RankeoProductos AS (
    -- Paso 2: Usamos una Window Function para rankear sin perder filas
    SELECT 
        *,
        DENSE_RANK() OVER (PARTITION BY Categoria ORDER BY ROI_Promedio DESC) AS Ranking_En_Categoria -- Utilizo DENDE_RANK para que no haya saltos visuales
    FROM ResumenVentas
)
-- Paso 3: Filtramos el Top de cada categoría
SELECT 
    Ranking_En_Categoria,
    Categoria,
    Producto,
    Canal,
    FORMAT(Utilidad_Neta_Total, 'C', 'es-AR') AS Utilidad_Formateada,  -- Formateo el numero a moneda argentina
    CAST(ROI_Promedio AS DECIMAL(10,2)) AS Porcentaje_ROI
FROM RankeoProductos
WHERE Ranking_En_Categoria <= 3
ORDER BY Categoria, Ranking_En_Categoria;
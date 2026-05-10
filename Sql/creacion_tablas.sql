USE EcommerceDB;
GO

CREATE TABLE VentasSuplementos (
    ID_Venta INT PRIMARY KEY,
    Fecha DATETIME,
    Producto VARCHAR(100),
    Categoria VARCHAR(50),
    Canal VARCHAR(50),
    Precio_Venta DECIMAL(10, 2),
    Costo_Repo DECIMAL(10, 2),
    Comision_Plat DECIMAL(10, 2),
    Costo_Envio DECIMAL(10, 2)
);
GO
import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear diccionario con datos de sucursales bancarias
sucursales_bancarias = {
    'id_sucursal': [201, 202, 203, 204, 205, 206],
    'nombre_sucursal': ['Centro Historico', 'Polanco', 'Santa Fe', 'Del Valle', 'Coyoacan', 'Reforma'],
    'gerente': ['Sr. Lopez', 'Sra. Diaz', 'Sr. Ramirez', 'Sra. Torres', 'Sr. Gomez', 'Sra. Vargas'],
    'empleados': [25, 35, 40, 20, 18, 30],
    'cajeros_automaticos': [4, 6, 8, 3, 2, 5],
    'clientes_activos': [5000, 12000, 15000, 4000, 3500, 10000],
    'captacion_mensual_millones': [50, 150, 200, 40, 35, 120],
    'ano_apertura': [1995, 2005, 2015, 1980, 1985, 2010],
    'horario_atencion': ['9:00-16:00', '9:00-19:00', '9:00-19:00', '9:00-16:00', '9:00-16:00', '9:00-19:00'],
    'calificacion_servicio': [4.2, 4.5, 4.7, 4.0, 3.9, 4.6]
}

print("Analisis Exploratorio de Datos EDA ")
print("EDA, Explorar Datalysis por Alejandra Rivera Valenzuela NC = 0200")
print("5. Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(sucursales_bancarias)
print("\n--- TABLA ORIGINAL DE SUCURSALES BANCARIAS ---")
print(df)
print("\nDICCIONARIO ML")

# 3. Exportar los datos a CSV
print("<3<3<3<3<3 Convertir el DataFrame en archivo CSV <3<3<3<3<3")
df.to_csv(
    'sucursales_bancarias_0200.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("<3<3<3<3 8. Leer los datos desde el archivo CSV<3<3<3<3  ")
print("sucursales_bancarias_0200.csv")

# 4. Leer el archivo CSV
df = pd.read_csv('sucursales_bancarias_0200.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
print("<3<3<3<3 9. Análisis Exploratorio de Datos (EDA) <3<3<3<3")

# 5. Primeros y últimos registros
print("<3<3<3<3 \n1. PRIMEROS REGISTROS (Head):<3<3<3<3")
print(df.head(3))  # Muestra los primeros 3
print("<3<3<3<3 \n2. ÚLTIMOS REGISTROS (Tail): <3<3<3<3")
print(df.tail(2))  # Muestra los últimos 2

# 6. Dimensiones y estructura
print("# <3<3<3<3 6. Dimensiones y estructura <3<3<3<3")
print(df)  # mostrar matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("<3<3<3<3\n7. ESTADÍSTICAS DESCRIPTIVAS:<3<3<3<3")
print(df.describe())

print("<3<3<3<3\n8. VALORES FALTANTES (Nulls):<3<3<3<3")
print(df.isnull().sum())

print("<3<3<3<3 \n9. REGISTROS DUPLICADOS: <3<3<3<3")
print(df.duplicated().sum())

print("<3<3<3<3 \n10. VALORES ÚNICOS POR COLUMNA: <3<3<3<3")
print(df.nunique())
print("Horarios únicos:", df['horario_atencion'].unique())

# 8. Análisis específico
print(df)
print("------------------------------------------------------------------")
print("\n11. SUCURSALES POR HORARIO DE ATENCIÓN:")
print(df['horario_atencion'].value_counts())

print("\n12. PROMEDIO DE CAPTACIÓN MENSUAL: $", df['captacion_mensual_millones'].mean(), "millones")
print("13. CAPTACIÓN MÁXIMA: $", df['captacion_mensual_millones'].max(), "millones")
print("14. CAPTACIÓN MÍNIMA: $", df['captacion_mensual_millones'].min(), "millones")

# 9. Ordenamiento, filtrado y agrupación
print("<3<3<3<3 \n15. SUCURSALES ORDENADAS POR CAPTACIÓN MENSUAL (Mayor a menor): <3<3<3<3")
print(df.sort_values(by='captacion_mensual_millones', ascending=False))

print("<3<3<3<3 \n16. SUCURSALES CON CAPTACIÓN MAYOR A $100 MILLONES: <3<3<3<3")
filtro = df[df['captacion_mensual_millones'] > 100]
print(filtro)

print("\n17. RESUMEN POR HORARIO DE ATENCIÓN:")
resumen = df.groupby('horario_atencion').agg(
    sucursales=('id_sucursal', 'count'),
    captacion_promedio=('captacion_mensual_millones', 'mean'),
    captacion_maxima=('captacion_mensual_millones', 'max')
)
print(resumen)

# 18. Gráfica de barras: Sucursales por horario de atención
print("Gráfica de barras: Sucursales por horario de atención")
conteo = df['horario_atencion'].value_counts()

plt.figure(figsize=(8, 5))
barras = plt.bar(conteo.index, conteo.values, color='skyblue')

# Agrega el valor de Y encima de cada barra
plt.bar_label(barras, padding=3)

plt.title('Sucursales por horario de atención Alejandra 0200')
plt.xlabel('Horario de atención')
plt.ylabel('Cantidad de sucursales')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Captación mensual por sucursal
plt.figure(figsize=(8, 5))
plt.bar(df['nombre_sucursal'], df['captacion_mensual_millones'], color='lightgreen')
plt.title('Captación mensual por sucursal EDA por Alejandra 0200')
plt.xlabel('Sucursal')
plt.ylabel('Captación mensual (millones)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de empleados por sucursal
plt.figure(figsize=(8, 5))
plt.hist(df['empleados'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de empleados por sucursal EDA por Alejandra 0200')
plt.xlabel('Cantidad de empleados')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Clientes activos vs Captación mensual
plt.figure(figsize=(8, 5))
plt.scatter(df['clientes_activos'], df['captacion_mensual_millones'], color='red', s=100)
plt.title('Relación entre clientes activos y captación mensual EDA por Alejandra 0200')
plt.xlabel('Clientes activos')
plt.ylabel('Captación mensual (millones)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de captación mensual
plt.figure(figsize=(7, 5))
plt.boxplot(df['captacion_mensual_millones'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de captación mensual (Boxplot) EDA Alejandra 0200')
plt.ylabel('Captación mensual (millones)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA Alejandra 0200')
plt.tight_layout()
plt.show()

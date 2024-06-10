import os
import pandas as pd
import matplotlib.pyplot as plt # type: ignore

# Carga del archivo al dataframe de trabajo
file_path = "C:/Users/jodam/Downloads/EstudiantesExtemporaneos2024-1.xlsx"

if not os.path.isfile(file_path):
  raise FileNotFoundError(f"{file_path} not found.")

piam20241 = pd.read_excel(file_path)
# Normalizar los valores en la columna 'tipo_identificacion'
piam20241['TIPOIDENTIFICACION'] = piam20241['TIPOIDENTIFICACION'].str.lower().replace({'cédula':"CC", 'tarjeta de identidad':"TI", 'pasaporte':"PS"})

# Distribución poblacional por tipo de identificación
tipoId = piam20241['TIPOIDENTIFICACION'].value_counts()
tipoId.index.name = 'Distribucion por Tipo de identificación'
tipoId.name = 'Distribucion Poblacional'
print(tipoId)

#Validación de registros
estrato = piam20241['ESTRATO'].value_counts()
print(estrato)

# Reemplazar valores vacíos y espacios en blanco por cero en la columna 'ESTRATO' y ordenar el estrato
piam20241["ESTRATO"] = piam20241["ESTRATO"].replace([' ', ''], 0)
piam20241["ESTRATO"] = piam20241["ESTRATO"].astype(int)
estrato = piam20241['ESTRATO'].value_counts().sort_index()

# distribución poblacional por estrato
estrato.index.name = 'Distribucion por Estrato'
estrato.name = 'Distribucion Poblacional'
print(estrato)

#Analisis Descriptivo de los derechos de matriculas y seguro
print(piam20241["DERECHOS_MATRICULA"].describe())
print(piam20241["DERECHOS_MATRICULA"].value_counts().sort_index())
print(piam20241["SEGURO_ESTUDIANTIL"].describe())
print(piam20241["SEGURO_ESTUDIANTIL"].value_counts().sort_index())


x = piam20241["ESTRATO"]
y = piam20241["DERECHOS_MATRICULA"]
plt.scatter(x, y)

# Formatear el eje Y para mostrar los números en formato normal (sin notación científica)
plt.ticklabel_format(style='plain', axis='y')
plt.title('Distribución de Derechos de Matrícula por Estrato')
plt.xlabel('Estrato')
plt.ylabel('Derechos de Matrícula')
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 08:11:49 2022

@author: squintra
"""

import pandas as pd
!pip install xlrd
import xlrd
import matplotlib.pyplot as plt

datos = pd.read_excel('datos_ayura.xlsx',sheet_name='datos')
datos.index=datos['FECHA']
datos = datos[~datos.index.duplicated(keep='first')]
datos = datos.sort_index()
datos['NivelEmbalse'].fillna(method='ffill',inplace=True)
datos['Pluviometria'].fillna(method='ffill',inplace=True)
datos['Solidos'].fillna(method='ffill',inplace=True)
datos['Caudal_24'].fillna(method='ffill',inplace=True)
datos['Caudal_36'].fillna(method='ffill',inplace=True)
datos['CaudalB45'].fillna(method='ffill',inplace=True)
datos['CaudalB123'].fillna(method='ffill',inplace=True)
datos['RN_ESPIRITU'].fillna(method='ffill',inplace=True)
datos['RN_PALMAS'].fillna(method='ffill',inplace=True)
datos['RN_PUENTEANG'].fillna(method='ffill',inplace=True)
datos['Manganeso'].fillna(method='ffill',inplace=True)
datos['pH'].fillna(method='ffill',inplace=True)
datos['Color'].fillna(method='ffill',inplace=True)
datos['Turbiedad_Natural'].fillna(method='ffill',inplace=True)
datos['TURBIEDAD'].fillna(method='ffill',inplace=True)
datos['CONDUCTIVIDAD'].fillna(method='ffill',inplace=True)

##Manganeso
datos['Manganeso'].plot()
datos['Manganeso'].describe()
datos['Manganeso'].quantile(0.95)
datos['Manganeso'][datos['Manganeso']>0.041] = datos['Manganeso'].quantile(0.95)
plt.hist(datos['Manganeso'])

##NivelEmbalse
datos['NivelEmbalse'].plot()
datos['NivelEmbalse'].describe()
plt.hist(datos['NivelEmbalse'])

##Pluviometría
datos['Pluviometria'].plot()
datos['Pluviometria'].describe()
plt.hist(datos['Pluviometria'])
datos['Pluviometria'].quantile(0.98)
datos['Pluviometria'][datos['Pluviometria']>0.25] = datos['Manganeso'].quantile(0.98)

#Solidos
datos['Solidos'].plot()
datos['Solidos'].describe()
plt.hist(datos['Solidos'])
datos['Solidos'].quantile(0.98)
datos['Solidos'].quantile(0.02)
datos['Solidos'][datos['Solidos']>59] = datos['Solidos'].quantile(0.98)
datos['Solidos'][datos['Solidos']<24.3] = datos['Solidos'].quantile(0.02)

#pH
datos['pH'].plot()
datos['pH'].describe()
plt.hist(datos['pH'])
datos['pH'].quantile(0.98)
datos['pH'].quantile(0.02)
datos['pH'][datos['pH']<6.51] = datos['pH'].quantile(0.02)

#Turbiedad Natural
datos['Turbiedad_Natural'].plot()
datos['Turbiedad_Natural'].describe()
plt.hist(datos['Turbiedad_Natural'])
datos['Turbiedad_Natural'].quantile(0.98)
datos['Turbiedad_Natural'].quantile(0.02)
datos['Turbiedad_Natural'][datos['Turbiedad_Natural']<69.2] = datos['Turbiedad_Natural'].quantile(0.98)

#Color
datos['Color'].plot()
datos['Color'].describe()
plt.hist(datos['Color'])
datos['Color'].quantile(0.98)
datos['Color'].quantile(0.02)
datos['Color'][datos['Color']<40] = datos['Color'].quantile(0.02)
datos['Color'][datos['Color']>687] = datos['Color'].quantile(0.98)

#Caudal_24
datos['Caudal_24'].plot()
datos['Caudal_24'].describe()
plt.hist(datos['Caudal_24'])

#Caudal_36
datos['Caudal_36'].plot()
datos['Caudal_36'].describe()
plt.hist(datos['Caudal_36'])

#CaudalB45
datos['CaudalB45'].plot()
datos['CaudalB45'].describe()
plt.hist(datos['CaudalB45'])

#CaudalB123
datos['CaudalB123'].plot()
datos['CaudalB123'].describe()
plt.hist(datos['CaudalB123'])

#RN_ESPIRITU
datos['RN_ESPIRITU'].plot()
datos['RN_ESPIRITU'].describe()
plt.hist(datos['RN_ESPIRITU'])
datos['RN_ESPIRITU'].quantile(0.98)
datos['RN_ESPIRITU'][datos['RN_ESPIRITU']>3.35] = datos['RN_ESPIRITU'].quantile(0.98)

#RN_PALMAS
datos['RN_PALMAS'].plot()
datos['RN_PALMAS'].describe()
plt.hist(datos['RN_PALMAS'])
datos['RN_PALMAS'].quantile(0.98)
datos['RN_PALMAS'][datos['RN_PALMAS']>1.83] = datos['RN_PALMAS'].quantile(0.98)

#RN_PALMAS
datos['RN_PUENTEANG'].plot()
datos['RN_PUENTEANG'].describe()
plt.hist(datos['RN_PUENTEANG'])
datos['RN_PUENTEANG'].quantile(0.98)
datos['RN_PUENTEANG'][datos['RN_PUENTEANG']>9.90] = datos['RN_PUENTEANG'].quantile(0.98)

#TURBIEDAD
datos['TURBIEDAD'].plot()
datos['TURBIEDAD'].describe()
plt.hist(datos['TURBIEDAD'])
datos['TURBIEDAD'].quantile(0.98)
datos['TURBIEDAD'].quantile(0.02)
datos['TURBIEDAD'][datos['TURBIEDAD']>61.04] = datos['TURBIEDAD'].quantile(0.98)
datos['TURBIEDAD'][datos['TURBIEDAD']<3.55] = datos['TURBIEDAD'].quantile(0.02)

datos.head(10)

datos.describe()

datos.info()

datos.isnull().sum()

# prompt: El app debe recoger los datos de país, ciudad, y dirección exacta.

# Dado que Colab/Jupyter Notebooks no pueden obtener la ubicación exacta del navegador del usuario
# sin una interacción compleja del frontend (como se explicó en los comentarios),
# la forma más práctica de "recoger" estos datos en este entorno es
# pidiéndole al usuario que los introduzca manualmente o usando un widget de formulario.

# Vamos a usar formularios de código en Google Colab para esto.

#@markdown ## Introduzca su Ubicación
pais = "España" #@param {type:"string"}
ciudad = "Madrid" #@param {type:"string"}
direccion_exacta = "Calle Gran Vía 10" #@param {type:"string"}

# Podemos imprimir los datos recogidos para verificar
print(f"País: {pais}")
print(f"Ciudad: {ciudad}")
print(f"Dirección Exacta: {direccion_exacta}")

# Ahora puedes usar estas variables (`pais`, `ciudad`, `direccion_exacta`)
# en tu código Python para procesar, guardar o usar los datos de ubicación.

# Ejemplo: podrías guardar estos datos en un diccionario o lista
ubicacion_recogida = {
    "país": pais,
    "ciudad": ciudad,
    "direccion_exacta": direccion_exacta
}

print("\nDatos de ubicación en un diccionario:")
print(ubicacion_recogida)

# Si necesitaras guardar esto en un archivo CSV o una base de datos,
# podrías usar bibliotecas como pandas o sqlite3.

# Ejemplo con pandas (si quieres agregarlo a un DataFrame)
import pandas as pd

# Crea un DataFrame con los datos recogidos
df_ubicaciones = pd.DataFrame([ubicacion_recogida])

print("\nDatos de ubicación en un DataFrame:")
df_ubicaciones

# Si tuvieras múltiples ubicaciones, las irías agregando a este DataFrame.
# Por ejemplo, si recogieras datos de otro usuario:
# pais2 = "México" #@param {type:"string"}
# ciudad2 = "Ciudad de México" #@param {type:"string"}
# direccion_exacta2 = "Av. Paseo de la Reforma 300" #@param {type:"string"}
# nueva_ubicacion = {"país": pais2, "ciudad": ciudad2, "direccion_exacta": direccion_exacta2}
# df_ubicaciones = pd.concat([df_ubicaciones, pd.DataFrame([nueva_ubicacion])], ignore_index=True)
# print("\nDataFrame con múltiples ubicaciones:")
# print(df_ubicaciones)

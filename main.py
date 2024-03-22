import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, CENTER, ROW, Pack
from bs4 import BeautifulSoup
import requests
url = 'https://dolarhoy.com/i/cotizaciones/dolar-blue'
datos = BeautifulSoup(requests.get(url).text, "html5lib")
print(datos.prettify())
precios_raw = datos.find_all("p")  # Los valores de precios están entre p-tags
actualizado_raw = datos.find_all('span')
actualizado = str(actualizado_raw[2])[37:62]
compra = str(precios_raw[0])[3:10]
venta = str(precios_raw[1])[3:10]


def button_handler(widget):
    print("hello")


def build(app):
    box = toga.Box()
    d_box = toga.Box()
    c_box = toga.Box()
    v_box = toga.Box()
    valores_box = toga.Box()

    mensaje = toga.Label("            Dólar Blue", style=Pack(text_align=CENTER))
    mensaje_actualizado = toga.Label(actualizado, style=Pack(text_align=CENTER))
    mensaje_compra = toga.Label("Compra: " + compra, style=Pack(text_align=LEFT))
    mensaje_venta = toga.Label("Venta: " + venta, style=Pack(text_align=RIGHT))
    d_box.add(mensaje)
    d_box.add(mensaje_actualizado)
    d_box.style.update(direction=COLUMN)
    d_box.style.padding = 20
    c_box.add(mensaje_compra)
    c_box.style.padding = 8
    v_box.add(mensaje_venta)
    v_box.style.padding = 8

    valores_box.add(v_box)
    valores_box.add(c_box)

    valores_box.style.update(direction=COLUMN)
    box.add(d_box)
    box.add(valores_box)

    box.style.update(direction=ROW)

    return box


def main():
    return toga.App("Dólar Blue", "dolar.blue", startup=build)


if __name__ == "__main__":
    main().main_loop()

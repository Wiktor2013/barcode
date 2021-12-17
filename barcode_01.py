import code128
from PIL import Image, ImageDraw, ImageFont
import sqlite3
import webbrowser

conn = sqlite3.connect("magazyn.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS articles (
    id	integer,
    code text,
    lot_number text,
    name text,
    measure	text,
    initial_quantity real,
    delivery real,
    usage real,
    end_quantity real,
    real_quantity real,
    PRIMARY KEY("id")
)''')
odczynnik = input("Podaj nazwę, kod albo lot odczynnika")
# def select_lotnumber(conn):


cur.execute("SELECT lot_number FROM articles WHERE code=?", (odczynnik, ))
x = cur.fetchall()
barcode_param = str(x[0]).replace("\'", '')
print(type(barcode_param))
print(barcode_param)
# print(row)
# for row in rows:
# barcode_param = row
#     # print(row)barcode_param
#     print(barcode_param)
# Get barcode value
# barcode_param = 'Lot 160221'

# Create barcode image
barcode_image = code128.image(barcode_param, height=100)

# Create empty image for barcode + text
top_bott_margin = 70
l_r_margin = 10
new_height = barcode_image.height + (2 * top_bott_margin)
new_width = barcode_image.width + (2 * l_r_margin)
new_image = Image.new('RGB', (new_width, new_height), (255, 255, 255))

# put barcode on new image
barcode_y = 100
new_image.paste(barcode_image, (0, barcode_y))

# object to draw text
draw = ImageDraw.Draw(new_image)

# Define custom text size and font
h1_size = 28
h2_size = 28
h3_size = 16
footer_size = 21

h1_font = ImageFont.truetype("DejaVuSans-Bold.ttf", h1_size)
h2_font = ImageFont.truetype("Ubuntu-Th.ttf", h2_size)
h3_font = ImageFont.truetype("Ubuntu-Th.ttf", h3_size)
footer_font = ImageFont.truetype("UbuntuMono-R.ttf", footer_size)

# Define custom text
company_name = 'BLIRT S.A.'
id1 = 'Magazyn Kładki'
license_num = 'ENZYMES'
cur.execute("SELECT name FROM articles WHERE code=?", (odczynnik, ))
nieobrobiony = str(cur.fetchone()).replace("\'", '')
print(nieobrobiony)
x = nieobrobiony.split(",")
product_type = x[0]
center_product_type = (barcode_image.width / 2) - len(product_type) * 5
center_barcode_value = (barcode_image.width / 2) - len(barcode_param) * 8

# Draw text on picture
draw.text((l_r_margin, 0), company_name, fill=(0, 0, 0), font=h1_font)
draw.text((l_r_margin, h1_size), id1, fill=(0, 0, 0), font=h2_font)
draw.text((l_r_margin + 2, (h1_size + h2_size + 5)), license_num, fill=(0, 0, 0), font=h3_font)
draw.text((center_product_type, (h1_size + h2_size + h3_size)), product_type, fill=(0, 0, 0), font=footer_font)
draw.text((center_barcode_value, (new_height - footer_size - 15)), barcode_param, fill=(0, 0, 0), font=h2_font)

# save in file
new_image.save('barcode_image.png', 'PNG')

# show in default viewer

webbrowser.open('barcode_image.png')

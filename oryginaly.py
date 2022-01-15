'''https://stackoverflow.com/questions/65471637/how-to-include-barcode-value-with-actual-barcode-python-code128-module'''
# import logging
# import azure.functions as func
# import code128
# import io
# from PIL import Image

########### pierwszy przyklad ###########
# barcode_param = '1234'
# barcode_bytes = io.BytesIO()
#
# logging.info('##### Generating barcode... #####')
# barcode = code128.image(barcode_param, height=100).save(barcode_bytes, "PNG")
# barcode_bytes.seek(0)
# logging.info('##### Barcode successfully generated #####')
# return func.HttpResponse(
#     barcode_bytes.getvalue(),
#     status_code=200,
#     mimetype='image/png')
#     barcode_bytes.close()


####### drugi przyklad #############

import code128
import io
from PIL import Image, ImageDraw, ImageFont

# Get barcode value
barcode_param = 'SUFFERINSUCCOTASH'

# Create barcode image
barcode_image = code128.image(barcode_param, height=100)

# Create empty image for barcode + text
top_bott_margin = 70
l_r_margin = 10
new_height = barcode_image.height + (2 * top_bott_margin)
new_width = barcode_image.width + (2 * l_r_margin)
new_image = Image.new( 'RGB', (new_width, new_height), (255, 255, 255))

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
company_name = 'YAY! CORP.'
id1 = '11-22-33-44'
license_num = 'WHY SOYNTENLY!'
product_type = 'GRADE A GREATNESS'
center_product_type = (barcode_image.width / 2) - len(product_type) * 5
center_barcode_value = (barcode_image.width / 2) - len(barcode_param) * 8

# Draw text on picture
draw.text( (l_r_margin, 0), company_name, fill=(0, 0, 0), font=h1_font)
draw.text( (l_r_margin, h1_size), id1, fill=(0, 0, 0), font=h2_font)
draw.text( (l_r_margin + 2, (h1_size + h2_size + 5)), license_num, fill=(0, 0, 0), font=h3_font)
draw.text( (center_product_type, (h1_size + h2_size + h3_size)), product_type, fill=(0, 0, 0), font=footer_font)
draw.text( (center_barcode_value, (new_height - footer_size - 15)), barcode_param, fill=(0, 0, 0), font=h2_font)

# save in file
new_image.save('barcode_image.png', 'PNG')
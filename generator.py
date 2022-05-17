import qrcode

from PIL import Image, ImageDraw

logo_file_name = 'sample_logo.png'
data_to_encode = "https://cascavel.ifpr.edu.br"

qr_code = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

qr_code.add_data(data_to_encode)
qr_code.make()

qr_code_image = qr_code.make_image().convert('RGB')

logo = Image.new('RGB', (100, 100))
d = ImageDraw.Draw(logo)
d.text((20, 20), 'IFPR', fill=(50, 160, 65))


logo_x_position = (qr_code_image.size[0] - logo.size[0]) // 2
logo_y_position = (qr_code_image.size[1] - logo.size[1]) // 2
logo_position = (logo_x_position, logo_y_position)

qr_code_image.paste(logo,logo_position)

qr_code_image.save('filename.png')

print('QR code gerado com sucesso')
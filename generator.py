import qrcode

from PIL import Image, ImageDraw, ImageFont


data_to_encode = "https://docs.google.com/forms/d/e/1FAIpQLSc4yWBZir8wdJ407IDwM-ZcrzBMOFqOY0qWUITSk7aEq4x-Hw/viewform?usp=pp_url&entry.1432566108={lab}&entry.1030287329={number}&entry.841035397=N%C3%A3o+liga?"

OPT_LAB = "Lab+Hardware"

for number in range(1,7):

    qr_code = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M
    )

    qr_code.add_data(data_to_encode.format(number=number,lab=OPT_LAB))
    qr_code.make()

    qr_code_image = qr_code.make_image().convert('RGB')

    # use a truetype font
    font = ImageFont.truetype("NotoSansCJK-Bold.ttc", 50)

    logo = Image.new('RGB', (130, 70), (255, 255, 255))
    d = ImageDraw.Draw(logo)
    d.text((10, 0), 'IFPR', fill=(50, 160, 65), font=font)


    logo_x_position = (qr_code_image.size[0] - logo.size[0]) // 2
    logo_y_position = (qr_code_image.size[1] - logo.size[1]) // 2
    logo_position = (logo_x_position, logo_y_position)

    qr_code_image.paste(logo,logo_position)

    qr_code_image.save('hardware/{lab}-{number}.png'.format(lab=OPT_LAB,number=number))

print('QR code gerado com sucesso')
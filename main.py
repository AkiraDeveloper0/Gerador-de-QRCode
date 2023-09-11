import qrcode

print("----------Gerador de QRCode----------")
link = input("Digite aqui o link: ")

imagem = qrcode.make(link)
imagem.save("QRCode_gerado.png")

print("----------O QRCode foi gerado----------")
import qrcode
from PIL import Image, ImageDraw, ImageFont

# --------------------------
# 1️⃣ Create QR code with LinkedIn blue
# --------------------------
linkedin_blue = "#0A66C2"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction for logo
    box_size=8,
    border=4,
)

qr.add_data("https://www.linkedin.com/in/syed-muhammad-talha-hashmi-data-scientist/")
qr.make(fit=True)

qr_img = qr.make_image(fill_color=linkedin_blue, back_color="white").convert("RGB")

# --------------------------
# 2️⃣ Add LinkedIn logo in center
# --------------------------
logo_path = r"D:\Python GitHub\QR Code Generator in Python\linkedin.png"
logo = Image.open(logo_path)

# Resize logo
logo_size = 80
logo = logo.resize((logo_size, logo_size))

# Center position
pos = ((qr_img.width - logo_size) // 2, (qr_img.height - logo_size) // 2)

# Paste logo (with transparency mask if PNG has transparency)
qr_img.paste(logo, pos, mask=logo)

# --------------------------
# 3️⃣ Add text below QR
# --------------------------
name = "Syed Muhammad Talha Hashmi"

# Load font
font = ImageFont.truetype("arial.ttf", 25)

# Measure text size
draw = ImageDraw.Draw(qr_img)
text_bbox = draw.textbbox((0, 0), name, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Create new image with extra space for text
new_img = Image.new("RGB", (qr_img.width, qr_img.height + text_height + 30), "white")
new_img.paste(qr_img, (0, 0))

# Draw text centered
draw = ImageDraw.Draw(new_img)
text_x = (qr_img.width - text_width) // 2
text_y = qr_img.height + 10
draw.text((text_x, text_y), name, fill="black", font=font)

# --------------------------
# 4️⃣ Save final image
# --------------------------
new_img.save("Talha_Linkedin_QR.png")
print("LinkedIn-style QR code saved successfully!")
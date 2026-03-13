
# LinkedIn QR Code Generator

A Python project to generate **custom LinkedIn-style QR codes** with your name and LinkedIn logo in the center.

This project allows you to quickly create a professional-looking QR code for your LinkedIn profile, which you can share on resumes, portfolios, or business cards.

---

## Features

- Generates QR codes for any LinkedIn URL
- Custom LinkedIn blue QR color (#0A66C2)
- Centers the LinkedIn logo in the QR code
- Adds your name below the QR code
- Saves the QR code as a PNG image

---

## Requirements

- Python 3.x
- Libraries:
  pip install qrcode[pil] pillow

---

## Usage

1. Place your LinkedIn logo in the project folder as `linkedin.png`.
2. Open `qr_generator.py` and update the `name` and `url` variables if needed.
3. Run the script:

    python qr_generator.py

4. The generated QR code will be saved in the `output/` folder (or the project folder if no output folder is used).

---

## Author

**Syed Muhammad Talha Hashmi**

- [LinkedIn](https://www.linkedin.com/in/syed-muhammad-talha-hashmi-data-scientist/)

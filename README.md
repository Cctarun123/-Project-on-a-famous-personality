🖼️ ASCII Art Generator (PPM P3)

This project converts a P3 ASCII PPM image into ASCII art using Python.
Each pixel is converted to grayscale and mapped to a character based on intensity, producing a text-based image output.

✨ Features

Reads P3 (ASCII) PPM image format

Converts RGB pixels to grayscale

Maps pixel intensity to ASCII characters

Saves output as a .txt file

Simple and beginner-friendly Python code

📂 Project Structure
.
├── ascii_art.py        # Main Python script
├── allu_arjun_p3.ppm   # Input image (P3 format)
├── ascii_output.txt    # Generated ASCII art
└── README.md

🛠️ Requirements

Python 3.x
(No external libraries required)

▶️ How to Run

Clone the repository:

git clone https://github.com/your-username/ascii-art-generator.git

Move into the project directory:
cd ascii-art-generator

Run the script:
python ascii_art.py

Output will be saved as:
ascii_output.txt

🔤 ASCII Mapping Used
ASCII_CHARS = "@%#*+=-:. "
Darker pixels → @, %, #
Lighter pixels → ., (space)

🚀 Future Improvements

Support for other image formats (PNG, JPG)
Adjustable output width
Colored ASCII output
Command-line arguments

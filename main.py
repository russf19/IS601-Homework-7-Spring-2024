import os
from pathlib import Path
import argparse
import qrcode
import validators
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Environment Variables for Configuration
QR_DIRECTORY = os.getenv('QR_CODE_DIR', 'qr_codes')
FILL_COLOR = os.getenv('FILL_COLOR', 'red')
BACK_COLOR = os.getenv('BACK_COLOR', 'white')

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Generate a QR code.')
    parser.add_argument('--url', help='The URL to encode in the QR code', required=True)
    args = parser.parse_args()

    # Initialize logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Validate URL
    if not validators.url(args.url):
        logging.error(f"Invalid URL provided: {args.url}")
        return

    # Generate and save the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(args.url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)

    # Create QR code directory if it doesn't exist
    Path(QR_DIRECTORY).mkdir(parents=True, exist_ok=True)

    # Save the QR code image
    filename = os.path.join(QR_DIRECTORY, 'qr_code.png')
    img.save(filename)
    logging.info(f"QR code successfully saved to {filename}")

if __name__ == "__main__":
    main()
    
# Python QR Code Generator (CLI)

Simple command-line tool to generate QR code PNG files from text or URLs.

## Requirements

- Python 3.9+

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Generate a QR code from text:

```bash
python src/main.py "https://example.com"
```

Generate with a custom file path:

```bash
python src/main.py "Hello from QR" --output output/my_qr.png
```

Tune size and border:

```bash
python src/main.py "Custom settings" --box-size 12 --border 2
```

Show help:

```bash
python src/main.py --help
```

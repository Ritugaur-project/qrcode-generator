"""Simple CLI for generating QR code PNG files."""

from __future__ import annotations

import argparse
from pathlib import Path

import qrcode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a QR code PNG from text."
    )
    parser.add_argument(
        "text",
        help="Text or URL to encode in the QR code.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="qrcode.png",
        help="Output PNG path (default: qrcode.png).",
    )
    parser.add_argument(
        "--box-size",
        type=int,
        default=10,
        help="Pixel size for each QR module (default: 10).",
    )
    parser.add_argument(
        "--border",
        type=int,
        default=4,
        help="Border thickness in modules (default: 4).",
    )
    return parser


def generate_qrcode(text: str, output: Path, box_size: int, border: int) -> Path:
    if box_size <= 0:
        raise ValueError("--box-size must be a positive integer.")
    if border < 0:
        raise ValueError("--border must be zero or a positive integer.")

    output.parent.mkdir(parents=True, exist_ok=True)
    image = qrcode.make(text, box_size=box_size, border=border)
    image.save(output)
    return output.resolve()


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        saved_path = generate_qrcode(
            text=args.text,
            output=Path(args.output),
            box_size=args.box_size,
            border=args.border,
        )
    except ValueError as exc:
        parser.error(str(exc))
        return

    print(f"QR code saved to: {saved_path}")


if __name__ == "__main__":
    main()

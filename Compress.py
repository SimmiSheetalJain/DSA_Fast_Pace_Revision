from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps


def compress_photo(
	input_path: str | Path = "SSJ.jpg",
	output_path: str | Path = "SSJ_compressed.jpg",
	max_size_mb: float = 1,
) -> Path:
	"""Compress a photo until its output is smaller than max_size_mb."""
	input_file = Path(input_path)
	output_file = Path(output_path)
	max_bytes = int(max_size_mb * 1024 * 1024)

	with Image.open(input_file) as source:
		image = ImageOps.exif_transpose(source).convert("RGB")
		scale = 1.0

		while scale >= 0.1:
			if scale == 1.0:
				candidate = image
			else:
				size = (
					max(1, round(image.width * scale)),
					max(1, round(image.height * scale)),
				)
				candidate = image.resize(size, Image.Resampling.LANCZOS)

			for quality in range(95, 4, -5):
				buffer = BytesIO()
				candidate.save(
					buffer,
					format="JPEG",
					quality=quality,
					optimize=True,
					progressive=True,
				)

				if buffer.tell() < max_bytes:
					output_file.parent.mkdir(parents=True, exist_ok=True)
					output_file.write_bytes(buffer.getvalue())
					print(
						f"Saved {output_file} ({buffer.tell() / 1024 / 1024:.2f} MB, "
						f"quality={quality}, size={candidate.size})"
					)
					return output_file

			scale *= 0.9

	raise RuntimeError("Could not compress the photo below the requested size.")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Compress a photo to a size limit.")
	parser.add_argument("input", nargs="?", default="SSJ.jpg")
	parser.add_argument("output", nargs="?", default="SSJ_compressed.jpg")
	parser.add_argument("--max-size-mb", type=float, default=1)
	args = parser.parse_args()

	compress_photo(args.input, args.output, args.max_size_mb)

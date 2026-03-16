from pathlib import Path
import numpy as np
from PIL import Image
from wordcloud import WordCloud


TEXT_FILE = Path("RomeoAndJuliet.txt")
MASK_FILE = Path("mask_star.png")
OUTPUT_FILE = Path("romeo_and_juliet_star_wordcloud.png")


def main() -> None:
    if not TEXT_FILE.exists():
        raise FileNotFoundError(f"Missing {TEXT_FILE}")
    if not MASK_FILE.exists():
        raise FileNotFoundError(f"Missing {MASK_FILE}")

    text = TEXT_FILE.read_text(encoding="utf-8", errors="ignore")
    mask_img = Image.open(MASK_FILE).convert("L")
    mask_arr = np.array(mask_img)
    mask_arr = 255 - mask_arr  # Invert the mask so words appear inside the star

    # background_color is NOT passed, so WordCloud uses its default.
    wc = WordCloud(mask=mask_arr)
    wc.generate(text)
    wc.to_file(OUTPUT_FILE)

    print(f"Saved: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()

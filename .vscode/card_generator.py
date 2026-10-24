import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


WIDTH = 1080
HEIGHT = 1440

FONT_BOLD = Path("C:/Windows/Fonts/msyhbd.ttc")
FONT_REGULAR = Path("C:/Windows/Fonts/msyh.ttc")


def wrap_text(text, font, max_width):
    paragraphs = text.split("\n")
    lines = []

    for paragraph in paragraphs:
        current = ""

        for char in paragraph:
            test = current + char

            if font.getlength(test) <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = char

        if current:
            lines.append(current)

    return lines


def generate_card(
    quote,
    book,
    note="",
    bg_color="#F7F4EF",
    card_color="#FFFFFF",
    text_color="#2F2A26",
    accent_color="#B98A5B",
    output_path="card.png",
):
    image = Image.new("RGB", (WIDTH, HEIGHT), bg_color)
    draw = ImageDraw.Draw(image)

    draw.rounded_rectangle(
        [60, 60, WIDTH - 60, HEIGHT - 60],
        radius=40,
        fill=card_color,
    )

    quote_font = ImageFont.truetype(str(FONT_BOLD), 72)
    book_font = ImageFont.truetype(str(FONT_BOLD), 42)
    note_font = ImageFont.truetype(str(FONT_REGULAR), 36)

    quote_lines = wrap_text(quote, quote_font, WIDTH - 240)
    quote_y = 260
    quote_line_height = 104

    for line in quote_lines:
        line_width = quote_font.getlength(line)
        x = (WIDTH - line_width) / 2
        draw.text((x, quote_y), line, font=quote_font, fill=text_color)
        quote_y += quote_line_height

    line_y = quote_y + 40
    draw.line(
        [WIDTH / 2 - 70, line_y, WIDTH / 2 + 70, line_y],
        fill=accent_color,
        width=4,
    )

    book_text = f"—— 《{book}》"
    book_width = book_font.getlength(book_text)
    draw.text(
        ((WIDTH - book_width) / 2, line_y + 70),
        book_text,
        font=book_font,
        fill=accent_color,
    )

    if note.strip():
        note_lines = wrap_text(note, note_font, WIDTH - 240)
        note_y = HEIGHT - 220 - len(note_lines) * 55

        for line in note_lines:
            line_width = note_font.getlength(line)
            x = (WIDTH - line_width) / 2
            draw.text((x, note_y), line, font=note_font, fill=text_color)
            note_y += 55

    image.save(output_path)
    return output_path
def load_templates(path="templates.json"):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
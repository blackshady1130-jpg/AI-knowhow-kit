import argparse
import json
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


W, H = 1080, 1920
MARGIN = 64
RED = "#D71920"
RED_DARK = "#A90F16"
RED_SOFT = "#FFF1F1"
PAPER = "#FFFDFC"
INK = "#171717"
MUTED = "#6A5F5F"
LINE = "#E9D4D4"
PALE = "#FFF8F6"


def font_path(*names):
    for name in names:
        path = Path("C:/Windows/Fonts") / name
        if path.exists():
            return str(path)
    return None


FONT_CN = font_path("msyh.ttc", "simhei.ttf", "simsun.ttc")
FONT_CN_BOLD = font_path("msyhbd.ttc", "simhei.ttf", "msyh.ttc")
FONT_MONO = font_path("consolab.ttf", "consola.ttf", "courbd.ttf", "msyh.ttc")


def load_font(size, bold=False, mono=False):
    path = FONT_MONO if mono else (FONT_CN_BOLD if bold else FONT_CN)
    return ImageFont.truetype(path, size)


def text_width(draw, text, font):
    if not text:
        return 0
    box = draw.textbbox((0, 0), str(text), font=font)
    return box[2] - box[0]


def wrap_text(draw, text, font, max_width, max_lines=None):
    text = re.sub(r"\s+", " ", str(text).strip())
    parts = re.findall(r"[A-Za-z0-9_,.%+#/-]+|[\u4e00-\u9fff]|[^\s]", text)
    lines, line = [], ""
    for part in parts:
        is_word = bool(re.match(r"[A-Za-z0-9_,.%+#/-]+$", part))
        is_cjk = bool(re.match(r"[\u4e00-\u9fff]$", part))
        prev_word = bool(re.search(r"[A-Za-z0-9_,.%+#/-]$", line))
        sep = " " if line and ((is_word and not line.endswith((" ", "/", "-"))) or (prev_word and is_cjk)) else ""
        candidate = line + sep + part
        if text_width(draw, candidate, font) <= max_width or not line:
            line = candidate
        else:
            lines.append(line.rstrip())
            line = part.lstrip()
            if max_lines and len(lines) >= max_lines:
                break
    if line and (not max_lines or len(lines) < max_lines):
        lines.append(line.rstrip())
    if max_lines and len(lines) == max_lines:
        last = lines[-1]
        while text_width(draw, last + "...", font) > max_width and len(last) > 1:
            last = last[:-1]
        if last != lines[-1]:
            lines[-1] = last + "..."
    return lines


def draw_multiline(draw, xy, text, font, fill, max_width, line_gap=8, max_lines=None):
    x, y = xy
    for line in wrap_text(draw, text, font, max_width, max_lines=max_lines):
        draw.text((x, y), line, font=font, fill=fill)
        y += font.size + line_gap
    return y


def round_rect(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_badge(draw, x, y, text):
    font = load_font(22, bold=True)
    tw = text_width(draw, text, font)
    round_rect(draw, (x, y, x + tw + 36, y + 42), 21, RED)
    draw.text((x + 18, y + 8), text, font=font, fill=PAPER)


def draw_target_logo(draw, cx, cy, size=142):
    r = size // 2
    round_rect(draw, (cx - r, cy - r, cx + r, cy + r), 32, RED, outline=RED_DARK, width=3)
    for rr in [40, 25, 9]:
        draw.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline=PAPER, width=7)
    draw.line((cx, cy - 54, cx, cy - 29), fill=PAPER, width=7)
    draw.line((cx + 29, cy, cx + 54, cy), fill=PAPER, width=7)
    draw.line((cx - 54, cy, cx - 29, cy), fill=PAPER, width=7)
    draw.line((cx, cy + 29, cx, cy + 54), fill=PAPER, width=7)


def draw_section_title(draw, x, y, text):
    draw.rectangle((x, y + 13, x + 8, y + 46), fill=RED)
    draw.text((x + 20, y), text, font=load_font(28, bold=True), fill=INK)
    return y + 52


def draw_stats(draw, x, y, section):
    y = draw_section_title(draw, x, y, section.get("title", "关键数据"))
    items = section.get("items", [])[:4]
    gap = 18
    col_w = (W - 2 * MARGIN - 72 - gap) // 2
    card_h = 154
    for idx, item in enumerate(items):
        row = idx // 2
        col = idx % 2
        xx = x + col * (col_w + gap)
        yy = y + row * (card_h + gap)
        box = (xx, yy, xx + col_w, yy + card_h)
        round_rect(draw, box, 18, PAPER, outline=LINE, width=2)
        draw.text((xx + 24, yy + 18), item.get("label", ""), font=load_font(22, bold=True), fill=RED_DARK)
        draw.text((xx + 24, yy + 54), item.get("big", ""), font=load_font(37, bold=True), fill=RED)
        draw_multiline(draw, (xx + 24, yy + 104), item.get("note", ""), load_font(19), MUTED, col_w - 48, line_gap=4, max_lines=2)
    rows = (len(items) + 1) // 2
    return y + rows * card_h + max(0, rows - 1) * gap + 24


def draw_cards(draw, x, y, section):
    y = draw_section_title(draw, x, y, section.get("title", "拆解"))
    items = section.get("items", [])[:4]
    gap = 18
    col_w = (W - 2 * MARGIN - 72 - gap) // 2
    card_h = int(section.get("height", 118))
    for idx, item in enumerate(items):
        row = idx // 2
        col = idx % 2
        xx = x + col * (col_w + gap)
        yy = y + row * (card_h + gap)
        round_rect(draw, (xx, yy, xx + col_w, yy + card_h), 18, PAPER, outline=LINE, width=2)
        draw.text((xx + 22, yy + 20), item.get("title", ""), font=load_font(25, bold=True), fill=RED_DARK)
        draw_multiline(draw, (xx + 22, yy + 60), item.get("text", ""), load_font(21), INK, col_w - 44, line_gap=6, max_lines=3)
    rows = (len(items) + 1) // 2
    return y + rows * card_h + max(0, rows - 1) * gap + 24


def draw_layers(draw, x, y, section):
    y = draw_section_title(draw, x, y, section.get("title", "先拆三层"))
    row_h = int(section.get("height", 92))
    for idx, item in enumerate(section.get("items", [])[:5], 1):
        round_rect(draw, (x, y, W - MARGIN - 36, y + row_h), 17, PALE, outline=LINE, width=2)
        draw.ellipse((x + 24, y + 25, x + 66, y + 67), fill=RED)
        draw.text((x + 37, y + 31), str(idx), font=load_font(18, bold=True, mono=True), fill=PAPER)
        draw.text((x + 88, y + 19), item.get("title", ""), font=load_font(25, bold=True), fill=RED_DARK)
        draw_multiline(draw, (x + 250, y + 20), item.get("text", ""), load_font(22), INK, 650, line_gap=5, max_lines=2)
        y += row_h + 12
    return y + 8


def draw_anchor_list(draw, x, y, section):
    y = draw_section_title(draw, x, y, section.get("title", "材料锚点"))
    row_h = int(section.get("height", 82))
    for item in section.get("items", [])[:5]:
        round_rect(draw, (x, y, W - MARGIN - 36, y + row_h), 16, PALE, outline=LINE, width=2)
        draw.text((x + 24, y + 18), item.get("title", ""), font=load_font(24, bold=True), fill=RED_DARK)
        draw_multiline(draw, (x + 210, y + 18), item.get("text", ""), load_font(22), INK, 650, line_gap=5, max_lines=2)
        y += row_h + 12
    return y + 8


def draw_red_callout(draw, x, y, section):
    lines = section.get("lines", [])
    box_h = 118 + max(0, len(lines) - 1) * 42
    round_rect(draw, (x, y, W - MARGIN - 36, y + box_h), 22, RED, outline=RED_DARK, width=2)
    draw.text((x + 30, y + 22), section.get("eyebrow", "核心判断"), font=load_font(24, bold=True), fill=PAPER)
    yy = y + 62
    for line in lines[:3]:
        draw.text((x + 30, yy), line, font=load_font(34, bold=True), fill=PAPER)
        yy += 44
    return y + box_h + 30


def draw_prompt_list(draw, x, y, section):
    y = draw_section_title(draw, x, y, section.get("title", "下次这样追问"))
    items = section.get("items", [])[:4]
    box_h = 58 + len(items) * 62
    round_rect(draw, (x, y, W - MARGIN - 36, y + box_h), 22, PAPER, outline=RED, width=3)
    yy = y + 24
    for idx, text in enumerate(items, 1):
        draw.ellipse((x + 30, yy + 9, x + 72, yy + 51), fill=RED)
        draw.text((x + 43, yy + 15), str(idx), font=load_font(18, bold=True, mono=True), fill=PAPER)
        draw_multiline(draw, (x + 92, yy), text, load_font(27, bold=True), INK, 770, line_gap=6, max_lines=2)
        yy += 62
    return y + box_h + 28


def draw_question_box(draw, x, y, section):
    y = draw_section_title(draw, x, y, section.get("title", "判断问题"))
    box_h = int(section.get("height", 112))
    round_rect(draw, (x, y, W - MARGIN - 36, y + box_h), 22, PAPER, outline=RED, width=3)
    draw_multiline(draw, (x + 30, y + 26), section.get("text", ""), load_font(29, bold=True), INK, 820, line_gap=7, max_lines=3)
    return y + box_h + 28


SECTION_RENDERERS = {
    "stats": draw_stats,
    "cards": draw_cards,
    "layers": draw_layers,
    "anchor_list": draw_anchor_list,
    "red_callout": draw_red_callout,
    "prompt_list": draw_prompt_list,
    "question_box": draw_question_box,
}


def render(spec, out_path):
    im = Image.new("RGB", (W, H), RED_SOFT)
    draw = ImageDraw.Draw(im)

    draw.rectangle((0, 0, W, 352), fill=RED)
    draw.rectangle((0, H - 150, W, H), fill=RED)

    card = (MARGIN, 72, W - MARGIN, H - 150)
    round_rect(draw, card, 34, PAPER, outline=LINE, width=2)

    x = MARGIN + 36
    y = 116
    draw.text((x, y), spec.get("brand", "AI行业判断笔记"), font=load_font(28, bold=True), fill=RED)
    draw.text((W - MARGIN - 160, y + 2), spec.get("date", ""), font=load_font(22, bold=True, mono=True), fill=MUTED)
    y += 62
    draw_badge(draw, x, y, spec.get("badge", "AI 行业 / 判断"))
    draw.text((x, y + 58), spec.get("subtitle", ""), font=load_font(23, bold=True), fill=MUTED)
    draw_target_logo(draw, W - MARGIN - 96, 252, size=148)

    y = 356
    title_font = load_font(int(spec.get("title_size", 55)), bold=True)
    for line in spec.get("title_lines", [])[:3]:
        draw.text((x, y), line, font=title_font, fill=INK)
        y += int(spec.get("title_line_gap", 70))

    y += 20
    round_rect(draw, (x, y, W - MARGIN - 36, y + 134), 24, RED_SOFT, outline=RED, width=3)
    draw.text((x + 28, y + 20), spec.get("today_label", "今天的判断"), font=load_font(23, bold=True), fill=RED_DARK)
    draw_multiline(draw, (x + 28, y + 56), spec.get("today_judgment", ""), load_font(28, bold=True), INK, 830, line_gap=7, max_lines=2)
    y += 164

    for section in spec.get("sections", []):
        renderer = SECTION_RENDERERS.get(section.get("type"))
        if renderer:
            y = renderer(draw, x, y, section)

    footer_y = H - 124
    draw.text((MARGIN + 34, footer_y), spec.get("footer_title", "不做资讯搬运，只拆可复用判断"), font=load_font(28, bold=True), fill=PAPER)
    draw.text((MARGIN + 34, footer_y + 48), spec.get("footer_subtitle", "关注方向：Agent / 评测 / 训练机制 / AI 产品"), font=load_font(23), fill=PAPER)
    draw.line((W - MARGIN - 220, footer_y + 18, W - MARGIN - 36, footer_y + 18), fill=PAPER, width=5)
    draw.line((W - MARGIN - 220, footer_y + 60, W - MARGIN - 78, footer_y + 60), fill=PAPER, width=5)

    if y > H - 190:
        print(f"WARNING: content may overflow into footer: y={y}")
    im.save(out_path, quality=95)
    print(out_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True, help="Path to JSON cover spec.")
    parser.add_argument("--out", help="Optional output PNG path.")
    args = parser.parse_args()

    spec_path = Path(args.spec)
    with spec_path.open("r", encoding="utf-8") as f:
        spec = json.load(f)
    out = Path(args.out) if args.out else spec_path.parent / spec.get("output", "cover_standard.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    render(spec, out)


if __name__ == "__main__":
    main()

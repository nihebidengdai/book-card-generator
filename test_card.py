from card_generator import generate_card, load_templates


templates = load_templates()

for index, template in enumerate(templates, start=1):
    generate_card(
        quote="人生不是由别人赋予的，而是由自己选择的。",
        book="被讨厌的勇气",
        note="这句话让我停止把选择权交给别人。",
        bg_color=template["bg_color"],
        card_color=template["card_color"],
        text_color=template["text_color"],
        accent_color=template["accent_color"],
        output_path=f"test_card_{index}.png",
    )

print("3张卡片已生成")
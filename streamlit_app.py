import streamlit as st
from pathlib import Path
from card_generator import generate_card, load_templates


st.set_page_config(page_title="书摘卡片生成器", layout="centered")

st.title("书摘卡片生成器")
st.caption("输入好句和个人理解，生成适合小红书的书摘卡片。")

templates = load_templates()
template_names = [template["name"] for template in templates]

quote = st.text_area("好句", height=180, placeholder="粘贴书中的原句")
book = st.text_input("书名", placeholder="例如：被讨厌的勇气")
note = st.text_area("我的理解", height=120, placeholder="写一句你自己的解读")

selected_name = st.selectbox("选择模板", template_names)
template = next(item for item in templates if item["name"] == selected_name)

if st.button("生成卡片", type="primary"):
    if not quote.strip() or not book.strip():
        st.warning("请先填写好句和书名。")
    else:
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / "card.png"

        generate_card(
            quote=quote.strip(),
            book=book.strip(),
            note=note.strip(),
            bg_color=template["bg_color"],
            card_color=template["card_color"],
            text_color=template["text_color"],
            accent_color=template["accent_color"],
            output_path=str(output_path),
        )

        st.image(str(output_path), width=360)

        with open(output_path, "rb") as file:
            st.download_button(
                "下载图片",
                data=file,
                file_name="书摘卡片.png",
                mime="image/png",
            )
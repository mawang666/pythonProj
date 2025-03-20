from docx import Document
import re

def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# 中文路径示例
docx_file_path = 'maps/完美情人2.docx'

try:
    # 读取 .docx 文件内容
    novel_content = read_docx(docx_file_path)

    # 使用正则表达式分割小说为章节
    split_content = re.split(r'(第[0-9一二三四五六七八九十]+章)', novel_content)

    # 初始化一个列表来存储章节和前置内容
    formatted_chapters = []

    # 添加第一个章节前的内容。如果有内容，这就是前言部分
    if split_content[0].strip():
        formatted_chapters.append(("前言", split_content[0]))

    # 合并每个章节的标题和内容
    for i in range(1, len(split_content), 2):
        formatted_chapters.append((split_content[i].strip(), split_content[i+1].strip()))

    # 打印所有章节及其前面的内容，确保包括前言
    for idx, (title, content) in enumerate(formatted_chapters):
        print(f"{title}:\n{content[:100]}...\n")

except Exception as e:
    print(f"读取文件时出错: {e}")
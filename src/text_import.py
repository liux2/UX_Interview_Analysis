try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import os
import zipfile

# Config for text extraction from docx.
WORD_NAMESPACE = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
PARA = WORD_NAMESPACE + "p"
TEXT = WORD_NAMESPACE + "t"


def get_docx_text(file_path):
    """Take the path of a docx file as argument, return the text in unicode."""
    document = zipfile.ZipFile(file_path)
    xml_content = document.read("word/document.xml")
    document.close()
    tree = XML(xml_content)

    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text for node in paragraph.getiterator(TEXT) if node.text]
        if texts:
            paragraphs.append("".join(texts))
    # Type String
    return "\n\n".join(paragraphs)


def intermediate_file(dir_path):
    """Dumps name tag for each conversation, retains answers."""
    text_body = ""
    # Loop thru dir for text files.
    for filename in os.listdir(dir_path):
        if filename.endswith(".doc") or filename.endswith(".docx"):
            text_body += get_docx_text(os.path.join(dir_path, filename))

    # Put String to an intermediate file
    with open("intermediate/intermediate_file", "w") as f:
        f.write(text_body)


# TODO: Add more file format support when requested.

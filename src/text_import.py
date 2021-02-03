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


def retain_main_body(file_path, start_tag, end_tag, question_mark):
    """Keeps only the body of the interview."""

    main_text_body = ""
    start_tag_list = []
    end_tag_list = []

    # Get the index of start and end positions
    with open(file_path, "r") as f:
        for num, line in enumerate(f):
            if start_tag in line:
                start_tag_list.append(num)
            elif end_tag in line:
                end_tag_list.append(num)
            else:
                pass

    # Check for eligibility
    # TODO: write a function that detects which doc misses the tag
    if len(start_tag_list) > len(end_tag_list):
        print("***The file contains more start tag than end tag***")
        return
    elif len(start_tag_list) < len(end_tag_list):
        print("***The file contains more end tag than start tag***")
        return
    else:
        pass
    # Get ranges, 2D list
    range_list = zip(start_tag_list, end_tag_list)
    # 1. texts between main and end.
    # It's an ugly af chunk of code IK! I will rewrite it if I can!
    for start, end in range_list:
        with open(file_path, "r") as f:
            for num, line in enumerate(f):
                if num in range(start + 1, end - 1) and (
                    not line.startswith(tuple(question_mark))
                ):
                    try:
                        main_text_body += line.split("：", 1)[1]
                    except IndexError:
                        pass

    with open("intermediate/intermediate_file", "w") as f:
        f.write(main_text_body)


# TODO: Add more file format support when requested.

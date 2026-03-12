import docx
import sys

def extract_text(file_path, output_path):
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        content = '\n'.join(full_text)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Extraction successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_text.py <file_path> <output_path>")
    else:
        extract_text(sys.argv[1], sys.argv[2])

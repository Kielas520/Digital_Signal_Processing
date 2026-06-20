import fitz
import sys
import os

def extract_pdf_to_markdown(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    
    all_text = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        all_text.append(f"<!-- Page {page_num + 1} -->\n\n{text}")
    
    output_path = os.path.join(output_dir, "content.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(all_text))
    
    print(f"Extracted {len(doc)} pages to {output_path}")
    doc.close()

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        extract_pdf_to_markdown(sys.argv[1], sys.argv[2])
    else:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        source_dir = os.path.join(base, "source")
        extracted_dir = os.path.join(source_dir, "extracted")
        for root, dirs, files in os.walk(source_dir):
            if root.startswith(extracted_dir):
                continue
            for fname in files:
                if fname.lower().endswith(".pdf"):
                    pdf_path = os.path.join(root, fname)
                    name = os.path.splitext(fname)[0]
                    out_dir = os.path.join(extracted_dir, name)
                    extract_pdf_to_markdown(pdf_path, out_dir)

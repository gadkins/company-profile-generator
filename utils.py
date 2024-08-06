import pypandoc
pypandoc.download_pandoc()

# Function to convert markdown file to Word document
def convert_md_to_docx(md_file, output_file):
    output = pypandoc.convert_file(md_file, 'docx', outputfile=output_file)
    assert output == ""
    print(f"Conversion successful! Word document saved as {output_file}")
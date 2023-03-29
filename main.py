import re
import PyPDF2

pdf_folder = 'preencher com o caminho da pasta com os documentos PDF no computador'

pdf_files = range(1, 183)

terms = [
        ["REDES", "SOCIAIS"],
        ["REDE", "SOCIAL"]
]

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for pdf_file in pdf_files:
        print(pdf_file)
        pdffileobj = open(pdf_folder + str(pdf_file) + '.pdf','rb')
        pdfreader = PyPDF2.PdfReader(pdffileobj)
        text = ""
        for page_num in range(0, len(pdfreader.pages)-1):
            pageobj = pdfreader.pages[page_num]
            text = text + pageobj.extract_text().replace("\n", "")
        text_list = list(filter(None, re.split(r'(\s|\.)', text.strip())))
        text_list = [value for value in text_list if value != " "]

        finds = []
        for term in terms:
            for word in range(0, len(text_list)):
                if term[0] == text_list[word].upper():
                    if term[1] == text_list[word+1].upper():
                        finds.append(word)

        text_paragraphs = []
        for find in finds:
            text_paragraph = text_list[find]
            finddot = False
            pos = find + 1
            while finddot == False:
                if (pos < len(text_list)):
                    if text_list[pos] != ".":
                        text_paragraph = text_paragraph + " " + text_list[pos]
                        pos += 1
                    else:
                        text_paragraph = text_paragraph + "."
                        finddot = True
                else:
                    finddot = True
            finddot = False
            pos = find - 1
            while finddot == False:
                if text_list[pos] != ".":
                    text_paragraph = text_list[pos] + " " + text_paragraph
                    pos -= 1
                else:
                    finddot = True
            text_paragraphs.append(text_paragraph)
        with open(pdf_folder + str(pdf_file) + '.txt', 'w', encoding="utf-8") as file:
            file.writelines('\n'.join(text_paragraphs))

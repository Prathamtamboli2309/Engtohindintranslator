import PyPDF2
import io
from googletrans import Translator

# creating a pdf reader object
# reader = PyPDF2.PdfReader('my.pdf')


# printing number of pages in pdf file
# print(len(reader.pages))

text=""

# for i in range(len(reader.pages)):
    # page = reader.pages[i]
    # text += page.extract_text()

print(text)


def translateTextFunc(text):
    translator = Translator()
    result = translator.translate(text=text,dest="hi")
    return result.text

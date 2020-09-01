import pyttsx3
import PyPDF2
book = open('cracking.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
audio = pyttsx3.init()
audio.setProperty('rate', 125)
audio.save_to_file('pages', 'test.mp3')
for num in range(13, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    audio.say(text)
    audio.runAndWait()
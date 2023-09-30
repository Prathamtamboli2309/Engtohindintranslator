import pyttsx3
from flask import Flask,request,jsonify, render_template
import translate
import fitz
import time

speak_data=""

app = Flask(__name__,template_folder='template')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/TranslateText')
def translateText():
    text = request.args.get('userText')
    result = translate.translateTextFunc(text)
    speak_data=result
    print(speak_data)
    return jsonify({'translatedText' : result})

@app.route("/TranslatePDF",methods=['POST'])
def TranslatePDF():
    pdf_data = request.data

    try:
        pdf_document = fitz.open(stream=pdf_data, filetype='pdf')
        text_pages = []
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text_pages.append(page.get_text())

        beforetime = time.time()
        result = ""
        for text in text_pages:
            Result += translate.translateTextFunc(text=text)
        aftertime = time.time()

        print(f"Time taken to translate: {aftertime-beforetime} seconds")
        return jsonify({"translatedText" : result})
    except Exception as e:
        return str(e), 500 

@app.route("/speak",methods=['GET'])

def speak():
    try:

        text = request.args.get('userText')
        print(text)
        result = translate.translateTextFunc(text)
   
        # print(data)
        engine = pyttsx3.init()

        voices=engine.getProperty('voices')


        print(result)
        engine.setProperty('voice',voices[2].id)
        engine.say(result)
        engine.runAndWait()
        engine.stop()
        print("hi")
        return jsonify({"translatedText" : result})
    except Exception as e:
        return str(e), 500 

if __name__ == "__main__":
    app.run(debug=True)

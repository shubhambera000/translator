from django.shortcuts import render, redirect
from .forms import *


def selector(request):
    return render(request, 'selector.html')


def model_img(request):
    x = 'Error.png'
    if request.method == 'POST':
        form = Loader(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            a = form.cleaned_data['img']
            x = str(a)

        elif 'back' in request.POST:
            return redirect('selector')
    elif 'back' in request.POST:
        return redirect('selector')
    else:
        form = Image()

    b = 'C:/Users/Dell/translater/media/images/'+x
    if 'lag' in request.POST:
        lang = request.POST.get('lag')
    else:
        lang = 'en'
    import pytesseract as tess
    import cv2
    d = None
    img = cv2.imread(b)
    if type(img) == type(d):
        img = cv2.imread('C:/Users/Dell/translater/media/images/Except.png')
    text = tess.image_to_string(img)
    from googletrans import Translator
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    data = translation.text
    return render(request, 'loader.html', {'form': form, 'data': data, 'data1': text})


def success(request):
    if request.method == 'POST':
        return redirect('selector')

    return render(request, 'success.html',)


def speech_to_text(request):
    if 'lang' in request.POST:
        lang = request.POST.get('lang')
    else:
        lang = 'en'
    import speech_recognition as sr
    from googletrans import Translator
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        output = " " + r.recognize_google(audio)
    except sr.UnknownValueError:
        output = "Could not understand audio"
    except sr.RequestError as e:
        output = "Could not request results; {0}".format(e)
    data = output
    translator = Translator()
    translation = translator.translate(data, dest=lang)

    if request.method == 'POST' and 'sun' in request.POST:

        import os
        from gtts import gTTS
        tts = gTTS(translation.text, lang=lang, slow=True)
        tts.save('hello.mp3')
        os.system('hello.mp3')
    elif 'back' in request.POST:
        return redirect('selector')
    return render(request, 'speech_to_text.html', {'data': translation.text, 'data1': data})

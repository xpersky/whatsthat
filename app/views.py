from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import os
import cv2
import numpy as np
from keras.models import load_model
import tensorflow as tf

graph = tf.get_default_graph()
model = load_model(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'whatsthat.h5'))

# Create your views here.

def index(request):
    return render(request,'app/home.html')

def check(request):
    if request.method == 'POST':
        if request.is_ajax():
            img = prepare_image(request)
            with graph.as_default():
                result = model.predict(img)
            output = fetch_result(result)
    return JsonResponse(output, safe=False)

def prepare_image(req):
    img = cv2.imdecode(np.fromstring(req.FILES['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
    img = cv2.resize(img,(224,224), interpolation = cv2.INTER_CUBIC)
    img = np.expand_dims(img,axis=0)/255
    return img

def fetch_result(res):
    pred_yes = res[0][0]
    pred_not = res[0][1]
    if pred_yes > pred_not:
        diag = 'cancer'
        prob = str(round(pred_yes,4))
    else:
        diag = 'not cancer'
        prob = str(round(pred_not,4))
    output = [diag,prob]
    return output

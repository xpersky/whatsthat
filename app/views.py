from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import TrainImagesOfCancer, TrainImagesNotCancer, Usage

import os
import cv2
import numpy as np
from keras.models import load_model
import tensorflow as tf

graph = tf.get_default_graph()
model = load_model(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'whatsthat.h5'))

# Render template

def index(request):
    return render(request,'app/home.html')

# Respond to user request

def check(request):
    if request.method == 'POST':
        if request.is_ajax():
            img = prepare_image(request)
            with graph.as_default():
                result = model.predict(img)
            output = fetch_result(result,request)
    return JsonResponse(output, safe=False)

def prepare_image(req):
    img = cv2.imdecode(np.fromstring(req.FILES['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
    img = cv2.resize(img,(224,224), interpolation = cv2.INTER_CUBIC)
    img = np.expand_dims(img,axis=0)/255
    return img

def fetch_result(res,req):
    pred_yes = res[0][0]
    pred_not = res[0][1]
    if pred_yes > pred_not:
        diag = 'cancer'
        prob = str(round(pred_yes,4))
        instance = TrainImagesOfCancer()
        instance.image = req.FILES['image']
        instance.save()
    else:
        diag = 'not cancer'
        prob = str(round(pred_not,4))
        instance = TrainImagesNotCancer()
        instance.image = req.FILES['image']
        instance.save()
    usage = Usage()
    usage.result = diag
    usage.save()
    return [diag,prob]

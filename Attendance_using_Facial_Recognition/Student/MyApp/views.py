from django.shortcuts import render
import requests
import json
import os
from django.utils import timezone
from datetime import datetime
from ml_models.ml import give_results
from .models import attendance

# Create your views here.

def login(request):
    return render(request, 'Login.html')

def capture_image(request):
    roll = request.POST["roll_number"]
    print(roll)
    return render(request, 'Capture_Image.html', {'roll': roll})

def fetch_compare(request):
    try:
        roll_number = request.GET['roll']
        #Get the first image
        response1 = requests.get(f'https://final-year-student-default-rtdb.firebaseio.com/{roll_number}.json')
        Dict = json.loads(response1.text)
        img_1 = Dict[list(Dict.keys())[len(list(Dict.keys()))-1]]['uri']

        response2 = requests.get(f'https://final-year-admin-default-rtdb.firebaseio.com/{roll_number}.json')
        Dict = json.loads(response2.text)
        img_2 = Dict[list(Dict.keys())[len(list(Dict.keys()))-1]]['uri']

        print("img_1 data printed")
        result = give_results(img_1, img_2)
        print(result)
        res = "Similar" if result<1 else "Different"
        if res=="Similar":
            curr = attendance.objects.get(roll=roll_number)
            # Code here makes sure, there are no double attendance
            x=datetime.now(tz=timezone.utc)-curr.dt
            if x.total_seconds()>=3600: #change it to 60sec for trail
                attendance.objects.filter(roll=roll_number).update(mrec = curr.mrec+1, dt=datetime.now(tz=timezone.utc))
                return render(request, 'success.html')
            else:
                return render(request, 'Later.html')
        else:
            return render(request, 'Failure.html')
    except:
        return render(request, 'contact.html')
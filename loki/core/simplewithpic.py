#!/usr/bin/python3 
import os
import time
import requests
import cv2
import sys
import gender_guesser.detector as gender
from bs4 import BeautifulSoup
from core.colours import *
import json
import csv

class Person(object):
    # Same as in simple.py, with nationality and to_dict method
    def __init__(self, target_gender=None, nationality=None):
        def strip_value(str):
            if 'value="' in str:
                text_beg = str.index('value="') + 7
                text_end = str.index('"/></div>')
                str = str[text_beg:text_end]
                return str
            if '<p>' in str:
                text_beg = str.index('<p>') + 3
                text_end = str.index('</p>')
                str = str[text_beg:text_end]
                return str
            return str

        person_data = {}
        url = 'https://www.fakepersongenerator.com/Index/generate'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'Referer': 'https://www.fakepersongenerator.com/'
        }
        
        for _ in range(3):
            try:
                req = requests.post(url, headers=headers, timeout=10)
                page = requests.get(req.url, headers=headers, timeout=10)
                if page.status_code == 200:
                    break
            except requests.RequestException as e:
                print(f"{bad} Request failed: {e}")
                time.sleep(1)
        else:
            raise ConnectionError("Failed to connect to fakepersongenerator.com after 3 attempts")

        soup = BeautifulSoup(page.content, 'html.parser')
        category = soup.select('.info-title')
        name_raw = soup.select('.click')
        data_raw = str(soup.select('.col-md-8'))
        data2 = soup.select('.info-detail')

        if not name_raw:
            print(f"{bad} No name found on the page.")
            name = "Unknown"
        else:
            name = name_raw[0].string.strip()

        index = data_raw.find('<p')
        data_main = []
        data_main_val = []

        while index != -1:
            iterator = 1
            index2 = data_raw.find('<p', index + iterator)
            build_string = data_raw[index + 3: index2 - 4] if index2 != -1 else data_raw[index + 3:]
            data_main.append(build_string)
            index = index2
            iterator += 1

        for a in range(len(data_main)):
            data_main[a] = data_main[a].replace('<b>', '').replace('</b>', '').replace('title="test">', '')
            data_main_val.append(data_main[a][data_main[a].index(':') + 2:])
            data_main[a] = data_main[a][:data_main[a].index(':')]
            person_data[data_main[a]] = data_main_val[a]

        for b in range(len(data2)):
            cat_text = category[b].string if category[b].string else category[b].get_text(strip=True)
            category[b] = cat_text.strip() if cat_text else "Unknown"
            data2[b] = strip_value(str(data2[b]))
            data2[b] = data2[b].replace('<', '<').replace('<br/>', '\n\t\t').replace('"', '"')
            person_data[category[b]] = data2[b]

        self.name = name
        self.gender = person_data.get('Gender', 'Unknown')
        self.birthday = person_data.get('Birthday')
        self.street = person_data.get('Street')
        self.telephone = person_data.get('Telephone')
        self.email = person_data.get("Email")
        self.occupation = person_data.get("Occupation(Job Title)")
        self.country = person_data.get("Country", nationality if nationality else "Unknown")

        if target_gender and self.gender.lower() != target_gender.lower():
            raise ValueError(f"Gender mismatch: {self.gender} != {target_gender}")

        if nationality and self.country.lower() != nationality.lower():
            raise ValueError(f"Nationality mismatch: {self.country} != {nationality}")

    def to_dict(self):
        return {
            "name": self.name,
            "gender": self.gender,
            "birthday": self.birthday,
            "street": self.street,
            "telephone": self.telephone,
            "email": self.email,
            "occupation": self.occupation,
            "country": self.country
        }

def save_data(person, output_format, filename):
    data_dict = person.to_dict()
    if output_format == 'txt':
        data_str = '\n'.join(f"{k}: {v}" for k, v in data_dict.items())
        with open(f"{filename}.txt", 'w') as file:
            file.write(data_str)
    elif output_format == 'json':
        with open(f"{filename}.json", 'w') as file:
            json.dump(data_dict, file, indent=4)
    elif output_format == 'csv':
        with open(f"{filename}.csv", 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data_dict.keys())
            writer.writeheader()
            writer.writerow(data_dict)

def simpleinfogatherwithpic(gender=None, nationality=None, output_format='txt'):
    while True:
        try:
            person = Person(gender, nationality)
            break
        except ValueError as e:
            print(f"{bad} {e}")
            time.sleep(1)

    print('%s Connecting to the internet' % info)
    time.sleep(0.5)
    print('%s Fetching Information' % info)
    time.sleep(0.5)
    print('%s %sName: %s%s' % (res, blue, end, person.name))
    time.sleep(0.5)
    print('%s %sGender: %s%s' % (res, blue, end, person.gender))
    time.sleep(0.5)
    print('%s %sCountry: %s%s' % (res, blue, end, person.country))

    try:
        os.mkdir(person.name)
    except OSError as e:
        print(f"{bad} Failed to create directory {person.name}: {e}")
        sys.exit(1)
    os.chdir(person.name)
    
    # Replace os.system with requests for distribution independence
    img_url = 'https://thispersondoesnotexist.com/'
    img_data = requests.get(img_url).content
    with open('image.png', 'wb') as img_file:
        img_file.write(img_data)
    
    save_data(person, output_format, person.name)
    print('%s Data stored in %s./%s%s' % (info, green, person.name, end))
    gender_by_name(person.name)

def gender_by_name(person_name):
    a = str(person_name)
    name_split = a.split()
    df = name_split[0]
    d = gender.Detector(case_sensitive=False)
    final_gender_from_name = d.get_gender(df)
    visual_main(a)

FACE_PROTO = "core/weights/opencv_face_detector.pbtxt"
FACE_MODEL = "core/weights/opencv_face_detector_uint8.pb"
AGE_PROTO = "core/weights/age_deploy.prototxt"
AGE_MODEL = "core/weights/age_net.caffemodel"
GENDER_PROTO = "core/weights/gender_deploy.prototxt"
GENDER_MODEL = "core/weights/gender_net.caffemodel"

FACE_NET = cv2.dnn.readNet(FACE_MODEL, FACE_PROTO)
AGE_NET = cv2.dnn.readNet(AGE_MODEL, AGE_PROTO)
GENDER_NET = cv2.dnn.readNet(GENDER_MODEL, GENDER_PROTO)

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
AGE_LIST = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)", "(38-43)", "(48-53)", "(60-100)"]
GENDER_LIST = ["male", "female"]

box_padding = 20

def get_face_box(net, frame, conf_threshold=0.7):
    frame_copy = frame.copy()
    frame_height = frame_copy.shape[0]
    frame_width = frame_copy.shape[1]
    blob = cv2.dnn.blobFromImage(frame_copy, 1.0, (300, 300), [104, 117, 123], True, False)
    net.setInput(blob)
    detections = net.forward()
    boxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frame_width)
            y1 = int(detections[0, 0, i, 4] * frame_height)
            x2 = int(detections[0, 0, i, 5] * frame_width)
            y2 = int(detections[0, 0, i, 6] * frame_height)
            boxes.append([x1, y1, x2, y2])
            cv2.rectangle(frame_copy, (x1, y1), (x2, y2), (0, 255, 0), int(round(frame_height / 150)), 8)
    return frame_copy, boxes

def age_gender_detector(input_path, person_name):
    image = cv2.imread(input_path)
    resized_image = cv2.resize(image, (640, 480))
    frame = resized_image.copy()
    frame_face, boxes = get_face_box(FACE_NET, frame)
    for box in boxes:
        face = frame[max(0, box[1] - box_padding):min(box[3] + box_padding, frame.shape[0] - 1), \
               max(0, box[0] - box_padding):min(box[2] + box_padding, frame.shape[1] - 1)]
        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        GENDER_NET.setInput(blob)
        gender_predictions = GENDER_NET.forward()
        gender = GENDER_LIST[gender_predictions[0].argmax()]
        a = "{}".format(gender)
        AGE_NET.setInput(blob)
        age_predictions = AGE_NET.forward()
        age = AGE_LIST[age_predictions[0].argmax()]
        b = "{}".format(age)
        final_function(a, b, person_name)

def final_function(a, b, person_name):
    gender_visual = a
    a = str(person_name)
    name_split = a.split()
    df = name_split[0]
    d = gender.Detector(case_sensitive=False)
    final_gender_from_name = d.get_gender(df)
    while gender_visual != final_gender_from_name:
        print('%s Gender Visual Confirmation:%s %s' % (bad, end, gender_visual))
        print('%s Getting the most suitable image%s' % (info, end))
        img_url = 'https://thispersondoesnotexist.com/'
        img_data = requests.get(img_url).content
        with open('image.png', 'wb') as img_file:
            img_file.write(img_data)
        time.sleep(1)
        gender_by_name(person_name)
    if gender_visual == final_gender_from_name:
        print('%s Suitable Picture Stored' % res)
        print('%s Exiting' % info)
        sys.exit(0)

def visual_main(a):
    person_name = a
    location_of_pic = './image.png'
    output = age_gender_detector(location_of_pic, person_name)

def maininfogather(gender=None, nationality=None, output_format='txt'):
    simpleinfogatherwithpic(gender, nationality, output_format)

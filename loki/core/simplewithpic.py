#!/usr/bin/python3 
import os
import time
import requests
import cv2
import sys
import gender_guesser.detector as gender
from bs4 import BeautifulSoup
from core.colours import *


class Person(object):
    def __init__(self):
        def strip_value(str):
            if ('value="') in str:
                text_beg = str.index('value="') + 7
                text_end = str.index('"/></div>')
                str = str[text_beg:text_end]
                return str
            if ('<p>') in str:
                text_beg = str.index('<p>') + 3
                text_end = str.index('</p>')
                str = str[text_beg:text_end]
                return str
            return str

        person_data = {}

        url = 'https://www.fakepersongenerator.com/Index/generate'
        req = requests.post(url)
        page = requests.get(req.url)

        soup = BeautifulSoup(page.content, 'html.parser')
        category = soup.select('.info-title')

        name_raw = soup.select('.click')
        data_raw = str(soup.select('.col-md-8'))
        data2 = soup.select('.info-detail')

        index = data_raw.find('<p')  # index for parsing data_raw

        name = name_raw[0].string.strip()
        data_main = []
        data_main_val = []

        while index != -1:
            iterator = 1
            index2 = data_raw.find('<p', index + iterator)
            build_string = data_raw[index + 3: index2 - 4]
            data_main.append(build_string)
            index = index2
            iterator += 1

        for a in range(len(data_main)):
            data_main[a] = data_main[a].replace('<b>', '').replace('</b>', '').replace('title="test">', '')
            data_main_val.append(data_main[a][data_main[a].index(':') + 2:])
            data_main[a] = data_main[a][:data_main[a].index(':')]
            person_data[data_main[a]] = data_main_val[a]

        for b in range(len(data2)):
            category[b] = category[b].string.strip()
            data2[b] = strip_value(str(data2[b]))
            data2[b] = data2[b].replace('&lt;', '<').replace('<br/>', '\n\t\t').replace('&quot;', '"')
            person_data[category[b]] = data2[b]

        self.name = name
        self.gender = person_data.get('Gender)')
        self.race = person_data.get('Race')
        self.birthday = person_data.get('Birthday')
        self.street = person_data.get('Street')
        self.telephone = person_data.get('Telephone')
        self.mobile = person_data.get('Mobile')
        self.email = person_data.get("Email")
        self.height = person_data.get("Height")
        self.weight = person_data.get("Weight")
        self.hair_color = person_data.get("Hair Color")
        self.blood_type = person_data.get("Blood Type")
        self.zodiac = person_data.get('Starsign(Tropical Zodiac)')
        self.mother_maiden_name = person_data.get("Mother's Maiden Name")
        self.civil_status = person_data.get("Civil Status")
        self.educational_background = person_data.get("Educational Background")
        self.disease_history = person_data.get("Disease History")
        self.social_security = person_data.get("Social Security Number")
        self.passport = person_data.get("Passport")
        self.driver_license = person_data.get("Driver License")
        self.car_license_plate = person_data.get("Car License Plate")
        self.employment_status = person_data.get("Employment Status")
        self.monthly_salary = person_data.get("Monthly Salary")
        self.occupation = person_data.get("Occupation(Job Title)")
        self.company_name = person_data.get("Company Name")
        self.company_size = person_data.get("company_Size")
        self.industry = person_data.get("Industry")
        self.credit_card_type = person_data.get("Credit Card Type")
        self.credit_card_number = person_data.get("Credit Card Number")
        self.cvv2 = person_data.get("CVV2")
        self.expires = person_data.get("Expires")
        self.paypal = person_data.get("Paypal")
        self.western_union_mtcn = person_data.get("Western Union MTCN")
        self.moneygram_mtcn = person_data.get("MoneyGram MTCN")
        self.account_balance = person_data.get("Account Balance")
        self.orders_lifetime = person_data.get("Orders Lifetime")
        self.total_consumption = person_data.get("Total Consumption")
        self.preferred_payment = person_data.get("Preferred Payment")
        self.family_members = person_data.get("Family Members")
        self.vehicle = person_data.get("Vehicle")
        self.online_status = person_data.get("Online Status")
        self.online_signature = person_data.get("Online Signature")
        self.online_biography = person_data.get("Online Biography")
        self.interest = person_data.get("Interest")
        self.favorite_color = person_data.get("Favorite Color")
        self.favorite_movie = person_data.get("Favorite Movie")
        self.favorite_music = person_data.get("Favorite Music")
        self.favorite_song = person_data.get("Favorite Song")
        self.favorite_book = person_data.get("Favorite Book")
        self.favorite_sports = person_data.get("Favorite Sports")
        self.favorite_tv = person_data.get("Favorite TV")
        self.favorite_movie_star = person_data.get("Favorite Movie Star")
        self.favorite_singer = person_data.get("Favorite Singer")
        self.favorite_food = person_data.get("Favorite Food")
        self.personality = person_data.get("Personality")
        self.person_style = person_data.get("Personal Style")
        self.website = person_data.get("Website")
        self.register_time = person_data.get("Register Time")
        self.register_ip = person_data.get("Register IP")
        self.points = person_data.get("Points")
        self.level = person_data.get("Level")
        self.number_of_comments = person_data.get("Number of Comments")
        self.posted_articles = person_data.get("Posted Articles")
        self.friends = person_data.get("Friends")
        self.language = person_data.get("Language")
        self.verified_status = person_data.get("Verified Status")
        self.security_question = person_data.get("Security Question")
        self.security_answer = person_data.get("Security Answer")
        self.browser_user_agent = person_data.get("Browser User Agent")
        self.system = person_data.get("System")
        self.guid = person_data.get("GUID")
        self.geo_coordinates = person_data.get("Geo coordinates")
        self.timezone = person_data.get("Timezone")
        self.ups_tracking = person_data.get("UPS Tracking Number")
        self.country = person_data.get("Country")
        self.country_code = person_data.get("Country Code")


def simpleinfogatherwithpic():
    person = Person()
    print('%s Connecting to the internet' % info)
    time.sleep(0.5)
    print('%s Fetching Information' % info)
    data = '''
{ 
    "personal details": {  
        "name": "%s",   
        "gender": "%s",   
        "birthday": "%s",
        "zodiac": "%s",
        "Mother Maiden Name": "%s",
        "Family Members": "%s",
        "Personality": "%s",
        "Person Style": "%s",
        "Language": "%s",
        "Verified Status": "%s",
        "Country": "%s",
        "Country Code": "%s",

    "Address and Location": {
        "street": "%s",
        "Geo Coordinates": "%s",
        "Timezone": "%s",

    "Employment":{
        "Employment Status": "%s",
        "Monthly Salary": "%s",
        "Occupation": "%s",
        "Company Name": "%s",
        "Company Size": "%s",
        "Industry": "%s",

    "Favorite": {
        "color": "%s",
        "Movie": "%s",
        "Music": "%s",
        "Song": "%s",
        "Book": "%s",
        "Sports": "%s",
        "TV": "%s",
        "Movie Star": "%s",
        "Singer": "%s",
        "Food": "%s",

    "Financial": {
        "Credit Card Type": "%s",
        "Credit Card Number": "%s",
        "CVV2": "%s",
        "Expires On:": "%s",
        "PayPal": "%s",
        "Western Union MTCN": "%s",
        "MoneyGram MTCN": "%s",
        "Account Balance": "%s",
        "Preferred Payment": "%s",

    "phonenumber": {
        "telephone": "%s",
        "mobile": "%s",

    "Online Details": {
        "Website": "%s",
        "email": "%s",
        "Online Status": "%s",
        "Online Signature": "%s",
        "Online Biography": "%s",
        "Security Question": "%s",
        "Security Answer": "%s",
        "Browser User Agent": "%s",

    "Physical Characteristics": {
        "height": "%s",
        "weight": "%s",
        "hair color": "%s",
        "blood types": "%s",

    "Medical History": {
        "Disease History": "%s",

    "Other Details": {
        "Civil Status": "%s",
        "Educational Background": "%s",
        "Social Security Number": "%s",
        "Passport": "%s",
        "Driver License": "%s",
        "Car License Plate": "%s",
        "Vehicle": "%s",
        "Register Time": "%s",
        "Register IP": "%s",
        "Points": "%s",
        "Level": "%s",
        "Number of Comments": "%s",
        "Posted Articles": "%s",
        "Friends": "%s",
        "UPS Tracking Number": "%s"

}}}}}}}}}}}\n ''' % (
    person.name, person.gender, person.birthday, person.zodiac, person.mother_maiden_name, person.family_members,
    person.personality, person.person_style, person.language, person.verified_status, person.country,
    person.country_code, person.street, person.geo_coordinates, person.timezone, person.employment_status,
    person.monthly_salary, person.occupation, person.company_name, person.company_size, person.industry,
    person.favorite_color, person.favorite_movie, person.favorite_music, person.favorite_song, person.favorite_book,
    person.favorite_sports, person.favorite_tv, person.favorite_movie_star, person.favorite_singer,
    person.favorite_food, person.credit_card_type, person.credit_card_number, person.cvv2, person.expires,
    person.paypal, person.western_union_mtcn, person.moneygram_mtcn, person.account_balance, person.preferred_payment,
    person.telephone, person.mobile, person.website, person.email, person.online_status, person.online_signature,
    person.online_biography, person.security_question, person.security_answer, person.browser_user_agent, person.height,
    person.weight, person.hair_color, person.blood_type, person.disease_history, person.civil_status,
    person.educational_background, person.social_security, person.passport, person.driver_license,
    person.car_license_plate, person.vehicle, person.register_time, person.register_ip, person.points, person.level,
    person.number_of_comments, person.posted_articles, person.friends, person.ups_tracking)

    time.sleep(0.5)
    print('%s Fetched information. The following is your Basic Identity' % info)
    time.sleep(0.5)
    print('%s %sName: %s%s' % (res, blue, end, person.name))
    time.sleep(0.5)
    print('%s %sGender: %s%s' % (res, blue, end, person.gender))
    time.sleep(0.5)
    print('%s %sBirthday: %s%s' % (res, blue, end, person.birthday))
    time.sleep(0.5)
    print('%s %sZodiac: %s%s' % (res, blue, end, person.zodiac))
    time.sleep(0.5)
    print('%s %sCountry: %s%s' % (res, blue, end, person.country))
    time.sleep(0.5)
    print('%s %sGeo Coordinates: %s%s' % (res, blue, end, person.geo_coordinates))
    time.sleep(0.5)
    print('%s %sTimezone: %s%s' % (res, blue, end, person.timezone))
    time.sleep(0.5)
    print('%s %sTelephone: %s%s' % (res, blue, end, person.telephone))
    time.sleep(0.5)
    print('%s %sEmail: %s%s' % (res, blue, end, person.email))
    time.sleep(0.5)
    print('%s %sHeight: %s%s' % (res, blue, end, person.height))
    time.sleep(0.5)
    print('%s %sWeight: %s%s' % (res, blue, end, person.weight))

    os.mkdir(person.name)
    os.chdir(person.name)
    os.system('curl https://thispersondoesnotexist.com/ --silent --output image.png')
#    os.system('mv image image.jpeg')
    with open("%s.txt" % person.name, 'w') as file:
        file.write(data)
        file.close()
        print('%s More detailed information stored in %s./%s%s directory' % (info, green, person.name, end))
    person_name = person.name
    gender_by_name(person_name)


def gender_by_name(person_name):
    a = str(person_name)
    name_split = a.split()
    df = name_split[0]
    d = gender.Detector(case_sensitive=False)
    final_gender_from_name = d.get_gender('%s' % df)
    visual_main(a)


######################################################################################################################
################################################## Visual Code #######################################################
######################################################################################################################

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
    final_gender_from_name = d.get_gender('%s' % df)
    while gender_visual != final_gender_from_name:
        print('%s Gender Visual Confirmation:%s %s' % (bad, end, gender_visual))
        print('%s Getting the most suitable image%s' % (info, end))
        os.system('curl https://thispersondoesnotexist.com/ --silent --output image.png')
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


def maininfogather():
    simpleinfogatherwithpic()
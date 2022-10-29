import time
from bs4 import BeautifulSoup
from core.colours import *
import requests
import gender_guesser.detector as gender
import os
import sys


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




def simpleinfogather():
    person = Person()
    print('%s Connecting to the internet' % info)
    time.sleep(0.5)
    print('%s Fetching Information' % info)

    a = str(person.name)
    name_split = a.split()
    df= name_split[0]
    d = gender.Detector(case_sensitive=False)
    final_gender_from_name = d.get_gender('%s' % df)

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
    
}}}}}}}}}}}\n ''' % (person.name, final_gender_from_name, person.birthday, person.zodiac, person.mother_maiden_name, person.family_members, person.personality, person.person_style, person.language, person.verified_status, person.country, person.country_code, person.street, person.geo_coordinates, person.timezone, person.employment_status, person.monthly_salary, person.occupation, person.company_name, person.company_size, person.industry, person.favorite_color, person.favorite_movie, person.favorite_music, person.favorite_song, person.favorite_book, person.favorite_sports, person.favorite_tv, person.favorite_movie_star, person.favorite_singer, person.favorite_food, person.credit_card_type, person.credit_card_number, person.cvv2, person.expires, person.paypal, person.western_union_mtcn, person.moneygram_mtcn, person.account_balance, person.preferred_payment, person.telephone, person.mobile, person.website, person.email, person.online_status, person.online_signature, person.online_biography, person.security_question, person.security_answer, person.browser_user_agent, person.height, person.weight, person.hair_color, person.blood_type, person.disease_history, person.civil_status, person.educational_background, person.social_security, person.passport, person.driver_license, person.car_license_plate, person.vehicle, person.register_time, person.register_ip, person.points, person.level, person.number_of_comments, person.posted_articles, person.friends, person.ups_tracking)

    time.sleep(0.5)
    print('%s Fetched information. The following is your Basic Identity' % info)
    time.sleep(0.5)
    print('%s %sName: %s%s' % (res, blue, end, person.name))
    time.sleep(0.5)    
    print('%s %sGender: %s%s' % (res, blue, end, final_gender_from_name))
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
    with open("%s.txt" % person.name, 'w') as file:
       file.write(data)
       file.close()
       print('%s More detailed information stored in %s./%s%s directory' % (info, green, person.name, end))
       sys.exit(0)


def simpleinfogathermale():

    person = Person()
    print('%s Connecting to the internet' % info)
    time.sleep(0.5)
    print('%s Fetching Information' % info)


    a = str(person.name)
    name_split = a.split()
    df= name_split[0]
    d = gender.Detector(case_sensitive=False)
    final_gender_from_name = d.get_gender('%s' % df)


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
    
}}}}}}}}}}}\n ''' % (person.name, final_gender_from_name, person.birthday, person.zodiac, person.mother_maiden_name, person.family_members, person.personality, person.person_style, person.language, person.verified_status, person.country, person.country_code, person.street, person.geo_coordinates, person.timezone, person.employment_status, person.monthly_salary, person.occupation, person.company_name, person.company_size, person.industry, person.favorite_color, person.favorite_movie, person.favorite_music, person.favorite_song, person.favorite_book, person.favorite_sports, person.favorite_tv, person.favorite_movie_star, person.favorite_singer, person.favorite_food, person.credit_card_type, person.credit_card_number, person.cvv2, person.expires, person.paypal, person.western_union_mtcn, person.moneygram_mtcn, person.account_balance, person.preferred_payment, person.telephone, person.mobile, person.website, person.email, person.online_status, person.online_signature, person.online_biography, person.security_question, person.security_answer, person.browser_user_agent, person.height, person.weight, person.hair_color, person.blood_type, person.disease_history, person.civil_status, person.educational_background, person.social_security, person.passport, person.driver_license, person.car_license_plate, person.vehicle, person.register_time, person.register_ip, person.points, person.level, person.number_of_comments, person.posted_articles, person.friends, person.ups_tracking)

    time.sleep(0.5)
    print('%s Fetched information. The following is your Basic Identity' % info)
    time.sleep(0.5)
    print('%s %sName: %s%s' % (res, blue, end, person.name))
    time.sleep(0.5)    
    print('%s %sGender: %s%s' % (res, blue, end, final_gender_from_name))
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


    if final_gender_from_name == "male":
        os.mkdir(person.name)
        os.chdir(person.name)
        with open("%s.txt" % person.name, 'w') as file:
            file.write(data)
            file.close()
            print('%s More detailed information stored in %s./%s%s directory' % (info, green, person.name, end))
            sys.exit(0)
    else:
        print('%s The name has been detected to not be a MALE name. Fetching Again' % info)
        simpleinfogathermale()


def simpleinfogathermalewithprofession(profession):

    person = Person()
    print('%s Connecting to the internet' % info)
    time.sleep(0.5)
    print('%s Fetching Information' % info)


    a = str(person.name)
    name_split = a.split()
    df= name_split[0]
    d = gender.Detector(case_sensitive=False)
    final_gender_from_name = d.get_gender('%s' % df)


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
    
}}}}}}}}}}}\n ''' % (person.name, final_gender_from_name, person.birthday, person.zodiac, person.mother_maiden_name, person.family_members, person.personality, person.person_style, person.language, person.verified_status, person.country, person.country_code, person.street, person.geo_coordinates, person.timezone, person.employment_status, person.monthly_salary, profession, person.company_name, person.company_size, person.industry, person.favorite_color, person.favorite_movie, person.favorite_music, person.favorite_song, person.favorite_book, person.favorite_sports, person.favorite_tv, person.favorite_movie_star, person.favorite_singer, person.favorite_food, person.credit_card_type, person.credit_card_number, person.cvv2, person.expires, person.paypal, person.western_union_mtcn, person.moneygram_mtcn, person.account_balance, person.preferred_payment, person.telephone, person.mobile, person.website, person.email, person.online_status, person.online_signature, person.online_biography, person.security_question, person.security_answer, person.browser_user_agent, person.height, person.weight, person.hair_color, person.blood_type, person.disease_history, person.civil_status, person.educational_background, person.social_security, person.passport, person.driver_license, person.car_license_plate, person.vehicle, person.register_time, person.register_ip, person.points, person.level, person.number_of_comments, person.posted_articles, person.friends, person.ups_tracking)

    time.sleep(0.5)
    print('%s Fetched information. The following is your Basic Identity' % info)
    time.sleep(0.5)
    print('%s %sName: %s%s' % (res, blue, end, person.name))
    time.sleep(0.5)    
    print('%s %sGender: %s%s' % (res, blue, end, final_gender_from_name))
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


    if final_gender_from_name == "male":
        os.mkdir(person.name)
        os.chdir(person.name)
        with open("%s.txt" % person.name, 'w') as file:
            file.write(data)
            file.close()
            print('%s More detailed information stored in %s./%s%s directory' % (info, green, person.name, end))
            sys.exit(0)
    else:
        print('%s The name has been detected to not be a MALE name. Fetching Again' % info)
        simpleinfogathermale()


def simpleinfogatherfemale():

    person = Person()
    print('%s Connecting to the internet' % info)
    time.sleep(0.5)
    print('%s Fetching Information' % info)


    a = str(person.name)
    name_split = a.split()
    df= name_split[0]
    d = gender.Detector(case_sensitive=False)
    final_gender_from_name = d.get_gender('%s' % df)


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
    
}}}}}}}}}}}\n ''' % (person.name, final_gender_from_name, person.birthday, person.zodiac, person.mother_maiden_name, person.family_members, person.personality, person.person_style, person.language, person.verified_status, person.country, person.country_code, person.street, person.geo_coordinates, person.timezone, person.employment_status, person.monthly_salary, person.occupation, person.company_name, person.company_size, person.industry, person.favorite_color, person.favorite_movie, person.favorite_music, person.favorite_song, person.favorite_book, person.favorite_sports, person.favorite_tv, person.favorite_movie_star, person.favorite_singer, person.favorite_food, person.credit_card_type, person.credit_card_number, person.cvv2, person.expires, person.paypal, person.western_union_mtcn, person.moneygram_mtcn, person.account_balance, person.preferred_payment, person.telephone, person.mobile, person.website, person.email, person.online_status, person.online_signature, person.online_biography, person.security_question, person.security_answer, person.browser_user_agent, person.height, person.weight, person.hair_color, person.blood_type, person.disease_history, person.civil_status, person.educational_background, person.social_security, person.passport, person.driver_license, person.car_license_plate, person.vehicle, person.register_time, person.register_ip, person.points, person.level, person.number_of_comments, person.posted_articles, person.friends, person.ups_tracking)

    time.sleep(0.5)
    print('%s Fetched information. The following is your Basic Identity' % info)
    time.sleep(0.5)
    print('%s %sName: %s%s' % (res, blue, end, person.name))
    time.sleep(0.5)    
    print('%s %sGender: %s%s' % (res, blue, end, final_gender_from_name))
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


    if final_gender_from_name == "female":
        os.mkdir(person.name)
        os.chdir(person.name)
        with open("%s.txt" % person.name, 'w') as file:
            file.write(data)
            file.close()
            print('%s More detailed information stored in %s./%s%s directory' % (info, green, person.name, end))
            sys.exit(0)
    else:
        print('%s The name has been detected to not be a FEMALE name. Fetching Again' % info)
        simpleinfogatherfemale()


def simpleinfogatherfemalewithprofession(profession):

    person = Person()
    print('%s Connecting to the internet' % info)
    time.sleep(0.5)
    print('%s Fetching Information' % info)


    a = str(person.name)
    name_split = a.split()
    df= name_split[0]
    d = gender.Detector(case_sensitive=False)
    final_gender_from_name = d.get_gender('%s' % df)


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
    
}}}}}}}}}}}\n ''' % (person.name, final_gender_from_name, person.birthday, person.zodiac, person.mother_maiden_name, person.family_members, person.personality, person.person_style, person.language, person.verified_status, person.country, person.country_code, person.street, person.geo_coordinates, person.timezone, person.employment_status, person.monthly_salary, profession, person.company_name, person.company_size, person.industry, person.favorite_color, person.favorite_movie, person.favorite_music, person.favorite_song, person.favorite_book, person.favorite_sports, person.favorite_tv, person.favorite_movie_star, person.favorite_singer, person.favorite_food, person.credit_card_type, person.credit_card_number, person.cvv2, person.expires, person.paypal, person.western_union_mtcn, person.moneygram_mtcn, person.account_balance, person.preferred_payment, person.telephone, person.mobile, person.website, person.email, person.online_status, person.online_signature, person.online_biography, person.security_question, person.security_answer, person.browser_user_agent, person.height, person.weight, person.hair_color, person.blood_type, person.disease_history, person.civil_status, person.educational_background, person.social_security, person.passport, person.driver_license, person.car_license_plate, person.vehicle, person.register_time, person.register_ip, person.points, person.level, person.number_of_comments, person.posted_articles, person.friends, person.ups_tracking)

    time.sleep(0.5)
    print('%s Fetched information. The following is your Basic Identity' % info)
    time.sleep(0.5)
    print('%s %sName: %s%s' % (res, blue, end, person.name))
    time.sleep(0.5)    
    print('%s %sGender: %s%s' % (res, blue, end, final_gender_from_name))
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


    if final_gender_from_name == "female":
        os.mkdir(person.name)
        os.chdir(person.name)
        with open("%s.txt" % person.name, 'w') as file:
            file.write(data)
            file.close()
            print('%s More detailed information stored in %s./%s%s directory' % (info, green, person.name, end))
            sys.exit(0)
    else:
        print('%s The name has been detected to not be a FEMALE name. Fetching Again' % info)
        simpleinfogatherfemale()


def simplewithprofession(profession):
    person = Person()
    print('%s Connecting to the internet' % info)
    time.sleep(0.5)
    print('%s Fetching Information' % info)


    a = str(person.name)
    name_split = a.split()
    df= name_split[0]
    d = gender.Detector(case_sensitive=False)
    final_gender_from_name = d.get_gender('%s' % df)




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
    
}}}}}}}}}}}\n ''' % (person.name, final_gender_from_name, person.birthday, person.zodiac, person.mother_maiden_name, person.family_members, person.personality, person.person_style, person.language, person.verified_status, person.country, person.country_code, person.street, person.geo_coordinates, person.timezone, person.employment_status, person.monthly_salary, profession, person.company_name, person.company_size, person.industry, person.favorite_color, person.favorite_movie, person.favorite_music, person.favorite_song, person.favorite_book, person.favorite_sports, person.favorite_tv, person.favorite_movie_star, person.favorite_singer, person.favorite_food, person.credit_card_type, person.credit_card_number, person.cvv2, person.expires, person.paypal, person.western_union_mtcn, person.moneygram_mtcn, person.account_balance, person.preferred_payment, person.telephone, person.mobile, person.website, person.email, person.online_status, person.online_signature, person.online_biography, person.security_question, person.security_answer, person.browser_user_agent, person.height, person.weight, person.hair_color, person.blood_type, person.disease_history, person.civil_status, person.educational_background, person.social_security, person.passport, person.driver_license, person.car_license_plate, person.vehicle, person.register_time, person.register_ip, person.points, person.level, person.number_of_comments, person.posted_articles, person.friends, person.ups_tracking)

    time.sleep(0.5)
    print('%s Fetched information. The following is your Basic Identity' % info)
    time.sleep(0.5)
    print('%s %sName: %s%s' % (res, blue, end, person.name))
    time.sleep(0.5)    
    print('%s %sGender: %s%s' % (res, blue, end, final_gender_from_name))
    time.sleep(0.5)
    print('%s %sBirthday: %s%s' % (res, blue, end, person.birthday))
    time.sleep(0.5)
    print('%s %sZodiac: %s%s' % (res, blue, end, person.zodiac))
    time.sleep(0.5)
    print('%s %sCountry: %s%s' % (res, blue, end, person.country))
    time.sleep(0.5)
    print('%s %sProfession: %s%s' % (res, blue, end, profession))
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
    with open("%s.txt" % person.name, 'w') as file:
       file.write(data)
       file.close()
       print('%s More detailed information stored in %s./%s%s directory' % (info, green, person.name, end))
       sys.exit(0)
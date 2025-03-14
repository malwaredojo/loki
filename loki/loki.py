#!/usr/bin/env python3
import argparse
from core.colours import green, end, bad, yellow, white, sarcastic
from core.simple import *
from core.simplewithpic import maininfogather
from core.social_media import create_social_accounts  # New module for social media

version = '0.0.1'

def args_func():
    parser = argparse.ArgumentParser(description="The Loki Framework v" + version, epilog="Automate Sock Puppet Creation")
    parser.add_argument('-s', '--simple', help='Simple Information Generator', dest='simple', action='store_true')
    parser.add_argument('-sp', '--simplewithpic', help='Simple Information Generation with Pic', dest='simplewithpic', action='store_true')
    parser.add_argument('-p', '--profession', help='Specify the Profession beforehand', dest='profession')
    parser.add_argument('-soc', '--social-create', help='Create Social Media Profiles (Facebook, Instagram, TikTok)', dest='socialmedia', action='store_true')
    parser.add_argument('-g', '--gender', choices=['male', 'female'], help='Specify the gender of the sock puppet', dest='gender')
    parser.add_argument('-n', '--nationality', help='Specify the nationality (e.g., US, UK, FR)', dest='nationality')
    parser.add_argument('-f', '--format', choices=['txt', 'json', 'csv'], default='txt', help='Output format (txt, json, csv)')
    parser.add_argument('-b', help='Print the banner', dest='bannerfunction', action='store_true')
    return parser.parse_args()

def bannerfunction():
    banner()

def banner():
    print('''%s
 The %s        _____  _     _ _____
     |      |     | |____/    |   %s
     |_____ |_____| |    \\_ __|__
                                  %sFramework v%s %s\n''' % (white, green, yellow, white, version, end))

def main():
    args = args_func()
    
    if args.simple:
        if args.gender == 'male':
            if args.profession:
                banner()
                simpleinfogathermalewithprofession(args.profession, nationality=args.nationality, output_format=args.format)
            else:
                banner()
                simpleinfogathermale(nationality=args.nationality, output_format=args.format)
        elif args.gender == 'female':
            if args.profession:
                banner()
                simpleinfogatherfemalewithprofession(args.profession, nationality=args.nationality, output_format=args.format)
            else:
                banner()
                simpleinfogatherfemale(nationality=args.nationality, output_format=args.format)
        elif args.profession:
            banner()
            simplewithprofession(args.profession, nationality=args.nationality, output_format=args.format)
        else:
            banner()
            simpleinfogather(nationality=args.nationality, output_format=args.format)

    elif args.simplewithpic:
        banner()
        maininfogather(args.gender, nationality=args.nationality, output_format=args.format)
    
    elif args.profession:
        banner()
        simplewithprofession(args.profession, nationality=args.nationality, output_format=args.format)

    elif args.bannerfunction:
        bannerfunction()
    
    elif args.socialmedia:
        banner()
        print('%s Creating social media accounts...' % info)
        person_data = simpleinfogather(nationality=args.nationality, output_format='dict')  # Get data as dict
        create_social_accounts(person_data)
    
    else:
        banner()
        help_statement = "Use '-h' or '--help' to see the options"
        exit('\n%s No argument(s) specified. ' % bad + help_statement + '\n')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit('\n%sExiting\n' % sarcastic)

#!/usr/bin/env python3
import argparse
from core.colours import green, end, bad, yellow, white, sarcastic
from core.simple import * 
from core.simplewithpic import maininfogather


version = '0.0.1'

def args_func():
    parser = argparse.ArgumentParser(description="The Loki Framework v" + version, epilog="Automate Sock Puppet Creation")
    parser.add_argument('-s','--simple',help='Simple Information Generator', dest='simple', action='store_true')
    parser.add_argument('-sp','--simplewithpic',help='Simple Information Generation with Pic', dest='simplewithpic', action='store_true')
    parser.add_argument('-p','--profession',help='Specify the Profession beforehand', dest='profession')
    parser.add_argument('-soc','--social-create',help='Simple Information Generation with Pic & Create Profiles on Facebook, Instagram, TikTok', dest='socialmedia', action='store_true')
    parser.add_argument('-g','--gender',choices=['male', 'female'], help='Specify the gender of the sock puppet', dest='gender')
    parser.add_argument('-b', help='Print the banner', dest='bannerfunction', action='store_true')
    return parser.parse_args()

def bannerfunction():
    banner()

def banner():
    print('''%s
 The %s        _____  _     _ _____
     |      |     | |____/    |   %s
     |_____ |_____| |    \_ __|__
                                  %sFramework v%s %s\n''' % (white, green, yellow, white, version, end))

def main():
    args = args_func()
    
    if args.simple == True:
        if args.gender == 'male':
            if args.profession is not None:
                banner()
                simpleinfogathermalewithprofession(args.profession)
            else:
                banner()
                simpleinfogathermale()
        
        elif args.gender == 'female':
            if args.profession is not None:
                banner()
                simpleinfogatherfemalewithprofession(args.profession)
            else:
                banner()
                simpleinfogatherfemale()

        elif args.profession is not None:
            banner()
            simplewithprofession(args.profession)
        
        else:
            banner()
            simpleinfogather()

    elif args.simplewithpic == True:
        banner()
        maininfogather() 
    
    elif args.profession is not None:
        banner()
        simplewithprofession(args.profession)

    elif args.bannerfunction == True:
        bannerfunction()
    elif args.socialmedia == True:
        banner()
        print('This feature is coming soon !!')

    else:
        banner()
        help_statement = "Use '-h' or '--help' to see the options"
        exit('\n%s No argument(s) specified. '  % bad + help_statement + '\n')
            

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit('\n%sExiting\n' % sarcastic)

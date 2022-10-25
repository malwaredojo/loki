#!/usr/bin/env python3
import argparse

from core.colours import green, end, bad, yellow, white, sarcastic
from core.simple import simpleinfogather, simplewithprofession
from core.simplewithpic import maininfogather


version = '0.0.1'


def args_func():
    parser = argparse.ArgumentParser(description="The Loki Framework v" + version, epilog="Automate Sock Puppet Creation")
    parser.add_argument('-s','--simple',help='Simple Information Generator', dest='simple', action='store_true')
    parser.add_argument('-sp','--simplewithpic',help='Simple Information Generation with Pic', dest='simplewithpic', action='store_true')
    parser.add_argument('-p','--profession',help='Specify the Profession beforehand', dest='profession')
    parser.add_argument('-soc','--social-create',help='Simple Information Generation with Pic & Create Profiles on Facebook, Instagram, TikTok', dest='socialmedia', action='store_true')
    parser.add_argument('-g','--gender',choices=['male', 'female'], help='Specify the gender of the sock puppet', dest='gender')
    return parser.parse_args()

def banner():
    print('''%s
 The %s        _____  _     _ _____
     |      |     | |____/    |   %s
     |_____ |_____| |    \_ __|__
                                  %sFramework v%s %s''' % (white, green, yellow, white, version, end))


def simple():
    banner()
    simpleinfogather()


def simplewithpic():
    banner()
    maininfogather()

def defined_profession(profession):
    banner()
    simplewithprofession(profession)


def main():
    args = args_func()
    
    if args.simple == True:
        if args.gender == 'male':
            print('Male')
        elif args.gender == 'female':
            print('Female')
        elif args.profession is not None:
            defined_profession(args.profession[0])
        else:
            simple()

    elif args.simplewithpic == True:
        simplewithpic() 
    
    elif args.profession is not None:
        defined_profession(args.profession[0])

    else:
        banner()
        help_statement = "Use '-h' or '--help' to see the options"
        exit('\n%s No argument(s) specified. '  % bad + help_statement + '\n')
            

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit('\n%sExiting\n' % sarcastic)
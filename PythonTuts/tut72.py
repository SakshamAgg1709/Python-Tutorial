# Command Line Utility in Python

import argparse #It helps in creating Command LIne Utility
import sys

# def calc(args):
#     if args.o == 'add':
#         return args.x + args.y
#     elif args.o == 'sub':
#         return args.x - args.y
#     elif args.o == 'mul':
#         return args.x * args.y
#     elif args.o == 'div':
#         return args.x/args.y
#     else:
#         return "Something Went Wrong"
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()#Argument Parser is class and we have created a object of this class
#     parser.add_argument('--x', type=float, default=1.0,
#                         help=" Enter frst Number. This is a utility for calculation. Please Contact Saksham for further discussion")
#     parser.add_argument('--y', type=float, default=3.0,
#                         help=" Enter Second number. This is a utility for calculation. Please Contact Saksham for further discussion")
#     parser.add_argument('--o', type=str, default= "add",
#                         help="This is a utility for calculation. Please Contact Saksham for further discussion")
#
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))

"""
This Command Utility can be used whenever you are working on  other programming languages and want to do any task in Python u can just call this command line utility inthat programm

We can run this utility in cmd or windows powershell - 

35.0


"""

"""Task -Faulty Calculator in command line"""

def calc2(args):
    if args.x == 45 and args.y == 3 and args.o == 'mul':
        return 555
    elif args.x == 56 and args.y == 9 and args.o == 'add':
        return 77
    elif args.x == 56 and args.y == 6 and args.o == 'div':
        return 4
    elif args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x/args.y

    else:
        return "Something Went Wrong"


if __name__ == '__main__':
    parser2 = argparse.ArgumentParser()#Argument Parser is class and we have created a object of this class
    parser2.add_argument('--x', type=float, default=1.0,
                        help=" Enter first Number. This is a utility for calculation. Please Contact Saksham for further discussion")
    parser2.add_argument('--y', type=float, default=3.0,
                        help=" Enter Second number. This is a utility for calculation. Please Contact Saksham for further discussion")
    parser2.add_argument('--o', type=str, default= "add",
                        help="This is a utility for calculation. Please Contact Saksham for further discussion")

    args = parser2.parse_args()
    sys.stdout.write(str(calc2(args)))
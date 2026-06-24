import argparse
from directory_fuzzer import directory_fuzz
from subdomain import subdomain_enum

def main():
    parser=argparse.ArgumentParser(description="Command line tool to find subdomain and directory brute forcing using custom wordlists",usage="python main.py -m <sub/dir> -u <example.com> -w </directory/wordlist.txt>")
    parser.add_argument("-m","--mode", metavar="",help="Mode of operation sub for subdomain enum and dir for directory brute forcing", required=True)
    parser.add_argument("-u", "--url", metavar="",help="Target domain or url eg: example.com")
    parser.add_argument("-w","--wordlist",metavar="",help="Path or wordlist file for brute force")
    args=parser.parse_args()

    if args.mode=="sub":
        subdomain_enum(args.url,args.wordlist)
    elif args.mode=="dir":
        directory_fuzz(args.url,args.wordlist)


if __name__=="__main__":
    main()
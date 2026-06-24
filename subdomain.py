import dns.resolver

def subdomain_enum(url,wordlist):
    try:
        with open(wordlist, "r") as f:
            line = f.readlines()
            print("====================  Brute forcing subdomain: ",url,"=====================")
            for l in line:
                l=l.strip()
                f_url=f"{l}.{url}"
                try:
                    if(dns.resolver.resolve(f_url,"A")):
                            print(f"{f_url} -> Found",sep=" ")
                except:
                    continue
    except FileNotFoundError:
        print(f"{wordlist} file not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__=="__main__":
    url = input("Enter the target URL: ")
    wordlist = input("Enter the path to the wordlist file: ")
    subdomain_enum(url, wordlist)
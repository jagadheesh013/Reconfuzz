import requests

def directory_fuzz(url,wordlist):
    st=[200,302,403,301,500]
    print("====================  Brute forcing directory: ",url,"=====================")

    try:
        with open(wordlist, "r") as f:
            line=f.readlines()
            for l in line:
                l=l.strip()
                f_url=f"https://{url}/{l}"

                try:
                    req=requests.get(f_url,timeout=2)
                    if req.status_code in st:
                        print(f"{f_url} -> {req.status_code}",sep=" ")
                except:
                    continue 

    except FileNotFoundError:
        print(f"{wordlist} file not found. Please check the path and try again.")

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__=="__main__":
    url = input("Enter the target URL: ")
    wordlist = input("Enter the path to the wordlist file: ")
    directory_fuzz(url, wordlist)
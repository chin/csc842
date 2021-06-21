import random
import re
import requests
import time
import sys

# urls not to retry
blacklist = ['"']
# list of desktop user agents for html requests from https://deviceatlas.com/blog/list-of-user-agent-strings
user_agents = {
        "win10inedge": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", 
        "chromeinchrome": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36", 
        "macinsafari": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9", 
        "win7inchrome": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36", 
        "linuxinfirefox": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
        }


def get_request(url, agent):
    r = requests.get(url, headers=agent)
    status_code = r.status_code
    if (status_code != 200):
        print("A bad request was made from {}.".format(agent))
    else:
        print("Another good request made.")
    return r


def search(rurl, d, agent):
    # using recursion deptite it being a bit dated
    #base case n = 0
    if d == 0:
        print("----base case reached")
        get_request(rurl, agent)
        return
    # n <= 1 cases
    else:
        print("----n+1 case reached")
        page = get_request(rurl, agent)
        if not page:
            print("Error loading web page. {} is being thrown out.".format(rurl))
            blacklist.append(rurl)
            return
        
        # https://stackoverflow.com/questions/15926142/regular-expression-for-finding-href-value-of-a-a-link
        links = re.findall('(?:href=[\'"])([:/.A-z?<_&\s=>0-9;-]+)', str(page.content))
        #if links is None:
        #    print("Error getting links from web page. {} is being thrown out.".format(rurl))
        #    blacklist.append(rurl)
        #    return
        #else:
        #    for l in links:
        #        if (l in blacklist):
        #            links = links.remove(l)
        #        if ("https://" not in l):
        #            print("----")
        #            print(l)
        #            print("----")
        #            links = links.remove(l)
        
        links = [i for i in links if "https://" in i]
        links = [i for i in links if i not in blacklist]
        print("----")
        print(links)
        print("----")

        if links is None or links == []:
            print("Error getting links from web page. {} is being thrown out.".format(rurl))
            blacklist.append(rurl)
            return 
        # must wait between click like people do
        wait = random.choice(range(5,20))
        rurl = random.choice(links)
        print("Clicking {} in {} seconds.".format(rurl, wait))
        time.sleep(wait)
        search(rurl, d-1, agent)


if __name__ == '__main__':
    # 41 most visited domains according to https://ahrefs.com/blog/most-visited-websites/ minus social medias
    urls = ["en.wikipedia.org", "www.youtube.com", "www.amazon.com", "www.fandom.com", "www.imdb.com", "www.reddit.com", "www.yelp.com", "www.ebay.com", "www.walmart.com", "craigslist.org", "www.healthline.com", "www.tripadvisor.com", "www.webmd.com", "www.netflix.com", "www.apple.com", "www.homedepot.com", "mail.yahoo.com", "www.cnn.com", "www.etsy.com", "www.google.com", "www.yahoo.com/?gccounter=1", "www.indeed.com", "www.target.com", "www.microsoft.com/en-us/?spl=2", "www.nytimes.com", "www.mayoclinic.org", "www.espn.com", "www.usps.com", "quizlet.com", "www.gamepedia.com", "www.lowes.com", "www.irs.gov", "www.nih.gov", "www.merriam-webster.com", "store.steampowered.com", "www.mapquest.com"]
    if len(sys.argv) != 1:
        print("You are doing too much.\n Usage: <script name>\nTHis iscript is not accepting arguements at this time.\n")
        exit(1)
    else:
        # continue with your normal programing
        print("Randomly selecting root url for dive from top {} most visited domains.".format(len(urls)))
        root_url = "https://" + random.choice(urls)
        depth = random.choice(range(1,20))
        agent = random.choice(list(user_agents.values()))
        agent = {"my_agent": agent}
        print ("From the root url {} there will be {} random clicks and the resulting url will be returned.".format(root_url, depth))
        search(root_url, depth, agent)

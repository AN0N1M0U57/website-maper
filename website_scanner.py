#!/usr/bin/env python

import requests
import re
import urlparse

class main:

    target_links = []

    def extract_links(self, url):
        respons = requests.get(url)
        return re.findall('(?:href=")(.*?)"', respons.content)

    def crawl(self, url):
        href_links = self.extract_links(url)
        for i in href_links:
            i = urlparse.urljoin(url, i)

            if "#" in i:
                i = i.split("#")[0]

            if (url in i) and (i not in self.target_links):
                self.target_links.append(i)
                print(i)
                self.crawl(i)
    
    def run_http(self):
        url = raw_input("Insert website: http://")
        if url == "0":
            run()
        else:
            target_url = "http://" + url
            self.crawl(target_url)
    
    def run_https(self):
        url = raw_input("Insert website: https://")
        if url == "0":
            run()
        else:
            target_url = "https://" + url
            self.crawl(target_url)

class main2:

    def request(self,url):
        try:
            return requests.get("http://" + url)
        except requests.exceptions.ConnectionError:
            pass

    def find_subdomains(self,url):
        with open("/root/Desktop/test/website-hacking/wordlists/name.txt", "r") as wordlist:
            for line in wordlist:
                word = line.strip()
                test_url = word + "." + url
                response = self.request(test_url)
                if response:
                    print("[+] Discovered subdomain >> " + test_url)

    def find_urls(self,url):
        with open("/root/Desktop/test/website-hacking/wordlists/big.txt", "r") as wordlist:
            for line in wordlist:
                word = line.strip()
                test_url = url + "/" + word
                response = self.request(test_url)
                if response:
                    print("[+] Discovered URL >> " + test_url)

    def run_subdoamins(self):
        target_url = raw_input("Insert website: ")
        if target_url == "0":
            run()
        else:
            self.find_subdomains(target_url)
        
    def run_url(self):
        target_url = raw_input("Insert website: ")
        if target_url == "0":
            run()
        else:
            self.find_urls(target_url)
            


try:
    

    def run():
        print("This script is created by AN0N1M0U5\nScaning target site")
        print("\n")
        print("[1] Find subdomains")
        print("[2] Find URLs")
        print("[3] Map site")
        print("[4] Exit")
        print("\n\n")
        option = raw_input("Insert option to use:")

        sitemap = main()
        urls = main2()
        if option == "1":
            print("\n")
            print("[0] Go Back")
            print("\n\n")
            urls.run_subdoamins()
        elif option == "2":
            print("\n")
            print("[0] Go Back")
            print("\n\n")
            urls.run_url()
        elif option == "3":
            print("\n")
            print("[1] Use HTTP")
            print("[2] Use HTTPS")
            print("[3] Go Back")
            print("[4] Exit")
            print("\n\n")
            option2 = raw_input("Chouse option: ")
            if option2 == "1":
                print("\n")
                print("[0] Go Back")
                print("\n\n")
                sitemap.run_http()
            elif option2 == "2":
                print("\n")
                print("[0] Go Back")
                print("\n\n")
                sitemap.run_https()
            elif option2 == "3":
                run()
            elif option2 == "4":
                print("[+] Exiting.....")
                exit()

        elif option == "4":
            print("[+] Exiting.....")
            exit()
    run()


except KeyboardInterrupt:
    print("[+] Program stopped!")
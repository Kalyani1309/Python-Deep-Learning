# import required libraries
from bs4 import BeautifulSoup
import requests


# Define Class WikiScrapping
class WikiScrapping:
    # function attributes
    url = "https://en.wikipedia.org/wiki/Machine_learning"
    source_doc = requests.get(url)
    soup = BeautifulSoup(source_doc.content, "html.parser")

    # Function to return the title of the page
    def get_title(self):
        # Return title of the page
        return self.soup.title.string

    # Function to return the links on the wiki page
    def get_wiki_links(self):
        link_list = []
        # Find all the links in the page (‘a’ tag)
        for link in self.soup.findAll('a'):
            # Iterate over each tag then return the link using attribute "href"
            link_list.append(link.get("href"))
        return link_list


# Object instantiation of WikiScrapping class
web = WikiScrapping()
# Printing the output on the console by calling the methods
print("Title of the web page: " + web.get_title())
print("\nAll the links with href attribute: {}".format(web.get_wiki_links()))

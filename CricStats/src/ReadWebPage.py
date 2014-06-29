import urllib2
from HTMLParser import HTMLParser

response = urllib2.urlopen('file:///Users/venkatakrishnanemana/Code/cricstats/SampleScoresheet.html')
html = response.read()


class MyHtmlParser (HTMLParser):
    is_table = False

    def handle_starttag(self, s_tag, attrs):
        if s_tag == 'table':
            self.is_table = True
        print "Encountered a start tag:", s_tag

    def handle_data(self, data):
        if self.is_table is True:
            print "Encountered some data  :", data

    def handle_endtag(self, tag):
        if self.is_table is True:
            print "Encountered an end tag :", tag
            self.is_table = False

parser = MyHtmlParser()
parser.feed(html)

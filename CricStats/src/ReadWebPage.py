import urllib2
from HTMLParser import HTMLParser

response = urllib2.urlopen ('http://www.espncricinfo.com/new-zealand-v-west-indies-2013-14/engine/match/683779.html?wrappertype=print');
html = response.read();

class myHtmlParser (HTMLParser):
    is_table = False;
    def handle_starttag(self, s_tag, attrs):
        if (s_tag == 'table'):
            self.is_table = True;
        print "Encountered a start tag:", s_tag
    def handle_data(self, data):
        if (self.is_table == True):
            print "Encountered some data  :", data
    def handle_endtag(self, tag):
        if (self.is_table == True):
            print "Encountered an end tag :", tag
            self.is_table = False;

parser = myHtmlParser()
parser.feed(html)

#adding a comment
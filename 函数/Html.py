
# -*- coding: utf-8 -*-


from html.parser import HTMLParser
from urllib import request

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._title = [False]
        self._time = [False]
        self._place = [False]
        self.time = ''
        
    def _attr(self, attrlist, attrname):
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
        return None
    
    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and self._attr(attrs, 'class') == 'event-title':
            self._title[0] = True
        if tag == 'time':
            self._time[0] = True
        if tag == 'span' and self._attr(attrs, 'class') == 'event-location':
            self._place[0] = True
            
    def handle_endtag(self, tag):
        if tag == 'time':
            self._time.append(self.time)
            self.time = ''
            self._time[0] = False
    
    def handle_startendtag(self, tag, attrs):
        pass
    
    def handle_data(self, data):
        if self._title[0]:
            self._title.append(data)
            self._title[0] = False
        if self._time[0]:
            self.time += data 
        if self._place[0]:
            self._place.append(data)
            self._place[0] = False
            
    def handle_comment(self, data):
        pass
    
    def handle_entityref(self, name):
        if self._time[0]:
            self.time += '-'
            
    def handle_charref(self, name):
        print('&#%s;' % name)
        
    def show_content(self):
        for n in range(1, len(self._title)):
            print('Title: %s' % self._title[n])
            print('Time:  %s' % self._time[n])
            print('Place: %s' % self._place[n])
            print('---------------------------------')

url = 'https://www.python.org/events/python-events/'
req = request.Request(url)
with request.urlopen(req) as f:
    html = f.read().decode('utf-8')

parser = MyHTMLParser()
parser.feed(html)
parser.show_content()



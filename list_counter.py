from html.parser import HTMLParser

class ListCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current_list_count = 0
        self.max_list_count = 0
        self.in_ul = False
        self.current_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
            if not self.in_ul:
                self.in_ul = True
                self.current_list_count = 0
            else:
                self.current_depth += 1
        elif tag == 'li' and self.in_ul and self.current_depth == 0:
            self.current_list_count += 1

    def handle_endtag(self, tag):
        if tag == 'ul':
            if self.current_depth > 0:
                self.current_depth -= 1
            else:
                self.max_list_count = max(self.max_list_count, self.current_list_count)
                self.in_ul = False
                self.current_list_count = 0
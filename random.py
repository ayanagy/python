
import webbrowser
from random import choice


random_page_generator = ['http://www.randomwebsite.com/cgi-bin/random.pl',
                         'http://www.uroulette.com/visit']


webbrowser.open(choice(random_page_generator), new=2)
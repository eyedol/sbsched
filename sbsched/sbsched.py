# coding: utf-8

from bs4 import BeautifulSoup

import urllib
import re

class Showings:

	def __init__(self):
		movie_title = ''
		self.times = []

	def __str__(self):
		return u'{} \n {}'.format(self.movie_title, self.times)
	__repr__ = __str__

class Schedule:

	def __init__(self):
		cinema = ''
		duration = ''
		self.showings = []
		self.movies = []

	def __str__(self):
		return u'{} \n {} \n {} \n {}'.format(self.cinema, self.duration, self.showings, self.movies)

class Sbsched:
	
	def __init__(self, cinema):
		self.cinema = cinema

	def crawl(self):
		r = urllib.urlopen('http://silverbirdcinemas.com/'+self.cinema).read()
		soup = BeautifulSoup(r, 'html.parser')
			
		# Fetch the movie playing date duration
		regex = "views-row-\d+"
		pattern = re.compile(regex)
		rows = re.findall(pattern,r)
		schs = []
		sc = Schedule()
		sc.cinema = self.cinema
		sc.duration = soup.select('div.field-content > p')[0].get_text()
		movies = soup.select('div.views-field-title > span.field-content > a')
		
		for movie in movies[:-5]:
			sc.movies.append(movie.get_text())

		for row in rows[1:-1]:
			movies = soup.select('div.'+row+' > div.views-field-title > span.field-content > a')
			show_times = soup.select('div.'+row+' > div.views-field > div.field-content > div.showtime_day')
			showing = Showings()
			showing.movie_title = movies[0].get_text()
			for show_time in show_times:
				showing.times.append(show_time.get_text())
			sc.showings.append(showing)
		return sc

import csv
import random

# average movie ticket prices from: http://www.nationmaster.com/au
# box office collection from: boxofficemojo.com

# assumptions
# row1 = 0 => 1 (both reference and tested have equal trend)
# row2 = 0 => 0.5/row1 (occurs when movie is higly trending, so reference  = 0) 
# random select 3 genre if >3 for a movie
# genre rating varies from country to country.

c = ['Germany', 'United Kingdom', 'United States', 'Mexico', 'France', 'Australia']

# The lesser the value, better the perfomance.

# DATASET format: [movie rating, director rating, actor1 rating, actor2 rating, genre1 rating, genre2 rating, genre3 rating, gross earnings]

germany=[[1]]*112
us=[[1]]*112
aus=[[1]]*112
uk=[[1]]*112
mex=[[1]]*112
france=[[1]]*112

l=[[0.00]]*112

'''
	[movie, director, actor1, actor2]
'''

# Laod the country from imdb dataset (kaggle)
meta_reader = csv.reader(open('movie_metadata.csv', 'r'))
l={}
flg=1
i=1
for row1 in meta_reader:
	if flg==1:
		flg=2
		continue
	# print row1
	l[row1[0][:len(row1[0])-2]] = row1[1:]
	i+=1
# the key of the created dict l is the movie name
# ==============   Loading Genres and creating mapper   ============== #



# This will load the movie genre's into a list gl corresponding to movie's index
movie_genre =[]
for nm in l.keys()[1:]:	# We are skipping the first movie. 
	print nm
	gl=l[nm][7].split("|")
	if len(gl)>3:								# if more than 3 genre's available we choose a subset of 3 elements
		templ = []
		while len(templ)!=3:
			ind1 = int(random.random()*len(gl))
			if ind1 not in templ:
				templ.append(ind1)
			# ind2 = int(random.random()*len(gl))
		gl[0] = gl[templ[0]]
		gl[1] = gl[templ[1]]
		gl[2] = gl[templ[2]]
		gl = gl[0:3]
	elif len(gl)==2:							# two genre's availabe, we repeat one of them
		ind = int(random.random()*len(gl))
		gl.append(gl[ind])
	elif len(gl)==1:							# only 1 genre available, we repeat it.
		gl = gl*3
	movie_genre.append(gl)
	# text_file.write(str(gl)+"\n")
# print (movie_genre)


# ==============   CREATING THE DATASET   ============== #


#####
#####

# print(len(l[1:])) = length of raw data

# print l.keys()[1:] = print the movie name, in order of geoMap file.

# print the year in order of the geomap file
#for x in l.keys()[1:]:
#	print l[x][3]




#####
#####



# Parse the movie ratings
for i in range(0, 112):   # len(l.keys) - 1 = 113
	fname = 'movie/geoMap ('+str(i)+').csv'

	reader = csv.reader(open(fname, 'r'))
	for row in reader:
		flag =0
		if len(row)<2:
			continue
		if row[0] == c[0]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			germany[i]=([round(ind, 4)])
		elif row[0] == c[1]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			uk[i]=([round(ind, 4)])
		elif row[0] == c[2]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			us[i]=([round(ind, 4)])
		elif row[0] == c[3]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			mex[i]=([round(ind, 4)])
		elif row[0] == c[4]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			france[i]=([round(ind, 4)])
		elif row[0] == c[5]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			aus[i]=([round(ind, 4)])


# Parse the director ratings
for i in range(0, 112):
	fname = 'director/geoMap('+str(i)+').csv'

	reader = csv.reader(open(fname, 'r'))
	for row in reader:
		if len(row)<2:
			continue
		if row[0] == c[0]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			germany[i].append(round(ind, 4))
			germany[i]=[germany[i][0], germany[i][-1]]
		elif row[0] == c[1]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			uk[i].append(round(ind, 4))
			uk[i]=[uk[i][0], uk[i][-1]]
		elif row[0] == c[2]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			us[i].append(round(ind, 4))
			us[i]=[us[i][0], us[i][-1]]
		elif row[0] == c[3]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			mex[i].append(round(ind, 4))
			mex[i]=[mex[i][0], mex[i][-1]]
		elif row[0] == c[4]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			france[i].append(round(ind, 4))
			france[i]=[france[i][0], france[i][-1]]
		elif row[0] == c[5]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			aus[i].append(round(ind, 4))
			aus[i]=[aus[i][0], aus[i][-1]]

for i in range(0, 112):
	fname = 'actor1/geoMap ('+str(i)+').csv'

	reader = csv.reader(open(fname, 'r'))
	for row in reader:
		if len(row)<2:
			continue
		if row[0] == c[0]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			germany[i].append(round(ind, 4))

		elif row[0] == c[1]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			uk[i].append(round(ind, 4))
		elif row[0] == c[2]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			us[i].append(round(ind, 4))
		elif row[0] == c[3]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			mex[i].append(round(ind, 4))
		elif row[0] == c[4]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			france[i].append(round(ind, 4))
		elif row[0] == c[5]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			aus[i].append(round(ind, 4))

# Parse the actor ratings
for i in range(0, 112):
	fname = 'actor2/geoMap('+str(i)+').csv'

	reader = csv.reader(open(fname, 'r'))
	for row in reader:
		if len(row)<2:
			continue
		if row[0] == c[0]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			germany[i].append(round(ind, 4))
		elif row[0] == c[1]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			uk[i].append(round(ind, 4))
		elif row[0] == c[2]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			us[i].append(round(ind, 4))
		elif row[0] == c[3]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			mex[i].append(round(ind, 4))
		elif row[0] == c[4]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			france[i].append(round(ind, 4))
		elif row[0] == c[5]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])
			aus[i].append(round(ind, 4))


# Creating genre rating map for countries.
germanyGen = {}
ukGen = {}
usGen = {}
mexGen = {}
franceGen = {}
ausGen = {}
for i in range(0, 24):
	fname = 'genres/geoMap ('+str(i)+').csv'

	reader = csv.reader(open(fname, 'r'))
	gen = 'temp'
	for row in reader:
		# print row
		if len(row)<3:
			continue
		if row[0] == 'Country':
			gen = row[2][0:row[2].index(' ')]
			if gen[len(gen)-1] == ':':
				gen = gen[:-1]
			if gen == 'Romantic':
				gen = 'Romance'
			if gen == 'Science':
				gen = 'Sci-Fi'
			if gen == 'Animated':
				gen = 'Animation'
			if gen == 'Biographical':
				gen = 'Biography'
			if gen == 'Sports':
				gen = 'Sport'
			# print gen
			continue

		if row[0] == c[0]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])	
			germanyGen[gen]=round(ind, 4)
		elif row[0] == c[1]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])	
			ukGen[gen]=round(ind, 4)
		elif row[0] == c[2]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])	
			usGen[gen]=round(ind, 4)
		elif row[0] == c[3]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])	
			mexGen[gen]=round(ind, 4)
		elif row[0] == c[4]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])	
			franceGen[gen]=round(ind, 4)
		elif row[0] == c[5]:
			if int(row[2]) == 0:
				ind = float(row[1])/0.5
			elif int(row[1]) == 0:
				ind = 0.5/float(row[2])
			else:
				ind = float(row[1])/int(row[2])	
			ausGen[gen]=round(ind, 4)

# Now we add the genre rating's to the final list.

for i in range(0, 112):		# for 112 movies
	for j in range(0, 3):	# 3 genre for each movie
		germany[i].append(germanyGen[movie_genre[i][j]])
		us[i].append(usGen[movie_genre[i][j]])
		aus[i].append(ausGen[movie_genre[i][j]])
		uk[i].append(ukGen[movie_genre[i][j]])
		mex[i].append(mexGen[movie_genre[i][j]])
		france[i].append(franceGen[movie_genre[i][j]])


# ==============   Loading Gross amount and assign country wise   ============== #

avgTicket = [12.29, 13.30, 10.00, 4.50, 12.29, 15.19]
# avgTicket = [1]*6

count_nm = ['Germany.txt', 'UK.txt', 'US.txt', 'Mexico.txt', 'France.txt', 'aus.txt']
countries = [germany, uk, us, mex, france, aus]

for k in range(len(count_nm)):
	box_office=[[],[]]
	reader = (open('gross/'+count_nm[k], 'r'))
	for row in reader:
		if len(row)<4:
			continue
		try:
			tt = (row.split("	"))[1:4]
			ttn = tt[0]
			ttg = int(tt[2][1:].replace(",", ""))
			# print tt
			box_office[0].append(ttn)
			box_office[1].append(ttg)
		except Exception, e:
			continue
	# print box_office[0]
	# counter = 0
	for i in range(0, 112): 
		if l.keys()[i] in box_office[0]:
			indx = box_office[0].index(l.keys()[i])
 			countries[k][i].append(round(box_office[1][indx]/avgTicket[k], 4))
		else:
			countries[k][i].append(0)



us[14][7] = 13017907.2
us[15][7] = 13017907.2



################################################################################################################

# print len(germany)
# print len(us)
# print len(aus)
# print len(uk)
# print len(mex)
# print len(france)

# import numpy
# import os
# nnn = numpy.array(uk)

# nnn.tofile("uk_numpy", dtype = det)

# ppp = numpy.fromfile("uk_numpy")
# print numpy.ndim(ppp)
# print numpy.ndim(nnn)

# To print the complete dataset for single country.
#for u in uk:
#	print u

# To print the complete dataset for 6 movies.
# for j in range(len(countries)):
# 	print "\n\n\nThe DATASET for "+ c[j]+ " is:\n\n"
# 	for i in range(112):
# 		print l.keys()[i], countries[j][i]
################################################################################################################


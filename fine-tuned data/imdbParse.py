import csv

reader = csv.reader(open('movie_metadata.csv', 'r'))
l={}
c=1
for row in reader:
	if c==1:
		c=2
		continue
	print row
	l[row[0][:len(row[0])-2]] = row[1:]

text_file = open("movie_name.txt", "w")
for nm in l.keys()[1:]:
	text_file.write(nm+"\n")
text_file.close()

text_file = open("movie_name_trailer.txt", "w")
for nm in l.keys()[1:]:
	text_file.write(nm+" trailer\n")
text_file.close()

text_file = open("movie_director.txt", "w")
for nm in l.keys()[1:]:
	text_file.write(l[nm][0]+"\n")
text_file.close()

text_file = open("movie_actor1.txt", "w")
for nm in l.keys()[1:]:
	text_file.write(l[nm][1]+"\n")
text_file.close()

text_file = open("movie_actor2.txt", "w")
for nm in l.keys()[1:]:
	text_file.write(l[nm][2]+"\n")
text_file.close()

text_file = open("movie_year.txt", "w")
for nm in l.keys()[1:]:
	text_file.write(l[nm][3]+"\n")
text_file.close()

text_file = open("movie_genre.txt", "w")
for nm in l.keys()[1:]:
	text_file.write(str(l[nm][7].split("|"))+"\n")
text_file.close()


genre = []
text_file = open("list_genre.txt", "w")
for nm in l.keys()[1:]:
	genre += (l[nm][7].split("|"))
genre = (set(genre))
for g in genre:
	text_file.write(g+"\n")
text_file.close()


reader = open("list_genre.txt", "r")
for row in reader:
	print row[:len(row)-1]





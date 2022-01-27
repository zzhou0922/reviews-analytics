data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:	
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print('The file is read. There are', len(data), 'reviews.')

sum_len = 0
for d in data:
	sum_len += len(d)
average = sum_len / len(data)
print('The average length of all reviews are', average)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new), 'reviews less than 100 in length.')

# good =[]
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('There are', len(good), 'reviews containing "good".')

# Below is a shorten method for the above function
good = [d for d in data if 'good' in d]
print(good)
# print('There are', len(good), 'reviews containing "good".')

# Below will print True or False 1 million times. 
bad = ['bad' in d for d in data]
print(bad)

# word count
wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # Add new key to wc dict
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('Which word would you like to search: ')
	if word == 'q':
		break
	if word not in wc:
		print('This word does not exist in all the reviews. Please search the other word.')
		continue
	print('The number of times', word, 'appeared was', str(wc[word]) + '.')
print('Thank you for use this search function.')


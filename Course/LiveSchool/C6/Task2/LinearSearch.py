def main():
	#Ask for input set given country find
	find = input("Enter a country: ")
	LinearSearch(find)

#Define LinearSearch with argument that is being searched for
def LinearSearch(find):
	#Create countriesEU array filled with 12 countries from eu		
	countriesEu = ["Great Britain", "France", "Iceland", "Ireland", "Spain", "Poland", "Portugal", "Slovakia", "Italy", "Sweden", "Switzerland", "Germany"]
	#For every element in countriesEu	
	for i in range(0, len(countriesEu)):
		#If element is == to the one being looked for
		if countriesEu[i] == find:
			#Print found message and return out of function	
			print("Found {} at point {}.".format(countriesEu[i], i))
			return
	#If its been through every element and can't find the one being looked for print could not be found message
	print("{} could not be found.".format(find))

if __name__ == "__main__":
	main()
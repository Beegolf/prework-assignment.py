#Question_1

def hello_name(user_name):
    print("Hello, " + user_name.title() + "!")

hello_name('Stella')

#Question_2

def first_odds():
    first_odds = list(range(1,100,1))
    print(first_odds)

#Question_3

def max_num_in_list(a_list):
    max = a_list[0]
    for i in list:
        if i > max:
            max = i
    return max
#3-1
    a_list = [28, 85, 105, 286]
        print(max_num_in_list(a_list))


# Question_4

    def is_leap_year(a_year):
	    if (a_year % 4) == 0:
		    if (a_year % 100) == 0:
			    if (a_year % 400) == 0:
				    return True
			    else:
				    return False
		    else:
			    return True
	    else:
		    return False

# Question 4 part 1
year = 5000
if(is_leap_year(a_year)):
	print("Leap Year")
else:
	print("Not a Leap Year")


#Question 5

def is_consecutive(a_list):
    a_list = [2, 5, 6, 3, 8]
	return sorted(a_list) == list(range(min(0), max(0)+1))
print(is_consecutive(a_list))
  

	

 

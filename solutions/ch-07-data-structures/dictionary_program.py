#####################################################################
#
# The essence of this practice is to create this data structure here:
#
d = {
    'Sam': 7,
    'rolls': ['rock', 'paper', 'scissors'],
    'done': True
}

#####################################################################
#
# This is unchanged from the instructions,
# sans formatting and display of output of expected.
# \t means tab in Python strings.
#

print(d["Sam"], "\t\t\t\t\t\t\t\t# <- outputs 7?")
print(d['rolls'], "\t# <- outputs ['rock', 'paper', 'scissors']?")
print(d.get('Sarah'), "\t\t\t\t\t\t\t# <- outputs None?")
print(d.get('Jeff', -1), "\t\t\t\t\t\t\t\t# <- outputs -1?")
print(d['done'], "\t\t\t\t\t\t\t# <- outputs True?")

####################################################################
# Output when running this:
#
# 7 								# <- outputs 7?
# ['rock', 'paper', 'scissors'] 	# <- outputs ['rock', 'paper', 'scissors']?
# None 							    # <- outputs None?
# -1 								# <- outputs -1?
# True 							    # <- outputs True?

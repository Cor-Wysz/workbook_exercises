with_a_newline = "\n"
x = "1 2 3 4"
y = "one two three four"
z = "True False False True"
xyz_list = [x, y, z]
format_xyz = with_a_newline.join(xyz_list)
 
with_a_space = " " 
these_braces = ["{}"] * 16
sixteen_curlybraces = with_a_space.join(these_braces)
 
line1 = "Try your"
line2 = "Own text here"
line3 = "Maybe a poem"
line4 = "Or a song about fear"
lines = [line1, line2, line3, line4]
improvised_text = with_a_space.join(lines)
 
these_statements = [format_xyz, sixteen_curlybraces, improvised_text]
ex_8_text = with_a_newline.join(these_statements) 

print(ex_8_text)

<<<<<<< HEAD
=======
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))

print(formatter.format(
	"I shall try my text here",
	"What I write, hopefully clear",
	"Free of syntax error",
	"And all I do fear"
))

>>>>>>> cc1736f9e499836153685155978f77dcb40f88b6

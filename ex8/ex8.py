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

my_poem_line1 = "I shall try my text here"
my_poem_line2 =	"What I write, hopefully clear"
my_poem_line3 =	"Free of syntax error"
my_poem_line4 =	"And all I do fear"
poem_lines = [my_poem_line1, my_poem_line2, my_poem_line3, my_poem_line4]
my_poem = with_a_space.join(poem_lines)
print(my_poem)


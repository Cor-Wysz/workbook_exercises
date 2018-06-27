tab = "\t"
tab_line = "I'm tabbed in"
tabby_cat = (tab + tab_line)
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
with_a_newline = "\n"

fat_line = " "
fat_line1 = "I'll do a list:"
fat_line2 = "\t* Cat food"
fat_line3 = "\t* Fishies"
fat_line4 = "\t* Catnip\n\t* Grass"
fat_lines = [fat_line, fat_line1, fat_line2, fat_line3, fat_line4]
fat_cat = with_a_newline.join(fat_lines)

cat_list = [tabby_cat, persian_cat, backslash_cat, fat_cat]


format_catlist = with_a_newline.join(cat_list)

print(format_catlist)


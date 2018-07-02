tab = "\t"
tab_line = "I'm tabbed in"
tabby_cat = (tab + tab_line)
persian_cat1 = "I'm split"
persian_cat2 = "on a line."
backslash_cat = "I'm \\ a \\ cat."
with_a_newline = "\n"

bullet_point = "* "
bullet_line = (with_a_newline + tab + bullet_point)

list_1 = (with_a_newline + "I'll do a list:")
list_2 = "Cat food"
list_3 = "Fishies"
list_4 = "Catnip"
list_5 = "Grass"
fat_list = [list_1, list_2, list_3, list_4, list_5]
fat_cat = bullet_line.join(fat_list)

cat_list = [tabby_cat, persian_cat1, persian_cat2, backslash_cat, fat_cat]

tabbed_catlist = tab.join(cat_list)
ex_10 =  with_a_newline.join(cat_list)


print(ex_10)


str_ = input()
str_replace = str_.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
print(str_replace.lower())

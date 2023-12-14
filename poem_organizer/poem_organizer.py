# Original string of poems with details
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925, Georgia Dusk:Jean Toomer:1923, Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# Print the original string
print(highlighted_poems)
print("==============================================================")

# Split the string into individual poem details
highlighted_poems_list = highlighted_poems.split(",")
# Print the list of poem details
print(highlighted_poems_list)
print("==============================================================")

# Create an empty list for stripped poem details
highlighted_poems_stripped = []
# Iterate through each poem detail and strip leading and trailing spaces
for i in highlighted_poems_list:
  stripped_string = i.strip()
  highlighted_poems_stripped.append(stripped_string)
  print(highlighted_poems_stripped)

print("==============================================================")

# Create an empty list for detailed poem information
highlighted_poems_details = []
# Iterate through each stripped poem detail
for index in highlighted_poems_stripped:
  # Split each detail into title, author, and publication year
  poem_details = index.split(":")
  highlighted_poems_details.append(poem_details)

# Print the detailed poem information
print(highlighted_poems_details)
print("==============================================================")

# Create empty lists for titles, poets, and dates
titles = []
poets = []
dates = []

# Iterate through the detailed poem information
for item in highlighted_poems_details:
  # Append title, poet, and date to their respective lists
  titles.append(item[0])
  poets.append(item[1])
  dates.append(item[2])

# Print the lists of titles, poets, and dates
print(titles)
print("==============================================================")
print(poets)
print("==============================================================")
print(dates)

# Iterate through the number of poems
for i in range(len(titles)):
    # Print a formatted string for each poem's details
    print("The poem {title} was published by {poet} in {date}.".format(title=titles[i], poet=poets[i], date=dates[i]))

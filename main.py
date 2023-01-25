import feedparser
import pandas as pd

url = input("Please enter the RSS feed URL: ")

university_name = input("Please enter the name of the university: ")

# Open the file with read only permit
keywordIO = open("keywords.txt", "r")

# use readlines to read all lines in the file and load into a list
keywords = keywordIO.readlines()

# This hashmap will store the link of papers and the number of times it has been found
paper_link_map = {}

line_count = 0

# Read the RSS feed with all the keywords and append to CSV file
for keyword in keywords:
    keyword = keyword.strip()
    data_source = feedparser.parse(url.replace("[keyword]",  keyword.replace(" ", "+")))
    print("\nScanning " + university_name + " thesis database for keyword: " + keyword + " ...")
    
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['title', 'link', 'description', 'keyword', 'university'])

    # Write the data
    for entry in data_source.entries:
        # Store the papers in the hashmap
        try:
            if entry.link in paper_link_map:
                paper_link_map[entry.link].append(line_count)
            else:
                paper_link_map[entry.link] = [line_count]

            print("Title: " + entry.title)
            # Create a new row of data
            new_row = {'title': entry.title, 'link': entry.link, 'description': entry.description, 'keyword': keyword, 'university': university_name}

            # Add the new row to the DataFrame
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

            line_count += 1
        except:
            print("Error adding: " + entry.title)
        
    # Append the new data to the CSV file
    df.to_csv(university_name.replace(" ", "_")+'.csv', mode='a', header=False, index=False)



# Close the file
keywordIO.close()

print("Merging duplicates...")

# Open the CSV file
df = pd.read_csv(university_name.replace(" ", "_")+ '.csv', names=['title', 'link', 'description', 'keyword', 'university'])

# Clean up CSV file by merging papers with the same link
for key, value in paper_link_map.items():
    # Stores the raw string of keywords
    newVal = ""

    # Stores all the keywords associated with that research paper
    keywords = []

    # Stores the duplicates in a dataframe
    duplicates = pd.DataFrame(df[df['link']==key])

    # Gets all associated keywords with that research paper
    for index, row in duplicates.iterrows():
        keywords.append(row['keyword'])

    # Constructs the keyword field
    for keyword in keywords:
        newVal += keyword + ";"

    # Edits the first row of the duplicates\
    df.at[value[0], 'keyword'] = newVal

# Remove duplicates
df.drop_duplicates(keep='first', subset=['link'], inplace=True)

# Write the new data to the CSV file
df.to_csv(university_name.replace(" ", "_")+ '.csv', mode='w', header=True, index=False)

print("Added " + str(len(df.index)-1) + " entries to the CSV file.")


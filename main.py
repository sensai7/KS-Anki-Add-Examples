import pandas as pd
from colored import Fore, Style
from func import *
import time
import re

# how to: From anki hit File > Export and export all the *notes* in plain text with all the extra checkboxes on, then change file_path to point to
# that file. Run the program and wait until completion. Then import the generated .tsv into anki to replace the notes


### SETTINGS ###
# start anew or just update new notes?
delete_existing_examples = True

# skip notes with "added_example" or "None" in tags
mind_existing_tags = False

# deck url
file_path = 'Example input.tsv'

### MAIN ###
data = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        if not line.startswith('#'):
            line = line.replace("\n", "")
            data.append(line.split('\t'))
column_names = ['uniqueID', 'cardModel', 'deck', 'kanjiStudyID', 'front', 'frontFurigana', 'back', 'tags']
df_deck = pd.DataFrame(data, columns=column_names)
# fix weird quotes
df_deck['uniqueID'] = df_deck['uniqueID'].str.replace('"', '', regex=False)
df_deck['back'] = df_deck['back'].str.replace('""', '"', regex=False)
df_deck['back'] = df_deck['back'].str.replace('"<', '<', regex=False)
df_deck['back'] = df_deck['back'].str.rstrip('"')
print(f"Deck {Fore.yellow}{file_path}{Style.reset} processed")

# load examples
file_path = 'tatoeba-corpus-jp-eng-cleaned.tsv'
data = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        data.append(line.strip().split('\t'))

column_names = ['jpID', 'jp', 'engID', 'eng']
df_sentences = pd.DataFrame(data, columns=column_names)
print(f"{Fore.yellow}Tatoeba examples{Style.reset} loaded")

test_words_n = len(df_deck)
# test_words_n = 30
skipped = 0
start_time = time.time()
total_time = 0

# Convert columns to lists for faster iteration
tags_list = df_deck["tags"].tolist()
back_list = df_deck["back"].tolist()
front_list = df_deck["front"].tolist()
front_furi = df_deck["frontFurigana"].tolist()

for i in range(test_words_n):
    if i % 100 == 0:
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time
        print(
            f"{i}/{test_words_n}\t{Fore.cyan}{round(i / test_words_n * 100, 2)}%{Style.reset}\tSkipped: {Fore.red}{skipped}{Style.reset}\tElapsed "
            f"time: {elapsed_time:.3f}s\tTotal: {total_time:.3f}s")
        skipped = 0
        start_time = time.time()

    tags = str(tags_list[i])

    if delete_existing_examples:
        if "with_example" or "added_example" in tags:
            pattern = r'<br><br>.*'
            back_list[i] = re.sub(pattern, '', back_list[i])
            tags_list[i] = ""
            tags = str(tags_list[i])
    elif mind_existing_tags and "None" not in tags:
        skipped += 1
        continue

    elif mind_existing_tags and "added_example" in tags:
        skipped += 1
        continue

    word = front_list[i]
    if "," in word:
        word = word.split(",")[0]

    variations = generate_variations(word)
    df_examples = get_examples(df_sentences, variations, max_examples=5)

    if len(df_examples) > 0 and "added_example" not in tags:  # there are examples
        tagging = "added_example"
        updated_back = back_list[i] + "<br><br><details><summary>Examples</summary><br>"

        # Loop through the first 5 examples
        for idx, row in df_examples.iloc[:5].iterrows():
            example = highlight_string(row['jp'], variations)
            translation = row['eng']
            updated_back += f"<br><details><summary>{example}</summary>{translation}</details>"

        updated_back += "</details>"
        back_list[i] = updated_back
    else:
        tagging = "no_examples_available"

    if not (mind_existing_tags and "added_homonyms_button" in tags):
        kanasearch = extract_furigana(front_furi[i])
        back_list[i] = back_list[
                           i] + f"<br><a href=\"kanjistudy://search?query={kanasearch}\" style=\"color:lightblue; text-decoration:underline;\">Search for homonyms</a>"
        tagging += " added_homonyms_button"

    tags_list[i] = tagging

# Assign the lists back to the DataFrame at once
df_deck["tags"] = tags_list
df_deck["back"] = back_list

print(f"{Fore.green}Example sentences added to notes!{Style.reset}")

# save file
if test_words_n != len(df_deck):
    df_deck = df_deck.head(test_words_n)

# Save the new file
file_path = 'Example output.tsv'
with open(file_path, 'w') as file:
    file.write("#separator:tab\n")
    file.write("#html:true\n")
    file.write("#guid column:1\n")
    file.write("#notetype column:2\n")
    file.write("#deck column:3\n")
    file.write("#tags column:8\n")

df_deck.to_csv(file_path, sep='\t', index=False, mode='a', header=False)

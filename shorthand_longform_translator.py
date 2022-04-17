# -*- coding: utf-8 -*-
"""
Created on 2022/03/19, Sat, 12:19:01 (UTC+8)

@author: Lapis Liozuli
Purpose: Convert shorthand into full text using a raw transcript and a dict for shortform to longform.
Steps:
1. Write transcript using shorthand.
2. Load dict from text file.
3. Convert the shorthand into longform using the dict.
4. Capitalise start of sentences.
5. Spell-check?

Dict entries may include spaces to avoid replacing parts of words.

Eventually may trawl huge datasets of text to determine word frequency.
Then automatically derive shorthand forms from common words by eliminating vowels and output to a list for additional verification.
Most words should be fine, but some collisions have to be manually avoided. Or change to a preference for phonetic acronyms instead.
The transcriber must still develop the skill of transcription, esp while listening to speech.

JSONDecodeError: Expecting ',' delimiter
Means that one of the dict entries is missing a double quote ("") or a comma (,)
Can use binary search to iden the offending entry.
OR use https://jsonlint.com/ to validate JSON.

Start compressing longer words/short-forms. Only compress words of length >4.
Add punctuation behind them like ' ',.: and also take note of spaces in front.
Differentiate between dashes and hyphens (maybe rep as '=').
Might possibly add short-forms for frequent word parts like '-tion'
Higher-level: Handle the adjective ([) and noun (]) suffixes. Maybe find altv symbols to rep them?
                                     
https://stackoverflow.com/questions/71229376/why-nltks-wordnet-lemmatizer-does-not-lemmatize-adverbs-and-adjectives
TLDR: It's hard.
"""
from os import path
import json
from nltk.stem import WordNetLemmatizer

# # Initial setup of the Lemmatizer and its dependencies.
# import nltk
# nltk.download()
# # Tried to install Open English Wordnet.
# from nltk.corpus import wordnet as wn
# nltk.download("punkt")
# # Installed WordNet in the end instead.
# nltk.download("wordnet")

# This goes in reverse chrono order. Will have to revert back once all the existing archives are completed.
# Also might store this in a separate text file as it gets longer.
# Or generate dates automatically and exclude missed dates?
dates = ["20220409", "20220326", "20220312", "20220226", "20220212", "20220129", "20211211", "20211127", "20211113"]
path_transcript_dir = r"C:\Users\Public\Documents\LapisLiozuli\Transcripts-of-QuiltMC-Dev-Meeting"
path_dicts_dir = path.join(path_transcript_dir, "Dicts and Wordlists")
path_raws_dir = path.join(path_transcript_dir, "Raws")
path_shorthand_dict = path.join(path_dicts_dir, "shorthand_dict.txt")
# This path is for quick and dirty testing.
path_temp = path.join(path_transcript_dir, "temp.txt")

# Use open-clause to avoid leaving files open.
def read_text_into_collection(filename, dstrc_collection):
    input_path = path.join(path_dicts_dir, filename + ".txt")
    if dstrc_collection == "list":
        with open(input_path, encoding="utf-8") as f:
            read_str = f.read()
        output_collection = read_str.split("\n")
    elif dstrc_collection == "dict":
        with open(input_path, encoding="utf-8") as f:
            read_str = f.read()
        output_collection = json.loads(read_str)
    return output_collection

# Use open-clause to avoid leaving files open.
def write_text_outfrom_collection(filename, dstrc_collection, input_collection):
    output_path = path.join(path_dicts_dir, filename + ".txt")
    if dstrc_collection == "list":
        with open(output_path, "w") as f:
            f.writelines("\n".join(input_collection))
    elif dstrc_collection == "dict":
        with open(output_path, "w") as f:
            f.write(json.dumps(input_collection).replace(", ", ",\n"))


# Generates a short-form by removal of vowels.
# An alternative would be to truncate the word and use the first four or so letters.
def abbreviate_word(word):
      # Ignore the first letter.
      brev = word[1:]
      # Remove all vowels. Might include "y" eventually?
      vowels_list = ["a", "e", "i", "o", "u"]
      for vowel in vowels_list:
            brev = brev.replace(vowel, "")
      brev = word[0] + brev
      return brev


# Check for keys with duplicate values.
def find_keys_w_duped_values(dict01):
      rev_multidict = {}
      for key, value in dict01.items():
           rev_multidict.setdefault(value, set()).add(key)
      print([key for key, values in rev_multidict.items() if len(values) > 1])


# Can kind of extract the lemmas from any word list.
def create_lem_list(input_wordlist, filename_deriv):
    wn_lem = WordNetLemmatizer()
    # 3.3K words. Reduces words to basic word form (lemma) over different parts of speech.
    lem_list = [wn_lem.lemmatize(word, pos="n") for word in input_wordlist]
    lem_list = [wn_lem.lemmatize(word, pos="v") for word in lem_list]
    lem_list = [wn_lem.lemmatize(word, pos="a") for word in lem_list]
    lem_list = [wn_lem.lemmatize(word, pos="r") for word in lem_list]
    lem_list = [wn_lem.lemmatize(word, pos="s") for word in lem_list]
    # 4198 words. Remove dupes.
    lem_list = list(set(lem_list))
    lem_list.sort()
    # 3278 words. Remove words of length <= 4.
    big_list = [word for word in lem_list if len(word) > 4]

    # Lemmatizer is unable to find root of larger nouns/adjectives, so use this brutal nested loop.
    blist_copy = big_list.copy()
    deriv_list = []
    for word in big_list:
          for blord in blist_copy:
                if word != blord and word in blord:
                      deriv_list.append(blord)
    deriv_list = list(set(deriv_list))
    deriv_list.sort()

    # Export to check for compound words.
    write_text_outfrom_collection(filename_deriv, "list", deriv_list)

    return big_list

punctuation_list = ["?", ":", "!", " ", ",", ".", ":", ";", "'", '"', "=", "#", "'s", "_", "-", "~"]
# Takes a list of words. Eventually can feed words from the processed transcripts back into this function.
# Perhaps add an list of exceptions that won"t have any trailing punc, such as contractions ("wouldn't").
# Tenses using future (|), present (-) and past (_).
# Descriptive ([) and noun (]) word modifications. May need to manually edit this, then later ref to a lang dictionary.
# Plural forms also would be a problem.
# I tried to avoid these use cases in the hardcoded shortforms.
def attach_punc_to_shortform(sf_dict):
    punc_dict = sf_dict.copy()
    sort_dict = sf_dict.copy()
    # Add trailing punctuations: spaces, commas, periods, colons, semicolons.
    for sf in sf_dict:
        # Generate capitalised form.
        sf_cap = sf.capitalize()
        if sf == sf_cap:
            sf_cap = "caps" + sf
        punc_dict[sf_cap] = punc_dict[sf].capitalize()
        # Capitalise words also as an alternate form.
        for shortform in [sf, sf_cap]:
            # Exclude names from the text processing loop.
            # But need to allow " 's " for names at some point.
            if sf[:2] != 'nn':
                # Maybe add "=" in future. "=" is the stand-in for "-" as it already represents "-ing".
                space_sf = " " + shortform
                for punc in punctuation_list:
                    sf_punc = space_sf + punc
                    punc_dict[sf_punc] = " " + punc_dict[shortform] + punc
                # Plural: Imperfect but should cover majority of words.
                # Extra space needed to avoid unnecessary translations. Both before and after.
                punc_dict[" " + shortform + "s "] = " " + punc_dict[shortform] + "s "
                # Future tense cannot be directly applied during the conversion using replace because the long-form flanks the word.
                # Extra space not needed, but added for standardisation.
                punc_dict[" " + shortform + "|"] = " will be " + punc_dict[shortform] + "ing"
                # Remove the original shortforms to prevent excessive replacements later on.
                # In other words, all shortforms in attach_dict should have a space in front of them.
                punc_dict.pop(shortform, "missing key")
                sort_dict.pop(shortform, "missing key")
    return punc_dict, sort_dict


# Defaults to latest entry which is the earliest date.
def convert_raw_transcript(shand_dict, idx=-1, debug=False):
    punc_dict, sort_dict = attach_punc_to_shortform(shand_dict)
    # Rearrange short-forms from long to short to prevent the shorter sf from overwriting the longer ones.
    desc_length_dict = {}
    for k in sorted(punc_dict, key=len, reverse=True):
    # for k in sorted(sort_dict, key=len, reverse=True):
        desc_length_dict[k] = punc_dict[k]
    # Add a debug term to check the final desc_length_dict.
    if debug:
        write_text_outfrom_collection("temp", "dict", desc_length_dict)
    # Use markdown files for inline text formatting. Have to avoid certain symb in shorthand.
    path_raw = path.join(path_raws_dir, "transcript_raw_qmcdevmtg_" + dates[idx] + ".md")
    # Transcript long.
    path_tlong = path.join(path_raws_dir, "tlong_qmcdevmtg_" + dates[idx] + ".md")

    with open(path_raw, encoding="utf-8") as traw:
      lines = traw.readlines()
    longlines = lines.copy()

    # List comprehension for brevity.
    for shand in desc_length_dict:
        longlines = [line.replace(shand, desc_length_dict[shand]) for line in longlines]

    # Convert past tense and present tense in an imperfect manner.
    tense_dict = {"-": "ing", "_": "ed"}
    tense_errors = {"eing": "ing", "eed": "ed"}
    for sf_tense in tense_dict:
        longlines = [line.replace(sf_tense, tense_dict[sf_tense]) for line in longlines]
    # Might want to remove common errors from the transcription like "-eing" to "-ing" or "-eed" to "-ed".
    for error in tense_errors:
        longlines = [line.replace(error, tense_errors[error]) for line in longlines]
    # Fix these words: 'Need' is converted to 'ned'. 'Being' is converted to 'bing'.
    longlines = [line.replace(' bing ', ' being ') for line in longlines]
    longlines = [line.replace(' ned ', ' need ') for line in longlines]
    longlines = [line.replace('=', '-') for line in longlines]

    with open(path_tlong, "w") as f:
      f.writelines(longlines)


def generate_new_dict():
    # Import word list. 25323 words.
    popular_dolph = read_text_into_collection("popular_dolph", "list")
    # 5050 words.
    top5K_wordfreqnet = read_text_into_collection("top5K_wordfreqnet", "list")
    # Should eventually be able to lemmatise only when needed.
    big_list = create_lem_list(top5K_wordfreqnet, "deriv_top5K")
    # 567 words after elimination. All these words contain lemmas.
    post_deriv_list = read_text_into_collection("post_deriv", "list")
    # The basic list that should contain only lemmas.
    rootword_list = [word for word in big_list if word not in post_deriv_list]
    # The dict of each word and its short-form.
    abrv_dict = {word: abbreviate_word(word) for word in rootword_list}
    # Truncate if short-form is >4 letters long? But that might add to the workload instead.
    truncate_dict = {word: word[:4] for word in rootword_list if len(abrv_dict[word]) > 4}
    # Export to edit it e.g. check for compound words, use truncated form instead.
    write_text_outfrom_collection("lem_dict", "dict", abrv_dict)
    # Collated from the lemmas and derivative words from top5K_wordfreqnet, past QDMs and post_deriv_list.
    # This was manually hardcoded. Ideally it can be automated in future, but hopefully these few thousand words should cover most use cases.
    collated_dict = read_text_into_collection("collated_dict", "dict")
    # Sort keys alphabetically. Added a lower() as most acronyms contain capitals which is annoying to type.
    collated_dict = {key.lower(): value for key, value in sorted(collated_dict.items())}
    # Flip keys (long-forms) and values (short-forms). This allows for a word to have multiple short-forms.
    post_collated_dict = dict((v,k) for k,v in collated_dict.items())
    write_text_outfrom_collection("post_collated_dict", "dict", post_collated_dict)
    # # Check if collated_dict has any words that share the same short-form.
    # find_keys_w_duped_values(post_collated_dict)
    # Short-to-Long dict that contains a few other custom short-forms. Mainly altv short-forms for existing words.
    # stl_dict will be a copy of post_collated_dict.
    # Feed stl_dict back into collated_dict to accumulate more short-forms over time.
    stl_dict = read_text_into_collection("stl_dict", "dict")

# Generate dict of abbreviations either by import or generation
# dirty_switch is True when building upon dicts, then False only when initialising dicts.
dirty_switch = True
# Run this when building on an existing dictionary of short-forms with new entries.
if dirty_switch:
    stl_dict = read_text_into_collection("stl_dict", "dict")
    # Read stl_dict.
    # Sort it alphabetically.
    stl_dict = {key.lower(): value for key, value in sorted(stl_dict.items())}
    # Update the text archive. But might erase some entries. Still, 4 out of 2500+ is only <2%.
    write_text_outfrom_collection("stl_dict", "dict", stl_dict)
# Only run this when first initialising a dictionary of short-forms.
else:
    generate_new_dict()

convert_raw_transcript(stl_dict, idx=-2)


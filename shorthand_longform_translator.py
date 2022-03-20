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

Start compressing longer words/short-forms. Only compress words of length >4.
Add punctuation behind them like ' ',.: and also take note of spaces in front.
Differentiate between dashes and hyphens (maybe rep as '=').
Might possibly add short-forms for frequent word parts like '-tion'
Higher-level: Handle the adjective ([) and noun (]) suffixes. Maybe find altv symbols to rep them?
                                     
https://stackoverflow.com/questions/71229376/why-nltks-wordnet-lemmatizer-does-not-lemmatize-adverbs-and-adjectives
TLDR: It's hard.

https://jsonlint.com/ to validate JSON.
"""
from os import path
import json
from nltk.stem import WordNetLemmatizer

# This goes in reverse chrono order. Will have to revert back once all the existing archives are completed.
dates = ["20220312", "20220226"]
path_transcript_dir = r"C:\Users\Public\Documents\LapisLiozuli\Transcripts-of-QuiltMC-Dev-Meeting"
path_shorthand_dict = path.join(path_transcript_dir, 'shorthand_dict.txt')
path_temp = path.join(path_transcript_dir, "temp.txt")

# # Setup of lemmatizer.
# import nltk
# nltk.download()
# # Tried to install Open English Wordnet.
# from nltk.corpus import wordnet as wn
# nltk.download('punkt')
# # Installed WordNet in the end instead.
# nltk.download('wordnet')


# Use open-clause to avoid leaving files open.
def read_text_into_collection(filename, dstrc_collection):
    input_path = path.join(path_transcript_dir, filename + ".txt")
    if dstrc_collection == 'list':
        with open(input_path, encoding='utf-8') as f:
            read_str = f.read()
        output_collection = read_str.split("\n")
    elif dstrc_collection == 'dict':
        with open(input_path, encoding='utf-8') as f:
            read_str = f.read()
        output_collection = json.loads(read_str)
    return output_collection


def write_collection_into_text(filename, dstrc_collection, input_collection):
    output_path = path.join(path_transcript_dir, filename + ".txt")
    if dstrc_collection == 'list':
        with open(output_path, 'w') as f:
            f.writelines("\n".join(input_collection))
    elif dstrc_collection == 'dict':
        with open(output_path, 'w') as f:
            f.write(json.dumps(input_collection).replace(", ", ",\n"))


# Check for keys with duplicate values.
def find_keys_w_duped_values(dict01):
      rev_multidict = {}
      for key, value in dict01.items():
           rev_multidict.setdefault(value, set()).add(key)
      return [key for key, values in rev_multidict.items() if len(values) > 1]


def abbreviate_word(word):
      # Ignore the first letter.
      brev = word[1:]
      # Remove all vowels. Might include 'y' eventually?
      vowels_list = ["a", "e", "i", "o", "u"]
      for vowel in vowels_list:
            brev = brev.replace(vowel, '')
      brev = word[0] + brev
      return brev


# Takes a list of words. Eventually can feed the processed transcripts back into this function.
def compress_words_to_shorthand(wordlist):
      # Compress by removing all vowels, unless the word begins with a vowel.
      # I.e. remove vowels from __word__[1:].
      # Rearrange short-forms from long to short.
      # Capitalise words also.
      # Add trailing punctuations: spaces, commas, periods, colons, semicolons.
      # Perhaps add an list of exceptions that won't have any trailing punc, such as contractions ('wouldn't').
      # Tenses using future (~), present (-) and past (_).
      # Descriptive ([) and noun (]) word modifications. May need to manually edit this, then later ref to a lang dictionary.
      # Plural forms also would be a problem.
      # How to abrv plurals? Maybe add '2'. But easier to add 's'.
      # So "conversation": "convo", "conversations": "convo2"?
      # Output to file.
      shand_dict = {}
      return shand_dict


# Defaults to latest entry which is the earliest date.
def convert_raw_transcript(shand_dict, idx=-1):
      # Use markdown files for inline text formatting. Have to avoid certain symb in shorthand.
      path_raw = path.join(path_transcript_dir, 'transcript_raw_qmcdevmtg_' + dates[idx] + '.md')
      # Transcript long.
      path_tlong = path.join(path_transcript_dir, 'tlong_qmcdevmtg_' + dates[idx] + '.md')
      
      with open(path_raw, encoding='utf-8') as traw:
          lines = traw.readlines()
      longlines = lines.copy()

      # List comprehension for brevity.
      for shand in js:
            longlines = [line.replace(shand, js[shand]) for line in longlines]
      
      with open(path_tlong, 'w') as f:
          f.writelines(longlines)


# Can kind of extract the lemmas from any word list.
def create_lem_list(input_wordlist, filename_deriv):
    wn_lem = WordNetLemmatizer()
    punctuations = "?:!.,;"

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
    write_collection_into_text(filename_deriv, 'list', deriv_list)

# Import word list. 25323 words.
popular_dolph = read_text_into_collection("popular_dolph", 'list')
# 5050 words.
top5K_wordfreqnet = read_text_into_collection("top5K_wordfreqnet", 'list')
# create_lem_list(top5K_wordfreqnet, "deriv_top5K")
# 567 words after elimination. All these words contain lemmas.
post_deriv_list = read_text_into_collection("post_deriv", 'list')
# The basic list that should contain only lemmas.
rootword_list = [word for word in big_list if word not in post_deriv_list]
# The dict of each word and its short-form.
abrv_dict = {word: abbreviate_word(word) for word in rootword_list}
# Export to edit it e.g. check for compound words, use truncated form instead.
write_collection_into_text("lem_dict", 'dict', abrv_dict)

# Import dict of abbreviations.
# # Currently my own written dict based on the past two QDM transcripts.
# shand_dict = read_text_into_collection("shorthand_dict", 'dict')
# shorthand_dict = compress_words_to_shorthand([])

# Collated from the lemmas and derivative words from top5K_wordfreqnet, past QDMs and post_deriv_list.
# This was manually hardcoded. Ideally it can be automated in future, but hopefully these few thousand words should cover most use cases.
collated_dict = read_text_into_collection("collated_dict", 'dict')
# Sort keys alphabetically.
collated_dict = {key: value for key, value in sorted(collated_dict.items())}
# Flip keys (long-forms) and values (short-forms). This allows for a word to have multiple short-forms.
collated_dict = dict((v,k) for k,v in collated_dict.items())
# # Check if collated_dict has any words that share the same short-form.
# find_keys_w_duped_values(collated_dict)
write_collection_into_text("post_collated_dict", 'dict', collated_dict)
# Short-to-Long dict that contains a few other custom short-forms. Mainly altv short-forms for existing words.
stl_dict = read_text_into_collection("stl_dict", 'dict')

# convert_raw_transcript(shand_dict, idx=-1)
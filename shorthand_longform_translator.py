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
"""
from os import path
import json
from nltk.stem.lancaster import LancasterStemmer

# This goes in reverse chrono order. Will have to revert back once all the existing archives are completed.
dates = ["20220312", "20220226"]
path_transcript_dir = r"C:\Users\Public\Documents\LapisLiozuli\Transcripts-of-QuiltMC-Dev-Meeting"
path_popular_dolph = path.join(path_transcript_dir, "popular_dolph.txt")


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
def convert_raw_transcript(idx=-1):
      # Use markdown files for inline text formatting. Have to avoid certain symb in shorthand.
      path_raw = path.join(path_transcript_dir, 'transcript_raw_qmcdevmtg_' + dates[idx] + '.md')
      # Transcript long.
      path_tlong = path.join(path_transcript_dir, 'tlong_qmcdevmtg_' + dates[idx] + '.md')
      
      with open(path_raw, encoding='utf-8') as traw:
          lines = traw.readlines()
          
      js = json.loads(data)
      longlines = lines.copy()
      # List comprehension for brevity.
      for shand in js:
            longlines = [line.replace(shand, js[shand]) for line in longlines]
      
      with open(path_tlong, 'w') as f:
          f.writelines(longlines)

# Import word list.
with open(path_popular_dolph, encoding='utf-8') as f:
    popular_dolph = f.read()
dolph_list = popular_dolph.split("\n")
# Remove words with same roots. Cuts word count by about half.
st = LancasterStemmer()
stem_dolph_list = [st.stem(word) for word in dolph_list]
stem_dolph_list = list(set(stem_dolph_list))
# Remove words of length <= 4. Cuts word count by 3K.
big_dolph_list = [word for word in stem_dolph_list if len(word) > 4]

abrv_dolph_dict = {word: abbreviate_word(word) for word in stem_dolph_list}
# shorthand_dict = compress_words_to_shorthand([])

# Import dict of abbreviations.
# Currently my own written dict, but will be outputted from another function.
path_shorthand_dict = path.join(path_transcript_dir, 'shorthand_dict.txt')
 # Use open-clause to avoid leaving files open.
with open(path_shorthand_dict, encoding='utf-8') as f:
    data = f.read()
    
# convert_raw_transcript()
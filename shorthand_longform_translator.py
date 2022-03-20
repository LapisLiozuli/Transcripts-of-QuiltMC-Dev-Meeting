# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 12:19:01 2022

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

# This goes in reverse chrono order. Will have to revert back once all the existing archives are completed.
dates = ["20220312", "20220226"]
transcript_dir = r"C:\Users\Lio Hong\Documents\LioHong\Python-Sandbox\Shorthand"


# Takes a list of words. Eventually can feed the processed transcripts back into this function.
def compress_words_to_shorthand(wordlist):
      # Rearrange short-forms from long to short.
      # Capitalise words also.
      # Add trailing punctuations: spaces, commas, periods, colons, semicolons.
      # Perhaps add an list of exceptions that won't have any trailing punc, such as contractions ('wouldn't').
      # Tenses using future (~), present (-) and past (_).
      # Descriptive ([) and noun (]) word modifications.
      # Output to file.
      shand_dict = {}
      return shand_dict

shorthand_dict = compress_words_to_shorthand([])
# Currently my own written dict, but will be outputted from another function.
shorthand_dict = path.join(transcript_dir, 'shorthand_dict.txt')
 # Use open-clause to avoid leaving files open.
with open(shorthand_dict, encoding='utf-8') as f:
    data = f.read()

# Defaults to latest entry which is the earliest date.
def convert_raw_transcript(idx=-1):
      # Use markdown files for inline text formatting. Have to avoid certain symb in shorthand.
      raw = path.join(transcript_dir, 'transcript_raw_qmcdevmtg_' + dates[idx] + '.md')
      # Transcript long.
      tlong = path.join(transcript_dir, 'tlong_qmcdevmtg_' + dates[idx] + '.md')
      
      with open(raw, encoding='utf-8') as traw:
          lines = traw.readlines()
          
      js = json.loads(data)
      longlines = lines.copy()
      # List comprehension for brevity.
      for shand in js:
            longlines = [line.replace(shand, js[shand]) for line in longlines]
      
      with open(tlong, 'w') as f:
          f.writelines(longlines)
    
convert_raw_transcript()
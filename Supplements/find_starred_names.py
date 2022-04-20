# -*- coding: utf-8 -*-
"""
Created on 2022/04/18, Mon, 21:04:36 (UTC+8)

@author: Lio Hong
Filename: find_starred_names.py
Purpose: Extract names in the format **NAME** from markdown texts for keeping track of attendance.
Steps:
Split the entire text by different kinds of punctuation
Flatten list of strings and lists?
Use list comprehension to extract only starred names.
list(set(namelist))
Every date will have its own namelist.

Maybe re-arrange into dataframe?
Then convert the dataframe into a markdown table.
Notes:
"""
from os import path
from itertools import chain
import json

dates = ["20220409", "20220326", "20220312", "20220226", "20220212", "20220129", "20211211", "20211127", "20211113"]
# dates = ["20220409"]
path_suppl_dir = r"C:\Users\Public\Documents\LapisLiozuli\Transcripts-of-QuiltMC-Dev-Meeting\Supplements"

punctuation_list = ["?", ":", "!", " ", ",", ".", ":", ";", "'", '"', "=", "#", "'s", "_", "-", "~", "(", ")"]
# punctuation_list = ["?", ":", "!", ",", ".", ":", ";", "'", '"', "=", "#", "'s", "_", "-", "~"]


def flatten_sublists_scalars(nested_list):
    if isinstance(nested_list, (list, tuple, set, range)):
        for entry in nested_list:
            yield from flatten_sublists_scalars(entry)
    else:
        yield nested_list
        
attd_dict = {}
for date in dates:
      # utc-8 doesn't work.
      with open(path.join(path_suppl_dir, "TranscriptQDM_" + date + ".md"), encoding="latin1") as transcript:
            lines = transcript.readlines()
      longlines = lines.copy()
      # Join into a giant string.
      whole_transcript = ' '.join(longlines)
      twords_list = [whole_transcript]
      for punc in punctuation_list:
            twords_list = [word.split(punc) for word in twords_list]
            twords_list = list(flatten_sublists_scalars(twords_list))
      
      names_list = []
      for tword in twords_list:
            if "**" in tword:
                  names_list.append(tword)

      names_list = list(set(names_list))
      old_names_list = names_list.copy()
      # Handle names with spaces.
      spaced_names = []
      for name in old_names_list:
            if name.count("*") < 4:
                  spaced_names.append(name)
                  names_list.remove(name)
      names_list.append(spaced_names)
      attd_dict[date] = names_list

# Dump to text.
switch = False
if switch:
      with open(path.join(path_suppl_dir, "attd_dict.txt"), "w") as f:
            f.write(json.dumps(attd_dict).replace(", ", ",\n"))

# Load from text
if not switch:
      with open(path.join(path_suppl_dir, "attendance_dict.txt"), encoding="latin1") as f:
          read_str = f.read()
      output_collection = json.loads(read_str)
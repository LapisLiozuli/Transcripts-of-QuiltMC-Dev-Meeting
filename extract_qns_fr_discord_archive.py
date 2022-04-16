# -*- coding: utf-8 -*-
"""
Created on 2022/04/16, Sat, 20:44:12 (UTC+8)

@author: LapisLiozuli
Filename: extract_qns_fr_discord_archive.py
Purpose:
Steps:
Notes:
"""
import json
with open(r"C:\Users\Public\Documents\LapisLiozuli\Transcripts-of-QuiltMC-Dev-Meeting\The Quilt Toolchain - Meetings - meeting-chat [908095149706444822].json", encoding="utf-8") as f:
    read_str = f.read()
mtgchat_archives = json.loads(read_str)

qns_list = [qn for qn in mtgchat_archives['messages'] if len(qn['embeds']) > 0]
stage_list = [qn for qn in qns_list if 'footer' in qn['embeds'][0]]
edited_stage_list = [{"timestamp":qn['timestamp'], "embeds":qn['embeds'] } for qn in stage_list]
stage_dict = {}
for i in range(len(edited_stage_list)):
    stage_dict[i] = edited_stage_list[i]
with open(r"C:\Users\Public\Documents\LapisLiozuli\Transcripts-of-QuiltMC-Dev-Meeting\mtgchat_questions.txt", "w") as f:
    f.write(json.dumps(stage_dict))
import os #line:1
import tkinter as tk #line:2
from tkinter import filedialog #line:3
from tkinter import messagebox #line:4
import random #line:5
import threading #line:6
import webbrowser #line:7
import pyaudio #line:8
import wave #line:9
import librosa #line:12
import librosa .display #line:13
import numpy as np #line:16
def generate_map (OOO0000OOO0OO0O00 ,OOO0OOOOOOOOO00O0 ,OO00OOOOO00O0O00O ):#line:18
    OOOO000OO0O0O0000 ,O00O00OOO00O0OOO0 =librosa .load (OOO0000OOO0OO0O00 )#line:19
    OOOOOOO0O000OOOOO =librosa .onset .onset_detect (y =OOOO000OO0O0O0000 ,sr =O00O00OOO00O0OOO0 )#line:20
    if OOO0OOOOOOOOO00O0 =="patterns":#line:22
        return generate_pattern_map (OOOOOOO0O000OOOOO ,O00O00OOO00O0OOO0 ,OO00OOOOO00O0O00O )#line:23
    else :#line:24
        return generate_random_map (OOOOOOO0O000OOOOO ,O00O00OOO00O0OOO0 ,OO00OOOOO00O0O00O )#line:25
def generate_random_map (OO0OO00O000000O0O ,OOO00OOOO0OO0000O ,O00OO00O000000000 ):#line:27
    OOOO0OO0OOOO00O0O =[]#line:28
    O0O0O000O0OOO0O00 =[]#line:29
    OO0OO00000OO0OOOO =librosa .frames_to_time (OO0OO00O000000O0O ,sr =OOO00OOOO0OO0000O )#line:30
    for OO000O000O0O00O00 in OO0OO00000OO0OOOO :#line:32
        OO00OO0000000O0O0 =random .randint (0 ,2 )#line:33
        OO0O000O00000OO0O =random .randint (0 ,2 )#line:34
        OOOO0OO0OOOO00O0O .append (OO00OO0000000O0O0 )#line:35
        O0O0O000O0OOO0O00 .append (OO0O000O00000OO0O )#line:36
    OO0O000OOO0OOO0OO =[]#line:38
    for OO00OO0000000O0O0 ,OO0O000O00000OO0O ,OO000O000O0O00O00 in zip (OOOO0OO0OOOO00O0O ,O0O0O000O0OOO0O00 ,OO0OO00000OO0OOOO ):#line:39
        OO0O000OOO0OOO0OO .append (f"{OO00OO0000000O0O0}|{OO0O000O00000OO0O}|{int(OO000O000O0O00O00*1000)}")#line:40
    if O00OO00O000000000 >1 :#line:43
        for OOOO0000000OO0O00 in range (O00OO00O000000000 -1 ):#line:44
            O000OO0OO0O000OO0 =[]#line:45
            for O000OOOO0O0OO00OO in range (len (OO0O000OOO0OOO0OO )-1 ):#line:46
                OO0O000OOO0O0OOO0 =int (OO0O000OOO0OOO0OO [O000OOOO0O0OO00OO ].split ("|")[2 ])#line:47
                O0OOOO0000O0O00OO =int (OO0O000OOO0OOO0OO [O000OOOO0O0OO00OO +1 ].split ("|")[2 ])#line:48
                if O0OOOO0000O0O00OO -OO0O000OOO0O0OOO0 >200 :#line:49
                    O0O0O0O0000O0O000 =random .randint (OO0O000OOO0O0OOO0 +100 ,O0OOOO0000O0O00OO -100 )#line:50
                    O000OO0OO0O000OO0 .append (f"{random.randint(0, 2)}|{random.randint(0, 2)}|{O0O0O0O0000O0O000}")#line:51
            OO0O000OOO0OOO0OO .extend (O000OO0OO0O000OO0 )#line:52
            OO0O000OOO0OOO0OO .sort (key =lambda OOO0O0O00O0000OO0 :int (OOO0O0O00O0000OO0 .split ("|")[2 ]))#line:53
    return ",".join (OO0O000OOO0OOO0OO )#line:55
def generate_pattern_map (OOOOO00O0OO00OOOO ,O000OO0O000O00O00 ,O0OO0O00OOOOOO0O0 ):#line:57
    O0OO00O000OOO00O0 =["2|0|0,0|2|132,0|0|221,2|2|331,0|1|455,2|2|575,0|1|711,2|0|833","2.2|2.2|0,2.11|2.11|22,2.03|2.11|49,2.03|2.03|59,1.94|2.03|78,1.86|2.03|97,1.86|1.94|99,1.77|1.94|113,1.77|1.86|123,1.69|1.86|131,1.6|1.86|145,1.6|1.77|149,1.51|1.77|174,1.51|1.69|181,1.43|1.69|193,1.43|1.6|195,1.43|1.51|210,1.34|1.51|215,1.34|1.43|231,1.26|1.43|240,1.26|1.34|248,1.17|1.34|255,1.17|1.26|272,1.09|1.26|274,1|1.26|296,1|1.17|299,0.91|1.17|312,0.91|1.09|314,0.83|1.09|329,0.83|1|333,0.83|0.91|353,0.74|0.91|357,0.74|0.83|365,0.66|0.83|368,0.66|0.74|376,0.57|0.74|385,0.57|0.66|394,0.49|0.66|397,0.49|0.57|403,0.4|0.57|410,0.4|0.49|417,0.31|0.4|428,0.23|0.31|435,0.14|0.23|447,0.06|0.23|457,0.06|0.14|459,-0.03|0.14|472,-0.03|0.06|475,-0.03|-0.03|494,-0.11|-0.03|507,-0.11|-0.11|522,-0.11|-0.11|563,-0.03|-0.11|579,0.06|-0.11|589,0.14|-0.11|597,0.23|-0.11|606,0.31|-0.03|615,0.4|-0.03|619,0.49|-0.03|627,0.57|-0.03|633,0.66|-0.03|639,0.74|-0.03|646,0.83|-0.03|659,0.91|-0.03|677,1|-0.03|688,1|0.06|752,1|0.14|763,1|0.23|777,1|0.31|787,1|0.4|799,1|0.49|804,1|0.57|811,1|0.66|819,1|0.74|828,1.09|0.83|837,1.09|0.91|845,1.09|1|858,1.09|1.09|867,1.09|1.17|878,1|1.17|882,1|1.26|886,1|1.34|901,1|1.43|914,1|1.51|923,1|1.6|932,1|1.69|938,1|1.77|946,1|1.86|952,1|1.94|958,1|2.03|968,1|2.11|976,1|2.2|987,1|2.29|998","2|2|0,0|2|130,2|2|242,0|1|358,2|2|474,0|0|572,2|2|678,1|0|784","2.11|1.94|0,2.03|1.94|12,1.94|1.94|39,1.94|1.94|58,1.86|1.94|63,1.77|1.94|80,1.69|1.94|103,1.6|1.94|118,1.51|1.94|135,1.43|1.94|151,1.34|1.94|164,1.26|1.94|181,1.17|1.94|197,1.09|1.94|206,1|1.94|221,0.91|1.94|239,0.83|1.94|247,0.74|1.94|259,0.66|1.94|264,0.57|1.94|273,0.49|1.94|284,0.4|1.94|293,0.31|1.94|301,0.23|1.94|312,0.14|1.94|324,0.06|1.94|335,-0.03|1.94|347,-0.11|1.94|357","2|0|0,0|2|112,2|0|220,0|2|324,0|0|452,2|2|560,0|0|674,2|2|784","2|2|0,2|1|34,2|0|70,1|0|116,0|0|158,0|1|194,0|2|228,1|2|257","0|2|0,0|1|24,0|0|40,1|0|68,2|0|102,2|1|148,2|2|202,1|2|236"]#line:66
    OO00000O0O000O000 =[]#line:68
    OOOOOO0OOOOOOO0OO =librosa .frames_to_time (OOOOO00O0OO00OOOO ,sr =O000OO0O000O00O00 )#line:69
    O0OOO0000O00000OO =False #line:70
    O00OOO000OOOO0O0O =0 #line:71
    for OOOO0OO0OO0000OOO in OOOOOO0OOOOOOO0OO :#line:73
        if not O0OOO0000O00000OO :#line:74
            OOOO0OOO000OO000O =random .choice (O0OO00O000OOO00O0 )#line:75
            O0000000OOO0OO0OO =float (OOOO0OOO000OO000O .split (',')[-1 ].split ('|')[2 ])/1000 #line:76
            O0OOO0000O00000OO =True #line:77
            O00OOO000OOOO0O0O =OOOO0OO0OO0000OOO +O0000000OOO0OO0OO #line:78
            for OOO000O00O0O0OOOO in OOOO0OOO000OO000O .split (','):#line:79
                O00O0O00OOOOO000O ,O00OOO0OOO000O00O ,OO00OOO0000OO00O0 =OOO000O00O0O0OOOO .split ('|')#line:80
                OO0OOO000OOO0OO00 =int (OO00OOO0000OO00O0 )+int (OOOO0OO0OO0000OOO *1000 )#line:81
                OO00000O0O000O000 .append (f"{O00O0O00OOOOO000O}|{O00OOO0OOO000O00O}|{OO0OOO000OOO0OO00}")#line:82
        elif OOOO0OO0OO0000OOO >O00OOO000OOOO0O0O :#line:83
            O0OOO0000O00000OO =False #line:84
    if O0OO0O00OOOOOO0O0 >1 :#line:87
        for O0OO0O0O0O00O0000 in range (O0OO0O00OOOOOO0O0 -1 ):#line:88
            O0OOO00OOOO000000 =[]#line:89
            for OOOO0OOOO0OO0OOOO in range (len (OO00000O0O000O000 )-1 ):#line:90
                O0O000O00O00O00OO =int (OO00000O0O000O000 [OOOO0OOOO0OO0OOOO ].split ("|")[2 ])#line:91
                O0O0OOOO000OOOOO0 =int (OO00000O0O000O000 [OOOO0OOOO0OO0OOOO +1 ].split ("|")[2 ])#line:92
                if O0O0OOOO000OOOOO0 -O0O000O00O00O00OO >200 :#line:93
                    OOOOO000OOO00OO00 =random .randint (O0O000O00O00O00OO +100 ,O0O0OOOO000OOOOO0 -100 )#line:94
                    O0OOO00OOOO000000 .append (f"{random.randint(0, 2)}|{random.randint(0, 2)}|{OOOOO000OOO00OO00}")#line:95
            OO00000O0O000O000 .extend (O0OOO00OOOO000000 )#line:96
            OO00000O0O000O000 .sort (key =lambda OOO00O000000O0O00 :int (OOO00O000000O0O00 .split ("|")[2 ]))#line:97
    return ",".join (OO00000O0O000O000 )#line:99
def select_music ():#line:101
    global selected_music_path #line:102
    selected_music_path =filedialog .askopenfilename (filetypes =[("MP3 files","*.mp3")])#line:103
    music_label .config (text =f"Selected music: {os.path.basename(selected_music_path)}")#line:104
def create_map ():#line:106
    global selected_music_path #line:107
    global mode_var #line:108
    global difficulty_slider #line:109
    OOO0000O0OO00000O =mode_var .get ()#line:111
    O0O0OOOOO0O000000 =difficulty_slider .get ()#line:112
    if not selected_music_path :#line:114
        messagebox .showwarning ("Warning","Please select a music first.")#line:115
        return #line:116
    def OO0O0O0OOOO0000OO ():#line:118
        try :#line:119
            OO000000OO000OOO0 =generate_map (selected_music_path ,OOO0000O0OO00000O ,O0O0OOOOO0O000000 )#line:120
            map_text .delete (1.0 ,tk .END )#line:121
            map_text .insert (tk .END ,OO000000OO000OOO0 )#line:122
            messagebox .showinfo ("Success",f"Map created successfully. Your map has been saved as '{os.path.basename(selected_music_path)} map.txt', enjoy! :D")#line:123
            save_map (selected_music_path ,OO000000OO000OOO0 )#line:124
            play_audio (selected_music_path ,OO000000OO000OOO0 )#line:125
        except Exception as O0O0O0OO00OO0OOOO :#line:126
            messagebox .showerror ("Error",f"An error occurred: {str(O0O0O0OO00OO0OOOO)}")#line:127
        finally :#line:128
            OOOO00O000O000OO0 .destroy ()#line:129
    OOOO00O000O000OO0 =tk .Toplevel (root )#line:131
    OOOO00O000O000OO0 .title ("Progress")#line:132
    O00O00OOO0O0O000O =tk .Label (OOOO00O000O000OO0 ,text ="Map is being generated...")#line:133
    O00O00OOO0O0O000O .pack ()#line:134
    OOO0OOO0OOOO0O0O0 =threading .Thread (target =OO0O0O0OOOO0000OO )#line:136
    OOO0OOO0OOOO0O0O0 .start ()#line:137
def save_map (O0O00OO0OO000OO0O ,O00OOOO00O0O0O0OO ):#line:139
    O0O0OOOOOO00O00OO =os .path .basename (O0O00OO0OO000OO0O ).split ('.')[0 ]+" map.txt"#line:140
    with open (O0O0OOOOOO00O00OO ,"w")as O00O000OO0O0OO00O :#line:141
        O00O000OO0O0OO00O .write (O00OOOO00O0O0O0OO )#line:142
def play_audio (OO0OO0OOO0O00OO0O ,OOO00OO00O0OO00O0 ):#line:144
    OO0OOOO000O0O0O00 =1024 #line:145
    O00O0O00OO00OO0OO =wave .open (OO0OO0OOO0O00OO0O ,'rb')#line:146
    O00O0OOOO00OO0OOO =pyaudio .PyAudio ()#line:147
    OOO00000O0O000O0O =O00O0OOOO00OO0OOO .open (format =O00O0OOOO00OO0OOO .get_format_from_width (O00O0O00OO00OO0OO .getsampwidth ()),channels =O00O0O00OO00OO0OO .getnchannels (),rate =O00O0O00OO00OO0OO .getframerate (),output =True )#line:154
    O0OOOO00O0000OO00 =[O0O0O0OOO00OO000O .split ('|')for O0O0O0OOO00OO000O in OOO00OO00O0OO00O0 .split (',')]#line:156
    for O0O0O0000O0O0000O in O0OOOO00O0000OO00 :#line:157
        OOO000O00OO0000OO ,O00OOO0OO00O00O0O ,O0O0OO00OOOOOOOO0 =int (O0O0O0000O0O0000O [0 ]),int (O0O0O0000O0O0000O [1 ]),float (O0O0O0000O0O0000O [2 ])/1000 #line:158
        OOO00000O0O000O0O .write (O00O0O00OO00OO0OO .read (int (O0O0OO00OOOOOOOO0 *O00O0O00OO00OO0OO .getframerate ())))#line:159
        print (f"Note played at {O0O0OO00OOOOOOOO0}s: X = {OOO000O00OO0000OO}, Y = {O00OOO0OO00O00O0O}")#line:160
    OOO00000O0O000O0O .stop_stream ()#line:162
    OOO00000O0O000O0O .close ()#line:163
    O00O0OOOO00OO0OOO .terminate ()#line:164
    O00O0O00OO00OO0OO .close ()#line:165
def open_credits_window ():#line:167
    O0OOOOO0OO0O0O0OO =tk .Toplevel (root )#line:168
    O0OOOOO0OO0O0O0OO .title ("Credits")#line:169
    O0O00000OO000OOOO ="dev : short_time2009\nideas : - bubupack\n        - my.narco\n        and mostly karathy !!!"#line:170
    OO00OO0OOOO00OOO0 =tk .Label (O0OOOOO0OO0O0O0OO ,text =O0O00000OO000OOOO )#line:171
    OO00OO0OOOO00OOO0 .pack (pady =10 )#line:172
    O0OOOOO0OO0O0O0OO .geometry ("300x150")#line:175
def open_support_window ():#line:177
    OO0O0O000O00O0OOO =tk .Toplevel (root )#line:178
    OO0O0O000O00O0OOO .title ("Support")#line:179
    OO0O0O0OOOO000O00 ="If you want to support me for my work, you can donate here :"#line:180
    OOO0OO00O0O0O00O0 =tk .Label (OO0O0O000O00O0OOO ,text =OO0O0O0OOOO000O00 )#line:181
    OOO0OO00O0O0O00O0 .pack (pady =10 )#line:182
    OOO00O0O0OOO0O00O =tk .Button (OO0O0O000O00O0OOO ,text ="Donate",command =open_donation_link )#line:184
    OOO00O0O0OOO0O00O .pack (pady =5 )#line:185
def open_donation_link ():#line:187
    webbrowser .open_new ("https://donorbox.org/auto-mapper")#line:188
def toggle_pattern_mode ():#line:190
    if pattern_mode .get ():#line:191
        mode_var .set ("patterns")#line:192
    else :#line:193
        mode_var .set ("random")#line:194
root =tk .Tk ()#line:196
root .title ("Random map generator")#line:197
root .geometry ("500x550")#line:198
button_frame =tk .Frame (root )#line:201
button_frame .pack (fill =tk .X )#line:202
credits_button =tk .Button (button_frame ,text ="Credits",command =open_credits_window )#line:205
credits_button .pack (side =tk .LEFT ,padx =5 ,pady =5 )#line:206
support_button =tk .Button (button_frame ,text ="Support",command =open_support_window )#line:208
support_button .pack (side =tk .LEFT ,padx =5 ,pady =5 )#line:209
selected_music_path =None #line:211
select_music_button =tk .Button (root ,text ="Select your music",command =select_music )#line:213
select_music_button .pack (pady =10 )#line:214
music_label =tk .Label (root ,text ="Selected music: None")#line:216
music_label .pack ()#line:217
mode_label =tk .Label (root ,text ="Mode :")#line:219
mode_label .pack ()#line:220
mode_var =tk .StringVar (value ="random")#line:222
random_mode_rb =tk .Radiobutton (root ,text ="Random mode",variable =mode_var ,value ="random")#line:224
random_mode_rb .pack ()#line:225
patterns_mode_rb =tk .Radiobutton (root ,text ="Pattern mode",variable =mode_var ,value ="patterns")#line:227
patterns_mode_rb .pack ()#line:228
difficulty_label =tk .Label (root ,text ="Difficulty:")#line:230
difficulty_label .pack ()#line:231
difficulty_slider =tk .Scale (root ,from_ =1 ,to =10 ,orient =tk .HORIZONTAL )#line:233
difficulty_slider .pack ()#line:234
create_map_button =tk .Button (root ,text ="Create your map",command =create_map )#line:236
create_map_button .pack (pady =10 )#line:237
map_text =tk .Text (root ,height =10 ,width =50 )#line:239
map_text .pack (pady =10 )#line:240
root .mainloop ()#line:242

# A simple format under pic
FOMET = """
⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃
🗓️𝐃𝐚𝐭𝐞 : <b>{}</b>

💾𝐅𝐢𝐥𝐞 𝐬𝐢𝐳𝐞 : <b>{}</b>

⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃
LINK ➮ <b>{}</b>

𝐇𝐨𝐰 𝐭𝐨 𝐨𝐩𝐞𝐧 🤷‍♂️
just tap the link
⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃
  """
BOTEFITMSG = """
Post Sent Successfully ✅
Elements in <b>"{}"</b>

<b>TG Link : <a href="{}">Tlink</a></b> 
<b>Vid Size : {}</b>   <b>Date : {}</b>
"""

# A simple format return sent elements datails see (line 72, 39 in pluggins->channel post)
# BOTEFITMSG = """
# Post Sent Successfully ✅
# Elements in <b>"{}{}"</b>

# <b>TG Link : <a href="{}">Tlink</a></b> & <b>Short Link: <a href="{}">SLink</a></b>
# <b>Vid Size : {}</b>   <b>Date : {}</b>
# """
#whole serials data return in dictionary
############{'serial name':["pic", "short link domin", "short link api", "To channel id"]}###############
#ex =>>>    '':['','','','']
DATAODD = {
 #zee noon 
        'Rajeshwari_Vilas_Coffee_Club_':['https://graph.org/file/8fb299e1497c166065892.jpg','','','-1002126345865'],
        'Seethe_Ramudi_Katnam_':['https://graph.org/file/517d41e6bda6f38ce7730.jpg','','','-1002126345865'],
        'Mukkupudaka_':['https://graph.org/file/b894f656bbc1f1dd477b4.jpg','','','-1002126345865'],
        'Gundamma_Katha_':['https://graph.org/file/3cbf790cb570d3c7dbe27.jpg','','','-1002126345865'],
        'Jabilli_Kosam_Aakashamalle_':['https://graph.org/file/67b5969a42a3b47ab0754.jpg','','','-1002126345865'],
        'Subhasya_Seeghram_':['https://graph.org/file/047e212145409524e7ec8.jpg','','','-1002126345865'],
        'Oohalu_Gusagusalade_':['https://graph.org/file/a289d5007caaeebe4b18e.jpg','','','-1002126345865'],
        'Radhaku_Neevera_Praanam_':['https://graph.org/file/0803b79007469aa17d04c.jpg','','','-1002126345865'],
  #zee evening 
        'Radhamma_Kuthuru_':['https://graph.org/file/9934bd7b3c3492dd01e42.jpg','','','-1002126345865'],
        'Chiranjeevi_Lakshmi_Sowbhagyavati_':['https://graph.org/file/f75069b1b3a99f5652e70.jpg','tnshort.net','1183b34c88b1fd4e898d7d9dc7b6fc6a2bea9dd9','-1002126345865'],
        'Nindu_Noorella_Saavasam_':['https://graph.org/file/a4005c14fd51c5a32cc2c.jpg','linkshortify.com','4bc6f1e34d0409e5b8bd2197d42462bb1ec6048a','-1002126345865'],
        'Jagadhatri_':['https://graph.org/file/ef6227a07dac67bc30785.jpg','linkshortify.com','','-1002126345865'],
        'Padamati_Sandhyaragam_':['https://graph.org/file/c9444bffe703c0133a28f.jpg','linkshortify.com','','-1002126345865'],
        'Trinayani_':['https://graph.org/file/33af2c68d9e4e297d733e.jpg','tnshort.net','0045de7eda3a082a38f05bdd0d1c4de1262709fb','-1002126345865'],
        'Prema_Entha_Maduram_':['https://graph.org/file/6e25ea2e439c46bb6184a.jpg','tnshort.net','cfafc72b0df2558f0f5ad4e1c906ce9f783281e3','-1002126345865'],
        'Ammayi_Garu_':['https://graph.org/file/f42f50a0838286f90e944.jpg','','','-1002126345865'],
        'Suryakantham_':['https://graph.org/file/f5f324be9836fdb1f95e9.jpg','','','-1002126345865']
  
}
DATAEVEN = {
 #zee noon
        'Rajeshwari_Vilas_Coffee_Club_':['https://graph.org/file/8fb299e1497c166065892.jpg','','','-1002126345865'],
        'Seethe_Ramudi_Katnam_':['https://graph.org/file/517d41e6bda6f38ce7730.jpg','','','-1002126345865'],
        'Mukkupudaka_':['https://graph.org/file/b894f656bbc1f1dd477b4.jpg','','','-1002126345865'],
        'Gundamma_Katha_':['https://graph.org/file/3cbf790cb570d3c7dbe27.jpg','','','-1002126345865'],
        'Jabilli_Kosam_Aakashamalle_':['https://graph.org/file/67b5969a42a3b47ab0754.jpg','','','-1002126345865'],
        'Subhasya_Seeghram_':['https://graph.org/file/047e212145409524e7ec8.jpg','','','-1002126345865'],
        'Oohalu_Gusagusalade_':['https://graph.org/file/a289d5007caaeebe4b18e.jpg','','','-1002126345865'],
  #zee evening 
        'Radhamma_Kuthuru_':['https://graph.org/file/9934bd7b3c3492dd01e42.jpg','','','-1002126345865'],
        'Chiranjeevi_Lakshmi_Sowbhagyavati_':['https://graph.org/file/f75069b1b3a99f5652e70.jpg','linkshortify.com','4bc6f1e34d0409e5b8bd2197d42462bb1ec6048a','-1002126345865'],
        'Nindu_Noorella_Saavasam_':['https://graph.org/file/a4005c14fd51c5a32cc2c.jpg','tnshort.net','1183b34c88b1fd4e898d7d9dc7b6fc6a2bea9dd9','-1002126345865'],
        'Jagadhatri_':['https://graph.org/file/ef6227a07dac67bc30785.jpg','tnshort.net','0045de7eda3a082a38f05bdd0d1c4de1262709fb','-1002126345865'],
        'Padamati_Sandhyaragam_':['https://graph.org/file/c9444bffe703c0133a28f.jpg','tnshort.net','cfafc72b0df2558f0f5ad4e1c906ce9f783281e3','-1002126345865'],
        'Trinayani_':['https://graph.org/file/33af2c68d9e4e297d733e.jpg','linkshortify.com','','-1002126345865'],
        'Prema_Entha_Maduram_':['https://graph.org/file/6e25ea2e439c46bb6184a.jpg','linkshortify.com','','-1002126345865'],
        'Ammayi_Garu_':['https://graph.org/file/f42f50a0838286f90e944.jpg','','','-1002126345865'],
        'Suryakantham_':['https://graph.org/file/f5f324be9836fdb1f95e9.jpg','','','-1002126345865']
}

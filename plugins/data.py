
# A simple format under pic
FOMET = """
Ꮛᴘɪᴤοᴅє ŋο   ➺  <b>[{}] ,  {}</b>

▬▬▬▬▬ ✮✯☆★ ❂ ★☆✯✮ ▬▬▬▬▬
       
𝕯𝖆𝖙𝖊 ➻ <b>{}</b>

             𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐛𝐲  ➠  @Dot_serials_bot 

                       ⚜⚜⚜⍟⚜⚜⚜    
 
    YOUR EPISODE LINK 🔗 
<b>{}</b>
<b>{}</b>

        👀👩‍💻 𝐇𝐨𝐰 𝐭𝐨 𝐨𝐩𝐞𝐧 👩‍💻👀
https://t.me/+Sb5ro1gyhgY0NWM1
https://t.me/+Sb5ro1gyhgY0NWM1
  """
# A simple format return sent elements datails see (line 72, 39 in pluggins->channel post)
BOTEFITMSG = """
Post Sent Successfully ✅
Elements in <b>"{}{}"</b>

<b>TG Link : <a href="{}">Tlink</a></b> & <b>Short Link: <a href="{}">SLink</a></b>
<b>Vid Size : {}</b>   <b>Date : {}</b>
"""
#whole serials data return in dictionary
############{'serial name':["pic", "short link domin", "short link api", "To channel id"]}###############
#ex =>>>    '':['','','','']
DATAODD = {
        'Rajeshwari_Vilas_Coffee_Club_':['https://graph.org/file/8fb299e1497c166065892.jpg','','','-1002126345865'],
        'Seethe_Ramudi_Katnam_':['https://graph.org/file/517d41e6bda6f38ce7730.jpg','','','-1002126345865'],
        'Mukkupudaka_':['https://graph.org/file/b894f656bbc1f1dd477b4.jpg','','','-1002126345865'],
        'Gundamma_Katha_':['https://graph.org/file/3cbf790cb570d3c7dbe27.jpg','','','-1002126345865'],
        'Jabilli_Kosam_Aakashamalle_':['https://graph.org/file/67b5969a42a3b47ab0754.jpg','','','-1002126345865'],
        'Subhasya_Seeghram_':['https://graph.org/file/047e212145409524e7ec8.jpg','','','-1002126345865'],
        'Oohalu_Gusagusalade_':['https://graph.org/file/a289d5007caaeebe4b18e.jpg','','','-1002126345865'],
  #noon
        'Radhamma_Kuthuru_':['https://graph.org/file/9934bd7b3c3492dd01e42.jpg','','','-1002126345865'],
        'Chiranjeevi_Lakshmi_Sowbhagyavati_':['https://graph.org/file/f75069b1b3a99f5652e70.jpg','','','-1002126345865'],
        'Nindu_Noorella_Saavasam_':['https://graph.org/file/a4005c14fd51c5a32cc2c.jpg','','','-1002126345865'],
        'Jagadhatri_':['https://graph.org/file/ef6227a07dac67bc30785.jpg','','','-1002126345865'],
        'Padamati_Sandhyaragam_':['https://graph.org/file/c9444bffe703c0133a28f.jpg','','','-1002126345865'],
        'Trinayani_':['https://graph.org/file/33af2c68d9e4e297d733e.jpg','','','-1002126345865'],
        'Prema_Entha_Maduram_':['https://graph.org/file/6e25ea2e439c46bb6184a.jpg','','','-1002126345865'],
        'Ammayi_Garu_':['https://graph.org/file/f42f50a0838286f90e944.jpg','','','-1002126345865'],
        'Suryakantham_':['https://graph.org/file/f5f324be9836fdb1f95e9.jpg','','','-1002126345865']
  
}
DATAEVEN = {
        'Rajeshwari_Vilas_Coffee_Club_':['https://graph.org/file/8fb299e1497c166065892.jpg','','','-1002126345865'],
        'Seethe_Ramudi_Katnam_':['https://graph.org/file/517d41e6bda6f38ce7730.jpg','','','-1002126345865'],
        'Mukkupudaka_':['https://graph.org/file/b894f656bbc1f1dd477b4.jpg','','','-1002126345865'],
        'Gundamma_Katha_':['https://graph.org/file/3cbf790cb570d3c7dbe27.jpg','','','-1002126345865'],
        'Jabilli_Kosam_Aakashamalle_':['https://graph.org/file/67b5969a42a3b47ab0754.jpg','','','-1002126345865'],
        'Subhasya_Seeghram_':['https://graph.org/file/047e212145409524e7ec8.jpg','','','-1002126345865'],
        'Oohalu_Gusagusalade_':['https://graph.org/file/a289d5007caaeebe4b18e.jpg','','','-1002126345865'],
  #noon
        'Radhamma_Kuthuru_':['https://graph.org/file/9934bd7b3c3492dd01e42.jpg','','','-1002126345865'],
        'Chiranjeevi_Lakshmi_Sowbhagyavati_':['https://graph.org/file/f75069b1b3a99f5652e70.jpg','','','-1002126345865'],
        'Nindu_Noorella_Saavasam_':['https://graph.org/file/a4005c14fd51c5a32cc2c.jpg','','','-1002126345865'],
        'Jagadhatri_':['https://graph.org/file/ef6227a07dac67bc30785.jpg','','','-1002126345865'],
        'Padamati_Sandhyaragam_':['https://graph.org/file/c9444bffe703c0133a28f.jpg','','','-1002126345865'],
        'Trinayani_':['https://graph.org/file/33af2c68d9e4e297d733e.jpg','','','-1002126345865'],
        'Prema_Entha_Maduram_':['https://graph.org/file/6e25ea2e439c46bb6184a.jpg','','','-1002126345865'],
        'Ammayi_Garu_':['https://graph.org/file/f42f50a0838286f90e944.jpg','','','-1002126345865'],
        'Suryakantham_':['https://graph.org/file/f5f324be9836fdb1f95e9.jpg','','','-1002126345865']
}

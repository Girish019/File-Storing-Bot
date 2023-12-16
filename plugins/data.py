
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
        'Rajeshwari_Vilas_Coffee_Club_':['','','',''],
        'Seethe_Ramudi_Katnam_':['','','',''],
        'Mukkupudaka_':['','','',''],
        'Gundamma_Katha_':['','','',''],
        'Jabilli_Kosam_Aakashamalle_':['','','',''],
        'Subhasya_Seeghram_':['','','',''],
        'Oohalu_Gusagusalade_':['','','',''],
  #noon
        'Radhamma_Kuthuru_':['https://graph.org/file/9934bd7b3c3492dd01e42.jpg','','',''],
        'Chiranjeevi_Lakshmi_Sowbhagyavati_':['https://graph.org/file/f75069b1b3a99f5652e70.jpg','','',''],
        'Nindu_Noorella_Saavasam_':['https://graph.org/file/a4005c14fd51c5a32cc2c.jpg','','',''],
        'Jagadhatri_':['https://graph.org/file/ef6227a07dac67bc30785.jpg','','',''],
        'Padamati_Sandhyaragam_':['https://graph.org/file/c9444bffe703c0133a28f.jpg','','',''],
        'Trinayani_':['https://graph.org/file/33af2c68d9e4e297d733e.jpg','','',''],
        'Prema_Entha_Maduram_':['https://graph.org/file/6e25ea2e439c46bb6184a.jpg','','',''],
        'Ammayi_Garu_':['https://graph.org/file/f42f50a0838286f90e944.jpg','','',''],
        'Suryakantham_':['https://graph.org/file/f5f324be9836fdb1f95e9.jpg','','','']
  
}
DATAEVEN = {
        'Radhaku_Neevera_Praanam_':['https://graph.org/file/dc119c8d45919db61181c.jpg','moneycase.link','0c2406a0cf1b54db75fcba4cbb8e389bdc675eee','-1001942664190'],
        'Gundamma_Katha_':['https://graph.org/file/baff21a920cc09f0ba89a.jpg','tnvalue.in','ff426552eda72230153ea3450a0bce0557183ccb','-1001942664190'],
        'Rajeshwari_Vilas_Coffee_Club_':['https://graph.org/file/15328d049e6d89a06030a.jpg','links4money.com','f2c99e727ba0a517e53f77a31b4f79d8acfc318c','-1001942664190'],
        'Ammayi_Garu_':['https://graph.org/file/2afa02552352eb1ad1654.jpg','links4money.com','f2c99e727ba0a517e53f77a31b4f79d8acfc318c','-1001942664190'],
        'Oohalu_Gusagusalade_':['https://graph.org/file/66f92045eece717617ac1.jpg','links4money.com','668f8a8d31c4d5e55da03d0d21ae740f3caf5d14','-1001942664190'],
        'Maa_Varu_Mastaaru_':['https://graph.org/file/0c7b76e2ffba37dc80f24.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001942664190'],
        'Chiranjeevi_Lakshmi_Sowbhagyavati_':['https://graph.org/file/2a210b8e8c9c008a21626.jpg','tnvalue.in','8fc4e5a5a7f1d571adfc7c02537d7c1e73da1a15','-1001942664190'],
        'Jagadhatri_':['https://graph.org/file/ea7b3f138cbb1cbf89328.jpg','linkshortify.com','9e82f5e0d917c633234194f39c2985752efd67e0','-1001942664190'],
        'Trinayani_':['https://graph.org/file/db548886e1746a102b62a.jpg','tnshort.net','cfafc72b0df2558f0f5ad4e1c906ce9f783281e3','-1001942664190'],
        'Radhamma_Kuthuru_':['https://graph.org/file/edffb4f77446259b8ca5e.jpg','links4money.com','ba4f1e7f7cfbea8b02c4c031be2270e354e95d47','-1001942664190'],
        'Prema_Entha_Maduram_':['https://graph.org/file/875789bddf3b18111a8b1.jpg','links4money.com','668f8a8d31c4d5e55da03d0d21ae740f3caf5d14','-1001942664190'],
        'Nindu_Noorella_Saavasam_':['https://graph.org/file/6bf07ca5c1fd598b73478.jpg','linkshortify.com','4bc6f1e34d0409e5b8bd2197d42462bb1ec6048a','-1001942664190'],
        'Subhasya_Seeghram_':['https://graph.org/file/9a8a693eca9c41a57bade.jpg','tnshort.net','1183b34c88b1fd4e898d7d9dc7b6fc6a2bea9dd9','-1001942664190'],
        'Seethe_Ramudi_Katnam_':['https://graph.org/file/40879ee73f036312ebb91.jpg','tnvalue.in','8fc4e5a5a7f1d571adfc7c02537d7c1e73da1a15','-1001942664190'],
}

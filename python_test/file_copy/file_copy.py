import os
from PIL import Image
from shutil import copyfile

filename_dir_path = '/home/hs.moon/data/yolov4_train_ssd'
src_dir_path = '/home/hs.moon/data/face/WIDER_train/images/'
des_dir_path = '/home/hs.moon/data/yolov4_train_ssd/'

origin_file_dir = ['0--Parade','1--Handshaking','2--Demonstration','3--Riot','4--Dancing','5--Car_Accident','6--Funeral','7--Cheering','8--Election_Campain','9--Press_Conference',
                   '10--People_Marching','11--Meeting','12--Group','13--Interview','14--Traffic','15--Stock_Market','16--Award_Ceremony','17--Ceremony','18--Concerts','19--Couple',
                   '20--Family_Group','21--Festival','22--Picnic','23--Shoppers','24--Soldier_Firing','25--Soldier_Patrol','26--Soldier_Drilling','27--Spa','28--Sports_Fan','29--Students_Schoolkids',
                   '30--Surgeons','31--Waiter_Waitress','32--Worker_Laborer','33--Running','34--Baseball','35--Basketball','36--Football','37--Soccer','38--Tennis','39--Ice_Skating',
                   '40--Gymnastics','41--Swimming', '42--Car_Racing', '43--Row_Boat', '44--Aerobics', '45--Balloonist',
                   '46--Jockey', '47--Matador_Bullfighter', '48--Parachutist_Paratrooper', '49--Greeting', 
                   '50--Celebration_Or_Party', '51--Dresses', '52--Photographers', '53--Raid', '54--Rescue',
                   '55--Sports_Coach_Trainer', '56--Voter', '57--Angler', '58--Hockey', '59--people--driving--car', '0',
                   '61--Street_Battle']

filenames = os.listdir(filename_dir_path)
for filename in filenames:
    head = filename.split('_')[0]
    filename_without_ext = filename.split('.')[0]
    print(filename)
    #print(head)
    #print(filename_without_ext)
    copyfile(src_dir_path+origin_file_dir[int(head)]+'/'+filename_without_ext+'.xml',des_dir_path+filename_without_ext+'.xml')


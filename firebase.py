import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import gmtime ,  strftime 
import datetime, pytz
from datetime import datetime , timezone , timedelta

tz = pytz.timezone('Asia/Bangkok')
now = datetime.now(tz)
time_now  = now.strftime("%H:%M")



cred = credentials.Certificate('keyfire/memoproject-f3d6e-firebase-adminsdk-fr0rq-4f172d0cbb.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

medical_refe = db.collection(u'medicine')


docs_medi = medical_refe.stream()

for medic in docs_medi:
    med = medic.to_dict()
    me = med['namemed']
    for ii in med['medtag']:
        if(ii == 'เช้า'):
            set_time = '01:30'
            if(time_now == set_time):
                print(me)
            else:
                print('0')
        else:
            set_time = '2.30'
            if(time_now == set_time):
                print(me)
            else:
                print('02')


    

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import gmtime ,  strftime


a = strftime("%H:%M")
print(a)
if a == '21:56':
    print("ok")
else:
    print("okk")

cred = credentials.Certificate('keyfire/memoproject-f3d6e-firebase-adminsdk-fr0rq-4f172d0cbb.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

medical_ref = db.collection(u'medical')
query_ref = medical_ref.where(u'time', u'==' , 'เช้า')

docs = query_ref.stream()


for doc in docs:
    medi = doc.to_dict()
    medi_loop = dict((k, v) for k, v in medi.items() if k == 'mname')
    print(medi_loop)
    # res = ''.join(key + str(val) for key, val in medi.items())
    # print(str(res))
 
  

    
    
    
 
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate("plaka_admin_sdk.json")
firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://plaka-e9d0b-default-rtdb.firebaseio.com'
})
ref = db.reference('/')
registered = ref.child('Registered')

registered.set({
    'Plate Number 1': 'NBC 1234',
    'Plate Number 2': '5678',
    'Plate Number 3': '9876',
    })
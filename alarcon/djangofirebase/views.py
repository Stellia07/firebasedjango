from django.shortcuts import render
import pyrebase

# Create your views here.
config = {
    "apiKey": "AIzaSyBQiUB90PTp-NcG9xcpe7W5vnzOPGLQYdc",
    "authDomain": "djangofirebase-7ab6f.firebaseapp.com",
    "projectId": "djangofirebase-7ab6f",
    "storageBucket": "djangofirebase-7ab6f.appspot.com",
    "messagingSenderId": "677165802371",
    "appId": "1:677165802371:web:be146982dc50d7ac038cb6",
    "databaseURL": "https://djangofirebase-7ab6f-default-rtdb.firebaseio.com",
    "measurementId": "G-4B1Q7SFQ21"
}



firebase-pyrebase.initialize_app (config)
authe-firebase.auth() 
database-firebase.database()
# Create your views here.
def index(request):
    my_recordname=database.child('Record').child('Name').get().val()
    my_recordage=database.child('Record').child('Age').get().val()
    my_recordprogram-database.child('Record').child('Program').get().val()
    my_recordschool-database.child('Record').child('School').get().val()
return render(request, 'index.html', {

"my_recordname": my_recordname,
"my_recordage":my_recordage,
"my_recordprogram": my_recordprogram,
"my_recordschool":my_recordschool,
})
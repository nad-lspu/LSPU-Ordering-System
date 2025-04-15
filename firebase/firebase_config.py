import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyC6WJzNijzPO8Bmg4mWEb_MIoJioj7xtJc",
    "authDomain": "grab-piyu-d.firebaseapp.com",
    "databaseURL": "https://grab-piyu-d-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "grab-piyu-d",
    "storageBucket": "grab-piyu-d.firebasestorage.app",
    "messagingSenderId": "grab-piyu-d.firebasestorage.app",
    "appId": "1:77622540773:web:df19e6b5e6dac23e61170c"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

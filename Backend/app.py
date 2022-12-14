from ast import JoinedStr
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, request, session, current_app, Blueprint, redirect
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func, create_engine
from datetime import datetime
## for JWT
from functools import wraps
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import requests
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
import os
import pathlib
import google.auth.transport.requests
from pip._vendor import cachecontrol


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TechRent.sqlite3'
app.config['SECRET_KEY'] = "randostring"
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    question1 = db.Column(db.String(256), nullable = False)
    question2 = db.Column(db.String(256), nullable = False)
    items = db.relationship('Items', backref="creator", lazy = False)

    def __init__(self, name, email, password, question1, question2):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password, method='sha256')
        self.question1 = question1
        self.question2 = question2

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not email or not password:
            print('Ivalid email:', email)
            print('Or invalid pword:', password)
            return None
        
        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            print('User not found')
            return None

        return user

    def to_dict(self):
        return dict(uid=self.uid, email=self.email, name=self.name)


class Items(db.Model):
    __tablename__ = 'items'

    # id, item_name, rating, brand, type, price, location, seller, image_url, posted_at
    id = db.Column(db.Integer, unique = True, primary_key=True)
    item_name = db.Column(db.String(50), nullable = False)
    rating = db.Column(db.Integer, nullable = True)
    brand = db.Column(db.String(50), nullable = True)
    item_type = db.Column(db.Text, nullable = True)
    price = db.Column(db.Float, nullable = False)
    location = db.Column(db.Text, nullable = False)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.uid'))
    image_url = db.Column(db.Text, nullable = False)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text, nullable = False)
    seller_email = db.Column(db.Text, nullable=True)
    seller_phone = db.Column(db.Text, nullable=True)

    def __init__(self, item_name, brand, item_type, price, location, seller_id, image_url, posted_at, description, seller_email, seller_phone):
        self.item_name = item_name
        self.brand = brand
        self.item_type = item_type
        self.price = price
        self.location = location
        self.seller_id = seller_id
        self.image_url = image_url
        self.posted_at = posted_at
        self.description = description
        self.seller_email = seller_email
        self.seller_phone = seller_phone

    def to_dict(self):
      return dict(id=self.id,
                  item_name=self.item_name,
                  posted_at=self.posted_at.strftime('%Y-%m-%d %H:%M:%S'),
                  seller_id=self.seller_id,
                  location=self.location,
                  price=self.price,
                  rating=self.rating,
                  brand=self.brand,
                  item_type=self.item_type,
                  image_url=self.image_url,
                  description=self.description,
                  seller_email=self.seller_email,
                  seller_phone=self.seller_phone
                  )

                
class Messages(db.Model):
    __tablename__ = 'messages'

    # mid, sender_username, recipient_username, message, sent_at
    mid = db.Column(db.Integer, unique = True, primary_key=True)
    sender_username = db.Column(db.String(50), nullable = False)
    recipient_username = db.Column(db.String(50), nullable = False)
    message_text = db.Column(db.String(500), nullable = True)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, sender_username, recipient_username, message_text, sent_at):
        self.sender_username = sender_username
        self.recipient_username = recipient_username
        self.message_text = message_text
        self.sent_at = sent_at

    def to_dict(self):
      return dict(mid=self.mid,
                  sender_username=self.sender_username,
                  recipient_username=self.recipient_username,
                  message = self.message_text,
                  sent_at=self.sent_at
                  )
class RefundReq(db.Model):
    __tablename__ = 'refund'

    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), primary_key=True, nullable = False)
    question1 = db.Column(db.String(256), nullable = False)
    
    def to_dict(self):
        return dict( name=self.name, email=self.email, question1=self.question1)
## decorator
def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            user = Users.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            print("Token Expired")
            return jsonify(expired_msg), 401 
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            print("Invalid Token")
            return jsonify(invalid_msg), 401

    return _verify


# @app.route("/")
@cross_origin()
# def helloWorld():
#   return "Hello, cross-origin-world!"


@app.route("/test",methods=['GET','POST'])
def test():
    return jsonify("Hkladjfiasdjfask ")


@app.route("/register", methods = ['GET','POST'])
def register():
    data = request.get_json()
    print('Request data: ', data)
    name = data['name']
    email = data['email']
    password = data['password']
    question1 = data['question1']
    question2 = data['question2']
    user = Users(name = name, email = email, password = password, question1=question1, question2=question2)
    db.session.add(user)
    db.session.commit()
    app.logger.info(user.uid)

    return jsonify(user.to_dict()), 201

@app.route('/login', methods=('POST',))
def login():
    data = request.get_json()
    user = Users.authenticate(**data)

    if not user:
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401

    token = jwt.encode({
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({ 'token': token, 'user': user.to_dict() })
    
@app.route('/items/', methods=('POST',))
#@token_required
def create_item():
    data = request.get_json()
    item_name = data['item_name']
    brand = data['brand']
    item_type = data['item_type']
    price = data['price']
    location = data['location']
    seller_id = data['seller_id']
    image_url = data['image_url']
    posted_at = datetime.now()
    description = data['description']
    seller_email = data['email']
    seller_phone = data['phone']
    item = Items(item_name=item_name, brand=brand, item_type=item_type, price=price, location=location, seller_id=seller_id, image_url=image_url, posted_at=posted_at, description=description, seller_email=seller_email, seller_phone=seller_phone)
    db.session.add(item)
    db.session.commit()
    app.logger.info(item.id)
    return jsonify(item.to_dict()), 201

@app.route('/messages', methods=('POST',))
#@token_required
def send_message():
    data = request.get_json()
    sender_username = data['sender_username']
    recipient_username = data['recipient']
    message_text = data['message']
    sent_at = datetime.now()
    message = Messages(sender_username = sender_username,recipient_username = recipient_username, message_text = message_text, sent_at = sent_at)
    db.session.add(message)
    db.session.commit()
    app.logger.info(message.mid)

    return jsonify(message.to_dict()), 201
    
    
@app.route('/items', methods=('GET',))
def fetch_items():
    items = Items.query.all()
    return jsonify([i.to_dict() for i in items])

@app.route('/messages', methods=('GET',))
def fetch_messages():
    messages = Messages.query.all()
    return jsonify([i.to_dict() for i in messages])

@app.route('/items/<int:item_id>', methods=('DELETE',))
#@token_required
def delete_item(item_id):
    item_to_delete = Items.query.get_or_404(item_id)
    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return jsonify(item_to_delete.to_dict()), 200
    except:
        return "There was an issue deleting the item"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "1086031692923-gtn8n1dn75oq563lkk54ahdsvm886okd.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)
def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper

@app.route("/")
def index():
    return "Hello World <a href='/googlelogin'><button>Login</button></a>"

@app.route("/googlelogin",methods=('GET',))
def googlelogin():
    authorization_url, state = flow.authorization_url()
    session["state"] = state

    return redirect(authorization_url)


@app.route("/protected_area")
@login_is_required
def protected_area():
    # return f"Hello {session['name']}! <br/> <a href='/googlelogout'><button>Logout</button></a>"
    return "protected <a href='/googlelogout'><button>Logout</button></a>"
    

@app.route("/googlelogout")
def googlelogout():
    session.clear()
    return redirect("/")

@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    # return id_info

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/protected_area")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()

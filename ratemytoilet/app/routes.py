from flask import request, jsonify
from app import app, db
from app.models import User, Location, Bathroom, Review

# Route to add a user
@app.route('/user/add', methods=['POST'])
def add_user():
    username = request.json.get('userName')
    user = User(userName=username)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added successfully!"}), 201

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.userName for user in users])

# Route to add a location
@app.route('/location/add', methods=['POST'])
def add_location():
    building = request.json.get('building')
    location = Location(building=building)
    db.session.add(location)
    db.session.commit()
    return jsonify({"message": "Location added successfully!"}), 201

# Route to get all locations
@app.route('/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify([loc.building for loc in locations])

# Route to add a bathroom
@app.route('/bathroom/add', methods=['POST'])
def add_bathroom():
    floor = request.json.get('floor')
    gender = request.json.get('gender')
    building = request.json.get('building')
    bathroom = Bathroom(floor=floor, gender=gender, building=building)
    db.session.add(bathroom)
    db.session.commit()
    return jsonify({"message": "Bathroom added successfully!"}), 201

# Route to get all bathrooms
@app.route('/bathrooms', methods=['GET'])
def get_bathrooms():
    bathrooms = Bathroom.query.all()
    return jsonify([{'floor': bath.floor, 'gender': bath.gender, 'building': bath.building} for bath in bathrooms])

# Route to add a review
@app.route('/review/add', methods=['POST'])
def add_review():
    additional_comments = request.json.get('additional_comments')
    overall_rating = request.json.get('overall_rating')
    cryability = request.json.get('cryability')
    cleanliness = request.json.get('cleanliness')
    poopability = request.json.get('poopability')
    userName = request.json.get('userName')
    bathroom_floor = request.json.get('bathroom_floor')
    bathroom_gender = request.json.get('bathroom_gender')
    review = Review(additional_comments=additional_comments, overall_rating=overall_rating, 
                    cryability=cryability, cleanliness=cleanliness, poopability=poopability,
                    userName=userName, bathroom_floor=bathroom_floor, bathroom_gender=bathroom_gender)
    db.session.add(review)
    db.session.commit()
    return jsonify({"message": "Review added successfully!"}), 201

# Route to get all reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([{'reviewID': rev.reviewID, 'additional_comments': rev.additional_comments, 
                     'overall_rating': rev.overall_rating, 'cryability': rev.cryability, 
                     'cleanliness': rev.cleanliness, 'poopability': rev.poopability, 
                     'userName': rev.userName, 'bathroom_floor': rev.bathroom_floor, 
                     'bathroom_gender': rev.bathroom_gender} for rev in reviews])

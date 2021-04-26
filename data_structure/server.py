import random
from datetime import datetime
from sqlite3 import Connection as SQLite3Connection

from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine

import binary_search_tree
import hash_table
import linked_list
import custom_queues

# app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_structure.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# configure sqlite3 to enforce foreign key contraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()
        
db = SQLAlchemy(app)
now = datetime.now()

# models
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade="all, delete")


class BlogPost(db.Model):
    __tablename__ = 'blog_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    
# routes
@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        name = data["name"],
        email = data["email"],
        address = data["address"],
        phone = data["phone"],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 200


@app.route("/user/descending_id", methods=["GET"])
def get_all_user_descending():
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()
    for user in users:
        all_users_ll.insert_beginning(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "phone": user.phone,
                "address": user.address,
            }
        )
    return jsonify(all_users_ll.to_list()), 200
        

@app.route("/user/ascending_id", methods=["GET"])
def get_all_user_ascending():
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()
    for user in users:
        all_users_ll.insert_at_end(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "phone": user.phone,
                "address": user.address,
            }
        )
    return jsonify(all_users_ll.to_list()), 200

@app.route("/user/<user_id>", methods=["GET"])
def get_one_user(user_id):
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()
    for user in users:
        all_users_ll.insert_beginning(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "phone": user.phone,
                "address": user.address,
            }
        )
    try:
        user = all_users_ll.get_user_by_id(user_id)
        return jsonify(user), 200
    except AttributeError as e:
        return jsonify({'message': 'user not found'}), 500
        

@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({'msg': 'user deleted'}), 200 

@app.route("/blog_post/<user_id>", methods=["POST"])
def create_post(user_id):
    data = request.get_json()
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({'meesage': "user doesn't exist"}), 400
    
    ht = hash_table.HashTable(10)
    ht.add_key_value("title", data["title"])
    ht.add_key_value("body", data["body"])
    ht.add_key_value("date", now)
    ht.add_key_value("user_id", user_id)
    
    new_post = BlogPost(
        title = ht.get_value('title'),
        body = ht.get_value('body'),
        date = ht.get_value('date'),
        user_id = ht.get_value('user_id')
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'meesage': "a new post created"}), 200

@app.route("/blog_post/<blog_post_id>", methods=["GET"])
def get_post(blog_post_id):
    blog_posts = BlogPost.query.all()
    random.shuffle(blog_posts)
    
    bst = binary_search_tree.BinarySearchTree()
    
    for post in blog_posts:
        bst.insert({
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "user_id": post.user_id,
        })
        
    post = bst.search(blog_post_id)
    if not post:
        return jsonify({"message": "post not found"}), 400
    return jsonify(post)

@app.route('/blog_post/numeric_body', methods=["GET"])
def get_numeric_post_bodies():
    posts = BlogPost.query.all()
    
    q = custom_queues.Queue()
    
    for post in posts:
        q.enqueue(post)
        
    return_list = list()
    
    for _ in range(len(posts)):
        post = q.dequeue()
        numeric_body = 0
        for char in post.data.body:
            numeric_body += ord(char)
            
        post.data.body = numeric_body
        
        return_list.append(
            {
                "id": post.data.id,
                "title": post.data.title,
                "body": post.data.body,
                "user_id": post.data.user_id,
            }
        )
    
    return jsonify(return_list)
        
    

@app.route("/user/<user_id>", methods=["GET"])
def get_all_posts(user_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods=["DELETE"])
def delete_post(blog_post_id):
    pass

if __name__ == "__main__":
    app.run(debug=True) 

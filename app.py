from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f'{self.id} {self.content}'


if not path.exists('database.db'):
        with app.app_context():
            db.create_all()

def todo_serializer(todo):
    return {
       'id': todo.id,
       'content': todo.content 
    }


@app.route('/api', methods=['GET'])
def home():
    return ([*map(todo_serializer, Todo.query.all())])

@app.route('/api/create', methods=['POST'])
def create():
    request_data = json.loads(request.data)
    todo = Todo(content=request_data['content'])
    with app.app_context():
        db.session.add(todo)
        db.session.commit()

    return {'201': 'Todo created successfully'}

@app.route('/api/<int:id>')
def show(id):
    return ([*map(todo_serializer, Todo.query.filter_by(id=id))])

@app.route('/api/<int:id>', methods=['POST'])
def delete(id):
    request_data = json.loads(request.data)
    Todo.query.filter_by(id=request_data['id']).delete()
    db.session.commit()

    return {'204': 'Deleted successfully'}

if __name__ == '__main__':
    app.run(debug=True)
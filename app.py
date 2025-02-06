from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (for simplicity)
posts = []

@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/api/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post = {'content': data['content']}
    posts.append(post)
    return jsonify(post), 201

if __name__ == '__main__':
    app.run(debug=True)

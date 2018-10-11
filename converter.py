from flask import Flask
app = Flask(__name__)
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'blog number %d' %postID
@app.route('/rev/<float:revno>')
def revision(revno):
    return 'Revision number %f' % revno
if __name__ == '__main__':
    app.run()

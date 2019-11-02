from flask import jsonify, request, g, url_for, current_app, flash, \
    jsonify, request, redirect, send_from_directory, render_template

from werkzeug.utils import secure_filename
from .. import db
from ..models import Post, Permission, ImageProfile
from . import api
from .decorators import permission_required
from .errors import forbidden


ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])


# fun to check the file type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# predict.
@api.route('/predict', methods=['GET', 'POST'])
def new_prediction():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return jsonify({"description":"no file part"})
            
        file = request.files['image']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return jsonify({"description":"no selected file"})

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            thisdir = os.path.abspath(os.path.dirname(__file__))
            IMAGES_FOLDER = os.path.join(thisdir, 'saved_images')
            file.save(os.path.join( IMAGES_FOLDER, filename ))
            # data
            lname = request.form['lastname']
            fname = request.form['firstname']
            description = request.form['description']
            # get the file path
            file_path = os.path.join(IMAGES_FOLDER, filename)
            # make the prediction
            prediction = predict(file_path)
            results = str(prediction)

            image_data = ImageProfile(firstname=firstname,
                                  lastname=lastname,
                                  imagename=filename,
                                  result=results,
                                  description=description)
            db.session.add(image_data)
            db.session.commit()
            return image_schema.jsonify(image_data)
            # return redirect(url_for('uploaded_file', filename=filename))
        else:
            print("That file extension is not allowed")
            return redirect(request.url)

    return render_template("api/predict_api.html")


# @api.route('/posts/')
# def get_posts():
#     page = request.args.get('page', 1, type=int)
#     pagination = Post.query.paginate(
#         page, per_page=current_app.config['VISUAL_DIAGNOSER_POSTS_PER_PAGE'],
#         error_out=False)
#     posts = pagination.items
#     prev = None
#     if pagination.has_prev:
#         prev = url_for('api.get_posts', page=page-1)
#     next = None
#     if pagination.has_next:
#         next = url_for('api.get_posts', page=page+1)
#     return jsonify({
#         'posts': [post.to_json() for post in posts],
#         'prev': prev,
#         'next': next,
#         'count': pagination.total
#     })


# @api.route('/posts/<int:id>')
# def get_post(id):
#     post = Post.query.get_or_404(id)
#     return jsonify(post.to_json())


# @api.route('/posts/', methods=['POST'])
# @permission_required(Permission.WRITE)
# def new_post():
#     post = Post.from_json(request.json)
#     post.author = g.current_user
#     db.session.add(post)
#     db.session.commit()
#     return jsonify(post.to_json()), 201, \
#         {'Location': url_for('api.get_post', id=post.id)}


# @api.route('/posts/<int:id>', methods=['PUT'])
# @permission_required(Permission.WRITE)
# def edit_post(id):
#     post = Post.query.get_or_404(id)
#     if g.current_user != post.author and \
#             not g.current_user.can(Permission.ADMIN):
#         return forbidden('Insufficient permissions')
#     post.body = request.json.get('body', post.body)
#     db.session.add(post)
#     db.session.commit()
#     return jsonify(post.to_json())

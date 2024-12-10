from app import app, response
from app.controller import AdminsController, CategoriesController, ProductsController, ArticlesController, CommentsController
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controller.ProductsController import Products, format_array

@app.route('/')
def index():
    return 'Hello Flask App'

@app.route('/api/login', methods=['POST'])
def loginAdmin():
    return AdminsController.loginAdmin()

@app.route('/api/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh_token():
    return AdminsController.refreshToken()

@app.route('/api/me', methods=['GET'])
@jwt_required()
def getMe():
    return AdminsController.get_me()

@app.route('/api/admin', methods=['GET', 'POST'])
@jwt_required()
def admins():
    if request.method == 'GET':
        return AdminsController.indexAdmin()
    else:
        return AdminsController.tambahAdmin()

@app.route('/api/admin/default', methods=['POST'])
def default():
    return AdminsController.defaultAdmin()

@app.route('/api/admin/<id>', methods=["GET", "PUT", "DELETE"])
@jwt_required()
def adminDetail(id):
    if request.method == 'GET':
        return AdminsController.detail_admin(id)
    elif request.method == "PUT":
        return AdminsController.ubahAdmin(id)
    elif request.method == "DELETE":
        return AdminsController.hapusAdmin(id)

@app.route('/api/category', methods=['GET', 'POST'])
@jwt_required()
def categories():
    if request.method == 'GET':
        return CategoriesController.indexCategory()
    else:
        return CategoriesController.tambahCategory()

@app.route('/api/category/<id>', methods=["PUT", "DELETE"])
@jwt_required()
def categoryDetail(id):
    if request.method == "PUT":
        return CategoriesController.ubahCategory(id)
    else:
        return CategoriesController.hapusCategory(id)

@app.route('/api/product', methods=['GET', 'POST'])
@jwt_required()
def products():
    if request.method == 'GET':
        return ProductsController.paginate_and_filter_manage()
    else:
        return ProductsController.tambahProduct()

@app.route('/api/product/<id>', methods=["GET", "PUT", "DELETE"])
@jwt_required()
def productDetail(id):
    if request.method == 'GET':
        return ProductsController.detail_product(id)
    elif request.method == "PUT":
        return ProductsController.ubahProduct(id)
    elif request.method == "DELETE":
        return ProductsController.hapusProduct(id)

@app.route('/api/product/guest', methods=['GET'])
def guestProduct():
    return ProductsController.paginate_and_filter()

@app.route('/api/product/guest/<id>', methods=["GET"])
def productGuestDetail(id):
    return ProductsController.detail_product(id)

@app.route('/api/article', methods=['GET', 'POST'])
@jwt_required()
def articles():
    if request.method == 'GET':
        return ArticlesController.paginateAndFilterArticlesManage()
    else:
        return ArticlesController.tambahArticle()

@app.route('/api/article/<id>', methods=["GET", "PUT", "DELETE"])
@jwt_required()
def detailArticle(id):
    if request.method == 'GET':
        return ArticlesController.detailArticleManage(id)
    elif request.method == "PUT":
        return ArticlesController.ubahArticle(id)
    elif request.method == "DELETE":
        return ArticlesController.hapusArticle(id)

@app.route('/api/article/guest', methods=['GET'])
def guestArticles():
    return ArticlesController.paginateAndFilterArticles()

@app.route('/api/article/guest/<id>', methods=['GET', 'POST'])
def guestDetailArticle(id):
    if request.method == 'GET':
        return ArticlesController.detailArticle(id)
    elif request.method == 'POST':
        return ArticlesController.tambahCommentForArticle(id)

@app.route('/api/comment', methods=['GET'])
@jwt_required()
def comments():
    return CommentsController.paginateAndFilterCommentsManage()

@app.route('/api/comment/<id>', methods=["GET", "PUT", "DELETE"])
@jwt_required()
def commentDetail(id):
    if request.method == 'GET':
        return CommentsController.detailComment(id)
    elif request.method == "PUT":
        return CommentsController.ubahComment(id)
    elif request.method == "DELETE":
        return CommentsController.hapusComment(id)




from flask import request
from app.model.products import Products
from app.model.admins import Admins
from app.model.categories import Categories
from app import response, db, app
import math
import re

def indexProduct():
    try:
        products = Products.query.all()
        data = format_array(products)
        return response.success(data)
    except Exception as e:
        print(e)
        return response.serverError([], "Gagal mengambil data produk.")

def format_array(datas):
    return [single_object(data) for data in datas]

def single_object(data):
    return {
        'id': data.id,
        'created_by': data.admin.name,
        'category_name': data.category.category_name,
        'product_name': data.product_name,
        'description': data.description,
        'price': str(data.price),
        'contact': data.contact,
        'img_file': data.img_file,
        'created_at': data.created_at,
        'updated_at': data.updated_at
    }

def detail_product(id):
    try:
        product = Products.query.filter_by(id=id).first()
        if not product:
            return response.notFound([], 'Produk tidak ditemukan')

        data = single_object(product)
        return response.success(data)
    except Exception as e:
        print(e)
        return response.serverError([], "Gagal mengambil detail produk.")

def tambahProduct():
    try:
        created_by = request.form.get('created_by') or request.json.get('created_by')
        category_id = request.form.get('category_id') or request.json.get('category_id')
        product_name = request.form.get('product_name') or request.json.get('product_name')
        description = request.form.get('description') or request.json.get('description')
        price = request.form.get('price') or request.json.get('price')
        contact = request.form.get('contact') or request.json.get('contact')
        img_file = request.form.get('img_file') or request.json.get('img_file')

        if not all([created_by, category_id, product_name, price]):
            return response.badRequest([], "Kolom created_by, category_id, product_name, dan price wajib diisi.")
        
        if not re.match(r'^[a-zA-Z0-9 ]*$', product_name):
            return response.badRequest([], "Nama produk tidak boleh mengandung karakter khusus.")

        if len(product_name) < 3 or len(product_name) > 100:
            return response.badRequest([], "Nama produk harus antara 3 hingga 100 karakter.")
        
        if description and (len(description) < 10 or len(description) > 10000):
            return response.badRequest([], "Deskripsi harus antara 10 hingga 10000 karakter.")

        # if contact and not re.match(r'^\d+$', contact):
        #     return response.badRequest([], "Kontak harus berupa angka.")

        try:
            price = float(price)
            if price <= 0:
                return response.badRequest([], "Harga harus lebih besar dari 0.")
        except ValueError:
            return response.badRequest([], "Harga harus berupa angka.")

        admin = Admins.query.filter_by(id=created_by).first()
        if not admin:
            return response.notFound([], "Admin ID tidak valid.")

        category = Categories.query.filter_by(id=category_id).first()
        if not category:
            return response.notFound([], "Category ID tidak valid.")

        try:
            price = float(price)
            if price <= 0:
                return response.badRequest([], "Harga harus lebih besar dari 0.")
        except ValueError:
            return response.badRequest([], "Harga harus berupa angka.")

        product = Products(
            created_by=created_by,
            category_id=category_id,
            product_name=product_name,
            description=description,
            price=price,
            contact=contact,
            img_file=img_file
        )

        db.session.add(product)
        db.session.commit()

        return response.created([], 'Sukses Menambahkan Data Produk')

    except Exception as e:
        db.session.rollback()
        print(e)
        return response.serverError([], f"Gagal menambahkan produk: {str(e)}")

def ubahProduct(id):
    try:
        product = Products.query.filter_by(id=id).first()
        if not product:
            return response.notFound([], "Produk tidak ditemukan.")

        created_by = request.form.get('created_by') or request.json.get('created_by')
        category_id = request.form.get('category_id') or request.json.get('category_id')
        product_name = request.form.get('product_name') or request.json.get('product_name')
        description = request.form.get('description') or request.json.get('description')
        price = request.form.get('price') or request.json.get('price')
        contact = request.form.get('contact') or request.json.get('contact')
        img_file = request.form.get('img_file') or request.json.get('img_file')

        if not all([created_by, category_id, product_name, price]):
            return response.badRequest([], "Kolom created_by, category_id, product_name, dan price wajib diisi.")
        
        if not re.match(r'^[a-zA-Z0-9 ]*$', product_name):
            return response.badRequest([], "Nama produk tidak boleh mengandung karakter khusus.")

        if len(product_name) < 3 or len(product_name) > 100:
            return response.badRequest([], "Nama produk harus antara 3 hingga 100 karakter.")
        
        if description and (len(description) < 10 or len(description) > 10000):
            return response.badRequest([], "Deskripsi harus antara 10 hingga 10000 karakter.")

        # if contact and not re.match(r'^\d+$', contact):
        #     return response.badRequest([], "Kontak harus berupa angka.")

        try:
            price = float(price)
            if price <= 0:
                return response.badRequest([], "Harga harus lebih besar dari 0.")
        except ValueError:
            return response.badRequest([], "Harga harus berupa angka.")

        product.created_by = created_by
        product.category_id = category_id
        product.product_name = product_name
        product.description = description
        product.price = price
        product.contact = contact
        product.img_file = img_file

        db.session.commit()

        return response.success(single_object(product))

    except Exception as e:
        db.session.rollback()
        print(e)
        return response.serverError([], "Gagal mengubah data produk.")

def hapusProduct(id):
    try:
        product = Products.query.filter_by(id=id).first()
        
        if not product:
            return response.notFound([], "Produk tidak ditemukan.")
        
        db.session.delete(product)
        db.session.commit()
        return response.success('Sukses menghapus produk!')

    except Exception as e:
        db.session.rollback()
        print(e)
        return response.serverError([], "Gagal menghapus produk.")

def paginate_and_filter():
    try:
        start = request.args.get('start', default=1, type=int)
        limit = request.args.get('limit', default=4, type=int)

        category_name = request.args.get('category_name', type=str)
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        keyword = request.args.get('keyword', type=str)

        query = Products.query

        if category_name:
            category = Categories.query.filter_by(category_name=category_name).first()
            if not category:
                return response.notFound([], "Kategori tidak ditemukan.")
            query = query.filter_by(category_id=category.id)

        if min_price is not None and max_price is not None:
            if min_price > max_price:
                return response.badRequest([], "Harga minimum tidak boleh lebih besar dari harga maksimum.")
            query = query.filter(Products.price.between(min_price, max_price))
        elif min_price is not None:
            query = query.filter(Products.price >= min_price)
        elif max_price is not None:
            query = query.filter(Products.price <= max_price)

        if keyword:
            keyword = f"%{keyword}%"
            query = query.filter(
                Products.product_name.ilike(keyword) | 
                Products.description.ilike(keyword)
            )

        total_data = query.count()

        if start < 1 or limit < 1:
            return response.badRequest([], "Parameter start dan limit harus lebih besar dari 0.")

        products = query.offset(start - 1).limit(limit).all()

        if not products:
            return response.notFound([], "Tidak ada produk yang ditemukan.")

        categories = Categories.query.all()
        category_names = [category.category_name for category in categories]

        pagination_data = {
            'success': True,
            'start_index': start,
            'per_page': limit,
            'total_data': total_data,
            'results': format_array(products),
        }

        base_url = "http://127.0.0.1:5000/api/product/guest"

        filter_params = []
        if category_name:
            filter_params.append(f"category_name={category_name}")
        if min_price is not None:
            filter_params.append(f"min_price={int(min_price) if min_price.is_integer() else min_price}")
        if max_price is not None:
            filter_params.append(f"max_price={int(max_price) if max_price.is_integer() else max_price}")
        if keyword:
            filter_params.append(f"keyword={keyword}")

        filter_query = "&".join(filter_params)

        if start > 1:
            previous_start = max(1, start - limit)
            previous_query = f"start={previous_start}&limit={limit}"
            pagination_data['previous'] = f"{base_url}?{previous_query}&{filter_query}" if filter_query else f"{base_url}?{previous_query}"
        else:
            pagination_data['previous'] = None

        if start + limit <= total_data:
            next_start = start + limit
            next_query = f"start={next_start}&limit={limit}"
            pagination_data['next'] = f"{base_url}?{next_query}&{filter_query}" if filter_query else f"{base_url}?{next_query}"
        else:
            pagination_data['next'] = None

        final_response = {
            'categories': category_names,
            'pagination': pagination_data
        }

        return response.success(final_response)

    except Exception as e:
        print(e)
        return response.serverError([], "Gagal mengambil data produk.")
    
def paginate_and_filter_manage():
    try:
        start = request.args.get('start', default=1, type=int)
        limit = request.args.get('limit', default=5, type=int)

        category_name = request.args.get('category_name', type=str)
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        keyword = request.args.get('keyword', type=str)

        query = Products.query

        if category_name:
            category = Categories.query.filter_by(category_name=category_name).first()
            if not category:
                return response.notFound([], "Kategori tidak ditemukan.")
            query = query.filter_by(category_id=category.id)

        if min_price is not None and max_price is not None:
            if min_price > max_price:
                return response.badRequest([], "Harga minimum tidak boleh lebih besar dari harga maksimum.")
            query = query.filter(Products.price.between(min_price, max_price))
        elif min_price is not None:
            query = query.filter(Products.price >= min_price)
        elif max_price is not None:
            query = query.filter(Products.price <= max_price)

        if keyword:
            keyword = f"%{keyword}%"
            query = query.filter(
                Products.product_name.ilike(keyword)
            )

        total_data = query.count()

        if start < 1 or limit < 1:
            return response.badRequest([], "Parameter start dan limit harus lebih besar dari 0.")

        products = query.offset(start - 1).limit(limit).all()

        if not products:
            return response.notFound([], "Tidak ada produk yang ditemukan.")

        categories = Categories.query.all()
        category_names = [category.category_name for category in categories]

        pagination_data = {
            'success': True,
            'start_index': start,
            'per_page': limit,
            'total_data': total_data,
            'results': format_array(products),
        }

        base_url = "http://127.0.0.1:5000/api/product"

        filter_params = []
        if category_name:
            filter_params.append(f"category_name={category_name}")
        if min_price is not None:
            filter_params.append(f"min_price={int(min_price) if min_price.is_integer() else min_price}")
        if max_price is not None:
            filter_params.append(f"max_price={int(max_price) if max_price.is_integer() else max_price}")
        if keyword:
            filter_params.append(f"keyword={keyword}")

        filter_query = "&".join(filter_params)

        if start > 1:
            previous_start = max(1, start - limit)
            previous_query = f"start={previous_start}&limit={limit}"
            pagination_data['previous'] = f"{base_url}?{previous_query}&{filter_query}" if filter_query else f"{base_url}?{previous_query}"
        else:
            pagination_data['previous'] = None

        if start + limit <= total_data:
            next_start = start + limit
            next_query = f"start={next_start}&limit={limit}"
            pagination_data['next'] = f"{base_url}?{next_query}&{filter_query}" if filter_query else f"{base_url}?{next_query}"
        else:
            pagination_data['next'] = None

        final_response = {
            'categories': category_names,
            'pagination': pagination_data
        }

        return response.success(final_response)

    except Exception as e:
        print(e)
        return response.serverError([], "Gagal mengambil data produk.")

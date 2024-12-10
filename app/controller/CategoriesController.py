from flask import request
from app.model.categories import Categories
from app.model.products import Products
from app import response, db, app
import re

def indexCategory():
    try:
        categories = Categories.query.all()
        data = [
            {
                'id': category.id,
                'category_name': category.category_name,
                'product_count': len(category.products),
                'created_at': category.created_at
            }
            for category in categories
        ]

        return response.success(data)
    except Exception as e:
        print(e)
        return response.serverError([], "Gagal mengambil data kategori.")

def format_array(datas):
    return [single_object(data) for data in datas]

def single_object(data):
    return {
        'id': data.id,
        'category_name': data.category_name,
        'created_at': data.created_at
    }

def tambahCategory():
    try:
        category_name = request.form.get('category_name') or request.json.get('category_name')

        if not category_name:
            return response.badRequest([], "Nama kategori wajib diisi.")
        
        if len(category_name) < 3:
            return response.badRequest([], "Nama kategori harus terdiri dari minimal 3 karakter.")
        
        if Categories.query.filter_by(category_name=category_name).first():
            return response.badRequest([], "Nama kategori sudah ada.")
        
        if len(category_name) > 50:
            return response.badRequest([], "Nama kategori tidak boleh lebih dari 50 karakter.")
        
        if not re.match("^[a-zA-Z0-9\s]+$", category_name):
            return response.badRequest([], "Nama kategori hanya boleh berisi huruf, angka, dan spasi.")

        category = Categories(category_name=category_name)
        db.session.add(category)
        db.session.commit()
        return response.created([], 'Sukses Menambahkan Data Category')
    except Exception as e:
        db.session.rollback()
        print(e)
        return response.serverError([], "Gagal menambahkan kategori.")

def ubahCategory(id):
    try:
        category_name = request.form.get('category_name') or request.json.get('category_name')
        if not category_name:
            return response.badRequest([], "Nama kategori wajib diisi.")
        
        if len(category_name) < 3:
            return response.badRequest([], "Nama kategori harus terdiri dari minimal 3 karakter.")
        
        if len(category_name) > 50:
            return response.badRequest([], "Nama kategori tidak boleh lebih dari 50 karakter.")
        
        if not re.match("^[a-zA-Z0-9\s]+$", category_name):
            return response.badRequest([], "Nama kategori hanya boleh berisi huruf, angka, dan spasi.")

        category = Categories.query.filter_by(id=id).first()
        if not category:
            return response.notFound([], "Kategori tidak ditemukan.")

        category.category_name = category_name
        db.session.commit()
        return response.success(single_object(category))
    except Exception as e:
        db.session.rollback()
        print(e)
        return response.serverError([], "Gagal mengubah data kategori.")

def hapusCategory(id):
    try:
        category = Categories.query.filter_by(id=id).first()
        if not category:
            return response.notFound([], 'Kategori tidak ditemukan.')

        db.session.delete(category)
        db.session.commit()
        return response.success('Berhasil menghapus kategori!')
    except Exception as e:
        db.session.rollback()
        print(e)
        return response.serverError([], "Gagal menghapus kategori.")
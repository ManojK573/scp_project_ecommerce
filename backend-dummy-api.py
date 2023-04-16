from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pymysql
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


#----------------getproducts(GET)--------------------------------#
# import pymysql
# import json
# import decimal

# class DecimalEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, decimal.Decimal):
#             return str(o)
#         return super(DecimalEncoder, self).default(o)

def lambda_handler_getproducts(event, context):
    connection = pymysql.connect(
    host = 'database-2.cwlja8pndlom.us-east-1.rds.amazonaws.com',
    user ='admin',
    password = 'admin123',
    db = 'edenthought',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
    )

    allproductsresult = []
    with connection.cursor() as cursor:
        query = 'SELECT p.id, p.title, p.brand, p.description,p.slug, p.price,p.image,c.name as category FROM store_product as p inner join store_category as c on p.category_id = c.id;'
        cursor.execute(query)
        allproductsresult = cursor.fetchall()
    
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,GET'
    }

    response = {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(allproductsresult,cls=DecimalEncoder)
    }

    return response

#-------------getproducts------------------------------------------------#

#-------------filterproductsbycategory(POST)---------------------------------------------#
# import pymysql
# import json
# import decimal

# class DecimalEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, decimal.Decimal):
#             return str(o)
#         return super(DecimalEncoder, self).default(o)

def lambda_handler_filterproductsbycategory(event, context):
    connection = pymysql.connect(
    host = 'database-2.cwlja8pndlom.us-east-1.rds.amazonaws.com',
    user ='admin',
    password = 'admin123',
    db = 'edenthought',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
    )

    allproductsresult = []
    category = event['category']
    with connection.cursor() as cursor:
        query = 'SELECT p.id, p.title, p.brand, p.description,p.slug, p.price,p.image,c.name as category FROM store_product as p inner join store_category as c on p.category_id = c.id where c.slug = "'+ category +'";'
        cursor.execute(query)
        allproductsresult = cursor.fetchall()
    
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,GET,POST'
    }

    response = {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(allproductsresult,cls=DecimalEncoder)
    }

    return response
#-------------filterproductsbycategory---------------------------------------------#

#-------------getproductdetails(POST)---------------------------------------------#
# import pymysql
# import json
# import decimal

# class DecimalEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, decimal.Decimal):
#             return str(o)
#         return super(DecimalEncoder, self).default(o)

def lambda_handler_getproductdetails(event, context):
    connection = pymysql.connect(
    host = 'database-2.cwlja8pndlom.us-east-1.rds.amazonaws.com',
    user ='admin',
    password = 'admin123',
    db = 'edenthought',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
    )

    allproductsresult = []
    product = event['product']
    with connection.cursor() as cursor:
        query = 'SELECT p.id, p.title, p.brand, p.description,p.slug, p.price,p.image,c.name as category FROM store_product as p inner join store_category as c on p.category_id = c.id where p.slug = "'+ product +'";'
        cursor.execute(query)
        allproductsresult = cursor.fetchall()
    
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,GET,POST'
    }

    response = {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(allproductsresult,cls=DecimalEncoder)
    }

    return response
#-------------getproductdetails---------------------------------------------#

#-------------getcategories(GET)-------------------------------------------------#
# import pymysql
# import json
# import decimal

def lambda_handler_getcategories(event, context):
    connection = pymysql.connect(
    host = 'database-2.cwlja8pndlom.us-east-1.rds.amazonaws.com',
    user ='admin',
    password = 'admin123',
    db = 'edenthought',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
    )

    allcategoryresult = []
    with connection.cursor() as cursor:
        query = 'SELECT * from store_category;'
        cursor.execute(query)
        allcategoryresult = cursor.fetchall()
    
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,GET'
    }

    response = {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(allcategoryresult)
    }

    return response
#-----------------getcategories-----------------------------------------#


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/getproducts')
@cross_origin()
def get_products():
    res = lambda_handler_getproducts({},{})
    return res['body']
    # category = request.args.get('category')
    # product = request.args.get('product')
    # with connection.cursor() as cursor:
    #     query = 'SELECT p.id, p.title, p.brand, p.description,p.slug, p.price,p.image,c.name as category FROM store_product as p inner join store_category as c on p.category_id = c.id'
    #     if(category != None):
    #         query = query+' where c.slug = "'+ category +'";'
    #     if(product != None):
    #         query = query+' where p.slug = "'+ product +'";'
    #     cursor.execute(query)
    #     allproductsresult = cursor.fetchall()
    #     return jsonify(allproductsresult)

@app.route('/filterproductsbycategory',methods = ['POST'])
@cross_origin()
def get_products_by_category():
    category = request.json
    print(category)
    res = lambda_handler_filterproductsbycategory(category,{})
    print(res)
    return res['body']

@app.route('/getproductdetails',methods = ['POST'])
@cross_origin()
def get_product_details():
    product = request.json
    print(product)
    res = lambda_handler_getproductdetails(product,{})
    print(res)
    return res['body']

@app.route('/getcategories')
@cross_origin()
def get_products_getcategories():
    res = lambda_handler_getcategories({},{})
    print(res)
    return res['body']
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

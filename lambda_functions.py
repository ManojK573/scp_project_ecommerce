#----------------getproducts(GET)--------------------------------#
import pymysql
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
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
import pymysql
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
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
import pymysql
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
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
import pymysql
import json
import decimal

def lambda_handler(event, context):
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
import psycopg2, os


def make_query(user):
    conn = psycopg2.connect(
        database=os.environ.get('POSTGRES_TABLE_NAME'), 
        user=os.environ.get('POSTGRES_USER'), 
        password=os.environ.get('POSTGRES_PASSWORD'), 
        host=os.environ.get('POSTGRES_HOST'), 
        port=os.environ.get('POSTGRES_PORT')
    )
    
    conn.autocommit = True
    cursor = conn.cursor()
    
    sql = f"SELECT color_favorito FROM users_usuarios WHERE usuario='{user}';"
    
    cursor.execute(sql)
    results = cursor.fetchall()
    print(sql)
    conn.commit()
    conn.close()
    return results
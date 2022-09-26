import psycopg2, os

data = [
    {'usuario': 'Tflow', 'contrasena': 'contraseñasegura123', 'color_favorito': 'magenta'},
    {'usuario': 'satoshi', 'contrasena': 'helloworld@', 'color_favorito': 'rojo'},
    {'usuario': 'admin', 'contrasena': 'DCCTF{noob_x03659_W3B}', 'color_favorito': 'que te importa'},
    {'usuario': 'Kingpin', 'contrasena': 'contraseñasegura123', 'color_favorito': 'verde'},
    {'usuario': 'geohot', 'contrasena': '#@|#1dqjidq', 'color_favorito': 'naranjo'},
    {'usuario': 'snowden', 'contrasena': 'dHw87d21g8^3', 'color_favorito': 'azul'},
    {'usuario': 'c0mrade', 'contrasena': '$d8qh2@A2_e2', 'color_favorito': 'amarillo'},
]

conn = psycopg2.connect(
    database=os.environ.get('POSTGRES_TABLE_NAME'), 
    user=os.environ.get('POSTGRES_USER'), 
    password=os.environ.get('POSTGRES_PASSWORD'), 
    host=os.environ.get('POSTGRES_HOST'), 
    port=os.environ.get('POSTGRES_PORT')
)

conn.autocommit = True

cursor = conn.cursor()

for user in data:
    cursor.execute(f"INSERT INTO users_usuarios (usuario, contrasena, color_favorito) VALUES ('{user['usuario']}', '{user['contrasena']}', '{user['color_favorito']}');")

conn.commit()
conn.close()

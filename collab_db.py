import sqlite3

def init_collab_db():
    conn = sqlite3.connect('collab_posts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, status TEXT, comments TEXT)''')
    conn.commit()
    conn.close()

def add_post(content):
    conn = sqlite3.connect('collab_posts.db')
    c = conn.cursor()
    c.execute('INSERT INTO posts (content, status, comments) VALUES (?, ?, ?)', (content, 'Draft', ''))
    conn.commit()
    conn.close()

def get_posts():
    conn = sqlite3.connect('collab_posts.db')
    c = conn.cursor()
    c.execute('SELECT id, content, status, comments FROM posts')
    posts = c.fetchall()
    conn.close()
    return posts

def update_post_status(post_id, status):
    conn = sqlite3.connect('collab_posts.db')
    c = conn.cursor()
    c.execute('UPDATE posts SET status=? WHERE id=?', (status, post_id))
    conn.commit()
    conn.close()

def add_comment(post_id, comment):
    conn = sqlite3.connect('collab_posts.db')
    c = conn.cursor()
    c.execute('UPDATE posts SET comments=? WHERE id=?', (comment, post_id))
    conn.commit()
    conn.close()
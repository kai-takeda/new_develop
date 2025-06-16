import sqlite3

# 接続
conn = sqlite3.connect('C:/sqlite/test.db')
cursor = conn.cursor()


print("=== 1. 基本的なデータ取得 ===")
# 全ての本を取得
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()
print("全ての本:")
for book in books:
    print(f"ID: {book[0]}, タイトル: {book[1]}, 著者: {book[2]}, 年: {book[3]}")
    
print("\n=== 2. 条件付き検索 ===")
# 特定の著者の本を検索
cursor.execute("SELECT * FROM books WHERE author = ?", ("夏目漱石",))
soseki_books = cursor.fetchall()
print("夏目漱石の作品:")
for book in soseki_books:
    print(f"- {book[1]} ({book[3]}年)")

# 変更を保存（INSERT/UPDATE/DELETE時）
conn.commit()

# 接続を閉じる
conn.close()
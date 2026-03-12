import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute ("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('notebook dell', 'computadores', 4200, 10)")
cursor.execute ("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('mouse logitech', 'perifericos', 90, 50)")
cursor.execute ("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('teclado gamer', 'perifericos', 250, 30)")
cursor.execute ("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('monitor samsung 24', 'monitores', 1100, 20)")
cursor.execute ("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('smartphone samsung', 'celulares', 2800, 15)")
cursor.execute ("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('headset gamer', 'audio', 350, 25)")
cursor.execute ("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('HD externo 1TB', 'armazenamento', 420, 18)")
cursor.execute ("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('SSD 480gb', 'armazenamento', 380, 22)")
cursor.execute ("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('WebCam full HD', 'acessorios', 200, 12)")
cursor.execute ("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('caixa de som bluetooth', 'audio', 260, 17)")

conexao.commit()
conexao.close()

print("DADOS INSERIDOS COM SUCESSO")
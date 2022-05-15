import psycopg2


con = psycopg2.connect(host='localhost', database='gerenciador', user='postgress', password='banco123')
cur = con.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis(hotel_id text PRIMARY KEY, \
                nome text, estrelas real, diaria real, cidade text)"

cur.execute(cria_tabela)
con.commit()
con.close()

from models.cadastro import cadastro
import services.database as db;

def incluir(cadastro):
    count = db.cursor.execute("""
    INSERT INTO cadastro (nome, telefone, email) 
    VALUES (?,?,?)""",
    cadastro.nome, cadastro.telefone, cadastro.email).rowcount
    db.cnxn.commit()

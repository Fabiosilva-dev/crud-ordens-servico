import os
import sqlite3

class OrdemDeServico:
    def __init__(self):
        # Define o caminho do banco de dados na mesma pasta do arquivo script
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_banco = os.path.join(diretorio_atual, 'ordens_servico.db')
        
        self.conn = sqlite3.connect(caminho_banco)
        self.c = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS ordens_servico(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome_cliente TEXT NOT NULL,
                       equipamento TEXT NOT NULL,
                       descricao_defeito TEXT NOT NULL,
                       servico_realizado TEXT NOT NULL,
                       valor_orcamento REAL NOT NULL,
                       data_abertura TEXT NOT NULL,
                       status_servico TEXT NOT NULL)''')
        self.conn.commit()
        
    def criar_servico(self, servico):
        query = ("INSERT INTO ordens_servico(nome_cliente,equipamento,descricao_defeito,servico_realizado,valor_orcamento,data_abertura,status_servico) VALUES (?,?,?,?,?,?,?)")
        self.c.execute(query, servico)
        self.conn.commit()

    def listar_servicos(self):
        self.c.execute('SELECT * FROM ordens_servico')
        dados = self.c.fetchall()
        for i in dados:
            print(f"{i[0]}/{i[1]}/{i[2]}/{i[3]}/{i[4]}/{i[5]}/{i[6]}/{i[7]}")
    
    def listar_servico_por_id(self, id):
        self.c.execute("SELECT * FROM ordens_servico WHERE id=?", (id,))
        dados = self.c.fetchone()
        if dados:
            print(f"ID:{dados[0]}/NOME:{dados[1]}/EQUIPAMENTO:{dados[2]}/DESCRIÇÃO-SERVIÇO:{dados[3]}/SERVIÇO-REALIZADO:{dados[4]}/VALOR-ORÇAMENTO{dados[5]}/DATA-ABERTURA:{dados[6]}/VALOR-SERVIÇO:{dados[7]}")
    
    def atualizar_servico(self, novos_valores):
        query = ("UPDATE ordens_servico SET nome_cliente=? , equipamento=?,descricao_defeito=?,servico_realizado=?,valor_orcamento=?,data_abertura=? ,status_servico=? WHERE id=?")
        self.c.execute(query, novos_valores)
        self.conn.commit()

    def deletar_servico(self, id):
        self.c.execute('DELETE FROM ordens_servico WHERE id=?', (id,))
        self.conn.commit()


# Bloco de execução para testes locais
if __name__ == "__main__":
    ordem = OrdemDeServico()
    
    # Exemplo de uso para listagem no terminal
    ordem.listar_servicos()
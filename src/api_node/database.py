from mysql import connector
from dataclasses import dataclass

@dataclass
class bshop_db:
    _connection: list|None = None

    def set_conn(self,**kwargs) -> None:
        '''
        Configura la conexion con la base de datos que usará esta clase
        
        :param kwargs: Parámetros que usará la conexión, comprobar: https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
        '''
        database = connector.connect(
            host=kwargs['host'],
            user=kwargs['user'],
            database=kwargs['database'],
            )
        cursor_db = database.cursor()

        if self._connection != None:
            self._connection['database'].close()
            self._connection['cursor'].close()

        self._connection = {'database':database,'cursor':cursor_db}
    
    def stm_select(self,columns: str,tables: str,where: str|None = None,order_by: str|None = None):
        cursor = self._connection['cursor']
        statement = f'SELECT {columns} FROM {tables}'
        if where: statement += f' WHERE {where}'
        if order_by: statement += f' ORDER BY {order_by}'
        statement += ';'

        return cursor.execute(statement)
    
    def stm_insert_into(self, table: str,values: list,columns: list|None = None):
        statement = 'INSERT INTO ? ? VALUES ?;'

    def stm_update(self, table: str, column_value: dict, where: str):
        statement = 'UPDATE ? SET ? WHERE ?;'

    def stm_delete(self, table:str,where: str|None):
        statement = 'DELETE FROM ? WHERE ?;'

def getall_products(conn: bshop_db):
    products = conn.stm_select(columns='*',tables='products_full')
    print(products)

if __name__ == "__main__":
    database = bshop_db()
    database.set_conn(user = 'remote',host = '10.3.3.205', database = 'bestashop_db')
    test = getall_products(database)
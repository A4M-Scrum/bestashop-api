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
        sql = "INSERT INTO %s(%s) VALUES (%s);"
        val = (table, str(columns)[2:-2], str(values)[2:-2])
        print('sql = ' + sql)
        print('columns = ' + str(columns))
        print('values:')
        for v in val:
            print(v)
        cursor = self._connection['cursor']
        cursor.execute(sql, val)
        self._connection['database'].commit()


    def stm_update(self, table: str, column_value: dict, where: str):
        statement = 'UPDATE ? SET ? WHERE ?;'

    def stm_delete(self, table:str,where: str|None):
        statement = 'DELETE FROM ? WHERE ?;'

def getall_products(conn: bshop_db):
    products = conn.stm_select(columns='*',tables='products')
    print(products)

def insert_product(conn: bshop_db, values: list):
    conn.stm_insert_into(table='products', columns=['seller_id, category_id, name, description, price, image_url'], values=values)

def insert_category(conn:bshop_db, values: list):
    conn.stm_insert_into(table='categories', columns=['name'], values=values)

def insert_seller(conn: bshop_db, values: list):
    conn.stm_insert_into(table='sellers', columns=['name'], values=values)


if __name__ == "__main__":
    database = bshop_db()
    database.set_conn(user = 'remote',host = '10.3.3.205', database = 'bestashop_db')
    insert_category(database, ['Coche'])
    insert_seller(database, values=['Honda'])
    test = getall_products(database)
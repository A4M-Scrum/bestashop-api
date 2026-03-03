from mysql import connector
from dataclasses import dataclass


@dataclass
class bshop_db:
    _connection: list | None = None

    def set_conn(self, **kwargs) -> None:
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

        self._connection = {'database': database, 'cursor': cursor_db}

    def stm_select(self, columns: str, tables: str, where: str | None = None, order_by: str | None = None):
        cursor = self._connection['cursor']
        statement = f'SELECT {columns} FROM {tables}'
        if where: statement += f' WHERE {where}'
        if order_by: statement += f' ORDER BY {order_by}'
        statement += ';'

        cursor.execute(statement)

        # Get the results of the query
        results = cursor.fetchall()

        # Get the information of the columns
        columns = cursor.description

        # Assign each item the name of the column
        # The result would be: "name_of_the_column": "value_of_the_column"
        # Do this for each column of each item
        # Probably a bad and inefficient way to do this, but it works, so...
        items = []
        for r in results:
            new_item = {}
            for index, c in enumerate(columns):
                new_item[c[0]] = r[index]
            items.append(new_item)

        return items

    def stm_insert_into(self, table: str, values: list, columns: list | None = None):
        cursor = self._connection['cursor']

        columns_str = ','.join(columns)
        sql = f'INSERT INTO {table}({columns_str}) VALUES ({str(values)[1:-1]});'
        print(sql)
        cursor.execute(sql)
        self._connection['database'].commit()

    def stm_update(self, table: str, column_value: dict, where: str):
        statement = 'UPDATE ? SET ? WHERE ?;'

    def stm_delete(self, table: str, where: str | None):
        statement = 'DELETE FROM ? WHERE ?;'


def getall_products(conn: bshop_db):
    products = conn.stm_select(columns='product_id, seller_id, category_id, name, description, price, image_url', tables='products')
    return products


def getall_categories(conn: bshop_db):
    result = conn.stm_select(columns='*', tables='categories')

    return result


def insert_product(conn: bshop_db, seller_id: int, category_id: int, name: str, description: str, price: float,
                   image_url: str):
    conn.stm_insert_into(
        table='products',
        columns=['seller_id, category_id, name, description, price, image_url'],
        values=[seller_id, category_id, name, description, price, image_url]
    )


def insert_category(conn: bshop_db, values: list):
    conn.stm_insert_into(table='categories', values=values, columns=['name'])


def insert_seller(conn: bshop_db, values: list):
    conn.stm_insert_into(table='sellers', values=values, columns=['name'])


if __name__ == "__main__":
    database = bshop_db()
    database.set_conn(user='remote', host='10.3.3.205', database='bestashop_db')
    # insert_category(database, ['Coche'])
    # insert_seller(database, values=['Honda'])
    insert_product(database, 2, 2, "Civic 2006", "Old reliable", 15000, "")
    test = getall_products(database)
    print(test)

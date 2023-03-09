from connection import Connection


class Table:

    def __init__(self):
        self.create_table()
    def create_table(self):
        commands = (
            """
            CREATE TABLE IF NOT EXISTS forecasts (
                id SERIAL PRIMARY KEY,
                sourse_company_id  INTEGER,
                company_name VARCHAR(255) NOT NULL,
                fact_Qliq_data1  INTEGER,
                fact_Qliq_data2  INTEGER,
                fact_Qoil_data1  INTEGER,
                fact_Qoil_data2  INTEGER,
                forecast_Qliq_data1  INTEGER,
                forecast_Qliq_data2  INTEGER,
                forecast_Qoil_data1  INTEGER,
                forecast_Qoil_data2  INTEGER,
                date date
            )
            """
        )
        obj = Connection()
        self.conn = obj.connect()
        self.cursor = self.conn.cursor()
        self.cursor.execute(commands)
        self.conn.commit()

    def insert_into_table(self, row):
        self.cursor.execute("INSERT INTO forecasts (sourse_company_id, company_name, fact_Qliq_data1,fact_Qliq_data2,fact_Qoil_data1, fact_Qoil_data2, forecast_Qliq_data1, forecast_Qliq_data2, forecast_Qoil_data1, forecast_Qoil_data2,date ) VALUES(%s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)", (row[0],row[1], row[2],row[3],row[4], row[5], row[6],row[7],row[8], row[9], row[10]))
        self.conn.commit()


    def select_total(self):
        self.cursor.execute("select sum(fact_Qliq_data1),sum(fact_Qliq_data2),"
                            "sum(fact_Qoil_data1),sum(fact_Qoil_data2), sum(forecast_Qliq_data1),sum(forecast_Qliq_data2)  ,sum(forecast_Qoil_data1),sum(forecast_Qoil_data2), date   "
                            " from forecasts group by date")
        print(self.cursor.fetchall())



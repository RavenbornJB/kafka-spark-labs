from cassandra.cluster import Cluster


class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)

    def shutdown(self):
        if self.session:
            self.session.shutdown()

    def insert_transaction(self, transaction):
        sid, rid, amount, transaction_date, fraud = transaction
        if fraud == 'true':  # first table only contains fraudulent transactions
            self.session.execute(f"INSERT INTO user_fraudulent (sid, rid, amount, transaction_date) "
                                 f"VALUES ('{sid}', '{rid}', {amount}, '{transaction_date}')")
        self.session.execute(f"INSERT INTO user_highest (sid, rid, amount, transaction_date, fraud) "
                             f"VALUES ('{sid}', '{rid}', {amount}, '{transaction_date}', {fraud})")
        self.session.execute(f"INSERT INTO user_date_sum (sid, rid, amount, transaction_date, fraud) "
                             f"VALUES ('{sid}', '{rid}', {amount}, '{transaction_date}', {fraud})")

    def first_query(self, sid):
        if not self.session:
            raise ValueError('session not set. call CassandraClient.connect first')
        return list(self.session.execute(f"SELECT * FROM user_fraudulent WHERE sid='{sid}';"))

    def second_query(self, sid):
        if not self.session:
            raise ValueError('session not set. call CassandraClient.connect first')
        return list(self.session.execute(f"SELECT * FROM user_highest WHERE sid='{sid}' LIMIT 3;"))

    def third_query(self, rid, start_date, end_date):
        if not self.session:
            raise ValueError('session not set. call CassandraClient.connect first')
        return list(self.session.execute(f"SELECT SUM(amount) FROM user_date_sum WHERE rid='{rid}'"
                             f"AND transaction_date>='{start_date}' AND transaction_date<='{end_date}';"))
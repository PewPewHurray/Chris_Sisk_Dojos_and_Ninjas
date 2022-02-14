from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db_name="dojos_and_ninjas_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, created_at, updated_at, dojo_id ) VALUES ( %(first_name)s, %(last_name)s, %(age)s, NOW() , NOW(), %(dojo_id)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.db_name).query_db(query, data)
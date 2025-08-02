class InMemoryDB:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name):
        if table_name not in self.tables:
            self.tables[table_name] = []

    def insert(self, table_name, record):
        if table_name not in self.tables:
            raise Exception(f"Table '{table_name}' does not exist.")
        self.tables[table_name].append(record)

    def query(self, table_name, conditions=None):
        if table_name not in self.tables:
            raise Exception(f"Table '{table_name}' does not exist.")

        records = self.tables[table_name]

        if conditions:

            def check_condition(record):
                for field, condition in conditions.items():
                    operator, value = condition.split(" ")
                    value = int(value) if value.isdigit() else value
                    if operator == ">" and not record[field] > value:
                        return False
                    elif operator == "<" and not record[field] < value:
                        return False
                    elif operator == "=" and not record[field] == value:
                        return False
                return True

            # Filter records based on the conditions
            records = [record for record in records if check_condition(record)]

        return records

    def clear(self):
        """Drops all tables in the DB"""
        self.tables = {}

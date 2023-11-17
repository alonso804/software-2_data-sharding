from pymongo import MongoClient
import uuid

# Colors
HEADER = "\033[95m"
OKBLUE = "\033[94m"
OKCYAN = "\033[96m"
OKGREEN = "\033[92m"
WARNING = "\033[93m"
FAIL = "\033[91m"
ENDC = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"


class Logger:
    @staticmethod
    def info(msg):
        print(OKCYAN + "[INFO] " + ENDC + str(msg))

    @staticmethod
    def warn(msg):
        print(WARNING + "[WARN] " + ENDC + str(msg))

    @staticmethod
    def error(msg):
        print(FAIL + "[ERROR] " + ENDC + str(msg))

    @staticmethod
    def ok(msg):
        print(OKGREEN + "[OK] " + ENDC + str(msg))

    @staticmethod
    def stopError(msg):
        raise SystemExit(FAIL + "[ERROR] " + ENDC + str(msg))

    @staticmethod
    def stopInfo(msg):
        raise SystemExit(OKCYAN + "[INFO] " + ENDC + str(msg))


class Mongo:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:30000/")
        self.test = self.client["is2-shard"]["test"]

        Logger.info("Connected to MongoDB")

    def __del__(self):
        self.client.close()
        Logger.info("Disconnected from MongoDB")

    def add_to_test(self, data):
        self.test.insert_one(data)
        Logger.info("Added to test collection")


if __name__ == "__main__":
    Logger.info("Starting program")

    mongo = Mongo()

    for i in range(0, 100):
        mongo.add_to_test({"name": uuid.uuid4().hex, "email": "alonso@gmail.com"})

    Logger.info("Ending program")

    del mongo

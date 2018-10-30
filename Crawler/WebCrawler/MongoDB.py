import pymongo

try:
    # Python 3.x
    from urllib.parse import quote_plus
except ImportError:
    # Python 2.x
    from urllib import quote_plus

usename = 'ats_test_01'
password = 'ats_test_01'
host = '10.97.2.44:27017/ATS_SYS'

uri = "mongodb://%s:%s@%s" % (
    quote_plus(usename), quote_plus(password), host)
client = pymongo.MongoClient(uri)


# client = pymongo.MongoClient('mongodb://ats_test_01:ats_test_01@10.97.2.44:27017/ATS_SYS')
db = client.ATS_SYS
collection = db.STUDENTS
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170102',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student3 = {
    'id': '20170103',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
# result = collection.insert_many([student1,student2,student3])
# print(result)
result = collection.find_one({'name': 'Jordan'})
print(type(result))
print(result)

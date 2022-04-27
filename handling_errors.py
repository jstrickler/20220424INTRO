import sqlite3

file_path = "DATA/wombats.txt"

try:
    with open(file_path) as file_in:
        for raw_line in file_in:
            print(raw_line.rstrip())
except (FileNotFoundError, PermissionError) as err:
    print(err)
    # log the exception
    # provide alternate value or data
    # ignore the exception
    # exit program gracefully
except NotADirectoryError as err:
    print(err)

nums = [0, 800, 80, 1000, 145,  32, 0, 255, 400, 19, 5, 5000]
for num in nums:
    try:
        result = 10000 / num
    except ZeroDivisionError as err:
        print(0.0)
        # print(err)
    else:
        print(result)

print("ALL DONE")

conn = None
try:
    conn = sqlite3.connect('wombats.db')
    cursor = conn.cursor()
except sqlite3.OperationalError as err:
    print(err)
    exit()
except Exception as err:
    print("OH NO!", err)
else:
    # cursor.execute('drop table wombats if exists')
    # cursor.execute('create table wombats (name varchar(32), age int)')
    cursor.close()
finally:
    # clean up messes (resources)
    if conn is not None:
        conn.close()

class MyError(Exception):
    pass


try:
    # blah blah blah
    raise MyError("I have a bad feeling about this")
except MyError as err:
    print(err)







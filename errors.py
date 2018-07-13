raise ValueError('character must be a single string')
raise ValueError('width must be greater than 2')

try
    ....
except ValueError as err:
    print(str(err))




# if we want to log errors that are not crashers:
import traceback

now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')
except:
    errorFile = open('errorInfo.txt', 'a')
    errorFile.write(now)
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written to errorInfo.txt")

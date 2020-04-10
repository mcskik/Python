import datetime

import Constants
import DateTimeConstants


def makeRequestFileSpec(file_name, file_ext):
    return makeRequestFileSpec(file_name, file_ext, datetime.datetime.now())


def makeRequestFileSpec(file_name, file_ext, date_time_now):
    return makeFileSpec(Constants.requestsPath, file_name, file_ext, date_time_now)


def makeResponseFileSpec(file_name, file_ext):
    return makeResponseFileSpec(file_name, file_ext, datetime.datetime.now())


def makeResponseFileSpec(file_name, file_ext, date_time_now):
    return makeFileSpec(Constants.responsesPath, file_name, file_ext, date_time_now)


def makeFileSpec(file_path, file_name, file_ext, date_time_now):
    date_time_stamp = date_time_now.strftime(DateTimeConstants.format_packed)
    return file_path + file_name + "_" + date_time_stamp + "." + file_ext


def writeFile(file_spec, contents):
    file_handle = open(file_spec, "w+")
    file_handle.write(contents)
    file_handle.close()
    return None

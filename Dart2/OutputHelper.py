import datetime

import FileHelper
import JsonHelper
import ProcessHelper


def viewJsonOutput(file_spec, file_ext, json_data, date_time_now=datetime.datetime.now()):
    output = JsonHelper.printFormattedJsonToString(json_data, sort=False)
    file_spec = FileHelper.makeResponseFileSpec(file_spec, file_ext, date_time_now)
    FileHelper.writeFile(file_spec, output)
    ProcessHelper.view(file_spec)

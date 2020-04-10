import io
import json
import sys

import Constants


def printFormattedJson(json_container, sort=True, indents=Constants.indentSize):
    if type(json_container) is str:
        print(json.dumps(json.loads(json_container), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_container, sort_keys=sort, indent=indents))
    return None


def printFormattedJsonToString(json_container, sort=True, indents=Constants.indentSize):
    # Redirect sys.stdout to an in memory buffer.
    keep_stdout = sys.stdout
    sys.stdout = io.StringIO()
    if type(json_container) is str:
        print(json.dumps(json.loads(json_container), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_container, sort_keys=sort, indent=indents))
    # Capture print output.
    output = sys.stdout.getvalue()
    # Restore original sys.stdout.
    sys.stdout = keep_stdout
    return output

import os
import subprocess

notepad = "C:\\WINDOWS\\SYSTEM32\\Notepad.exe"


def view(file_spec):
    run1(notepad, file_spec)


def run1(program_spec, file_spec):
    command = program_spec + " " + file_spec
    os.system(command)

def run(program_spec, file_spec):
    cmd = [program_spec, file_spec]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)


def runAndCaptureOutput(program_spec, file_spec):
    cmd = [program_spec, file_spec]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    process.wait()
    for line in process.stdout:
        print(line)

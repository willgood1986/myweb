#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

success_result = 0
fail_reason_unknown=-1
fail_reason_not_a_file = -100
fail_reason_not_a_directory= -200
fail_reason_file_not_exist = -300
fail_reason_directory_not_exist = -400
fail_reason_target_file_exists_already = -500

ERRORS = {
    0: "Successful operation on {val}",
    -100: "{val} is not a valid file",
    -200: "{val} is not a valid directory",
    -300: "file {val} does not exist",
    -400: "directory {val} does not exist",
    -500: "target file {val} exists already"
}

def error_define():
    for k in ERRORS:
        print("{key}:{val}".format(key=k, val=ERRORS[k].replace("{val}", "")))

def equals(first, second):
   return first == second

def is_a_file(i_file):
    return os.path.isfile(i_file)

def does_file_exist(i_file):
    return os.path.exists(i_file)

def check_file(i_file):
    result = success_result
    if is_a_file(i_file):
        if not does_file_exist(i_file):
            result = fail_reason_file_not_exist
    else:
        result = fail_reason_not_a_file

def is_success(i_result):
    return equals(i_result, success_result)

def delete_file(i_file):
    '''Delete an existing file '''
    try:
        result = check_file(i_file)
        if is_success(i_result):
            os.remove(i_file)
    except:
        result = fail_reason_unknown
    finally:
        return result, ERRORS[result].format(val=i_file)

def rename_file(i_oldfile, i_newfile):
    result = success_result
    try:
        os.rename(i_oldfile, i_newfile)
    except:
        result = fail_reason_unknown
    finally:
        return result, ERRORS[result].format(val=i_oldfile)

def create_temp_file():
    return os.tmpfile

def get_files_under_directory(i_directory):
    none

if(equals(__name__, "__main__")):
    error_define()

#!/usr/bin/env python3
"""Remove all generated files by scripts."""

import os
from os.path import abspath, join, isdir, dirname
from shutil import rmtree


def remove_generated_files(path):
    """Remove all generated files by scripts.

    Args:
        path (str): path to the main directory
    """
    path = abspath(path)

    dir_list = [
        'examples',
        'kimpy',
        'scripts',
        'tests',
        join('tests', 'neighlist'),
    ]

    dir_list_files = {
        'examples': [
            "error.py",
            "example_collections.py",
            "example_simulator_model.py"
        ],
        'kimpy': [
            "KIM_Collections_bind.cpp",
            "KIM_ComputeArgumentName_bind.cpp",
            "KIM_ComputeArguments_bind.cpp",
            "KIM_Log_bind.cpp",
            "KIM_Model_bind.cpp",
            "KIM_SemVer_bind.cpp",
            "KIM_SimulatorModel_bind.cpp",
            "__init__.py",
            "callbacks.hpp",
            "err.py",
            "neighlist",
            "sim_buffer.h",
        ],
        'scripts': [
            "KIM_FieldName_bind.cpp-template",
            "generate_CollectionItemType_bind_test.py",
            "generate_Collection_bind_test.py",
            "generate_ComputeCallbackName_bind_test.py",
            "generate_DataType_bind_test.py",
            "generate_LanguageName_bind_test.py",
            "generate_LogVerbosity_bind_test.py",
            "generate_ModelRoutineName_bind_test.py",
            "generate_Numbering_bind_test.py",
            "generate_SpeciesName_bind_test.py",
            "generate_SupportStatus_bind_test.py",
            "generate_UnitSystem_bind_test.py",
            "generate_all.py",
            "generate_bind_test_commons.py",
            "test_field_name.py-template",
        ],
        'tests': [
            "error.py",
            "neighlist",
            "test_callbacks.py",
            "test_compute_argument_name.py",
            "test_model.py",
            "test_model_neigh_library.py",
            "test_sem_ver.py",
        ],
        join('tests', 'neighlist'): [
            'cpp_example',
            'test_graphite.py',
        ]
    }

    for dir_name in dir_list:
        dir_path = join(path, dir_name)
        if not isdir(dir_path):
            continue

        os.chdir(dir_path)

        for file_name in os.listdir('.'):
            if file_name not in dir_list_files[dir_name]:
                if isdir(file_name):
                    msg = "The folder `{}` is generated by ".format(file_name)
                    try:
                        os.rmdir(file_name)
                    except:
                        rmtree(file_name)
                else:
                    msg = "The file `{}` is generated by ".format(file_name)
                    os.remove(file_name)
                msg += "kimpy scripts and will be removed."
                print(msg)

    os.chdir(path)


if __name__ == '__main__':
    remove_generated_files(join(dirname(abspath(__file__)), '..'))
#!/usr/bin/env python3

from json import loads
from os import chdir
from os import system
from sys import argv

PROJECT_DIR = ''
PACKAGE_JSON = ''

def main():
    if len(argv) < 3:
        print(f'use: {argv[0]} <package.json> <nodejs_project_directory>')
        return 
    
    PROJECT_DIR=argv[2]
    PACKAGE_JSON=argv[1]

    libs_to_exclude = [
        'react', 
        'react-dom', 
        'react-native'
    ] # ajuste a lista de excluidos por aqui

    with open(PACKAGE_JSON) as file:
        file_data = file.read()
        data_filtered = file_data.replace('\n', '').replace(' ', '')
        data_dict = loads(data_filtered)
        deps_projects = data_dict['dependencies']
        libs = deps_projects.keys()
        libs = list(libs)

        if len(libs):
            for lib_to_remove in libs_to_exclude:
                try:
                    libs.remove(lib_to_remove)
                except ValueError:
                    continue

            print(f'Total number of js libs to install: {len(libs)}')

            # go to project directory and making the installations
            chdir(PROJECT_DIR)
            if not system('which yarn'): # checking if you have yarn installed :)
                if input(f'Do you want to install dependecies on {PROJECT_DIR}? [y/n]') == 'y':
                    for lib in libs:
                        try:
                            print(f'[INFO] installing {lib} on project ... please wait')
                            if not system(f'yarn add {lib}'):
                                print(f'lib {lib} installed sucess!')
                                print()
                            else:
                                print('operaction failed!')
                        except Exception as err:
                            print(f'[ERROR] message: {err}')
                else:
                    print('bye')
            else:
                print("yarn command is not installed!")
                return 

if __name__=="__main__":
    main()

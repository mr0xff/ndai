#!/usr/bin/env python3
"""
	Este é um simples script que facilita a instalação de versões de lib recentes
	de um projecto que está sendo instalado.
	
	Next.js 
"""
from json import loads
from os import chdir
from os import system

PROJECT_DIR = '/tmp' # change this directory according you root project directory
PACKAGE_JSON = 'package.json' # default node module configurations

def main():
    libs_to_exclude = [
        'react', 
        'react-dom', 
        'react-native'
    ]

    with open('package.json') as file:
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
                            if not system(f'yarn add {lib}@latest'):
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

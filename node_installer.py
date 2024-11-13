#!/usr/bin/env python3

from sys import argv
from os import system
from json import loads

BLACK_LIST_DEPS = { 
  "dep": [ 
    "react", 
    "react-dom", 
    "next" 
  ], 
  "devDep": [
    "typescript",
    "@types/node",
    "@types/react",
    "@types/react-dom",
    "postcss",
    "tailwindcss",
    "eslint",
    "eslint-config-next"
  ]
}

def read_json_dependencies(json_name):
  with open(json_name) as json_file:
    f = json_file.read()
    return [ 
      list(loads(f)['dependencies']), 
      list(loads(f)['devDependencies'])
    ]

def main():
  try:
    if len(argv) != 2:
      print("use: node_installer.py <json_file>")
      return

    dps = read_json_dependencies(argv[1])
    # project dev
    if system('which yarn') != 0:
      raise Exception('[-] Sem o yarn instaldo!')

    print('[*] Inslando as deps do projecto...')
    for k in dps[0]:
      try: 
        BLACK_LIST_DEPS['dep'].index(k)
        continue
      except:
        if system(f'yarn add {k}') != 0:
          print(f'[-] Erro ao inslatar o modulo {k}')
          continue
        print(f'[+] pacote {k} instaldo com sucesso!')
    # dev dependencies

    print('[*] Inslando as deps do desenvolvedor...')
    for k in dps[1]:
      try: 
        BLACK_LIST_DEPS['devDep'].index(k)
        continue
      except:
        if system(f'yarn add -D {k}') != 0:
          print(f'[-] Erro ao inslatar o modulo {k}')
          continue
        print(f'[+] pacote {k} instaldo com sucesso!')
      
    
    print('[+] Terminado de configurar as deps do projecto')
  except FileNotFoundError:
    print("arquivo não encontrado!")
  except Exception as e:
    print(f'[-] Erro: {e}')

if __name__ == "__main__":
  main()
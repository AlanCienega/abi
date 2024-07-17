import os
import subprocess

def run_test(file_path):
    result = subprocess.run(['python', 'app.py', file_path], capture_output=True, text=True)
    return result.stdout

def main():
    tests = {
        "tests/hola.abi": "Abi\n",
        "tests/asignar_numero.abi": "10\n",
        "tests/incremento_numero.abi": "20\n",
        "tests/decremento_numero.abi": "-10\n",
        "tests/agregar_texto.abi": "uno dos tres cuatro\n",
        "tests/quitar_texto.abi": "vaca y pollito\n",
        "tests/ciclo.abi": "Abi\nAbi\nAbi\n",
        "tests/incremento_arreglo.abi": "['uno', 'otro']\n",
        "tests/decremento_arreglo.abi": "['equis', 'ye']\n",
    }

    for test_file, expected_output in tests.items():
        output = run_test(test_file)
        if output == expected_output:
            print(f"{test_file}: PASSED")
        else:
            print(f"{test_file}: FAILED")
            print(f"Expected: {expected_output}")
            print(f"Got: {output}")

if __name__ == "__main__":
    main()

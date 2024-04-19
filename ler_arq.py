import subprocess

def ler_e_executar(arquivo):
    with open(arquivo, 'r') as file:
        for linha in file:
            url = linha.strip()
            subprocess.run(['node', 'busca_video.js', url])

if __name__ == "__main__":
    ler_e_executar('urls.txt')
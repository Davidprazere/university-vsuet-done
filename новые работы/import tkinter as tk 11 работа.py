import tkinter as tk
import requests
import json

def obter_dados():
    repo_nome = entrada_nome_repo.get()
    url = f'https://api.github.com/repos/{repo_nome}'
    
    try:
        resposta = requests.get(url)
        dados_repo = resposta.json()

        # Filtrar as informações desejadas
        resultado = {
            'company': None,
            'created at': dados_repo['created_at'],
            'email': None,
            'id': dados_repo['id'],
            'name': dados_repo['name'],
            'url': dados_repo['url']
        }

        # Anexar ao arquivo JSON
        with open('resultado.json', 'w') as arquivo:
            json.dump(resultado, arquivo, indent=4)

    except requests.exceptions.RequestException as e:
        resultado_label.config(text=f"Erro: {e}")

# Interface gráfica
app = tk.Tk()
app.title("Obter Dados do Repositório GitHub")

# Campo de entrada
entrada_nome_repo = tk.Entry(app, width=30)
entrada_nome_repo.pack(pady=10)

# Botão
obter_dados_botao = tk.Button(app, text="Obter Dados", command=obter_dados)
obter_dados_botao.pack(pady=10)

# Rótulo para exibir resultados ou mensagens de erro
resultado_label = tk.Label(app, text="")
resultado_label.pack(pady=10)

app.mainloop()
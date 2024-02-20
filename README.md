# Automação de Lixeira OneDrive

Este projeto utiliza o Selenium para automatizar o processo de esvaziar a lixeira no OneDrive, facilitando a gestão de arquivos e mantendo o ambiente de armazenamento limpo.

## Requisitos

- Python 3.11.5
- Selenium
- WebDriver Manager

## Configuração

Primeiro, clone o repositório para sua máquina local:

git clone https://github.com/matheuslarcher20/automacao.git
cd automacao
pip install selenium webdriver-manager
python esvaziar_lixeira.py



GPT
Para integrar as informações fornecidas e criar um README.md adequado para o seu projeto no GitHub, que inclui o script Python para automação usando Selenium, aqui está um exemplo de como estruturá-lo. Este exemplo assume que o foco principal do projeto é automatizar o processo de esvaziar a lixeira no OneDrive:

markdown
Copy code
# Automação de Lixeira OneDrive

Este projeto utiliza o Selenium para automatizar o processo de esvaziar a lixeira no OneDrive, facilitando a gestão de arquivos e mantendo o ambiente de armazenamento limpo.

## Requisitos

- Python 3.6+
- Selenium
- WebDriver Manager

## Configuração

Primeiro, clone o repositório para sua máquina local:

bash
git clone https://github.com/matheuslarcher20/automacao.git
cd automacao
Instale as dependências necessárias:

bash
Copy code
pip install selenium webdriver-manager
Uso
Para executar o script esvaziar_lixeira.py, primeiro certifique-se de atualizar o caminho absoluto para o diretório do perfil do usuário no script. Depois, execute o seguinte comando no terminal:

bash
Copy code
python esvaziar_lixeira.py
Notas Importantes
Certifique-se de que o ChromeDriver compatível com a versão do seu navegador Chrome está instalado.
Atualize a variável absolute_path_to_profile no script para refletir o caminho do seu perfil do usuário do Chrome.
O script está configurado para não executar em modo headless por padrão. Para habilitar o modo headless, remova o comentário da linha chrome_options.add_argument("--headless").
Contribuindo
Contribuições para o projeto são bem-vindas. Sinta-se livre para forkar o repositório, fazer suas alterações e abrir um pull request.

Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE.md para detalhes.

## Contato

- Matheus Larcher no GitHub: [matheuslarcher20](https://github.com/matheuslarcher20)
- LinkedIn: [Matheus Larcher](https://www.linkedin.com/in/matheus-larcher-6215b1179/)
- LinkedIn: [Site](https://lambda-ai.durable.co/pt)

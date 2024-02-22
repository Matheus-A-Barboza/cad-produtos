# Cadastro Automatizado de Produtos

### Este é um projeto em Python desenvolvido para automatizar o processo de cadastro de produtos em um site específico do cliente. O script é capaz de acessar o site do cliente e cadastrar todos os produtos presentes em uma planilha CSV, contendo todas as informações necessárias para o cadastro.
Funcionalidades

    Acesso automatizado ao site do cliente.
    Cadastro de produtos utilizando informações de uma planilha CSV.
    Processamento em lote para cadastro eficiente de múltiplos produtos.

## Requisitos

### Certifique-se de ter os seguintes requisitos instalados antes de executar o script:

    Python 3.x
    Bibliotecas necessárias: pandas, time, pyautogui

## Instalação

    Clone ou faça o download deste repositório.

    Instale as dependências necessárias usando o gerenciador de pacotes Python (pip):

    bash

    pip install -r requirements.txt

## Uso

    Prepare uma planilha CSV contendo os detalhes dos produtos a serem cadastrados. Certifique-se de que os campos na planilha correspondam aos campos necessários para o cadastro no site do cliente.

    Execute o script principal:

    bash

    python cadastro_produtos.py

    Siga as instruções fornecidas pelo script, que incluem fornecer as credenciais de acesso ao site, o caminho para a planilha CSV e outros detalhes relevantes.

## Exemplo de Estrutura da Planilha CSV

A estrutura da planilha CSV deve seguir um formato específico para garantir o correto processamento dos dados pelo script. Aqui está um exemplo de como a planilha pode ser estruturada:

    |  Nome do Produto  |	     Descrição           |    Preço    |	Categoria	  |   SKU   |
    | Produto 1	    | Descrição do Produto 1	 | 10.99       | Eletrônicos	          | SKU001  |
    | Produto 2	    | Descrição do Produto 2	 | 20.50       | Vestuário	          | SKU002  |
    | Produto 3	    | Descrição do Produto 3	 | 5.99	       | Livros	                  | SKU003  |

Certifique-se de que os nomes das colunas correspondam exatamente aos nomes esperados pelo script.
Contribuindo

Se desejar contribuir com melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.
Aviso Legal

Este projeto foi desenvolvido para fins educacionais e de demonstração. Não nos responsabilizamos pelo uso indevido ou ilegal deste script para qualquer finalidade.
## Licença

 Este projeto é distribuído sob a licença MIT.

# App de Cold Call

Este projeto fornece um aplicativo de linha de comando para auxiliar o time comercial durante cold calls. Os contatos são lidos de uma planilha do Google Sheets e o resultado de cada ligação é salvo em `results.csv`.

## Como usar

1. **Obter os leads**
   - Exporte a planilha do Google para um arquivo CSV chamado `leads.csv` e coloque-o na raiz do projeto; **ou**
   - Permita que o script faça o download direto informando o ID da planilha com `--sheet-id`.
2. **Executar o aplicativo**

   ```bash
   python app.py --csv sample_leads.csv
   ```

   Substitua `sample_leads.csv` pelo seu arquivo `leads.csv` ou remova `--csv` para que o script tente baixar a planilha.
3. **Registrar o resultado**
   - Para cada contato exibido, informe `s` para sucesso, `n` para não atendeu, `p` para passar ou `q` para sair.
4. **Consultar os resultados**
   - As respostas serão salvas em `results.csv`.

## Dependências

- Python 3
- Nenhuma biblioteca externa é necessária; o script utiliza apenas bibliotecas da distribuição padrão.

## Exemplo de dados

O arquivo `sample_leads.csv` contém um conjunto fictício de leads para teste.

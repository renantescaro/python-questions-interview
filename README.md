# Projeto: Job Interview Python Functions

Projeto com as questões e seus testes unitários

---

## 🚀 Como Executar as Questões

Para rodar cada script individualmente e ver os resultados no console, utilize os comandos abaixo a partir da pasta raiz do projeto:

```bash
python main\questions\question_1.py
python main\questions\question_2.py
python main\questions\question_3.py
python main\questions\question_4.py
```
---

## 🧪 Executando os Testes Unitários

Para validar todas as funções de uma única vez, utilize o arquivo de lote configurado na raiz:

```bash
run_tests.bat
```

O comando interno executado pelo script é:
```bash
python -m unittest discover -v -s main/tests -p "test_*.py" -t main
```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.14+**
* **Unittest**: Framework nativo para testes automatizados.
* **Math e Datetime**: Bibliotecas nativas para cálculos e manipulação de datas.

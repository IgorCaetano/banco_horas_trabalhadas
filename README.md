# 🕒 Controle de Horas Trabalhadas

Este é um simples aplicativo de desktop desenvolvido em Python para rastrear e registrar horas de trabalho. A ferramenta permite cronometrar atividades, pausar, contabilizar o tempo com um resumo e gerar relatórios mensais.

---

## ✨ Funcionalidades

- Cronômetro: Inicie, pause e zere a contagem de tempo com botões intuitivos.

- Registro de Atividades: Ao contabilizar um período, é possível adicionar um breve resumo da tarefa realizada.

- Armazenamento Automático: Cada registro é salvo automaticamente em uma planilha do Excel (.xlsx) correspondente ao mês atual.

- Relatórios Mensais: Consulte o total de horas trabalhadas em qualquer mês selecionando o arquivo correspondente.

- Visualização Rápida: A tela principal exibe um somatório atualizado das horas trabalhadas no mês corrente.


---


## 🛠️ Ferramentas Utilizadas

- **Python 3**: Linguagem de programação principal.

- **Tkinter**: Biblioteca padrão do Python para a criação da interface gráfica (GUI).

- **Pandas**: Biblioteca utilizada para manipulação e salvamento dos dados em planilhas do Excel.

## 🚀 Como Usar a Aplicação

A interface é dividida em duas telas principais: a do cronômetro e a de relatórios.

### Tela Principal (Cronômetro)

1. **Iniciar**: Clique no botão verde `Iniciar` para começar a contagem do tempo. O mesmo botão pode ser usado para retomar a contagem após uma pausa.

2. **Pausar**: O botão laranja `Pausar` interrompe o cronômetro. O tempo decorrido fica salvo, e você pode retomá-lo clicando em `Iniciar` novamente.

3. **Contabilizar**: Ao finalizar uma tarefa, clique no botão azul `Contabilizar`. Uma nova tela se abrirá para que você digite um resumo da atividade. Ao confirmar, o tempo será salvo na planilha do mês e o cronômetro será zerado.

4. **Zerar**: O botão vermelho `Zerar` reinicia o cronômetro a qualquer momento, descartando o tempo contado.

5. **Obter horas trabalhadas**: Este botão leva você para a tela de relatórios.


---

### Tela de Relatórios

1. **Selecione o mês**: No menu suspenso, escolha um dos arquivos de planilha disponíveis.

2. **Obter horas**: Clique neste botão para calcular e exibir o total de horas registradas no arquivo selecionado.

3. **Voltar**: Retorna para a tela principal do cronômetro.

---

## 📂 Onde Consultar as Planilhas

As planilhas com os registros de horas são salvas automaticamente na mesma pasta onde o programa está sendo executado.

Cada arquivo é nomeado com o número do mês correspondente. Por exemplo:

- Registros de Janeiro serão salvos em 1.xlsx.

- Registros de Setembro serão salvos em 9.xlsx.

- Registros de Dezembro serão salvos em 12.xlsx.

Você pode abrir esses arquivos com qualquer editor de planilhas, como Microsoft Excel, Google Sheets ou LibreOffice Calc, para visualizar os detalhes de data, resumo e duração de cada período contabilizado.

---

## 🏃 Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado em seu sistema.

2. Instale as dependências necessárias. A principal é a biblioteca pandas e seu motor para Excel:

```python
pip install -r requirements.txt
```

3. Execute o arquivo através do terminal:

```python
python work_timer.py
```

4. O aplicativo será iniciado.

Para criar um executável (sem ícone pré-setado):
```python
pyinstaller --onefile --noconsole work_timer.py
```

Para criar um executável (com ícone pré-setado):
```python
pyinstaller --onefile --noconsole --add-binary "meu_icone.ico;." work_timer.py
```

---

## Resultados

### Início do app

<img width="420" height="309" alt="image" src="https://github.com/user-attachments/assets/81727a8b-f02f-4b52-9429-bce9b61ef9c2" />

### Resumo de trabalho realizado naquele período de tempo

<img width="416" height="307" alt="image" src="https://github.com/user-attachments/assets/b9573b5b-9538-4465-b464-d3a422f3975f" />


### Catalogação de hora trabalhada realizada

<img width="417" height="305" alt="image" src="https://github.com/user-attachments/assets/d1ec5b7d-0cf0-4940-99a2-fc01a29ed072" />

### Resumo de horas de um mês selecionado

<img width="413" height="306" alt="image" src="https://github.com/user-attachments/assets/5cd03e1c-70be-4b22-b357-c1de10c90971" />

### Planilha de dados criada no mesmo diretório do arquivo .exe

<img width="643" height="88" alt="image" src="https://github.com/user-attachments/assets/b032ddf8-a086-41d5-956f-7bd422043ba9" />

### Planilha gerada do mês

<img width="376" height="198" alt="image" src="https://github.com/user-attachments/assets/2aca94eb-a2c3-4679-8cd4-a962254c3d10" />

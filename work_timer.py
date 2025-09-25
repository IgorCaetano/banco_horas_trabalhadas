# -*- coding: utf-8 -*-

# Importação das bibliotecas necessárias
import tkinter as tk
from tkinter import ttk, messagebox
import time
import pandas as pd
import os
from datetime import datetime

class TimeTrackerApp:
    """
    Classe principal da aplicação de Controle de Horas.
    Gerencia a interface gráfica, o cronômetro e a manipulação de dados.
    """
    def __init__(self, root):
        """
        Construtor da classe. Inicializa a janela principal e todos os seus componentes (widgets).
        """
        # --- Configuração da Janela Principal ---
        self.root = root
        self.root.title("Controle de Horas")
        self.root.geometry("420x280")  # Dimensões da janela
        self.root.resizable(False, False)  # Impede o redimensionamento da janela
        self.root.configure(bg="#f5f5f5")  # Cor de fundo

        # --- Variáveis de Controle do Cronômetro ---
        self.start_time = None  # Armazena o tempo de início do cronômetro
        self.running = False    # Flag para indicar se o cronômetro está rodando
        self.elapsed_time = 0   # Armazena o tempo decorrido, considerando as pausas

        # --- Estrutura de Frames (Telas) ---
        # Frame principal, onde o cronômetro é exibido
        self.main_frame = tk.Frame(root, bg="#f5f5f5")
        self.main_frame.pack(fill="both", expand=True)

        # Frame da tela de relatórios
        self.report_frame = tk.Frame(root, bg="#f5f5f5")

        # Frame para inserção do resumo da atividade
        self.summary_frame = tk.Frame(root, bg="#f5f5f5")

        # --- Widgets da Tela Principal (main_frame) ---
        self.timer_label = tk.Label(self.main_frame, text="00:00:00", font=("Helvetica", 36), bg="#f5f5f5")
        self.timer_label.pack(pady=15)

        # Frame para agrupar os botões de controle do cronômetro
        buttons_frame = tk.Frame(self.main_frame, bg="#f5f5f5")
        buttons_frame.pack(pady=5)

        # Estilo padrão para os botões
        btn_style = {"width": 10, "height": 2, "font": ("Arial", 10, "bold")}

        # Botões de controle
        self.start_button = tk.Button(buttons_frame, text="Iniciar", bg="green", fg="white", command=self.start, **btn_style)
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = tk.Button(buttons_frame, text="Pausar", bg="orange", fg="white", command=self.pause, **btn_style)
        self.pause_button.grid(row=0, column=1, padx=5)

        self.save_button = tk.Button(buttons_frame, text="Contabilizar", bg="dodgerblue", fg="white", command=self.prepare_summary, **btn_style)
        self.save_button.grid(row=0, column=2, padx=5)

        self.reset_button = tk.Button(buttons_frame, text="Zerar", bg="red", fg="white", command=self.reset, **btn_style)
        self.reset_button.grid(row=0, column=3, padx=5)

        # Label para exibir o total de horas trabalhadas no mês atual
        self.monthly_summary_label = tk.Label(self.main_frame, text="", font=("Arial", 11, "bold"), bg="#f5f5f5", fg="black")
        self.monthly_summary_label.pack(pady=10)

        # Botão para navegar até a tela de relatórios
        self.report_button = tk.Button(self.main_frame, text="Obter horas trabalhadas", bg="gray", fg="white", command=self.show_report_page, font=("Arial", 10, "bold"), height=2, width=40)
        self.report_button.pack(pady=15)

        # --- Widgets da Tela de Relatórios (report_frame) ---
        self.file_label = tk.Label(self.report_frame, text="Selecione o mês:", font=("Arial", 12), bg="#f5f5f5")
        self.file_label.pack(pady=5)

        self.month_combo = ttk.Combobox(self.report_frame, state="readonly")
        self.month_combo.pack(pady=5)

        self.get_hours_button = tk.Button(self.report_frame, text="Obter horas", bg="dodgerblue", fg="white", command=self.get_hours, font=("Arial", 10, "bold"))
        self.get_hours_button.pack(pady=5)

        self.result_label = tk.Label(self.report_frame, text="", font=("Arial", 12, "bold"), bg="#f5f5f5", fg="black")
        self.result_label.pack(pady=10)

        self.back_button = tk.Button(self.report_frame, text="Voltar", bg="gray", fg="white", command=self.show_main_page, font=("Arial", 10, "bold"))
        self.back_button.pack(pady=5)

        # --- Widgets da Tela de Resumo (summary_frame) ---
        self.summary_label = tk.Label(self.summary_frame, text="Resumo do período:", font=("Arial", 12), bg="#f5f5f5")
        self.summary_label.pack(pady=5)

        self.summary_entry = tk.Entry(self.summary_frame, width=40)
        self.summary_entry.pack(pady=5)

        self.confirm_button = tk.Button(self.summary_frame, text="Marcar horas", bg="green", fg="white", command=self.save_time_with_summary, font=("Arial", 10, "bold"))
        self.confirm_button.pack(pady=10)

        self.cancel_button = tk.Button(self.summary_frame, text="Cancelar", bg="gray", fg="white", command=self.cancel_summary, font=("Arial", 10, "bold"))
        self.cancel_button.pack()

        # --- Inicialização ---
        # Carrega o somatório do mês atual ao iniciar o programa
        self.update_monthly_summary()

    def update_timer(self):
        """
        Atualiza o label do cronômetro a cada segundo.
        Esta função é chamada recursivamente enquanto a flag 'running' for True.
        """
        if self.running:
            # Calcula o tempo decorrido desde o início
            current_time = time.time()
            self.elapsed_time = current_time - self.start_time
            
            # Formata o tempo para o formato HH:MM:SS
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time))
            
            # Atualiza o texto do label
            self.timer_label.config(text=formatted_time)
            
            # Agenda a próxima chamada desta função para daqui a 1000ms (1 segundo)
            self.root.after(1000, self.update_timer)

    def start(self):
        """
        Inicia ou retoma a contagem do cronômetro.
        """
        if not self.running:
            # Ajusta o tempo de início para compensar o tempo já decorrido antes de uma pausa
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_timer()

    def pause(self):
        """
        Pausa a contagem do cronômetro.
        """
        if self.running:
            self.running = False

    def reset(self):
        """
        Zera o cronômetro, parando a contagem e reiniciando o tempo decorrido.
        """
        self.running = False
        self.elapsed_time = 0
        self.timer_label.config(text="00:00:00")

    def prepare_summary(self):
        """
        Prepara a tela para o usuário inserir um resumo da atividade.
        Pausa o cronômetro e troca para a tela de resumo.
        """
        if self.elapsed_time == 0:
            messagebox.showwarning("Aviso", "Nenhum tempo para contabilizar!")
            return
        
        # Pausa o cronômetro e troca a visualização para o frame de resumo
        self.running = False
        self.main_frame.pack_forget()
        self.summary_frame.pack(fill="both", expand=True)

    def cancel_summary(self):
        """
        Cancela a operação de salvar, limpando o campo de resumo e voltando para a tela principal.
        """
        self.summary_entry.delete(0, tk.END)  # Limpa o campo de texto
        self.summary_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def save_time_with_summary(self):
        """
        Salva o tempo contabilizado e o resumo em um arquivo Excel.
        O arquivo é nomeado com o número do mês correspondente.
        """
        summary = self.summary_entry.get().strip()
        
        # Limpa o campo de texto e volta para a tela principal
        self.summary_entry.delete(0, tk.END)
        self.summary_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

        end_time = datetime.now()

        # Cria um DataFrame do pandas com os dados da sessão atual
        data = {
            "date": [end_time.strftime("%d/%m/%Y")],
            "summary": [summary],
            "duration": [time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time))]
        }
        df = pd.DataFrame(data)

        # Define o nome do arquivo com base no mês atual (ex: "6.xlsx" para Junho)
        filename = f"{end_time.month}.xlsx"
        
        # Verifica se o arquivo do mês já existe
        if os.path.exists(filename):
            # Se existir, lê os dados antigos e concatena com os novos
            old_df = pd.read_excel(filename)
            df = pd.concat([old_df, df], ignore_index=True)

        # Salva o DataFrame (novo ou concatenado) no arquivo Excel
        df.to_excel(filename, index=False)
        messagebox.showinfo("Sucesso", f"Período salvo em {filename}!")

        # Zera o cronômetro e atualiza o resumo mensal na tela principal
        self.reset()
        self.update_monthly_summary()

    def show_report_page(self):
        """
        Exibe a tela de relatórios, escondendo a tela principal.
        """
        self.main_frame.pack_forget()
        self.report_frame.pack(fill="both", expand=True)

        # Procura por todos os arquivos .xlsx no diretório atual para popular o combobox
        files = [f for f in os.listdir() if f.endswith(".xlsx")]
        self.month_combo["values"] = files
        if files:
            self.month_combo.current(0) # Seleciona o primeiro arquivo da lista por padrão

        self.result_label.config(text="") # Limpa o resultado de consultas anteriores

    def show_main_page(self):
        """
        Exibe a tela principal, escondendo a tela de relatórios.
        """
        self.report_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def get_hours(self):
        """
        Calcula o total de horas trabalhadas a partir do arquivo selecionado no combobox.
        """
        file = self.month_combo.get()
        if not file:
            messagebox.showwarning("Aviso", "Selecione um mês!")
            return

        df = pd.read_excel(file)
        total_seconds = 0

        # Itera sobre a coluna 'duration' do DataFrame
        for d in df["duration"]:
            # Converte a string "HH:MM:SS" para segundos
            h, m, s = map(int, d.split(":"))
            total_seconds += h * 3600 + m * 60 + s

        # Converte o total de segundos para horas
        total_hours = total_seconds / 3600
        total_hours_show = f'{total_hours:.4f}'
        
        # Exibe o resultado no label, formatando para o padrão brasileiro (vírgula)
        self.result_label.config(
            text=f"Total de horas trabalhadas: {str(total_hours_show).replace('.', ',')} h"
        )

    def update_monthly_summary(self):
        """
        Calcula e exibe o total de horas trabalhadas no mês atual na tela principal.
        """
        now = datetime.now()
        filename = f"{now.month}.xlsx"

        # Se o arquivo do mês atual não existir, exibe 0 horas
        if not os.path.exists(filename):
            self.monthly_summary_label.config(
                text=f"Somatório de horas trabalhadas do mês {now.month}: 0 h"
            )
            return

        # Se o arquivo existir, calcula o total de horas de forma semelhante ao get_hours()
        df = pd.read_excel(filename)
        total_seconds = 0
        for d in df["duration"]:
            h, m, s = map(int, d.split(":"))
            total_seconds += h * 3600 + m * 60 + s

        total_hours = total_seconds / 3600
        total_hours_show = f'{total_hours:.4f}'
        
        # Atualiza o label na tela principal
        self.monthly_summary_label.config(
            text=f"Somatório de horas trabalhadas do mês {now.month}: {str(total_hours_show).replace('.', ',')} h"
        )


if __name__ == "__main__":
    """
    Ponto de entrada do programa.
    Cria a janela principal do Tkinter e inicia a aplicação.
    """
    root = tk.Tk()

    try:
        # Caminho absoluto do ícone
        icone_path = os.path.join(os.path.dirname(os.getcwd()), "meu_icone.ico")
        root.iconbitmap(icone_path)
    except Exception as e:
        pass

    app = TimeTrackerApp(root)

    root.mainloop()

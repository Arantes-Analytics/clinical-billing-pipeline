import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import threading
import pickle
from processar_arquivos import executar_leitura_arquivos
from tools import centralizar_janela, pegar_caminho_onde_abre_o_exe
from tkinter import messagebox


class tela_principal:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Controle de Faturamento")
        self.janela.resizable(False, False)
        centralizar_janela(450, 225, self.janela)  # largura x altura

        self.janela.bind("<F1>", lambda e: self.tela_sobre())
        self.janela.bind("<Escape>", lambda e: self.sair_programa())

        self.janela.iconbitmap("icone.ico")

        self.criar_menu()
        self.cria_objetos_tela()
        self.carregar_dados_salvos()

        # Intercepta o clique no 'X'
        self.janela.protocol("WM_DELETE_WINDOW", self.sair_programa)
        self.janela.mainloop()

    def executar_processo_atualizacao(self):
        if len(self.txt_destino.get()) == 0 or len(self.txt_log_erro.get()) == 0 or len(self.txt_origem.get()) == 0:
            messagebox.showwarning('Alerta', 'É necessario preencher os caminhos dos arquivos')
        else:
            self.lbl_processando.pack(side="left", padx=5)
            self.spinner.pack(side="left")
            self.spinner.start(10)

            retorno = executar_leitura_arquivos(
                self.txt_destino.get(),
                self.txt_origem.get(),
                self.txt_log_erro.get()
            )

            if retorno == 1:
                messagebox.showinfo("Info", "Operação concluída com sucesso!")
            else:
                messagebox.showerror("Error", "Falha na operação!\n\n"+ str(retorno))
            
            self.spinner.stop()
            self.spinner.pack_forget()
            self.lbl_processando.pack_forget()
    
    def iniciar_carregamento(self):
       threading.Thread(target=self.executar_processo_atualizacao).start()

    def salvar_dados_text_box(self, dic={}):
        with open('conf.pkl', 'wb') as arquivo:
            pickle.dump(dic, arquivo)

    def carregar_dados_salvos(self):
        # Carregando os dados do arquivo .pkl
        try:
            dic = {}
            with open('conf.pkl', 'rb') as arquivo:
                dic = pickle.load(arquivo)
       
            self.txt_origem.insert(0, dic[0])
            self.txt_destino.insert(0, dic[1])
            self.txt_log_erro.insert(0, dic[2])
        except Exception:
            # cria as pastas no diretorio do exe
            caminho_padrao = pegar_caminho_onde_abre_o_exe()
            self.txt_origem.insert(0, caminho_padrao)
            self.txt_log_erro.insert(0, caminho_padrao)

    def sair_programa(self):
        dic = {0: self.txt_origem.get(),  1: self.txt_destino.get(), 2: self.txt_log_erro.get()}
        self.salvar_dados_text_box(dic)
        self.janela.destroy()

    def selecionar_diretorio(self, entry):
        pasta = filedialog.askdirectory()
        if pasta:
            entry.delete(0, tk.END)
            entry.insert(0, pasta)

    def selecionar_arquivo(self, entry):
        # Abre a janela de diálogo e retorna o caminho do arquivo
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo",
            filetypes=(("Arquivos de texto", "*.xlsx"),
                       ("Todos os arquivos", "*.*"))
        )
        if caminho_arquivo:
            entry.delete(0, tk.END)
            entry.insert(0, caminho_arquivo)

    def criar_campo_text_box(self, texto, linha, tipo=1):
        frame = tk.Frame(self.janela)
        frame.pack(fill="x", padx=20, pady=4)

        tk.Label(frame, text=texto, width=18, anchor="w").pack(side="left")

        entry = tk.Entry(frame)
        entry.pack(side="left", fill="x", expand=True, padx=5)

        if tipo == 1:
            comando = lambda: self.selecionar_diretorio(entry)
        else:
            comando = lambda: self.selecionar_arquivo(entry)

        tk.Button(frame, text="📂", width=3, command=comando).pack(side="right")

        return entry

    def cria_objetos_tela(self):
        frame_principal = tk.Frame(self.janela)
        frame_principal.pack(padx=20, pady=2)

        # CAMPOS
        self.txt_origem = self.criar_campo_text_box("Demonstrativos:", 0, 1)
        self.txt_destino = self.criar_campo_text_box("Planilha Faturamento:", 1, 2)
        self.txt_log_erro = self.criar_campo_text_box("Log's de erros:", 2, 1)

        # STATUS PROCESSANDO
        self.frame_status = tk.Frame(self.janela)
        self.frame_status.pack(pady=10)

        self.lbl_processando = tk.Label(
            self.frame_status,
            text="Processando...",
            font=("Segoe UI", 10)
        )

        self.spinner = ttk.Progressbar(
            self.frame_status,
            mode="indeterminate",
            length=180
        )

        # BOTÕES
        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=10)

        btn1 = ttk.Button(frame_botoes, text="Executar", width=12,
                        command=self.iniciar_carregamento)
        btn1.pack(side="left", padx=10)

        btn2 = ttk.Button(frame_botoes, text="Sair", width=12,
                        command=self.sair_programa)
        btn2.pack(side="left", padx=10)

        self.janela.grid_columnconfigure(0, weight=1)
        self.janela.grid_columnconfigure(1, weight=1)

    def criar_menu(self):
        barra_menu = tk.Menu(self.janela)
        menu_ajuda = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Menu", menu=menu_ajuda)
        menu_ajuda.add_command(label="Manual", command=self.abrir_pdf_ajuda)
        menu_ajuda.add_command(label="Sobre", command=self.tela_sobre)
        self.janela.config(menu=barra_menu)

    def tela_sobre(self):
        largura = 300
        altura = 150

        sobre = tk.Toplevel(self.janela)
        sobre.title("Sobre")

        # Tornar filha da janela principal
        sobre.transient(self.janela)

        # Bloquear interação com a principal
        sobre.grab_set()

        # Posição da janela principal
        x_pai = self.janela.winfo_rootx()
        y_pai = self.janela.winfo_rooty()
        largura_pai = self.janela.winfo_width()
        altura_pai = self.janela.winfo_height()

        # Calcular centro
        x = x_pai + (largura_pai // 2) - (largura // 2)
        y = y_pai + (altura_pai // 2) - (altura // 2)

        sobre.geometry(f"{largura}x{altura}+{x}+{y}")

        tk.Label(
            sobre,
            text="Sistema de controle Faturamento.\nDesenvolvido por LS Treinamentos.\nVersão 1.1",
            justify="center"
        ).pack(expand=True)

        tk.Button(sobre, text="OK", width=10,
                  command=sobre.destroy).pack(pady=10)
    
    def abrir_pdf_ajuda(self):
        import webbrowser
        caminho = "manual_sistema.pdf"
        webbrowser.open(caminho)


if __name__ == '__main__':
    executar = tela_principal()

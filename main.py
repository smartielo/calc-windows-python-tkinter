import tkinter as tk
from tkinter import ttk, font
import math

class CalculadoraAvancada:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Avançada")
        master.geometry("400x600")
        
        # Variáveis de estado
        self.modo_atual = "Padrão"
        self.valor_memoria = 0
        self.historico = []
        
        # Configuração do display
        self.display_font = font.Font(size=24)
        self.display = tk.Entry(master, font=self.display_font, 
                               justify='right', bd=10, insertwidth=1)
        self.display.grid(row=0, column=0, columnspan=5, sticky='nsew')
        self.display.insert(0, '0')
        
        # Frame para os modos
        self.frame_modos = ttk.Frame(master)
        self.frame_modos.grid(row=1, column=0, columnspan=5, sticky='nsew')
        
        # Botões de modo
        modos = ["Padrão", "Científica", "Programador"]
        for i, modo in enumerate(modos):
            btn = ttk.Button(self.frame_modos, text=modo, 
                           command=lambda m=modo: self.mudar_modo(m))
            btn.grid(row=0, column=i, sticky='nsew', padx=2, pady=2)
        
        # Frame para os botões
        self.frame_botoes = ttk.Frame(master)
        self.frame_botoes.grid(row=2, column=0, columnspan=5, sticky='nsew')
        
        # Criar botões padrão
        self.criar_botoes_padrao()
        
        # Configurar pesos das linhas/colunas
        for i in range(5):
            master.grid_columnconfigure(i, weight=1)
        for i in range(3):
            master.grid_rowconfigure(i, weight=1)
    
    def mudar_modo(self, modo):
        self.modo_atual = modo
        self.limpar_display()
        
        # Destruir botões existentes
        for widget in self.frame_botoes.winfo_children():
            widget.destroy()
        
        # Criar novos botões conforme o modo
        if modo == "Padrão":
            self.criar_botoes_padrao()
        elif modo == "Científica":
            self.criar_botoes_cientifica()
        elif modo == "Programador":
            self.criar_botoes_programador()
    
    def criar_botoes_padrao(self):
        botoes = [
            ('MC', 0, 0), ('MR', 0, 1), ('MS', 0, 2), ('M+', 0, 3), ('M-', 0, 4),
            ('%', 1, 0), ('CE', 1, 1), ('C', 1, 2), ('⌫', 1, 3), ('/', 1, 4),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3), ('1/x', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3), ('x²', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3), ('√', 4, 4),
            ('±', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]
        
        for (texto, linha, coluna) in botoes:
            cmd = lambda x=texto: self.clique_botao(x)
            btn = ttk.Button(self.frame_botoes, text=texto, command=cmd)
            btn.grid(row=linha, column=coluna, sticky='nsew', padx=2, pady=2)
        
        # Configurar pesos
        for i in range(5):
            self.frame_botoes.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.frame_botoes.grid_rowconfigure(i, weight=1)
    
    def criar_botoes_cientifica(self):
        botoes = [
            ('π', 0, 0), ('e', 0, 1), ('sin', 0, 2), ('cos', 0, 3), ('tan', 0, 4),
            ('log', 1, 0), ('ln', 1, 1), ('x^y', 1, 2), ('10^x', 1, 3), ('e^x', 1, 4),
            ('(', 2, 0), (')', 2, 1), ('n!', 2, 2), ('mod', 2, 3), ('|x|', 2, 4),
            ('MC', 3, 0), ('MR', 3, 1), ('MS', 3, 2), ('M+', 3, 3), ('M-', 3, 4),
            ('%', 4, 0), ('CE', 4, 1), ('C', 4, 2), ('⌫', 4, 3), ('/', 4, 4),
            ('7', 5, 0), ('8', 5, 1), ('9', 5, 2), ('*', 5, 3), ('1/x', 5, 4),
            ('4', 6, 0), ('5', 6, 1), ('6', 6, 2), ('-', 6, 3), ('x²', 6, 4),
            ('1', 7, 0), ('2', 7, 1), ('3', 7, 2), ('+', 7, 3), ('√', 7, 4),
            ('±', 8, 0), ('0', 8, 1), ('.', 8, 2), ('=', 8, 3), ('Hex', 8, 4)
        ]
        
        for (texto, linha, coluna) in botoes:
            cmd = lambda x=texto: self.clique_botao(x)
            btn = ttk.Button(self.frame_botoes, text=texto, command=cmd)
            btn.grid(row=linha, column=coluna, sticky='nsew', padx=2, pady=2)
        
        # Configurar pesos
        for i in range(5):
            self.frame_botoes.grid_columnconfigure(i, weight=1)
        for i in range(9):
            self.frame_botoes.grid_rowconfigure(i, weight=1)
    
    def criar_botoes_programador(self):
        botoes = [
            ('Hex', 0, 0), ('Dec', 0, 1), ('Oct', 0, 2), ('Bin', 0, 3), ('Qword', 0, 4),
            ('A', 1, 0), ('B', 1, 1), ('C', 1, 2), ('D', 1, 3), ('E', 1, 4),
            ('F', 2, 0), ('AND', 2, 1), ('OR', 2, 2), ('XOR', 2, 3), ('NOT', 2, 4),
            ('Lsh', 3, 0), ('Rsh', 3, 1), ('Mod', 3, 2), ('<<', 3, 3), ('>>', 3, 4),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3), ('%', 4, 4),
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3), ('1/x', 5, 4),
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3), ('x²', 6, 4),
            ('0', 7, 0), ('.', 7, 1), ('=', 7, 2), ('+', 7, 3), ('√', 7, 4)
        ]
        
        for (texto, linha, coluna) in botoes:
            cmd = lambda x=texto: self.clique_botao(x)
            btn = ttk.Button(self.frame_botoes, text=texto, command=cmd)
            btn.grid(row=linha, column=coluna, sticky='nsew', padx=2, pady=2)
        
        # Configurar pesos
        for i in range(5):
            self.frame_botoes.grid_columnconfigure(i, weight=1)
        for i in range(8):
            self.frame_botoes.grid_rowconfigure(i, weight=1)
    
    def clique_botao(self, texto):
        current = self.display.get()
        
        if texto == 'C':
            self.limpar_display()
        elif texto == 'CE':
            self.limpar_entrada()
        elif texto == '⌫':
            if len(current) > 1:
                self.display.delete(len(current)-1)
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, '0')
        elif texto == '=':
            try:
                resultado = str(eval(current))
                self.historico.append(f"{current} = {resultado}")
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == '±':
            if current.startswith('-'):
                self.display.delete(0)
            else:
                self.display.insert(0, '-')
        elif texto == 'x²':
            try:
                resultado = str(float(current) ** 2)
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == '√':
            try:
                resultado = str(math.sqrt(float(current)))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == '1/x':
            try:
                resultado = str(1 / float(current))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == 'π':
            self.display.delete(0, tk.END)
            self.display.insert(0, str(math.pi))
        elif texto == 'e':
            self.display.delete(0, tk.END)
            self.display.insert(0, str(math.e))
        elif texto == 'sin':
            try:
                resultado = str(math.sin(math.radians(float(current))))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == 'cos':
            try:
                resultado = str(math.cos(math.radians(float(current))))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == 'tan':
            try:
                resultado = str(math.tan(math.radians(float(current))))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == 'log':
            try:
                resultado = str(math.log10(float(current)))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == 'ln':
            try:
                resultado = str(math.log(float(current)))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == 'x^y':
            self.display.insert(tk.END, '**')
        elif texto == '10^x':
            try:
                resultado = str(10 ** float(current))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == 'e^x':
            try:
                resultado = str(math.exp(float(current)))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == 'n!':
            try:
                resultado = str(math.factorial(int(float(current))))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto == 'mod':
            self.display.insert(tk.END, '%')
        elif texto == '|x|':
            try:
                resultado = str(abs(float(current)))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Erro')
        elif texto in ['MC', 'MR', 'MS', 'M+', 'M-']:
            self.operacao_memoria(texto)
        elif texto in ['Hex', 'Dec', 'Oct', 'Bin']:
            self.converter_base(texto)
        elif texto in ['AND', 'OR', 'XOR', 'NOT', 'Lsh', 'Rsh', '<<', '>>']:
            self.operacao_bitwise(texto)
        elif texto in ['A', 'B', 'C', 'D', 'E', 'F'] and self.modo_atual == "Programador":
            self.display.insert(tk.END, texto.lower())
        else:
            if current == '0' and texto not in ['+', '-', '*', '/', '.']:
                self.display.delete(0, tk.END)
            self.display.insert(tk.END, texto)
    
    def limpar_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, '0')
    
    def limpar_entrada(self):
        current = self.display.get()
        if current != '0':
            self.display.delete(0, tk.END)
            self.display.insert(0, '0')
    
    def operacao_memoria(self, op):
        try:
            valor = float(self.display.get())
            
            if op == 'MC':
                self.valor_memoria = 0
            elif op == 'MR':
                self.display.delete(0, tk.END)
                self.display.insert(0, str(self.valor_memoria))
            elif op == 'MS':
                self.valor_memoria = valor
            elif op == 'M+':
                self.valor_memoria += valor
            elif op == 'M-':
                self.valor_memoria -= valor
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, 'Erro')
    
    def converter_base(self, base):
        try:
            valor = self.display.get()
            
            if base == 'Hex':
                num = int(float(valor))
                self.display.delete(0, tk.END)
                self.display.insert(0, hex(num))
            elif base == 'Dec':
                if valor.startswith('0x'):
                    num = int(valor, 16)
                elif valor.startswith('0o'):
                    num = int(valor, 8)
                elif valor.startswith('0b'):
                    num = int(valor, 2)
                else:
                    num = float(valor)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(num))
            elif base == 'Oct':
                num = int(float(valor))
                self.display.delete(0, tk.END)
                self.display.insert(0, oct(num))
            elif base == 'Bin':
                num = int(float(valor))
                self.display.delete(0, tk.END)
                self.display.insert(0, bin(num))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, 'Erro')
    
    def operacao_bitwise(self, op):
        try:
            valor = int(float(self.display.get()))
            
            if op == 'AND':
                pass  # Implementar operação AND
            elif op == 'OR':
                pass  # Implementar operação OR
            elif op == 'XOR':
                pass  # Implementar operação XOR
            elif op == 'NOT':
                resultado = ~valor
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
            elif op == 'Lsh' or op == '<<':
                pass  # Implementar left shift
            elif op == 'Rsh' or op == '>>':
                pass  # Implementar right shift
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, 'Erro')

# Criar e executar a aplicação
root = tk.Tk()
app = CalculadoraAvancada(root)
root.mainloop()
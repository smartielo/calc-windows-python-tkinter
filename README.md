# Calculadora Avançada em Python

Uma calculadora multi-modo com interface gráfica inspirada na calculadora do Windows, desenvolvida com Python e Tkinter.

## ✨ Funcionalidades

### 🔢 Modos de Operação
- **Padrão**: Operações matemáticas básicas
- **Científica**: Funções avançadas (trigonometria, logaritmos, etc.)
- **Programador**: Conversão entre bases e operações bitwise

### 🧮 Principais Operações
| Categoria        | Operações                          |
|------------------|-----------------------------------|
| Básicas          | +, -, *, /, %, √, x², 1/x, ±      |
| Memória          | MC, MR, MS, M+, M-                |
| Científicas      | sin, cos, tan, log, ln, π, e, n!  |
| Programador      | Hex, Dec, Oct, Bin, AND, OR, XOR  |

### 🖥️ Interface
- Troca dinâmica entre modos
- Layout responsivo
- Teclas de navegação (CE, C, ⌫)

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/calculadora-python.git
```
2. Acesse o diretório:
```bash
cd calculadora-python
```
3. Execute o programa:
```bash
python calculadora.py
```
## 📦 Pré-requisitos
- Python 3.6+
- Tkinter (geralmente incluso no Python)

## 🛠️ Estrutura do Código
Copy
calculadora.py
├── Classe CalculadoraAvancada
│   ├── mudar_modo()
│   ├── criar_botoes_padrao()
│   ├── criar_botoes_cientifica()
│   ├── criar_botoes_programador()
│   └── clique_botao()
└── Funções auxiliares
    ├── operacao_memoria()
    ├── converter_base()
    └── operacao_bitwise()
## 🌟 Roadmap
- Modo Padrão
- Modo Científico
- Modo Programador (básico)
- Histórico visível
- Atalhos de teclado
- Temas (claro/escuro)

## 🤝 Como Contribuir
- Faça um fork do projeto
- Crie sua branch (git checkout -b feature/nova-funcionalidade)
- Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')
- Push para a branch (git push origin feature/nova-funcionalidade)
- Abra um Pull Request

📄 Licença
Distribuído sob licença MIT. Veja LICENSE para mais informações.

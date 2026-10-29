# Exercícios de Programação

Repositório com exercícios de programação para praticar lógica e desenvolver habilidades de resolução de problemas.

## Como adicionar um exercício

Coloque o exercício dentro da pasta `entrada/` e faça o push. A GitHub Action
organiza, numera e move o arquivo para a pasta da linguagem certa.

Duas formas são aceitas:

**1. Uma pasta com os arquivos do exercício** (recomendado quando há mais de um arquivo)

```
entrada/cartao-visita/
├── CartaoVisita.java
└── README.md
```

**2. Um arquivo solto**

```
entrada/calculadora.py
```

Depois:

```bash
git add -A
git commit -m "feat: exercicio calculadora"
git push
```

Em alguns segundos o bot move tudo para `python/ex001/`, `java/ex001/`, etc.
Para receber o resultado na sua máquina:

```bash
git pull
```

### Regras

- Cada exercício deve ter código de **uma única linguagem**. HTML, CSS e JS
  contam como uma linguagem só (`html-css-js`).
- A numeração (`ex001`, `ex002`, ...) é automática, na ordem alfabética dos
  nomes. O nome que você escolher não é preservado.
- Arquivos e pastas que começam com `.` são ignorados.
- Se a linguagem não for identificável, o script para e **não move nada**.
- Se preferir não depender do GitHub, rode `python3 scripts/organizar.py` antes
  de commitar.

### Linguagens reconhecidas

Python, Java, JavaScript, TypeScript, HTML/CSS/JS, C, C++, C#, PHP, Go, Rust,
Ruby, Kotlin, Swift e SQL.

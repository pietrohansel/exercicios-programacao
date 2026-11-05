# Exercícios de Programação

Repositório com exercícios de programação para praticar lógica e desenvolver habilidades de resolução de problemas.

## Estrutura

| Pasta | Conteúdo |
| --- | --- |
| `entrada/` | Área de envio. A GitHub Action move os exercícios daqui para a pasta da linguagem correta. |
| `python/`, `java/`, `c/`, ... | Exercícios organizados por linguagem e numerados (`ex001`, `ex002`, ...). |
| `scripts/organizar.py` | Script usado pela Action e para organizar os exercícios localmente. |
| `.github/workflows/` | Actions de organização e de validação do código. |

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
- A pasta é renomeada automaticamente para `ex001`, `ex002`, ... na ordem
  alfabética dos nomes. Os nomes dos arquivos dentro dela são preservados.
- Arquivos e pastas que começam com `.` são ignorados.
- Se a linguagem não for identificável, o script para e **não move nada**.
- Se preferir não depender do GitHub, rode `python3 scripts/organizar.py` antes
  de commitar.

### Linguagens reconhecidas

Python, Java, JavaScript, TypeScript, HTML/CSS/JS, C, C++, C#, PHP, Go, Rust,
Ruby, Kotlin, Swift, SQL e Assembly.

## Como executar localmente

Pré-requisitos, conforme a linguagem do exercício:

- **Python:** Python 3.10 ou superior
- **Java:** JDK 21 ou superior
- **C:** GCC
- **HTML/CSS/JS:** um navegador
- **SQL:** o cliente do banco usado no exercício
- **Assembly:** `as` e `ld` (binutils)

Exemplos:

```bash
# Python
python3 python/ex001/127.py

# Java com package (confira o package no arquivo)
javac -d /tmp/classes java/ex001/ex001.java
java -cp /tmp/classes ex001.ex001

# Java sem package
javac -d /tmp/classes java/ex031/Main.java
java -cp /tmp/classes Main

# C (compile fora da árvore para não versionar o binário)
gcc c/ex001/main.c -o /tmp/main
/tmp/main

# Assembly
as -o /tmp/main.o assembly/ex001/main.asm
ld -o /tmp/main /tmp/main.o
/tmp/main
```

Para HTML/CSS/JS, abra o arquivo `.html` no navegador. Para SQL, execute o
arquivo com o cliente do seu banco de dados.

## Validação automática

O workflow `.github/workflows/validar.yml` roda em pushes e pull requests e
verifica:

- sintaxe dos arquivos Python;
- compilação de cada pasta de exercícios Java;
- sintaxe dos arquivos C;
- montagem dos arquivos Assembly.

Assim, erros de sintaxe aparecem no GitHub antes de se espalharem pelo
repositório.

## Segurança e arquivos ignorados

Nunca versione arquivos `.env` nem credenciais. O `.gitignore` já bloqueia
`.env` e variações (`.env.local`, `.env.production`, etc.); se precisar
documentar as variáveis usadas, crie um `.env.example` com valores fictícios.

O `.gitignore` também cobre binários compilados, `__pycache__`, ambientes
virtuais, `node_modules`, pastas de build e arquivos de IDE/sistema.

## Padrão de commits

O repositório usa o formato **Conventional Commits**:

```text
<tipo>: <descrição curta>
```

Tipos aceitos: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`,
`build`, `ci`, `chore` e `revert`.

Exemplos:

```bash
git commit -m "feat: adiciona exercício de calculadora"
git commit -m "fix: corrige leitura de entrada do exercício 12"
git commit -m "chore: atualiza .gitignore"
```

### Template e validação no seu clone

O repositório inclui um template em `.gitmessage` e um hook de validação em
`.githooks/commit-msg`. Ative-os uma vez em cada clone:

```bash
git config commit.template .gitmessage
git config core.hooksPath .githooks
```

Depois disso:

- `git commit` sem `-m` abre o editor já com o template;
- mensagens fora do padrão são recusadas;
- o assunto deve ter no máximo 72 caracteres.

Para ignorar a validação em uma emergência, use `git commit --no-verify`.

## Licença

Este repositório está licenciado sob a licença MIT. Veja o arquivo
[LICENSE](LICENSE) para mais detalhes.


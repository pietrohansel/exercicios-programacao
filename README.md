# Exercícios de Programação

[![Validar exercicios](https://github.com/pietrohansel/exercicios-programacao/actions/workflows/validar.yml/badge.svg?branch=main)](https://github.com/pietrohansel/exercicios-programacao/actions/workflows/validar.yml)

Este é um **repositório automatizado** para guardar os exercícios e pequenos
projetos que faço enquanto estudo programação — em curso técnico, faculdade,
cursos avulsos ou simplesmente praticando por conta própria.

Ao estudar programação, uma coisa é certa: você fará muitos exercícios e
desenvolverá diversos projetos. A ideia aqui é não espalhar isso em pastas
soltas. Cada exercício entra numa área de envio (`entrada/`) e um bot do GitHub
se encarrega de organizar, numerar e guardar tudo na pasta da linguagem certa.
O acervo cresce sem virar bagunça e fica fácil reencontrar um exercício depois.

O que acontece automaticamente a cada push:

- o exercício sai de `entrada/` e vai para `linguagens/<linguagem>/exNNN`;
- o índice `linguagens/README.md` é regerado com a contagem por linguagem;
- o código é validado (lint, testes, sintaxe e compilação) antes de entrar.

## Estrutura

| Pasta | Conteúdo |
| --- | --- |
| `entrada/` | Área de envio. A GitHub Action move os exercícios daqui para a pasta da linguagem correta. |
| `linguagens/` | Pasta única com uma subpasta por linguagem (`python/`, `java/`, `c/`, ...), cada uma com os exercícios numerados (`ex001`, `ex002`, ...). |
| `linguagens/README.md` | Índice gerado automaticamente com a contagem de exercícios por linguagem. |
| `scripts/organizar.py` | Script usado pela Action e para organizar os exercícios localmente. |
| `scripts/indice.py` | Gera o índice de `linguagens/README.md`. |
| `tests/` | Testes do script de organização (`pytest`). |
| `Makefile` | Atalhos para setup, testes, lint, formatação e organização local. |
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

Depois é só commitar e dar push:

```bash
git add entrada/calculadora
git commit -m "feat: adiciona exercício de calculadora"
git push
```

Use o caminho específico do exercício (e não `git add -A`) para não incluir
arquivos locais por engano. O passo a passo completo, os tipos de commit e os
erros mais comuns estão em [Padrão de commits](#padrão-de-commits).

Em alguns segundos o bot move tudo para `linguagens/python/ex001/`,
`linguagens/java/ex001/`, etc. Para receber o resultado na sua máquina:

```bash
git pull
```

### Regras

- Cada exercício deve ter código de **uma única linguagem**.
- **JavaScript sozinho vai para `linguagens/javascript/`.** Só vai para `linguagens/html-css-js/`
  quando o exercício tem HTML ou CSS junto (ex.: `index.html` + `app.js`),
  porque aí é uma página web e o JS faz parte dela.

  ```
  entrada/ex2/ex2.js                 -> linguagens/javascript/ex001/ex2.js
  entrada/ex1/ (ex1.html + ex1.js)   -> linguagens/html-css-js/ex001/
  ```
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
python3 linguagens/python/ex001/127.py

# Java com package (confira o package no arquivo)
javac -d /tmp/classes linguagens/java/ex001/ex001.java
java -cp /tmp/classes ex001.ex001

# Java sem package
javac -d /tmp/classes linguagens/java/ex031/Main.java
java -cp /tmp/classes Main

# C (compile fora da árvore para não versionar o binário)
gcc linguagens/c/ex001/main.c -o /tmp/main
/tmp/main

# Assembly
as -o /tmp/main.o linguagens/assembly/ex001/main.asm
ld -o /tmp/main /tmp/main.o
/tmp/main
```

Para HTML/CSS/JS, abra o arquivo `.html` no navegador. Para SQL, execute o
arquivo com o cliente do seu banco de dados.

## Validação automática

O workflow `.github/workflows/validar.yml` roda em pushes e pull requests e
verifica:

- lint (`ruff`) e testes (`pytest`) do script de organização;
- sintaxe dos arquivos Python;
- compilação de cada pasta de exercícios Java;
- sintaxe dos arquivos C;
- montagem dos arquivos Assembly.

Assim, erros aparecem no GitHub antes de se espalharem pelo repositório.

## Desenvolvimento local

Os comandos ficam no `Makefile`:

```bash
make setup     # cria .venv-dev, instala dependências e ativa os hooks
make test      # roda os testes do script de organização
make lint      # ruff nos scripts e testes
make format    # formata scripts e testes
make organize  # organiza entrada/ e atualiza o índice, sem depender do GitHub
```

O `make setup` também configura o template de commit e os hooks de
`pre-commit` (ruff + validação da mensagem de commit).

## Segurança e arquivos ignorados

Nunca versione arquivos `.env` nem credenciais. O `.gitignore` já bloqueia
`.env` e variações (`.env.local`, `.env.production`, etc.), chaves (`*.pem`,
`*.key`), `credentials.json` e `secrets.*`; se precisar documentar as variáveis
usadas, crie um `.env.example` com valores fictícios.

O repositório também conta com **secret scanning** e **push protection** do
GitHub: um segredo conhecido é bloqueado antes de entrar no histórico.

O `.gitignore` cobre ainda binários compilados, `__pycache__`, ambientes
virtuais, `node_modules`, pastas de build e arquivos de IDE/sistema.

## Padrão de commits

Toda mensagem segue o formato **Conventional Commits**:

```text
<tipo>: <descrição curta>
```

- `tipo` é uma palavra fixa, em minúsculas: `feat`, `fix`, `docs`, `style`,
  `refactor`, `perf`, `test`, `build`, `ci`, `chore` ou `revert`;
- depois do tipo vêm dois-pontos e **um espaço**;
- a descrição não pode ser vazia, e o assunto inteiro deve ter **até 72
  caracteres**;
- o escopo é opcional, em minúsculas e sem espaço: `docs(readme): ...`;
- acentos e `ç` são permitidos na descrição.

### Qual tipo usar

| O que você fez | Tipo | Exemplo |
| --- | --- | --- |
| Novo exercício ou projeto | `feat` | `feat: adiciona exercício de calculadora` |
| Correção de bug no código | `fix` | `fix: corrige leitura de entrada do exercício 12` |
| README, comentários, documentação | `docs` | `docs: revisa a introdução do README` |
| Formatação, sem mudar lógica | `style` | `style: formata scripts com ruff` |
| Reorganização sem mudar comportamento | `refactor` | `refactor: separa organizar em funções` |
| Testes novos ou ajustados | `test` | `test: cobre pasta sem código` |
| Dependências e build | `build` | `build: atualiza requirements-dev` |
| Workflows, Dependabot, Actions | `ci` | `ci: adiciona lint e testes` |
| Tarefas gerais (`.gitignore`, mover pastas) | `chore` | `chore: atualiza .gitignore` |
| Reversão de um commit anterior | `revert` | `revert: desfaz commit de organização` |

### Fazendo um commit (passo a passo)

**Adicionar um exercício** — o caso mais comum:

```bash
mkdir -p entrada/calculadora
$EDITOR entrada/calculadora/calculadora.py

git status --short                  # confere o que vai entrar
git add entrada/calculadora         # caminho específico, não "git add -A"
git commit -m "feat: adiciona exercício de calculadora"
git push
```

Depois do push a Action move a pasta para `linguagens/python/exNNN` e cria o
commit dela sozinha. Você não precisa numerar nem mover nada à mão.

**Mexer em script, documentação ou CI:**

```bash
git add scripts/organizar.py tests/test_organizar.py
git commit -m "fix: ignora venv na detecção de linguagem"
git push
```

**Com corpo explicando o porquê:**

```bash
git commit -m "refactor: separa organizar em funções" \
           -m "Permite testar sem tocar em arquivos reais."
```

**Pelo editor, usando o template:**

```bash
git add <arquivos>
git commit
```

O editor abre o `.gitmessage`. Apague as linhas `#` e escreva o assunto **na
primeira linha**:

```text
docs: revisa a introdução do README

Explica por que o repositório é organizado por linguagem.
```

Se salvar o arquivo apenas com as linhas de comentário, nada é commitado: o
hook recusa com `Mensagem de commit inválida` e o commit não chega a existir.
Nesse caso o `git push` responde `Everything up-to-date` e parece que o push
falhou, quando na verdade não havia nada para enviar.

### Antes de dar push

```bash
git status -sb            # "ahead 1" = o commit existe
git log --oneline -1      # a mensagem saiu como você queria?
make lint && make test    # apenas se mexeu em scripts/ ou tests/
```

Se aparecer `nothing to commit, working tree clean` e `main...origin/main` sem
`[à frente N]`, não há nada para enviar.

### Erros comuns

| Saída | Causa | O que fazer |
| --- | --- | --- |
| `Mensagem de commit inválida` | assunto vazio ou sem `tipo:` | refaça o commit com mensagem válida |
| `O assunto do commit tem N caracteres` | passou de 72 | resuma ou detalhe no corpo |
| `Everything up-to-date` no push | o commit não foi criado | `git status` e refaça o commit |
| `Cannot force-push to a protected branch` | `--amend` ou `--force` em commit já enviado | faça um commit novo |
| `ruff` failed | erro de lint em `scripts/` ou `tests/` | `make lint`, corrija e `git add` de novo |

A branch `main` é protegida contra deleção e force-push, mas aceita pushes
normais.

### Template e validação no seu clone

O repositório inclui um template em `.gitmessage`, um hook de validação em
`.githooks/commit-msg` e um `pre-commit` (`ruff`, YAML e conflitos de merge).
Ative tudo com:

```bash
make setup
```

Depois disso:

- `git commit` sem `-m` abre o editor já com o template;
- mensagens fora do padrão são recusadas;
- o assunto deve ter no máximo 72 caracteres;
- o `ruff` roda automaticamente nos arquivos de `scripts/` e `tests/`.

Se o hook reclamar de lint, rode `make lint` e `make format`, adicione as
correções e repita o commit. Para ignorar a validação em uma emergência, use
`git commit --no-verify` — mas isso pula o `ruff` junto.

## Licença

Este repositório está licenciado sob a licença MIT. Veja o arquivo
[LICENSE](LICENSE) para mais detalhes.


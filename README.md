## Comandos Git

### Fazer clone do projeto
Esse comando baixa uma cópia completa do repositório remoto para a sua máquina, criando uma pasta com todos os arquivos e o histórico do projeto:

```bash
git clone https://github.com/citoh/python-unifecaf-2026-1.git
```

### Acessar a pasta do projeto
Esse comando entra na pasta do projeto clonada, permitindo executar os demais comandos Git no repositório correto:

```bash
cd python-unifecaf-2026-1
```

### Atualizar o projeto com git pull
Esse comando busca e aplica na sua cópia local as alterações mais recentes enviadas para o repositório remoto atualmente configurado:

```bash
git pull
```

### Limpar alterações locais já feitas
Esse comando descarta alterações realizadas em arquivos já rastreados pelo Git e restaura o conteúdo deles para o último estado salvo no repositório local:

```bash
git restore .
```

### Limpar arquivos novos não rastreados
Esse comando remove arquivos e pastas criados localmente que ainda não foram adicionados ao controle de versão:

```bash
git clean -fd
```

### Limpar todas as alterações locais de uma vez
Esses comandos restauram os arquivos rastreados e removem arquivos não rastreados, deixando o projeto local em um estado limpo:

```bash
git restore .
git clean -fd
```

### Acessar a branch original do projeto
Esse comando troca para a branch `main`, que contém a versão original do projeto:

```bash
git checkout main
```

### Acessar a branch com respostas
Esse comando troca para a branch `resolucao`, que contém a versão com as respostas:

```bash
git checkout resolucao
```

### Listar as branches disponíveis
Esse comando mostra todas as branches locais e indica em qual branch você está no momento:

```bash
git branch
```

### Buscar as branches remotas antes de trocar de branch
Esse comando atualiza as referências locais do repositório remoto, ajudando a garantir que a branch desejada esteja visível localmente:

```bash
git fetch --all
```

### Fazer fork para o próprio repositório
Esse processo cria uma cópia do repositório original na sua conta do GitHub. Primeiro, faça o fork pela interface do GitHub. Depois, clone o fork para a sua máquina usando a URL do seu próprio repositório:

```bash
git clone https://github.com/SEU_USUARIO/python-unifecaf-2026-1.git
```

### Entrar no projeto clonado a partir do fork
Esse comando acessa a pasta do repositório clonado do seu fork:

```bash
cd python-unifecaf-2026-1
```

### Conectar o fork ao repositório original
Esse comando adiciona o repositório original como uma referência chamada `upstream`, permitindo buscar atualizações da fonte original do projeto:

```bash
git remote add upstream https://github.com/citoh/python-unifecaf-2026-1.git
```

### Verificar os repositórios configurados
Esse comando mostra os repositórios remotos configurados no projeto, como `origin` e `upstream`:

```bash
git remote -v
```

### Atualizar o próprio repositório com o original
Esses comandos buscam as atualizações do repositório original, trocam para a branch `main`, aplicam as mudanças localmente e depois enviam essa atualização para o seu fork no GitHub:

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### Atualizar a branch com respostas no próprio fork a partir do original
Esses comandos trocam para a branch `resolucao`, buscam as alterações do repositório original para essa branch, aplicam as mudanças localmente e enviam a atualização para o seu fork:

```bash
git fetch upstream
git checkout resolucao
git merge upstream/resolucao
git push origin resolucao
```

---
Ementa do Curso:  

# UniFECAF | Computational Logic Using Python

Repositório da disciplina **Computational Logic Using Python**, contendo materiais, exemplos práticos, algoritmos e exercícios desenvolvidos ao longo do curso.

### 1️⃣ Fundamentos de Lógica Computacional

🚀 **Aula 1 - Estruturas lógicas: proposições, operadores lógicos e tabelas-verdade**  
🚀 **Aula 2 - Regras de inferência e equivalências lógicas**  
🚀 **Aula 3 - Construção de algoritmos baseados em lógica**  
🚀 **Aula 4 - Solução de problemas com pensamento computacional**  

<sup>**2️⃣ Introdução ao Python**</sup>  

<sup>Aula 5 - Sintaxe e estrutura básica da linguagem Python</sup>  
<sup>Aula 6 - Variáveis, tipos de dados e operadores</sup>  
<sup>Aula 7 - Estruturas de controle: condicionais e loops</sup>  

<sup>**3️⃣ Estruturas de Decisão e Repetição**</sup>  

<sup>Aula 8 - Condicionais simples e compostos (if, elif, else)</sup>  
<sup>Aula 9 - Estruturas de repetição (for, while)</sup>  
<sup>Aula 10 - Controle de fluxo e interrupções (break, continue)</sup>  
<sup>Aula 11 - Utilização eficiente de estruturas de controle</sup>  
<sup>Aula 12 - Conexão com SGBD</sup>  

<sup>**4️⃣ Estruturas de Dados e Funções**</sup>  

<sup>Aula 13 - Listas, tuplas e dicionários em Python</sup>  
<sup>Aula 14 - Manipulação de strings e arquivos</sup>  
<sup>Aula 15 - Criação e uso de funções</sup>  
"""

output_path = "/mnt/data/README.md"

pypandoc.convert_text(content, 'md',
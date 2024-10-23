# **Projeto: Upload de Arquivos para Amazon S3**  

## 📋 **Descrição do Projeto**  
Este projeto tem como objetivo automatizar o upload de arquivos de uma pasta local chamada **exames** para um **bucket S3** na AWS. O código utiliza **Python** com o SDK **boto3** para se conectar ao S3 e realizar operações de envio de arquivos. Além disso, as credenciais e variáveis sensíveis são gerenciadas por meio de um arquivo **`.env`** para garantir a segurança.

---

## 🛠️ **Tecnologias Utilizadas**
- **Python** 3.11.5  
- **boto3**: SDK para acesso à API da AWS  
- **Poetry**: Gerenciador de pacotes e ambientes virtuais  
- **dotenv**: Carregamento seguro de variáveis de ambiente  
- **AWS S3**: Armazenamento em nuvem  
- **IAM (Identity and Access Management)**: Gerenciamento de usuários e permissões na AWS  

---

## 📁 **Estrutura do Projeto**
```
📂 projeto-s3-upload
├── .env                  # Variáveis de ambiente (credentials e configuração do S3)
├── .gitignore            # Arquivos a serem ignorados pelo Git
├── etl.py                # Código principal do projeto
├── README.md             # Documentação do projeto (este arquivo)
└── poetry.lock / pyproject.toml # Arquivos do Poetry
```

---

## ⚙️ **Configuração e Instalação**

### 1. **Pré-requisitos**
- **Conta AWS** com acesso ao IAM e S3  
- **Python** instalado na versão 3.11.x  
- **Poetry** instalado para gerenciar pacotes e dependências  
- **Git** para versionamento e controle de código

### 2. **Instalação das Dependências**
No diretório do projeto, rode o seguinte comando para inicializar o ambiente e instalar as bibliotecas:

```bash
poetry install
```

### 3. **Configuração do Arquivo `.env`**
Crie um arquivo **`.env`** com as seguintes variáveis:

```
AWS_ACCESS_KEY_ID=<sua_access_key>
AWS_SECRET_ACCESS_KEY=<sua_secret_key>
AWS_REGION=us-east-1  # Altere conforme sua região
BUCKET_NAME=exames-amais
```

---

## 🔑 **Configuração de Acesso na AWS**  

1. **Criação do Bucket**  
   Acesse o console AWS S3 e crie um bucket com o nome **`exames-amais`** (ou qualquer outro nome que configure no `.env`).  

2. **Configuração do IAM**  
   - Crie uma **política IAM** com permissões restritas apenas para esse bucket.  
   - Crie um **usuário IAM** e adicione a política criada.  
   - Gere a **Access Key** e **Secret Key** do usuário em **Security Credentials > Access Keys > Create Access Key**.  
   - **Tags** foram adicionadas ao bucket e ao usuário para boas práticas de governança.

---

## 🚀 **Como Executar o Projeto**

1. **Ativar o Ambiente Virtual**  
   Caso o ambiente já tenha sido criado, ative-o:

```bash
poetry shell
```

2. **Executar o Código**  

```bash
poetry run python etl.py
```

---

## 📋 **Funcionamento do Código**  

1. **Leitura dos Arquivos**  
   A função `read_files_exames()` lê os arquivos da pasta **exames** e retorna uma lista de nomes de arquivos.

2. **Upload para o S3**  
   A função `upload_arq_s3()` realiza o upload dos arquivos listados para o bucket S3 especificado no `.env`.  

3. **Orquestração**  
   A função `orq_functions()` coordena a leitura dos arquivos e o upload para o S3.

---

## ⚠️ **Possíveis Erros e Soluções**  
1. **"O sistema não pode encontrar o arquivo especificado"**  
   - Verifique se a pasta de exames foi criada e se os arquivos estão no diretório correto.  

2. **Erro de Credenciais**  
   - Certifique-se de que as **Access Keys** no `.env` são válidas e têm as permissões necessárias.  

3. **Erro de Permissão no Bucket**  
   - Verifique se a política IAM tem permissões corretas para o bucket S3.






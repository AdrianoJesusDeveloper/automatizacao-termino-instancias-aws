# Automação do Encerramento de Instâncias EC2 com AWS Lambda e EventBridge

Este projeto tem como objetivo demonstrar a criação de uma solução automatizada para encerramento de instâncias EC2 na AWS utilizando **Lambda Functions**, **IAM Policies** e **Amazon EventBridge**.

## 🚀 Funcionalidades

- Criação de uma política personalizada do IAM para término de instâncias EC2.
- Implementação de uma função Lambda em Python.
- Associação da política IAM à função Lambda.
- Agendamento automático da execução via Amazon EventBridge.
- Eliminação segura de recursos após uso.

## 🧱 Arquitetura

A arquitetura da solução envolve os seguintes componentes:

- **IAM Policy**: Permite à função Lambda acessar e encerrar instâncias EC2.
- **Lambda Function**: Código em Python que identifica e encerra instâncias.
- **EventBridge**: Responsável por acionar a função Lambda periodicamente.

## 📂 Estrutura


automatizacao-termino-instancias-aws

│


├── README.md

├── lambda

│   └── Terminator.py

├── policy

│   └── politica_terminar_ec2.json

├── docs

│   └── diagramas.png (ilustrações opcionais)

├── .gitignore

└── LICENSE (opcional)




- `lambda/Terminator.py`: Script que realiza a finalização das instâncias.
- `policy/politica_terminar_ec2.json`: Política IAM em formato JSON.
- `docs/`: Espaço para diagramas, imagens ou documentações complementares.

## 🛠️ Como utilizar

1. Crie a política do IAM utilizando o arquivo JSON disponível em `policy/`.
2. Crie a função Lambda com a role associada à política criada.
3. Faça o upload do código `Terminator.py` na função Lambda.
4. Programe a execução usando EventBridge com expressões cron ou rate.
5. Teste a execução criando instâncias EC2 e aguardando o término automático.

## 🧹 Limpeza dos recursos

Para evitar custos, exclua os seguintes recursos após uso:
- Função Lambda
- Role do IAM
- Política IAM
- Regra do EventBridge

## 📝 Autor: 
### Adriano Costa 

Este projeto foi desenvolvido como parte de estudos de automação em ambientes cloud com AWS.




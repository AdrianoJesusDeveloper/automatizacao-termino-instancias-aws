![INÍCIO](docs/capa.png)

---

## 📌 Descrição

Automatização do encerramento de instâncias EC2 usando AWS Lambda, IAM e EventBridge. Projeto com foco em práticas de automação na nuvem.

---

## 🧠 Funcionalidades

- 🔐 Criação de uma política IAM personalizada.
- 🧬 Implementação de função Lambda com Python.
- ⚙️ Agendamento via Amazon EventBridge.
- 🧹 Remoção segura dos recursos após uso.

---

## 🧱 Arquitetura da Solução

![Arquitetura da Solução](docs/policy_body.png)
![função do IAM](docs/role_terminate_ec2-created.png)
![função do Lambda](docs/lambda_created.png)

---

## 📁 Estrutura do Projeto

```plaintext
📦 automatizacao-termino-instancias-aws
├── 📄 README.md
├── 📁 lambda
│   └── 🐍 Terminator.py
├── 📁 policy
│   └── 📄 politica_terminar_ec2.json
├── 📁 docs
│   └── 🖼️ arquitetura.png
└── 📄 .gitignore
```

---

## 🛠️ Como Utilizar

1. Crie a **política IAM** (`policy/politica_terminar_ec2.json`).
2. Crie a **função Lambda** com a role associada.
3. Faça upload do script `lambda/Terminator.py`.
4. Configure um **gatilho no EventBridge** com expressão `rate(12 hours)` ou `rate(5 minutes)`.
5. Monitore e teste com uma instância EC2 ativa.

---

- `lambda/Terminator.py`: Script que realiza a finalização das instâncias.
- `policy/politica_terminar_ec2.json`: Política IAM em formato JSON.
- `docs/`: Espaço para diagramas, imagens ou documentações complementares.

---

## 🧹 Limpeza de Recursos

Para evitar custos:

- Exclua a função Lambda
- Remova a role e a política do IAM
- Apague a regra do EventBridge

---

## ✍️ Autor

### Adriano Costa

Este projeto foi desenvolvido como parte de estudos práticos em automação de infraestrutura com foco em ambientes cloud utilizando AWS durante o curso de **AWS Cloud Developer na Escola da Nuvem**.

# 🎮 Playground - Mini Projetos de Aprendizado

Este repositório contém uma coleção de mini projetos focados em diferentes tecnologias de banco de dados e cache, desenvolvidos para fins de aprendizado e experimentação.

## 📁 Estrutura do Projeto

```
playground/
├── README.md                 # Este arquivo
├── mongodb/                  # Projetos MongoDB
│   ├── docker-compose.yml   # Configuração Docker
│   ├── README.md            # Documentação específica
│   ├── init-scripts/        # Scripts de inicialização
│   └── house-price-sample-data.json
├── redis/                    # Projetos Redis
│   ├── docker-compose.yml   # Redis Stack + Redis Commander
│   ├── README.md            # Guia completo do Redis
│   ├── scripts/             # Scripts .redis de exemplo
│   ├── sample-data/         # Dados de exemplo
│   └── python-cache-demo/   # Demo Python + Redis Cache
└── neo4j/                    # Projetos Neo4j (futuro)
```

## 🍃 MongoDB

### **Configuração e Dados**
- **Docker Compose**: Configuração completa com MongoDB
- **Scripts de Inicialização**: `01-init-databases.js` para setup automático
- **Dados de Exemplo**: Dataset de preços de casas em JSON

### **Estrutura Detalhada**
```
mongodb/
├── docker-compose.yml           # Serviço MongoDB com volumes
├── init-scripts/
│   └── 01-init-databases.js    # Criação de databases e collections
├── house-price-sample-data.json # Dataset de exemplo
└── README.md                    # Documentação completa
```

### **Funcionalidades**
- Setup automatizado de databases
- Dados de exemplo para experimentação
- Documentação com conceitos básicos do MongoDB
- Exemplos de queries e operações

## 🔴 Redis

### **Redis Stack Completo**
- **Redis Stack**: Inclui módulos JSON, TimeSeries, Graph e Search
- **RedisInsight**: Interface web para visualização
- **Redis Commander**: Interface alternativa para administração
- **Scripts de Exemplo**: Códigos `.redis` prontos para executar

### **Estrutura Detalhada**
```
redis/
├── docker-compose.yml           # Redis Stack + Redis Commander
├── README.md                    # Guia completo com exemplos
├── scripts/                     # Scripts de exemplo
│   ├── basic-examples.redis     # Comandos básicos
│   ├── json-examples.redis      # RedisJSON
│   ├── timeseries-examples.redis # RedisTimeSeries
│   ├── graph-examples.redis     # RedisGraph
│   ├── search-examples.redis    # RedisSearch
│   └── run-all-examples.redis   # Executa todos os exemplos
├── sample-data/                 # Dados de exemplo
│   ├── ecommerce-products.json  # Produtos de e-commerce
│   └── sensor-data.json         # Dados de sensores
└── python-cache-demo/          # Projeto Python + Redis
```

### **Python Cache Demo**
Projeto completo demonstrando cache Redis vs API direta:

#### **Tecnologias**
- **FastAPI**: Framework web moderno
- **Redis**: Cache em memória
- **JSONPlaceholder**: API externa para testes

#### **Estrutura do Projeto**
```
python-cache-demo/
├── app.py                      # API FastAPI principal
├── test_performance.py         # Script de testes de performance
├── requirements.txt            # Dependências Python
├── start_demo.bat             # Script de inicialização
├── postman_collection.json    # Coleção Postman
├── README.md                  # Documentação detalhada
└── .gitignore                 # Arquivos ignorados
```

#### **Funcionalidades**
- **API REST** com 5 endpoints (posts, users, comments, albums, todos)
- **Cache Redis** com TTL de 5 minutos
- **Parâmetro `use_cache`** para comparar performance
- **Testes automatizados** de performance
- **Documentação interativa** (Swagger UI)
- **Coleção Postman** pronta para usar

#### **Exemplos de Uso**
```bash
# Iniciar o ambiente
cd redis/python-cache-demo
start_demo.bat

# Testar performance
python test_performance.py

# Acessar documentação
# http://localhost:8000/docs
```

#### **Resultados de Performance**
- **API Externa**: ~300-400ms
- **Cache Redis**: ~1-5ms
- **Melhoria**: ~90-95% mais rápido com cache

## 🎯 Objetivos dos Projetos

### **MongoDB**
- Aprender conceitos de NoSQL
- Experimentar com documentos JSON
- Praticar queries e agregações
- Entender diferenças entre SQL e NoSQL

### **Redis**
- Dominar cache em memória
- Explorar diferentes estruturas de dados
- Aprender módulos avançados (JSON, TimeSeries, Graph)
- Implementar padrões de cache

### **Python Cache Demo**
- Demonstrar impacto do cache na performance
- Praticar desenvolvimento de APIs
- Aprender integração Redis + Python
- Implementar testes de performance

## 🛠️ Tecnologias Utilizadas

- **Docker & Docker Compose**: Containerização
- **MongoDB**: Banco NoSQL
- **Redis Stack**: Cache e estruturas de dados
- **Python 3.12**: Linguagem de programação
- **FastAPI**: Framework web
- **Postman**: Testes de API
- **RedisInsight**: Interface visual Redis

## 📊 Dados de Exemplo

### **MongoDB**
- Dataset de preços de casas
- Estrutura JSON complexa
- Dados para experimentação

### **Redis**
- Produtos de e-commerce
- Dados de sensores IoT
- Estruturas para diferentes módulos

## 🚀 Como Executar

### **MongoDB**
```bash
cd mongodb
docker-compose up -d
```

### **Redis**
```bash
cd redis
docker-compose up -d
# Acesse RedisInsight: http://localhost:8001
```

### **Python Cache Demo**
```bash
cd redis/python-cache-demo
pip install -r requirements.txt
python app.py
# Acesse API: http://localhost:8000
```

## 📚 Documentação

Cada projeto possui documentação detalhada:
- **Conceitos básicos** da tecnologia
- **Instruções de instalação**
- **Exemplos práticos**
- **Casos de uso**
- **Troubleshooting**

## 🎨 Próximos Passos

- **Neo4j**: Projetos com grafos
- **Elasticsearch**: Busca full-text
- **PostgreSQL**: Banco relacional avançado
- **Kafka**: Streaming de dados
- **Machine Learning**: Modelos preditivos

---

*Este playground serve como base para experimentação e aprendizado prático com diferentes tecnologias de dados.*

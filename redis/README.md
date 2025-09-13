# Redis Playground 🚀

Este é um ambiente de aprendizado completo para Redis, configurado com diferentes módulos para trabalhar com diversos tipos de dados: documentos JSON, séries temporais, grafos, e muito mais!

## 🏗️ Arquitetura

Este playground inclui:

- **Redis Stack**: Redis com módulos integrados (JSON, TimeSeries, Graph, Search, etc.)
- **RedisInsight**: Interface web para visualização e gerenciamento
- **Redis Commander**: Interface alternativa para administração
- **Scripts de exemplo**: Códigos prontos para testar diferentes funcionalidades
- **Dados de exemplo**: Conjuntos de dados para experimentar

## 🚀 Como usar

### 1. Iniciar o ambiente

```bash
cd redis
docker-compose up -d
```

### 2. Acessar as interfaces

- **RedisInsight**: http://localhost:8001
- **Redis Commander**: http://localhost:8081
- **Redis CLI**: `docker exec -it redis-playground redis-cli`

### 3. Executar scripts de exemplo

```bash
# Executar script de dados JSON
docker exec -it redis-playground redis-cli < scripts/json-examples.lua

# Executar script de séries temporais
docker exec -it redis-playground redis-cli < scripts/timeseries-examples.lua

# Executar script de grafos
docker exec -it redis-playground redis-cli < scripts/graph-examples.lua
```

## 📚 O que é Redis?

Redis (Remote Dictionary Server) é um banco de dados em memória de código aberto que pode ser usado como:

- **Cache**: Armazenamento temporário de alta velocidade
- **Banco de dados**: Persistência de dados com diferentes estruturas
- **Message broker**: Sistema de mensageria pub/sub
- **Session store**: Armazenamento de sessões de usuário

### Características principais:

- ⚡ **Velocidade**: Operações em memória = latência ultra-baixa
- 🔄 **Flexibilidade**: Múltiplas estruturas de dados
- 📈 **Escalabilidade**: Suporte a clustering e replicação
- 🛠️ **Módulos**: Extensibilidade através de módulos

## 🗂️ Estruturas de Dados Básicas

### 1. Strings
```redis
SET nome "João"
GET nome
INCR contador
```

### 2. Lists
```redis
LPUSH lista "item1"
RPUSH lista "item2"
LRANGE lista 0 -1
```

### 3. Sets
```redis
SADD tags "redis" "database" "cache"
SMEMBERS tags
SINTER tags1 tags2
```

### 4. Hashes
```redis
HSET usuario:1 nome "João" idade 30
HGET usuario:1 nome
HGETALL usuario:1
```

### 5. Sorted Sets
```redis
ZADD ranking 100 "player1" 200 "player2"
ZRANGE ranking 0 -1 WITHSCORES
```

## 🔧 Módulos Avançados

### JSON Module
Trabalhe com documentos JSON nativamente:

```redis
JSON.SET usuario:1 $ '{"nome":"João","idade":30,"endereco":{"cidade":"São Paulo"}}'
JSON.GET usuario:1 $.nome
JSON.SET usuario:1 $.endereco.estado '"SP"'
```

### TimeSeries Module
Para dados temporais e métricas:

```redis
TS.CREATE temperatura LABELS sensor temp
TS.ADD temperatura * 25.5
TS.RANGE temperatura - +
```

### Graph Module
Para relacionamentos complexos:

```redis
GRAPH.QUERY social "CREATE (a:Person {name:'Alice'})"
GRAPH.QUERY social "MATCH (a:Person) RETURN a"
```

### Search Module
Busca full-text:

```redis
FT.CREATE idx ON JSON PREFIX 1 doc: SCHEMA $.nome AS nome TEXT
FT.SEARCH idx "João"
```

## 📊 Casos de Uso Comuns

### 1. Cache de Sessão
```redis
SETEX session:abc123 3600 '{"user_id":1,"permissions":["read","write"]}'
```

### 2. Contador de Visualizações
```redis
INCR page:views:home
EXPIRE page:views:home 86400
```

### 3. Leaderboard
```redis
ZADD leaderboard 1000 "player1" 950 "player2"
ZREVRANGE leaderboard 0 9 WITHSCORES
```

### 4. Rate Limiting
```redis
INCR rate_limit:user:123
EXPIRE rate_limit:user:123 60
```

## 🎯 Scripts de Exemplo

### E-commerce
- Catálogo de produtos (JSON)
- Carrinho de compras (Hash)
- Recomendações (Sets)
- Histórico de compras (TimeSeries)

### Redes Sociais
- Posts e comentários (JSON)
- Seguidores (Sets)
- Timeline (Lists)
- Grafos de relacionamentos (Graph)

### Monitoramento
- Métricas de sistema (TimeSeries)
- Logs de aplicação (Lists)
- Alertas (Pub/Sub)
- Dashboards (Search)

## 🔍 Comandos Úteis

### Informações do servidor
```redis
INFO
CLIENT LIST
MEMORY USAGE chave
```

### Análise de dados
```redis
KEYS *
TYPE chave
TTL chave
```

### Limpeza
```redis
FLUSHDB
FLUSHALL
DEL chave
```

## 📈 Performance e Boas Práticas

### 1. Use pipelines para operações em lote
```redis
MULTI
SET key1 value1
SET key2 value2
EXEC
```

### 2. Configure TTL apropriado
```redis
SETEX cache:data 300 "value"
```

### 3. Use estruturas de dados adequadas
- Strings: valores simples
- Hashes: objetos com campos
- Lists: filas e stacks
- Sets: relacionamentos únicos
- Sorted Sets: rankings e scores

### 4. Monitore memória
```redis
INFO memory
MEMORY USAGE chave
```

## 🛠️ Troubleshooting

### Problemas comuns:

1. **Out of memory**: Ajuste `maxmemory` e política de eviction
2. **Conexões**: Verifique `maxclients` e timeouts
3. **Persistência**: Configure `save` ou `appendonly`
4. **Performance**: Use `SLOWLOG` para identificar gargalos

### Comandos de diagnóstico:
```redis
SLOWLOG GET 10
INFO clients
CONFIG GET maxmemory
```

## 📚 Recursos Adicionais

- [Documentação oficial Redis](https://redis.io/docs/)
- [Redis University](https://university.redis.com/)
- [Redis Labs Academy](https://academy.redislabs.com/)
- [Redis Modules](https://redis.io/modules/)

## 🎉 Próximos Passos

1. Explore os scripts de exemplo
2. Experimente com diferentes estruturas de dados
3. Teste os módulos avançados
4. Crie seus próprios casos de uso
5. Monitore performance com RedisInsight

---

**Dica**: Use `redis-cli --help` para ver todos os comandos disponíveis e `redis-cli --latency` para monitorar latência em tempo real!

# Redis Cache Demo - Python API 🚀

Este projeto demonstra a diferença de performance entre requisições com cache Redis vs requisições diretas à API.

## 🏗️ Arquitetura

- **FastAPI**: Framework web moderno e rápido
- **Redis**: Cache em memória para armazenar respostas da API
- **JSONPlaceholder**: API externa para testes (posts, usuários, comentários, etc.)

## 🚀 Como usar

### 1. Instalar dependências

```bash
cd redis/python-cache-demo
pip install -r requirements.txt
```

### 2. Iniciar o Redis (se não estiver rodando)

```bash
# Na pasta redis/
docker-compose up -d
```

### 3. Executar a API

```bash
python app.py
```

A API estará disponível em: http://localhost:8000

### 4. Documentação interativa

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📊 Endpoints Disponíveis

### Dados da API Externa
- `GET /posts/{post_id}` - Buscar post por ID
- `GET /users/{user_id}` - Buscar usuário por ID  
- `GET /comments/{comment_id}` - Buscar comentário por ID
- `GET /albums/{album_id}` - Buscar álbum por ID
- `GET /todos/{todo_id}` - Buscar tarefa por ID

### Parâmetros de Cache
Todos os endpoints aceitam o parâmetro `use_cache`:
- `use_cache=true` (padrão): Usa cache Redis
- `use_cache=false`: Requisição direta à API

### Gerenciamento de Cache
- `GET /cache/stats` - Estatísticas do Redis
- `DELETE /cache/clear` - Limpar todo o cache
- `DELETE /cache/clear/{pattern}` - Limpar cache por padrão

## 🧪 Testando Performance

### 1. Teste com Cache (Primeira requisição)
```bash
GET http://localhost:8000/posts/1?use_cache=true
```
**Resultado esperado**: `"source": "api"`, tempo de resposta ~200-500ms

### 2. Teste com Cache (Segunda requisição)
```bash
GET http://localhost:8000/posts/1?use_cache=true
```
**Resultado esperado**: `"source": "cache"`, tempo de resposta ~1-5ms

### 3. Teste sem Cache
```bash
GET http://localhost:8000/posts/1?use_cache=false
```
**Resultado esperado**: `"source": "api"`, tempo de resposta ~200-500ms

## 📈 Exemplo de Resposta

```json
{
  "data": {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  "source": "cache",
  "cached": true,
  "response_time_ms": 2.45,
  "timestamp": 1694567890.123
}
```

## 🔧 Configurações

### Redis
- **Host**: localhost
- **Port**: 6379
- **TTL**: 300 segundos (5 minutos)

### API Externa
- **Base URL**: https://jsonplaceholder.typicode.com
- **Timeout**: 10 segundos

## 📊 Monitoramento

### Estatísticas do Cache
```bash
GET http://localhost:8000/cache/stats
```

Retorna:
- Número de clientes conectados
- Uso de memória
- Hits/misses do cache
- Chaves armazenadas

### Limpar Cache
```bash
# Limpar tudo
DELETE http://localhost:8000/cache/clear

# Limpar apenas posts
DELETE http://localhost:8000/cache/clear/post
```

## 🎯 Casos de Teste Sugeridos

### 1. Teste de Performance Básico
1. Faça 10 requisições para `/posts/1?use_cache=true`
2. Compare os tempos de resposta
3. Observe que a primeira é mais lenta (API) e as demais são rápidas (cache)

### 2. Teste de TTL (Time To Live)
1. Faça uma requisição para cachear dados
2. Aguarde 5 minutos
3. Faça a mesma requisição - deve buscar da API novamente

### 3. Teste de Diferentes Tipos de Dados
1. Teste com posts, usuários, comentários
2. Compare performance entre diferentes tamanhos de dados

### 4. Teste de Concorrência
1. Faça múltiplas requisições simultâneas
2. Observe como o cache melhora a performance

## 🛠️ Troubleshooting

### Erro de Conexão com Redis
```
Erro ao buscar do cache: Error 111 connecting to localhost:6379
```
**Solução**: Verifique se o Redis está rodando (`docker-compose up -d`)

### Erro de Timeout da API
```
Erro na API externa: Read timed out
```
**Solução**: Verifique sua conexão com a internet

### Cache não está funcionando
1. Verifique as estatísticas: `GET /cache/stats`
2. Verifique se o Redis está conectado
3. Teste limpar e recriar o cache

## 📚 Próximos Passos

1. **Implementar cache distribuído** com múltiplas instâncias
2. **Adicionar métricas** de performance (Prometheus/Grafana)
3. **Implementar invalidação** de cache baseada em eventos
4. **Adicionar compressão** para dados grandes
5. **Implementar cache warming** (pré-carregamento)

## 🔗 Recursos Adicionais

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Redis Python Client](https://redis-py.readthedocs.io/)
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)
- [Redis Caching Patterns](https://redis.io/docs/manual/patterns/distributed-locks/)

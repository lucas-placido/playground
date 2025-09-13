from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import redis
import requests
import time
import json
from typing import Optional
import os

# Configuração do Redis
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

# Configuração da API externa (JSONPlaceholder para testes)
API_BASE_URL = "https://jsonplaceholder.typicode.com"

app = FastAPI(
    title="Redis Cache Demo API",
    description="API para demonstrar cache com Redis vs requisições diretas",
    version="1.0.0",
)


def get_from_cache(key: str) -> Optional[dict]:
    """Busca dados do cache Redis"""
    try:
        cached_data = redis_client.get(key)
        if cached_data:
            return json.loads(cached_data)
        return None
    except Exception as e:
        print(f"Erro ao buscar do cache: {e}")
        return None


def save_to_cache(key: str, data: dict, ttl: int = 300) -> bool:
    """Salva dados no cache Redis com TTL"""
    try:
        redis_client.setex(key, ttl, json.dumps(data))
        return True
    except Exception as e:
        print(f"Erro ao salvar no cache: {e}")
        return False


def make_api_request(endpoint: str) -> dict:
    """Faz requisição para a API externa"""
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro na API externa: {str(e)}")


@app.get("/")
async def root():
    """Endpoint raiz com informações da API"""
    return {
        "message": "Redis Cache Demo API",
        "endpoints": {
            "posts": "/posts/{post_id}",
            "users": "/users/{user_id}",
            "comments": "/comments/{comment_id}",
            "albums": "/albums/{album_id}",
            "todos": "/todos/{todo_id}",
        },
        "cache_info": {"enabled": True, "ttl": "300 segundos (5 minutos)"},
    }


@app.get("/posts/{post_id}")
async def get_post(post_id: int, use_cache: bool = True):
    """
    Busca um post por ID
    - use_cache=true: Usa cache Redis (padrão)
    - use_cache=false: Requisição direta à API
    """
    cache_key = f"post:{post_id}"

    if use_cache:
        # Tentar buscar do cache primeiro
        start_time = time.time()
        cached_data = get_from_cache(cache_key)
        cache_response_time = time.time() - start_time

        if cached_data:
            return {
                "data": cached_data,
                "source": "cache",
                "cached": True,
                "response_time_ms": round(cache_response_time * 1000, 2),
                "timestamp": time.time(),
            }

    # Fazer requisição à API
    start_time = time.time()
    try:
        api_data = make_api_request(f"/posts/{post_id}")
        response_time = time.time() - start_time

        # Salvar no cache se habilitado
        if use_cache:
            save_to_cache(cache_key, api_data, ttl=300)

        return {
            "data": api_data,
            "source": "api",
            "cached": False,
            "response_time_ms": round(response_time * 1000, 2),
            "timestamp": time.time(),
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")


@app.get("/users/{user_id}")
async def get_user(user_id: int, use_cache: bool = True):
    """Busca um usuário por ID"""
    cache_key = f"user:{user_id}"

    if use_cache:
        start_time = time.time()
        cached_data = get_from_cache(cache_key)
        cache_response_time = time.time() - start_time

        if cached_data:
            return {
                "data": cached_data,
                "source": "cache",
                "cached": True,
                "response_time_ms": round(cache_response_time * 1000, 2),
                "timestamp": time.time(),
            }

    start_time = time.time()
    try:
        api_data = make_api_request(f"/users/{user_id}")
        response_time = time.time() - start_time

        if use_cache:
            save_to_cache(cache_key, api_data, ttl=300)

        return {
            "data": api_data,
            "source": "api",
            "cached": False,
            "response_time_ms": round(response_time * 1000, 2),
            "timestamp": time.time(),
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")


@app.get("/comments/{comment_id}")
async def get_comment(comment_id: int, use_cache: bool = True):
    """Busca um comentário por ID"""
    cache_key = f"comment:{comment_id}"

    if use_cache:
        start_time = time.time()
        cached_data = get_from_cache(cache_key)
        cache_response_time = time.time() - start_time

        if cached_data:
            return {
                "data": cached_data,
                "source": "cache",
                "cached": True,
                "response_time_ms": round(cache_response_time * 1000, 2),
                "timestamp": time.time(),
            }

    start_time = time.time()
    try:
        api_data = make_api_request(f"/comments/{comment_id}")
        response_time = time.time() - start_time

        if use_cache:
            save_to_cache(cache_key, api_data, ttl=300)

        return {
            "data": api_data,
            "source": "api",
            "cached": False,
            "response_time_ms": round(response_time * 1000, 2),
            "timestamp": time.time(),
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")


@app.get("/albums/{album_id}")
async def get_album(album_id: int, use_cache: bool = True):
    """Busca um álbum por ID"""
    cache_key = f"album:{album_id}"

    if use_cache:
        start_time = time.time()
        cached_data = get_from_cache(cache_key)
        cache_response_time = time.time() - start_time

        if cached_data:
            return {
                "data": cached_data,
                "source": "cache",
                "cached": True,
                "response_time_ms": round(cache_response_time * 1000, 2),
                "timestamp": time.time(),
            }

    start_time = time.time()
    try:
        api_data = make_api_request(f"/albums/{album_id}")
        response_time = time.time() - start_time

        if use_cache:
            save_to_cache(cache_key, api_data, ttl=300)

        return {
            "data": api_data,
            "source": "api",
            "cached": False,
            "response_time_ms": round(response_time * 1000, 2),
            "timestamp": time.time(),
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")


@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int, use_cache: bool = True):
    """Busca uma tarefa por ID"""
    cache_key = f"todo:{todo_id}"

    if use_cache:
        start_time = time.time()
        cached_data = get_from_cache(cache_key)
        cache_response_time = time.time() - start_time

        if cached_data:
            return {
                "data": cached_data,
                "source": "cache",
                "cached": True,
                "response_time_ms": round(cache_response_time * 1000, 2),
                "timestamp": time.time(),
            }

    start_time = time.time()
    try:
        api_data = make_api_request(f"/todos/{todo_id}")
        response_time = time.time() - start_time

        if use_cache:
            save_to_cache(cache_key, api_data, ttl=300)

        return {
            "data": api_data,
            "source": "api",
            "cached": False,
            "response_time_ms": round(response_time * 1000, 2),
            "timestamp": time.time(),
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")


@app.get("/cache/stats")
async def get_cache_stats():
    """Retorna estatísticas do cache Redis"""
    try:
        info = redis_client.info()
        return {
            "redis_info": {
                "connected_clients": info.get("connected_clients", 0),
                "used_memory_human": info.get("used_memory_human", "N/A"),
                "keyspace_hits": info.get("keyspace_hits", 0),
                "keyspace_misses": info.get("keyspace_misses", 0),
                "total_commands_processed": info.get("total_commands_processed", 0),
            },
            "cache_keys": redis_client.keys("post:*")
            + redis_client.keys("user:*")
            + redis_client.keys("comment:*")
            + redis_client.keys("album:*")
            + redis_client.keys("todo:*"),
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao obter estatísticas: {str(e)}"
        )


@app.delete("/cache/clear")
async def clear_cache():
    """Limpa todo o cache"""
    try:
        redis_client.flushdb()
        return {"message": "Cache limpo com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao limpar cache: {str(e)}")


@app.delete("/cache/clear/{key_pattern}")
async def clear_cache_pattern(key_pattern: str):
    """Limpa cache por padrão de chave"""
    try:
        keys = redis_client.keys(f"{key_pattern}:*")
        if keys:
            redis_client.delete(*keys)
            return {
                "message": f"Cache limpo para padrão '{key_pattern}': {len(keys)} chaves removidas"
            }
        return {"message": f"Nenhuma chave encontrada para padrão '{key_pattern}'"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao limpar cache: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

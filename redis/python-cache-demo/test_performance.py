#!/usr/bin/env python3
"""
Script para testar performance do cache Redis vs API direta
Execute: python test_performance.py
"""

import requests
import time
import statistics
from typing import List, Dict
import json

API_BASE_URL = "http://localhost:8000"


def make_request(endpoint: str, use_cache: bool = True) -> Dict:
    """Faz requisição para a API local"""
    url = f"{API_BASE_URL}{endpoint}"
    params = {"use_cache": use_cache}

    start_time = time.time()
    response = requests.get(url, params=params)
    end_time = time.time()

    if response.status_code == 200:
        data = response.json()
        # Usar o tempo interno da API (mais preciso) em vez do tempo total da requisição HTTP
        internal_time = data.get("response_time_ms", 0)
        return {
            "success": True,
            "response_time_ms": internal_time,  # Tempo interno da API
            "http_time_ms": round(
                (end_time - start_time) * 1000, 2
            ),  # Tempo total HTTP
            "source": data.get("source", "unknown"),
            "cached": data.get("cached", False),
        }
    else:
        return {
            "success": False,
            "error": f"HTTP {response.status_code}",
            "response_time_ms": round((end_time - start_time) * 1000, 2),
        }


def run_performance_test(endpoint: str, iterations: int = 10) -> Dict:
    """Executa teste de performance para um endpoint"""
    print(f"\n🧪 Testando {endpoint}")
    print("=" * 50)

    # Limpar cache primeiro
    requests.delete(f"{API_BASE_URL}/cache/clear")

    # Teste 1: Primeira requisição (sem cache)
    print("1️⃣ Primeira requisição (API externa)...")
    result1 = make_request(endpoint, use_cache=True)
    if result1["success"]:
        print(f"   ✅ Sucesso - Fonte: {result1['source']}")
        print(f"   ⏱️  Tempo interno: {result1['response_time_ms']}ms")
        print(f"   🌐 Tempo HTTP total: {result1['http_time_ms']}ms")
    else:
        print(f"   ❌ Erro: {result1['error']}")
        return None

    # Teste 2: Requisições com cache
    print(f"\n2️⃣ {iterations} requisições com cache...")
    cache_times = []
    for i in range(iterations):
        result = make_request(endpoint, use_cache=True)
        if result["success"]:
            cache_times.append(result["response_time_ms"])
            print(
                f"   {i+1:2d}. {result['response_time_ms']:6.2f}ms (HTTP: {result['http_time_ms']:6.2f}ms) - {result['source']}"
            )
        else:
            print(f"   {i+1:2d}. ERRO: {result['error']}")

    # Teste 3: Requisições sem cache
    print(f"\n3️⃣ {iterations} requisições sem cache...")
    no_cache_times = []
    for i in range(iterations):
        result = make_request(endpoint, use_cache=False)
        if result["success"]:
            no_cache_times.append(result["response_time_ms"])
            print(
                f"   {i+1:2d}. {result['response_time_ms']:6.2f}ms (HTTP: {result['http_time_ms']:6.2f}ms) - {result['source']}"
            )
        else:
            print(f"   {i+1:2d}. ERRO: {result['error']}")

    # Estatísticas
    if cache_times and no_cache_times:
        cache_avg = statistics.mean(cache_times)
        cache_min = min(cache_times)
        cache_max = max(cache_times)

        no_cache_avg = statistics.mean(no_cache_times)
        no_cache_min = min(no_cache_times)
        no_cache_max = max(no_cache_times)

        improvement = ((no_cache_avg - cache_avg) / no_cache_avg) * 100

        print(f"\n📊 ESTATÍSTICAS (Tempo Interno da API):")
        print(f"   Cache Redis:")
        print(f"     Média: {cache_avg:.2f}ms")
        print(f"     Min:   {cache_min:.2f}ms")
        print(f"     Max:   {cache_max:.2f}ms")
        print(f"   API Direta:")
        print(f"     Média: {no_cache_avg:.2f}ms")
        print(f"     Min:   {no_cache_min:.2f}ms")
        print(f"     Max:   {no_cache_max:.2f}ms")
        print(f"   🚀 Melhoria: {improvement:.1f}% mais rápido com cache")

        return {
            "endpoint": endpoint,
            "cache_avg": cache_avg,
            "no_cache_avg": no_cache_avg,
            "improvement": improvement,
            "cache_times": cache_times,
            "no_cache_times": no_cache_times,
        }

    return None


def get_cache_stats():
    """Obtém estatísticas do cache"""
    try:
        response = requests.get(f"{API_BASE_URL}/cache/stats")
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None


def main():
    """Função principal"""
    print("🚀 REDIS CACHE PERFORMANCE TEST")
    print("=" * 60)

    # Verificar se a API está rodando
    try:
        response = requests.get(f"{API_BASE_URL}/", timeout=5)
        if response.status_code != 200:
            print("❌ API não está respondendo. Execute: python app.py")
            return
    except:
        print("❌ Não foi possível conectar à API. Execute: python app.py")
        return

    print("✅ API conectada com sucesso!")

    # Estatísticas iniciais
    stats = get_cache_stats()
    if stats:
        print(f"\n📊 Estatísticas iniciais do Redis:")
        print(f"   Clientes conectados: {stats['redis_info']['connected_clients']}")
        print(f"   Memória usada: {stats['redis_info']['used_memory_human']}")
        print(f"   Chaves no cache: {len(stats['cache_keys'])}")

    # Endpoints para testar
    endpoints = ["/posts/1", "/users/1", "/comments/1", "/albums/1", "/todos/1"]

    results = []

    # Executar testes
    for endpoint in endpoints:
        result = run_performance_test(endpoint, iterations=5)
        if result:
            results.append(result)

    # Resumo final
    if results:
        print(f"\n🏆 RESUMO FINAL")
        print("=" * 60)

        total_improvement = 0
        for result in results:
            print(
                f"{result['endpoint']:15} - {result['improvement']:6.1f}% mais rápido"
            )
            total_improvement += result["improvement"]

        avg_improvement = total_improvement / len(results)
        print(f"{'MÉDIA':15} - {avg_improvement:6.1f}% mais rápido")

        # Estatísticas finais
        stats = get_cache_stats()
        if stats:
            print(f"\n📊 Estatísticas finais do Redis:")
            print(f"   Hits: {stats['redis_info']['keyspace_hits']}")
            print(f"   Misses: {stats['redis_info']['keyspace_misses']}")
            print(f"   Chaves no cache: {len(stats['cache_keys'])}")

    print(f"\n✅ Teste concluído!")


if __name__ == "__main__":
    main()

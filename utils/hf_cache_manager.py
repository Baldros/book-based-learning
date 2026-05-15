#!/usr/bin/env python3
"""
Gerenciador de Cache do Hugging Face (Resiliente)
- Detecção automática de cache e atributos (repos vs repo_folders)
- Suporte a múltiplas versões da biblioteca huggingface_hub
- Lista modelos com detalhes e remove com segurança
Requer: pip install huggingface_hub
"""

import os
import shutil
from pathlib import Path
from huggingface_hub import scan_cache_dir
from typing import Optional, Any, List

def get_attr(obj: Any, possibilities: List[str], default: Any = None) -> Any:
    """Tenta obter o primeiro atributo disponível de uma lista de possibilidades."""
    for attr in possibilities:
        if hasattr(obj, attr):
            return getattr(obj, attr)
    return default

def get_cache_dir() -> Optional[str]:
    """Tenta localizar o diretório de cache baseado em variáveis de ambiente ou padrão."""
    env_vars = ['HF_HOME', 'HUGGINGFACE_HUB_CACHE', 'TRANSFORMERS_CACHE']
    for var in env_vars:
        path = os.environ.get(var)
        if path:
            return path
    
    default_win = Path.home() / ".cache" / "huggingface" / "hub"
    if default_win.exists():
        return str(default_win)
    
    return None

def list_models(cache_dir: Optional[str] = None, detailed: bool = False):
    """
    Lista todos os modelos no cache HF com descoberta dinâmica de atributos.
    """
    try:
        cache_info = scan_cache_dir(cache_dir=cache_dir)
    except Exception as e:
        print(f"❌ Erro ao escanear cache: {e}")
        return

    # Info do cache (Resiliente)
    actual_cache_path = get_attr(cache_info, ['cache_dir', 'cache_path'], cache_dir or "Hugging Face Default")
    repos_list = get_attr(cache_info, ['repos', 'repo_folders'], [])
    total_size = get_attr(cache_info, ['size_on_disk_str'], f"{getattr(cache_info, 'size_on_disk', 0) / (1024**3):.2f} GB")

    print(f"\n📁 Cache HF: {actual_cache_path}")
    print(f"📊 Total de repos: {len(repos_list)}")
    print(f"💾 Tamanho total estimado: {total_size}")
    print("-" * 50)
    
    # Ordenar repositórios
    try:
        sorted_repos = sorted(repos_list, key=lambda x: x.repo_id)
    except:
        sorted_repos = repos_list

    for repo in sorted_repos:
        repo_id = getattr(repo, 'repo_id', 'Unknown')
        repo_type = getattr(repo, 'repo_type', 'model')
        repo_path = get_attr(repo, ['repo_path', 'repo_folder'], "N/A")
        size = get_attr(repo, ['size_on_disk_str'], f"{getattr(repo, 'size_on_disk', 0) / (1024**2):.1f} MB")
        
        print(f"📦 [{repo_type}] {repo_id}")
        print(f"   Tamanho: {size}")
        print(f"   Pasta: {repo_path}")
        
        if detailed:
            snapshots = getattr(repo, 'snapshots', getattr(repo, 'revisions', []))
            if snapshots:
                print("   Snapshots:")
                for snapshot in snapshots:
                    rev = getattr(snapshot, 'revision', 'N/A')
                    s_dir = get_attr(snapshot, ['snapshot_dir', 'snapshot_path'], "N/A")
                    print(f"     - 🆔 {rev[:8]}... (Hash completo: {rev})")
                    print(f"       📍 {s_dir}")
                    try:
                        files = list(Path(s_dir).glob('*'))
                        if files:
                            print(f"       📄 Arquivos: {', '.join([f.name for f in files[:5]])}{'...' if len(files) > 5 else ''}")
                    except:
                        pass
        print()

def delete_model(repo_id: str, cache_dir: Optional[str] = None):
    """
    Deleta o modelo pelo repo_id.
    """
    cache_info = scan_cache_dir(cache_dir=cache_dir)
    repos_list = get_attr(cache_info, ['repos', 'repo_folders'], [])
    found_repos = [r for r in repos_list if getattr(r, 'repo_id', None) == repo_id]
    
    if not found_repos:
        print(f"❌ Modelo '{repo_id}' não encontrado.")
        return

    for repo in found_repos:
        repo_path = get_attr(repo, ['repo_path', 'repo_folder'])
        size = get_attr(repo, ['size_on_disk_str'], f"{getattr(repo, 'size_on_disk', 0) / (1024**2):.1f} MB")
        
        print(f"\n⚠️  Preparando para deletar: {repo_id}")
        print(f"   Local: {repo_path}")
        print(f"   Tamanho: {size}")
        
        confirm = input(f"Tem certeza que deseja deletar? [s/N]: ")
        if confirm.lower() == 's' and repo_path:
            try:
                shutil.rmtree(repo_path)
                print(f"✅ Sucesso: {repo_id} removido.")
            except Exception as e:
                print(f"❌ Erro ao deletar: {e}")
        else:
            print("🚫 Operação cancelada.")

def main():
    current_cache = get_cache_dir()
    
    while True:
        print("\n" + "="*35)
        print(" HF CACHE MANAGER (Super Resiliente) ")
        print("="*35)
        print(f"Diretório atual: {current_cache or 'Padrão library'}")
        print("-" * 35)
        print("1. Listar modelos (Resumo)")
        print("2. Listar modelos (Detalhado)")
        print("3. Deletar modelo")
        print("4. Alterar diretório de cache")
        print("0. Sair")
        
        choice = input("\nEscolha: ")
        
        if choice == '1':
            list_models(cache_dir=current_cache)
        elif choice == '2':
            list_models(cache_dir=current_cache, detailed=True)
        elif choice == '3':
            repo_id = input("Digite o Repo ID (ex: bert-base-uncased): ")
            delete_model(repo_id, cache_dir=current_cache)
        elif choice == '4':
            new_path = input("Digite o novo caminho do cache: ")
            if os.path.isdir(new_path):
                current_cache = new_path
                print(f"✅ Alterado para: {current_cache}")
            else:
                print("❌ Caminho inválido.")
        elif choice in ('0', 's'):
            print("Encerrando...")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()

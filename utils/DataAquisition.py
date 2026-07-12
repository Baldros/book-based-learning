"""
# Apresentação:

O objetivo aqui é construir um processo de aquisição de dados para o estudo de
Processamento de Linguagem Natural. O script baixa dados a partir de uma URL e,
avaliando pela extensão do arquivo, decide se o conteúdo é:

* texto puro (ex.: https://www.gutenberg.org/cache/epub/5200/pg5200.txt) — nesse
  caso o arquivo é apenas salvo na pasta destino;
* um arquivo compactado (ex.: .tar.gz, .zip, .gz ...) — nesse caso o conteúdo é
  descompactado e colocado na pasta destino.

Uso via linha de comando:

    python DataAquisition.py -u <url> -o <pasta_destino>

Exemplos:

    python DataAquisition.py -u https://www.gutenberg.org/cache/epub/5200/pg5200.txt -o data
    python DataAquisition.py -u http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz -o data

## Links úteis:
* requests: https://requests.readthedocs.io/en/latest/
* Documentação (BeautifulSoup): https://beautiful-soup-4.readthedocs.io/en/latest/
* Vídeo (Let's Data): https://www.youtube.com/watch?v=aNtzKGTujuA
"""

from __future__ import annotations

# Importações:
import argparse
import bz2
import gzip
import lzma
import shutil
import sys
import tarfile
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests

# Extensões reconhecidas como arquivos tar (possivelmente comprimidos).
_TAR_SUFFIXES = (
    ".tar",
    ".tar.gz", ".tgz",
    ".tar.bz2", ".tbz", ".tbz2",
    ".tar.xz", ".txz",
)

# Extensões de compressão de um único arquivo (não são coleções como tar/zip).
_SINGLE_COMPRESS = {
    ".gz": gzip,
    ".bz2": bz2,
    ".xz": lzma,
}

# User-Agent para evitar bloqueios de servidores (ex.: Project Gutenberg).
_HEADERS = {"User-Agent": "Mozilla/5.0 (DataAquisition; +https://github.com/Baldros/book-based-learning)"}


def filename_from_url(url: str) -> str:
    """Extrai o nome do arquivo a partir de uma URL (ignorando a query string)."""
    path = urlparse(url).path
    name = Path(unquote(path)).name
    return name or "download"


def is_archive(url_or_name: str) -> bool:
    """Retorna True se o nome/URL indica um arquivo compactado, pela extensão."""
    name = filename_from_url(url_or_name).lower()
    if name.endswith(_TAR_SUFFIXES) or name.endswith(".zip"):
        return True
    return any(name.endswith(ext) for ext in _SINGLE_COMPRESS)


def download(url: str, dest_path: Path, *, timeout: int = 30, chunk_size: int = 8192) -> Path:
    """
    Baixa o conteúdo de uma URL para ``dest_path`` (streaming, adequado a
    arquivos grandes).

    Parâmetros:
    url (str): URL de origem.
    dest_path (Path): caminho do arquivo de destino.
    timeout (int): tempo limite da requisição, em segundos.
    chunk_size (int): tamanho do bloco de leitura, em bytes.

    Retorna:
    Path: o caminho do arquivo salvo.
    """
    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=timeout, headers=_HEADERS) as resp:
        resp.raise_for_status()
        with open(dest_path, "wb") as arq:
            for chunk in resp.iter_content(chunk_size=chunk_size):
                if chunk:
                    arq.write(chunk)
    return dest_path


def _is_within(directory: Path, target: Path) -> bool:
    """Garante que ``target`` está contido em ``directory`` (evita path traversal)."""
    directory = Path(directory).resolve()
    target = Path(target).resolve()
    return directory == target or directory in target.parents


def _extract_tar(archive_path: Path, dest_dir: Path) -> list[Path]:
    with tarfile.open(archive_path) as tar:
        for member in tar.getmembers():
            if not _is_within(dest_dir, dest_dir / member.name):
                raise ValueError(f"Membro inseguro no tar: {member.name!r}")
        try:
            # Python >= 3.12: filtro de segurança na extração.
            tar.extractall(dest_dir, filter="data")
        except TypeError:
            tar.extractall(dest_dir)
        return [dest_dir / m.name for m in tar.getmembers() if m.isfile()]


def _extract_zip(archive_path: Path, dest_dir: Path) -> list[Path]:
    with zipfile.ZipFile(archive_path) as zf:
        for member in zf.namelist():
            if not _is_within(dest_dir, dest_dir / member):
                raise ValueError(f"Membro inseguro no zip: {member!r}")
        zf.extractall(dest_dir)
        return [dest_dir / m for m in zf.namelist() if not m.endswith("/")]


def _decompress_single(archive_path: Path, dest_dir: Path, module, ext: str) -> list[Path]:
    out_path = dest_dir / archive_path.name[: -len(ext)]
    with module.open(archive_path, "rb") as src, open(out_path, "wb") as dst:
        shutil.copyfileobj(src, dst)
    return [out_path]


def extract_archive(archive_path: Path, dest_dir: Path) -> list[Path]:
    """
    Descompacta ``archive_path`` em ``dest_dir``, escolhendo o formato pela
    extensão. Suporta .zip, tar (.tar/.tar.gz/.tgz/.tar.bz2/.tar.xz) e
    compressão de arquivo único (.gz/.bz2/.xz).

    Retorna:
    list[Path]: caminhos dos arquivos extraídos.
    """
    archive_path = Path(archive_path)
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    name = archive_path.name.lower()

    if name.endswith(".zip"):
        return _extract_zip(archive_path, dest_dir)
    if name.endswith(_TAR_SUFFIXES):
        return _extract_tar(archive_path, dest_dir)
    for ext, module in _SINGLE_COMPRESS.items():
        if name.endswith(ext):
            return _decompress_single(archive_path, dest_dir, module, ext)

    raise ValueError(f"Formato de arquivo não suportado: {archive_path.name!r}")


def acquire(
    url: str,
    dest_dir: str | Path = "data",
    *,
    file_name: str | None = None,
    keep_archive: bool = False,
    timeout: int = 30,
) -> list[Path]:
    """
    Aquisita os dados de ``url`` para ``dest_dir``.

    Se a URL apontar para um arquivo compactado, ele é baixado e descompactado
    na pasta destino; caso contrário, o arquivo (texto puro) é apenas salvo.

    Parâmetros:
    url (str): URL de origem.
    dest_dir (str | Path): pasta destino (criada se não existir).
    file_name (str | None): nome do arquivo baixado. Se None, usa o nome
        derivado da URL.
    keep_archive (bool): se True, mantém o arquivo compactado após extrair.
    timeout (int): tempo limite da requisição, em segundos.

    Retorna:
    list[Path]: caminhos dos arquivos resultantes na pasta destino.
    """
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    name = file_name or filename_from_url(url)

    if is_archive(url):
        archive_path = download(url, dest_dir / name, timeout=timeout)
        try:
            extracted = extract_archive(archive_path, dest_dir)
        finally:
            if not keep_archive and archive_path.exists():
                archive_path.unlink()
        return extracted

    target = download(url, dest_dir / name, timeout=timeout)
    return [target]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Aquisita dados de uma URL (texto puro ou arquivo compactado)."
    )

    parser.add_argument(
        "-u",
        "--url",
        required=True,
        help="URL de origem dos dados.",
    )

    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Pasta destino onde os dados serão salvos/descompactados.",
    )

    parser.add_argument(
        "-n",
        "--file-name",
        default=None,
        help="Nome do arquivo baixado (opcional; padrão: derivado da URL).",
    )

    parser.add_argument(
        "--keep-archive",
        action="store_true",
        help="Mantém o arquivo compactado após a extração.",
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Tempo limite da requisição, em segundos (padrão: 30).",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        results = acquire(
            url=args.url,
            dest_dir=args.output,
            file_name=args.file_name,
            keep_archive=args.keep_archive,
            timeout=args.timeout,
        )
    except Exception as e:  # noqa: BLE001 - reporta qualquer falha ao usuário
        print(f"Erro ao aquisitar {args.url}: {e}", file=sys.stderr)
        return 1

    print(f"{len(results)} arquivo(s) salvo(s) em: {args.output}")
    for path in results:
        print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

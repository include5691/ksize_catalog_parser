import logging
import pathlib
from urllib.parse import urlparse
from .categories import get_subcategories_urls
from .products import get_products
from .write import write_products_csv

def _get_dir_path(url: str) -> pathlib.Path:
    parsed_url = urlparse(url)
    dir_path = pathlib.Path(__file__).parent.parent / "csv_files" / parsed_url.path.split("-")[-1]

def parse_caregory(url: str):
    subcategories = get_subcategories_urls(url)
    if not subcategories:
        logging.error(f"Subcategories not found for url {url}")
        return None
    for subcategory in subcategories:
        dir_path = _get_dir_path(subcategory)
        if not dir_path.exists():
            parse_subcategory(subcategory)

def parse_subcategory(url: str, categories_path: str | None = None):
    products = get_products(url, categories_path)
    if not products:
        logging.error(f"Products not found for url {url}")
        return None
    dir_path = _get_dir_path(url)
    if not dir_path.exists():
        dir_path.mkdir(parents=True)
    for n in range(len(products) // 15 + 1):
        write_products_csv(products[n*15:(n+1)*15], file_name=str(dir_path) + f"{dir_path.name}_{n}.csv")
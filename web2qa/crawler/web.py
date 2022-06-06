from haystack.connector import Crawler
from haystack import Document
from typing import List
import tempfile
import shutil
import json


def crawl_pages(pages: List[str], filters: List[str] = []) -> List[Document]:
    """
    Crawls the pages and returns the crawled pages as Documents.
    """
    # Create temporary directory
    dirpath = tempfile.mkdtemp()
    # Crawl pages
    crawler = Crawler(output_dir=dirpath)

    docs = crawler.crawl(urls=pages,
                         filter_urls=filters)
    
    # Read json files in tempdir
    docs = [json.loads(open(f).read()) for f in docs if f.absolute().as_posix().endswith('.json')]

    # Remove temporary directory
    shutil.rmtree(dirpath)

    # Convert to Document
    docs = [Document(**doc) for doc in docs]

    return docs

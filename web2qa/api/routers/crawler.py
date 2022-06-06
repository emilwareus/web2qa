from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from web2qa.crawler.web import crawl_pages


router = APIRouter(
    prefix="/crawler",
    tags=["crawler"],
    responses={404: {"description": "Not found"}},
)


class Page(BaseModel):
    urls: List[str]
    crawl_depth: Optional[int]
    max_links: Optional[int]
    filter_urls: Optional[List[str]]


class Pages(BaseModel):
    pages: List[Page]


@router.post("/index-pages")
async def index_pages(pages: Pages):
    docs_out = []
    for page in pages.pages:
        docs = crawl_pages(
            pages=page.url,
            filters=page.filter_urls,
        )
        docs_out.extend(docs)
    return docs_out

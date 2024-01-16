from typing import List, Optional, Dict, Any, Union, Literal

from ._base import BaseModel


class GenerateOpenEndedTextResult(BaseModel):
    id: str
    data: str


class GenerateSummarizeChapterResult(BaseModel):
    chapter_number: int
    start: int
    end: int
    chapter_title: str
    chapter_summary: str


class GenerateSummarizeHighlightResult(BaseModel):
    start: int
    end: int
    highlight: str


class GenerateSummarizeResult(BaseModel):
    id: str
    summary: Optional[str] = None
    chapters: Optional[List[GenerateSummarizeChapterResult]] = None
    highlights: Optional[List[GenerateSummarizeHighlightResult]] = None


class GenerateGistResult(BaseModel):
    id: str
    title: str
    topics: List[str]
    hashtags: List[str]

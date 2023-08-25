from dataclasses import dataclass
from typing import List

@dataclass
class Segment:
    id: int
    seek: int
    start: float
    end: float
    text: str
    tokens: List[int]
    temperature: float
    avg_logprob: float
    compression_ratio: float
    no_speech_prob: float

@dataclass
class TranscriptionResult:
    text: str
    segments: List[Segment]
    language: str

    @staticmethod
    def from_dict(data):
        segments = [Segment(**segment) for segment in data["segments"]]
        return TranscriptionResult(data["text"], segments, data["language"])
from dataclasses import dataclass
from typing import List

from core.domain.models.transcription import Transcription

@dataclass
class Conversation:
    transcriptions: List[Transcription]
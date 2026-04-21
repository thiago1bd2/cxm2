
from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Literal, Optional

import yaml
from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator

# Schemas do load_config

class AppConfig(BaseModel):
    name: str = Field(min(min_lenght=1))
    description: Optional[str] = None
    version: str = Field(min_length=2)
    mode: Literal['PROD','DRY_RUN','AUDIT_ONLY']
    timezone: Optional[str] = None

class Paths(BaseModel):
    source_root: str = Field(min_length=1)
    destination_root: str = Field(min_length=1)

    


import pathlib
from omegaconf import OmegaConf

PROJECT_DIR = pathlib.Path(__file__).parent
CONFIG = OmegaConf.load(PROJECT_DIR / "config.yaml")

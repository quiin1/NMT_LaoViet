from .default_loader import DefaultLoader
from .multilingual_loader import MultiLoader
from .preprocess_data import PreprocessData

loaders = {"monoloader": DefaultLoader, "multiloader": MultiLoader, "preprocessdata": PreprocessData}

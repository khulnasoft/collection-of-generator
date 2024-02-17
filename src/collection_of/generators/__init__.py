from typing import List, Optional

from collection_of import utils
from collection_of.generators import markdown_list
from src.collection_of.generators import collection_generator

AVAILABLE_GENERATORS: List[collection_generator.BaseGenerator] = [
    markdown_list.MarkdownListGenerator(),
]


def get_generator(name: str) -> Optional[collection_generator.BaseGenerator]:

    generator_dict = {
        utils.simplify_str(generator.name): generator
        for generator in AVAILABLE_GENERATORS
    }

    if utils.simplify_str(name) in generator_dict:
        return generator_dict[utils.simplify_str(name)]

    return None

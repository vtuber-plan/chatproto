from typing import Dict, List, Optional, Union

def apply_chat_template(
        messages: Union[List[Dict[str, str]], "Conversation"],
        chat_template: Optional[str],
        add_generation_prompt=True,
        tokenize=False,
        padding=False,
        truncation=False,
        max_length: Optional[int]=None,
        return_tensors: Optional[str]=None):
    pass

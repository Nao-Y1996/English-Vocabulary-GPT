from openai.types.chat import ChatCompletion

from english_vacablary_gpt.vocabulary_gpt import VocabularyGPT, VocabularyGPTResponse
from english_vacablary_gpt.vocabulary_parser import Vocabulary

if __name__ == '__main__':
    response: VocabularyGPTResponse = VocabularyGPT.create_vocabulary("extreme")
    print(response.get_prompt_tokens())
    print(response.get_completion_tokens())
    print(response.get_total_tokens())
    vocabulary: Vocabulary = response.get_vocabulary()
    markdown_output = vocabulary.to_markdown()
    with open("output.md", mode="w") as f:
        f.write(markdown_output)

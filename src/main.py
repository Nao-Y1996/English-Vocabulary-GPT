import sys

from english_vacablary_gpt.vocabulary_gpt import VocabularyGPT, VocabularyGPTResponse
from english_vacablary_gpt.vocabulary_parser import Vocabulary

if __name__ == '__main__':
    # 実行時の引数を受け取る
    word = sys.argv[1]

    response: VocabularyGPTResponse = VocabularyGPT.create_vocabulary(word)
    print(response.usage())
    vocabulary: Vocabulary = response.get_vocabulary()
    markdown_output = vocabulary.to_markdown()
    with open("output.md", mode="w") as f:
        f.write(markdown_output)

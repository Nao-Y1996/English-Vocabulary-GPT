import json


class EnJa:
    def __init__(self, en_ja: dict[str: str]) -> None:
        self.en: str = en_ja['en']
        self.ja: str = en_ja['ja']


class Meaning:
    def __init__(self, meaning: dict[str: str]) -> None:
        self.meaning = meaning['meaning']
        self.note = meaning['note']


class Explanation:
    def __init__(self, explanation: dict[str: str]) -> None:
        self.partOfSpeech = explanation['partOfSpeech']
        self.meaningsJa = [Meaning(meaning) for meaning in explanation['meaningsJa']]  # 意味のリスト
        self.sentences = [EnJa(sentence) for sentence in explanation['sentences']]  # 例文のリスト
        self.synonyms = [EnJa(synonyms) for synonyms in explanation['synonyms']]  # 類義語のリスト
        self.antonyms = [EnJa(antonyms) for antonyms in explanation['antonyms']]  # 対義語のリスト


class RelatedTerm:
    def __init__(self, related_term: dict[str: str]) -> None:
        self.en = related_term['en']
        self.ja = related_term['ja']


class Vocabulary:
    def __init__(self, json_str: str) -> None:
        data = json.loads(json_str)
        self.word: str = data['word']
        self.explanations: list[Explanation] = [Explanation(explanation) for explanation in data['explanations']]
        self.related_term: list[RelatedTerm] = [RelatedTerm(related_term) for related_term in data['related_term']]

    def to_markdown(self) -> str:
        markdown_output = f"# {self.word}\n"
        for explanation in self.explanations:
            part_of_speech = explanation.partOfSpeech
            markdown_output += f"## {part_of_speech.capitalize()}\n"
            for meaning in explanation.meaningsJa:
                markdown_output += f"- {meaning.meaning}"
                if meaning.note:
                    markdown_output += f"（{meaning.note}）"
                markdown_output += "\n"

            if explanation.sentences:
                markdown_output += "### 例文\n"
                for sentence in explanation.sentences:
                    markdown_output += f"- {sentence.en}（{sentence.ja}）\n"

            if explanation.synonyms:
                markdown_output += "### 類義語\n"
                for synonyms in explanation.synonyms:
                    markdown_output += f"- {synonyms.en}（{synonyms.ja}）\n"

            if explanation.antonyms:
                markdown_output += "### 対義語\n"
                for antonyms in explanation.antonyms:
                    markdown_output += f"- {antonyms.en}（{antonyms.ja}）\n"
        if self.related_term:
            markdown_output += "## 関連語\n"
            for related_term in self.related_term:
                markdown_output += f"- {related_term.en}（{related_term.ja}）\n"

        return markdown_output

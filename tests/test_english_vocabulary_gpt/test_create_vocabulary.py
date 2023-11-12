from english_vacablary_gpt.vocabulary_parser import Vocabulary

data = """
{
  "word": "major",
  "explanations": [
    {
      "partOfSpeech": "形容詞",
      "meaningsJa": [
        {"meaning":"主要な", "note": ""},
        {"meaning":"大きな", "note": ""},
        {"meaning":"重要な", "note": ""}],
      "sentences": [
        {"en": "He played a major role.", "ja": "彼は主要な役割を果たした" },
        { "en": "He is a major shareholder.", "ja": "彼は大株主だ" },
        { "en": "He has a major responsibility.","ja": "彼は大きな責任を負っている。" }
      ],
      "synonyms": [],
      "antonyms": [{  "en": "minor", "ja": "マイナーな"}]
    },
    {
      "partOfSpeech": "動詞",
      "meaningsJa": [{"meaning":"~を専攻する", "note": "major in ~ の形で使う"}],
      "sentences": [
        {"en": "I major in computer science.",  "ja": "私はコンピュータサイエンスを専攻している。" }
      ],
      "synonyms": [{"en": "specialize in", "ja": "専攻する"}],
      "antonyms": []
    }
  ],
  "related_term": [{"en": "majority", "ja": "大多数"}]
}
"""


def test_create_vocabulary():
    vocabulary: Vocabulary = Vocabulary(data)
    assert vocabulary.word == 'major'

    assert vocabulary.explanations[0].partOfSpeech == '形容詞'
    assert vocabulary.explanations[0].meaningsJa[0].meaning == '主要な'
    assert vocabulary.explanations[0].meaningsJa[0].note == ''
    assert vocabulary.explanations[0].sentences[0].en == 'He played a major role.'
    assert vocabulary.explanations[0].sentences[0].ja == '彼は主要な役割を果たした'
    assert len(vocabulary.explanations[0].synonyms) == 0
    assert vocabulary.explanations[0].antonyms[0].en == 'minor'
    assert vocabulary.explanations[0].antonyms[0].ja == 'マイナーな'

    assert vocabulary.explanations[1].partOfSpeech == '動詞'
    assert vocabulary.explanations[1].meaningsJa[0].meaning == '~を専攻する'
    assert vocabulary.explanations[1].meaningsJa[0].note == 'major in ~ の形で使う'
    assert vocabulary.explanations[1].sentences[0].en == 'I major in computer science.'
    assert vocabulary.explanations[1].sentences[0].ja == '私はコンピュータサイエンスを専攻している。'
    assert vocabulary.explanations[1].synonyms[0].en == 'specialize in'
    assert vocabulary.explanations[1].synonyms[0].ja == '専攻する'
    assert len(vocabulary.explanations[1].antonyms) == 0

    assert vocabulary.related_term[0].en == 'majority'
    assert vocabulary.related_term[0].ja == '大多数'

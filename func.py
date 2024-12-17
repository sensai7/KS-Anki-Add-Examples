import re


def extract_furigana(entry_furigana):
    # Get the first word if multiple
    first_entry = entry_furigana.split(',')[0]
    # Remove kanji, spaces, and brackets
    cleaned = re.sub(r'[一-龯\s\[\]]', '', first_entry)

    return cleaned


def generate_variations(word):
    variations = set()
    variations.add(word)

    # Handling Ichidan verbs (ending in 'る' after a vowel) and godan
    if word.endswith('る'):
        # Remove the last 'る' to get the stem
        base = word[:-1]

        # Adding common conjugations for Ichidan verbs
        variations.update([
            # ichidan
            f"{base}ます",  # polite form
            f"{base}ません",  # polite neg
            f"{base}ました",  # polite past
            f"{base}て",  # te-form
            f"{base}た",  # past form
            f"{base}ない",  # negative form
            f"{base}なかった",  # negative past form
            f"{base}よう",  # volitional form
            f"{base}られる",  # potential form
            f"{base}させる",  # causative form
            f"{base}させられる"  # causative passive form
            # godan
            f"{base}ります",  # polite form
            f"{base}りません",  # polite neg
            f"{base}りました",  # polite past
            f"{base}って",  # te-form
            f"{base}った",  # past form
            f"{base}らない",  # negative form
            f"{base}らなかった",  # negative past form
            f"{base}ろう",  # volitional form
            f"{base}れる",  # potential form
        ])

    # Handling Godan verbs
    elif word.endswith(('う', 'く', 'す', 'つ', 'ぬ', 'ぶ', 'む', 'ぐ')):
        base = word[:-1]

        if word.endswith('う'):
            variations.update([
                f"{base}います",  # polite form (e.g., 買います)
                f"{base}いません",  # polite neg
                f"{base}いました",  # polite past
                f"{base}って",  # te-form (e.g., 買って)
                f"{base}った",  # past form (e.g., 買った)
                f"{base}わない",  # negative form (e.g., 買わない)
                f"{base}わなかった",  # negative past form (e.g., 買わなかった)
                f"{base}おう",  # volitional form (e.g., 買おう)
                f"{base}える",  # potential form (e.g., 買える)
                f"{base}われる",  # passive form (e.g., 買われる)
                f"{base}わせる",  # causative form (e.g., 買わせる)
                f"{base}わせられる"  # causative passive form (e.g., 買わせられる)
            ])

        elif word.endswith('く'):
            variations.update([
                f"{base}きます",  # polite form (e.g., 書きます)
                f"{base}きません",  # polite neg
                f"{base}きました",  # polite past
                f"{base}いて",  # te-form (e.g., 書いて)
                f"{base}いた",  # past form (e.g., 書いた)
                f"{base}かない",  # negative form (e.g., 書かない)
                f"{base}かなかった",  # negative past form (e.g., 書かなかった)
                f"{base}こう",  # volitional form (e.g., 書こう)
                f"{base}ける",  # potential form (e.g., 書ける)
                f"{base}かれる",  # passive form (e.g., 書かれる)
                f"{base}かせる",  # causative form (e.g., 書かせる)
                f"{base}かせられる"  # causative passive form (e.g., 書かせられる)
            ])

        elif word.endswith('ぐ'):
            variations.update([
                f"{base}ぎます",  # polite form (e.g., 泳ぎます)
                f"{base}ぎません",  # polite neg
                f"{base}ぎました",  # polite past
                f"{base}いで",  # te-form (e.g., 泳いで)
                f"{base}いだ",  # past form (e.g., 泳いだ)
                f"{base}がない",  # negative form (e.g., 泳がない)
                f"{base}がなかった",  # negative past form (e.g., 泳がなかった)
                f"{base}ごう",  # volitional form (e.g., 泳ごう)
                f"{base}げる",  # potential form (e.g., 泳げる)
                f"{base}がれる",  # passive form (e.g., 泳がれる)
                f"{base}がせる",  # causative form (e.g., 泳がせる)
                f"{base}がせられる"  # causative passive form (e.g., 泳がせられる)
            ])

        elif word.endswith('す'):
            variations.update([
                f"{base}します",  # polite form (e.g., 話します)
                f"{base}しません",  # polite neg
                f"{base}しました",  # polite past
                f"{base}して",  # te-form (e.g., 話して)
                f"{base}した",  # past form (e.g., 話した)
                f"{base}さない",  # negative form (e.g., 話さない)
                f"{base}さなかった",  # negative past form (e.g., 話さなかった)
                f"{base}そう",  # volitional form (e.g., 話そう)
                f"{base}せる",  # potential form (e.g., 話せる)
                f"{base}される",  # passive form (e.g., 話される)
                f"{base}させる",  # causative form (e.g., 話させる)
                f"{base}させられる"  # causative passive form (e.g., 話させられる)
            ])

        elif word.endswith('つ'):
            variations.update([
                f"{base}ちます",  # polite form (e.g., 待ちます)
                f"{base}ちません",  # polite neg
                f"{base}ちました",  # polite past
                f"{base}って",  # te-form (e.g., 待って)
                f"{base}った",  # past form (e.g., 待った)
                f"{base}たない",  # negative form (e.g., 待たない)
                f"{base}たなかった",  # negative past form (e.g., 待たなかった)
                f"{base}とう",  # volitional form (e.g., 待とう)
                f"{base}てる",  # potential form (e.g., 待てる)
                f"{base}たれる",  # passive form (e.g., 待たれる)
                f"{base}たせる",  # causative form (e.g., 待たせる)
                f"{base}たせられる"  # causative passive form (e.g., 待たせられる)
            ])

        elif word.endswith('ぬ') or word.endswith('む'):
            ending_char = word[-1]
            if ending_char == 'ぬ':
                variations.update([
                    f"{base}にます",  # polite form (e.g., 死にます)
                    f"{base}にません",  # polite neg
                    f"{base}にました",  # polite past
                    f"{base}んで",  # te-form (e.g., 死んで)
                    f"{base}んだ",  # past form (e.g., 死んだ)
                    f"{base}なない",  # negative form (e.g., 死なない)
                    f"{base}ななかった",  # negative past form (e.g., 死ななかった)
                    f"{base}のう",  # volitional form (e.g., 死のう)
                    f"{base}ねる",  # potential form (e.g., 死ねる)
                    f"{base}なれる",  # passive form (e.g., 死なれる)
                    f"{base}なせる",  # causative form (e.g., 死なせる)
                    f"{base}なせられる"  # causative passive form (e.g., 死なせられる)
                ])
            elif ending_char == 'む':
                variations.update([
                    f"{base}みます",  # polite form (e.g., 読みます)
                    f"{base}みません",  # polite neg
                    f"{base}みました",  # polite past
                    f"{base}んで",  # te-form (e.g., 読んで)
                    f"{base}んだ",  # past form (e.g., 読んだ)
                    f"{base}まない",  # negative form (e.g., 読まない)
                    f"{base}まなかった",  # negative past form (e.g., 読まなかった)
                    f"{base}もう",  # volitional form (e.g., 読もう)
                    f"{base}める",  # potential form (e.g., 読める)
                    f"{base}まれる",  # passive form (e.g., 読まれる)
                    f"{base}ませる",  # causative form (e.g., 読ませる)
                    f"{base}ませられる"  # causative passive form (e.g., 読ませられる)
                ])

        elif word.endswith('ぶ'):
            variations.update([
                f"{base}びます",  # polite form (e.g., 飛びます)
                f"{base}びません",  # polite neg
                f"{base}びました",  # polite past
                f"{base}んで",  # te-form (e.g., 飛んで)
                f"{base}んだ",  # past form (e.g., 飛んだ)
                f"{base}ばない",  # negative form (e.g., 飛ばない)
                f"{base}ばなかった",  # negative past form (e.g., 飛ばなかった)
                f"{base}ぼう",  # volitional form (e.g., 飛ぼう)
                f"{base}べる",  # potential form (e.g., 飛べる)
                f"{base}ばれる",  # passive form (e.g., 飛ばれる)
                f"{base}ばせる",  # causative form (e.g., 飛ばせる)
                f"{base}ばせられる"  # causative passive form (e.g., 飛ばせられる)
            ])

    # Handling i-adjectives (ending in 'い')
    elif word.endswith('い') and len(word) > 1:
        base = word[:-1]  # Remove the last 'い' to get the adjective stem

        # Adding common conjugations for i-adjectives
        variations.update([
            f"{base}くない",  # negative form (e.g., 高くない)
            f"{base}かった",  # past form (e.g., 高かった)
            f"{base}くなかった",  # negative past form (e.g., 高くなかった)
            f"{base}く",  # adverbial form (e.g., 高く)
        ])

    return variations


def get_examples(df_sentences, variations, max_examples=3):
    # Generate all variations of the word
    # variations = generate_variations(word)

    # Create a regex pattern to match any of the variations
    pattern = '|'.join(re.escape(variation) for variation in variations)

    # Retrieve up to max_examples sentences that contain any of the variations
    df_three_examples = df_sentences[df_sentences['jp'].str.contains(pattern, regex=True)].head(max_examples)

    return df_three_examples


def highlight_string(text, words_set):
    for w in words_set:
        text = text.replace(w, f"<font color='#FFFF00'>{w}</font>")
    return text

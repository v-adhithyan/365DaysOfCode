import re
from collections import Counter
from itertools import product
from difflib import SequenceMatcher

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    with open(RSS_FEED, "r") as f:
        rss = f.read()
        return TAG_HTML.findall(rss)


def get_top_tags(tags):
    counter = Counter(tags)
    return counter.most_common(TOP_NUMBER)


def get_similarities(tags):
    similar_tags = set()
    for a, b in product(tags, repeat=2):
        s = SequenceMatcher(a=a, b=b)
        ratio = s.quick_ratio()
        if ratio > SIMILAR:
            similar_tags.add((a, b))
    return list(similar_tags)


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))

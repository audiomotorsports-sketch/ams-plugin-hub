#!/usr/bin/env python3
"""Owner corrections of 2026-10-07 (evening), applied to every city-page draft.

Read-only toward every site. Edits only markdown drafts under city_rewrite/.
Run:  python3 -I apply_owner_corrections.py [folder ...]
Idempotent: a draft that already carries the marker line is only re-checked
for phone / review-count / lobby wording.
"""
import glob, hashlib, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
MARK = '<!-- owner-details-2026-10-07 -->'

PHONE_OLD = re.compile(r'\(?310\)?[ .-]?513[ .-]?8800')
PHONE_NEW = '(213) 429-1092'

LOBBY = [
    (re.compile(r'wait-in-the-lobby job'), 'wait-inside job'),
    (re.compile(r'\b(is|that is) a lobby wait\b'), r'\1 a wait-inside job'),
    (re.compile(r'\bwaited on in the lobby\b'), 'waited on inside the shop'),
    (re.compile(r'\bwait out in the lobby\b'), 'wait it out inside the shop'),
    (re.compile(r'\b(wait|stay) in the lobby\b'), r'\1 inside'),
    (re.compile(r'\bin the lobby\b'), 'inside the shop'),
    (re.compile(r'\blobby\b'), 'waiting area inside'),
]

# Sentence pools. {c} = city name. Chosen by a stable hash of brand+slug so
# neighbouring pages differ. All are owner-stated facts (2026-10-07).
AMENITY = [
    "If you would rather wait inside than make two trips from {c}, the shop has seating, a TV with Netflix, free Wi-Fi, a restroom and a water fountain.",
    "Waiting inside is easy for {c} customers: there is seating, Netflix on the TV, free Wi-Fi, a restroom and a water fountain, and a mall, movie theaters, restaurants and a Starbucks are within walking distance.",
    "Plenty of {c} drivers wait inside; there is seating, a TV with Netflix, free Wi-Fi and a restroom, and if you want to stretch your legs a mall, coffee shops and restaurants are a short walk away.",
    "You can wait inside with free Wi-Fi, Netflix on the TV, seating, a restroom and a water fountain, or walk to the mall, a movie theater or a Starbucks nearby while the {c} job is finished.",
    "For a longer job from {c}, some people walk to the mall, the movie theaters or a coffee shop nearby; the DoubleTree down the street has a full bar, and Cabrillo Beach is about 12 minutes away.",
    "Wait inside (seating, Netflix, free Wi-Fi, restroom, water fountain) or take a walk: restaurants, coffee shops, a Starbucks, a mall and movie theaters are all within walking distance, which {c} customers tell us makes the drop-off painless.",
]
WELCOME = [
    "Everyone is welcome here, and the shop is LGBTQ-friendly, the same way it says on Google and Yelp.",
    "The shop is LGBTQ-friendly and everyone from {c} is welcome, as our Google and Yelp listings state.",
    "Everyone is welcome; we are an LGBTQ-friendly shop and say so on Google and Yelp.",
    "{c} customers of every background are welcome, and the shop is openly LGBTQ-friendly on Google and Yelp.",
    "We are LGBTQ-friendly and everyone is welcome; it is on our Google and Yelp pages and it is how the shop runs.",
]
FREEWAY = [
    "The shop sits right off the 110 freeway, with easy access from the 405 and the 710 as well, so three freeways lead to it from {c}.",
    "From {c} you can reach us by the 110, the 405 or the 710; the shop is right off the 110 at Avalon Blvd.",
    "Three freeways lead here: we are right off the 110, and the 405 and 710 drop you close by, whichever way {c} traffic sends you.",
    "Coming from {c}, take whichever is moving: the shop is right off the 110 and easy from the 405 and the 710.",
]
# Owner-described customer groups, by city slug (plain words, no partnership claims).
GROUPS = {
    'san-pedro': "A lot of our San Pedro customers are ILWU longshore workers and refinery and rail-yard crews who come in before or after a shift.",
    'wilmington': "Wilmington is longshore, rail-yard and refinery country, and workers from all three come through the shop regularly.",
    'carson': "Carson customers include ILWU longshore workers, Union Pacific rail-yard crews, people from the local refineries, Metro bus operators and plenty of engineers and office staff from the bigger employers nearby.",
    'west-carson': "Many West Carson customers work at the port, the rail yard or one of the refineries and book around their shifts.",
    'harbor-city': "Harbor City neighbors who work the port, the refineries or the rail yard are regulars here, often dropping the car off on the way to a shift.",
    'hawthorne': "A good number of Hawthorne customers are SpaceX employees and engineers who book a lunch-hour drop-off and pick up after work.",
    'el-segundo': "El Segundo sends us engineers and staff from the aerospace and corporate offices along the 105, usually on a weekday drop-off.",
    'torrance': "Torrance customers range from refinery and port workers to engineers and staff at the corporate campuses along the 405.",
    'lomita': "Lomita customers include port and refinery workers on shift schedules, so early drop-offs are normal here.",
    'long-beach': "Long Beach is where a large share of our LGBTQ customers come from, and everyone is welcome here; Metro operators and port workers from Long Beach are regulars too.",
    'gardena': "Gardena sends us Metro bus operators and plenty of commuters who work at the bigger employers around the 110 and the 405.",
    'compton': "Compton customers include Metro operators and rail-yard and port workers who book around shift changes.",
}

def pick(pool, key):
    h = int(hashlib.sha1(key.encode()).hexdigest(), 16)
    return pool[h % len(pool)]

def city_of(text, slug):
    m = re.search(r'^city:\s*(.+)$', text, re.M)
    return m.group(1).strip() if m else slug.replace('-', ' ').title()

def add_details(text, brand, slug):
    if MARK in text:
        return text, False
    c = city_of(text, slug)
    key = f'{brand}/{slug}'
    sents = [pick(AMENITY, key + 'a').format(c=c)]
    if slug == 'long-beach':
        sents.append("Long Beach is home to many of our LGBTQ customers, and everyone is welcome at the shop; it is on our Google and Yelp pages and it is how we work.")
    else:
        sents.append(pick(WELCOME, key + 'w').format(c=c))
    sents.append(pick(FREEWAY, key + 'f').format(c=c))
    if slug in GROUPS and slug != 'long-beach':
        sents.append(GROUPS[slug])
    para = MARK + '\n' + ' '.join(sents) + '\n'
    # Insert before the H2 that precedes the first "### " question heading.
    lines = text.split('\n')
    first_q = next((i for i, l in enumerate(lines) if l.startswith('### ')), None)
    if first_q is None:
        return text, False
    h2 = next((i for i in range(first_q, -1, -1) if lines[i].startswith('## ')), None)
    if h2 is None:
        return text, False
    lines[h2:h2] = [para]
    return '\n'.join(lines), True

def fix(path, brand, slug):
    t0 = open(path, encoding='utf-8').read()
    t = PHONE_OLD.sub(PHONE_NEW, t0)
    t = t.replace('650+ reviews', '654 reviews').replace('770+ reviews', '777 reviews')
    t = t.replace('650+', '654').replace('770+', '777')
    for rx, rep in LOBBY:
        t = rx.sub(rep, t)
    t, added = add_details(t, brand, slug)
    if t != t0:
        open(path, 'w', encoding='utf-8').write(t)
    return t != t0, added

if __name__ == '__main__':
    folders = sys.argv[1:] or sorted(glob.glob(os.path.join(BASE, '*/drafts')) + glob.glob(os.path.join(BASE, '*/drafts_pending')))
    changed = added = total = 0
    for folder in folders:
        folder = os.path.join(BASE, folder) if not os.path.isabs(folder) else folder
        brand = os.path.basename(os.path.dirname(folder))
        for p in sorted(glob.glob(os.path.join(folder, '*.md'))):
            total += 1
            ch, ad = fix(p, brand, os.path.basename(p)[:-3])
            changed += ch; added += ad
    print(f'files={total} changed={changed} details_added={added}')

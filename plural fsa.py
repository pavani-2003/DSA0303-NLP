class PluralFiniteStateMachine:
    def __init__(self):
        self.state = 'start'

    def pluralize(self, noun):
        self.state = 'start'
        if noun.endswith('s') or noun.endswith('x') or noun.endswith('z') or noun.endswith('ch') or noun.endswith('sh'):
            return noun + 'es'
        elif noun.endswith('y'):
            if self.state == 'start':
                self.state = 'vowel'
            return noun[:-1] + 'ies'
        elif noun.endswith('f') or noun.endswith('fe'):
            return noun[:-2] + 'ves'
        else:
            return noun + 's'

# Test the pluralization machine
pluralizer = PluralFiniteStateMachine()

nouns = ['cat', 'dog', 'fox', 'city', 'baby', 'leaf', 'wolf', 'church', 'fish']

for noun in nouns:
    plural = pluralizer.pluralize(noun)
    print(f'{noun} (plural) -> {plural}')

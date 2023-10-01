# Unit 3


class Parser:
    def __init__(self, dataSet):
        self.dataSet = dataSet
        self.words = list()
        self.abreviations = list()
    
    def remove_backslash_n(self):
        for i in range(len(self.dataSet)):
            self.dataSet[i] = self.dataSet[i].strip('\n')
    
    def find_the_broken_word_between_two_consecutive_lines(self):
        '''
        example:
            line 24) uppercase and lowercase letters can be used to represent a person’s name, and a field con-
            line 25) sisting of decimal digits could represent a person’s age.
        
        '''
        # need to fix bug from adams.txt
        for i in range(len(self.dataSet)-1):
            line = self.dataSet[i]
            nextLine = self.dataSet[i+1]
            try:
                if line[-1] == '-':
                    end = nextLine.find(' ')
                    if not end == -1:
                        secondPart = nextLine[:end]
                        self.dataSet[i+1] = nextLine[end+1:]
                    else:
                        secondPart = nextLine
                        self.dataSet[i+1] = ""

                    self.dataSet[i] = line[:-1] + secondPart
            except:
                print(i)
                raise "buggg"
    
    def replace_parentheses_with_space(self):
        for i in range(len(self.dataSet)):
            for c in '()':
                self.dataSet[i] = self.dataSet[i].replace(c, ' ')
    
    def replace_square_braces_with_space(self):
        for i in range(len(self.dataSet)):
            for c in '[]':
                self.dataSet[i] = self.dataSet[i].replace(c, ' ')

    def replace_curly_braces_with_space(self):
        for i in range(len(self.dataSet)):
            for c in '{}':
                self.dataSet[i] = self.dataSet[i].replace(c, ' ')
    
    def replace_tilda_with_space(self):
        for i in range(len(self.dataSet)):
            self.dataSet[i] = self.dataSet[i].replace('—', ' ')
            
    def replace_black_circle_with_space(self):
        for i in range(len(self.dataSet)):
            self.dataSet[i] = self.dataSet[i].replace('•', ' ')
                
    def replace_dot_comma_with_space(self):
        for i in range(len(self.dataSet)):
            for c in '.,':
                self.dataSet[i] = self.dataSet[i].replace(c, ' ')
    
    def replace_colon_semicolon_with_space(self):
        for i in range(len(self.dataSet)):
            for c in ';:':
                self.dataSet[i] = self.dataSet[i].replace(c, ' ')
        
    def breakdown_to_words(self):
        for line in self.dataSet:
            for word in line.split():
                self.words.append(word)

    def remove_extra(self, li):
        for word in li:
            self.words.remove(word)
    
    def find_abreviations(self):
        extra = list()
        for word in self.words:
            if word.isupper() and len(word) > 1:
                self.abreviations.append(word)
                extra.append(word)
        self.remove_extra(extra)
        
    def toLower(self):
        for i in range(len(self.words)):
            self.words[i] = self.words[i].lower()
            
    def remove_numbers(self):
        extra = list()
        for word in self.words:
            if word.isdigit():
                extra.append(word)
        self.remove_extra(extra)
    
    def remove_one_length_words(self):
        extra = list()
        for word in self.words:
            if len(word) == 1:
                extra.append(word)
        self.remove_extra(extra)
                
    def remove_articles_words(self):
        extra = list()
        articles = ['a', 'an', 'the']
        for word in self.words:
            if word in articles:
                extra.append(word)
        self.remove_extra(extra)
        
    def remove_To_Be_words(self):
        extra = list()
        ToBe = ['am', 'is', 'are']
        for word in self.words:
            if word in ToBe:
                extra.append(word)
        self.remove_extra(extra)
    
    def remove_conjunctions(self):
        extra = list()
        conj = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so', 'as', 'if']
        for word in self.words:
            if word in conj:
                extra.append(word)
        self.remove_extra(extra)
        
    def remove_prepositions(self):
        extra = list()
        prep = [
            'from', 'for', 'about', 'but', 'or', 'and', 'on', 'at', 'in',
            'above', 'of', 'by', 'with', 'than', 'around', 'under', 'to'
        ]
        for word in self.words:
            if word in prep:
                extra.append(word)
        self.remove_extra(extra)

    # Pronouns  
    # 1) Personal Pronouns:
    # 1-1) Subject Pronouns
    def remove_subject_pronouns(self):
        extra = list()
        subj = ['i', 'you', 'he', 'she', 'it', 'we', 'they']
        for word in self.words:
            if word in subj:
                extra.append(word)
        self.remove_extra(extra)
        
    # 1-2) Object Pronouns
    def remove_object_pronouns(self):
        extra = list()
        obj = ['me', 'you', 'him', 'her', 'it', 'us', 'them']
        for word in self.words:
            if word in obj:
                extra.append(word)
        self.remove_extra(extra)
    
    def remove_personal_pronouns(self):
        self.remove_subject_pronouns()
        self.remove_object_pronouns()

    # 2) Possessive Pronouns
    def remove_possessive_pronouns(self):
        extra = list()
        pos = ['mine', 'yours', 'his', 'hers', 'its', 'ours', 'theirs']
        for word in self.words:
            if word in pos:
                extra.append(word)
        self.remove_extra(extra)

    # 3) Relative Pronouns
    def remove_relative_pronouns(self):
        extra = list()
        rel = ['who', 'whom', 'which', 'that', 'where', 'whose']
        for word in self.words:
            if word in rel:
                extra.append(word)
        self.remove_extra(extra)

    # 4) Demonstrative Pronouns
    def remove_demonstrative_pronouns(self):
        extra = list()
        demo = ['this', 'that', 'these', 'those']
        for word in self.words:
            if word in demo:
                extra.append(word)
        self.remove_extra(extra)

    # 5) Reflexive Pronouns
    def remove_reflexive_pronouns(self):
        extra = list()
        ref = [
            'myself', 'yourself', 'himself', 'herself',
            'itself', 'ourselves', 'themselves'
        ]
        for word in self.words:
            if word in ref:
                extra.append(word)
        self.remove_extra(extra)
    
    def remove_pronouns(self):
        self.remove_personal_pronouns()
        self.remove_possessive_pronouns()
        self.remove_relative_pronouns()
        self.remove_demonstrative_pronouns()
        self.remove_reflexive_pronouns()

    def remove_uncategorized(self, custom = []):
        extra = list()
        junk = ['be', 'have', 'do', 'not']
        junk.extend(custom)
        for word in self.words:
            if word in junk:
                extra.append(word)
        self.remove_extra(extra)

    def key(self):
        return self.words
            
    def abr(self):
        print(self.abreviations)
    
    def show(self):
        print(self.dataSet)


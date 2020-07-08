class SearchEngineBase(object):
    def __init__(self):
        pass

    
    def add_corpus(self, file_path):
        with open(file_path, 'r', encoding="utf-8") as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    
    def process_corpus(self, id, text):
        raise Exception('process corpus not implemented.')


    def search(self, query):
        raise Exception('search not implemented')


def main(search_engine):
    for file_path in ['C:/file/tmp/1.txt','C:/file/tmp/2.txt','C:/file/tmp/3.txt',
                    'C:/file/tmp/4.txt','C:/file/tmp/5.txt','C:/file/tmp/6.txt',
                    'C:/file/tmp/7.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)

class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}


    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text
    
    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results

import re

class BOWEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.__id_to_words = {}

    
    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]',' ', text) 
        # 转为小写
        text = text.lower()
        # 生成单词列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词 set
        return set(word_list)

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.inverted_index = {}

    def process_corpus(self, id, text):
        # 将文本分解为单词集合
        words = self.parse_text_to_words(text)
        # 循环集合,创建单词对应文本id
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)

    def search(self, query):
        # 将查询单词转换为list
        query_words = list(self.parse_text_to_words(query))
        # 创建空集合存储查询单词的index
        query_words_index = list()
        # 循环查询单词列表,初始化index为0
        for query_word in query_words:
            query_words_index.append(0)
        # 如果查询单词不在初始化的id字典中
        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []
        
        result = []
        while True:
            current_ids = []

            for idx, query_word in enumerate(query_words):
                current_idx = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]

                if current_idx >= len(current_inverted_list):
                    return result

                current_ids.append(current_inverted_list[current_idx])
            
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue

            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1


    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]',' ', text) 
        # 转为小写
        text = text.lower()
        # 生成单词列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词 set
        return set(word_list)
        
    
import pylru

class LRUCache(object):
    def __init__(self, size=32):
        self.cache = pylru.lrucache(size)

    def has(self, key):
        return key in self.cache

    def get(self, key):
        return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value

class BOWInvertedIndexEngineWithCache(BOWInvertedIndexEngine, LRUCache):
    def __init__(self):
        super().__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print('cache hit!')
            return self.get(query)

        result = super(BOWInvertedIndexEngineWithCache, self).search(query)
        self.set(query, result)
        return result



# search_engine = BOWEngine()
# search_engine = SimpleEngine()
# search_engine = BOWInvertedIndexEngine()
search_engine = BOWInvertedIndexEngineWithCache()
main(search_engine)
class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.page_count = self.page_count()
        self.item_count = self.count_item_len()

    def page_count(self):
        symbols_count = len(self.data.replace(' ', ''))
        return (symbols_count + self.items_on_page - 1) // self.items_on_page

    def count_item_len(self):
        return len(self.data)

    def count_items_on_page(self, page_number):
        if page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing")
        start_index = page_number * self.items_on_page
        end_index = min(start_index + self.items_on_page, self.item_count)
        return end_index - start_index

    def find_page(self, symbol_or_word):
        if symbol_or_word not in self.data:
            raise Exception(f"'{symbol_or_word}' is missing on the pages")
        occurrences = []
        start_index = 0
        while True:
            index = self.data.find(symbol_or_word, start_index)
            if index == -1:
                break
            page_number = index // self.items_on_page
            occurrences.append(page_number)
            start_index = index + 1
        return occurrences

    def display_page(self, page_number):
        if page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing")
        start_index = page_number * self.items_on_page
        end_index = min(start_index + self.items_on_page, self.item_count)
        return self.data[start_index:end_index]


lala = Pagination("Sweet Transvestite",5)
print(lala.display_page(1))

print(dir(lala))
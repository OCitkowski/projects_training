
class PaginationHelperBest:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1
class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

        # returns the number of items within the entire collection

    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        if len(self.collection) % self.items_per_page == 0:
            return len(self.collection) // self.items_per_page
        else:
            return len(self.collection) // self.items_per_page + 1

    def page_item_count(self, page_index):
        # page_index = float(page_index)
        if len(self.collection) // self.items_per_page < page_index:
            return -1
        elif len(self.collection) // self.items_per_page == page_index:
            items_per_page = len(self.collection) % self.items_per_page
            if items_per_page == 0:
                return -1
            else:
                return len(self.collection) % self.items_per_page
        else:
            return self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range

    def page_index(self, item_index):
        print(f'{len(self.collection)} *** {item_index}')

        if item_index >= len(self.collection) or item_index < 0:
            return -1
        else:
            return (item_index + 1) // self.items_per_page
if __name__ == '__main__':
    collection = range(1, 25)
    print(len(collection))
    helper = PaginationHelper(collection, 3)
    #
    # print(f'{helper.page_count()}  **page_count** ')
    # # assert helper.page_count() == 3
    # #
    # print(f'{helper.item_count()}  **item_count** ')
    # # assert helper.item_count() == 7
    #
    # print(f'{helper.page_item_count(0)}')
    # print(f'{helper.page_item_count(1)}')
    # print(f'{helper.page_item_count(2)}')
    # print(f'{helper.page_item_count(3)}')
    # print(f'{helper.page_item_count(4)}')
    #
    # assert helper.page_index(3) == 2

    print(f'{helper.page_index(0)}')
    print(f'{helper.page_index(5)}')
    print(f'{helper.page_index(8)}')
    print(f'{helper.page_index(10)}')
    print(f'{helper.page_index(24)}')

class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"

    def __eq__(self, other):
        return self.uid == other.uid

    def is_recent(self, n):
        return (2025 - self.year) <= n


class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Author: {self.author}, Pages: {self.pages}"


class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return f"Article -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Journal: {self.journal}, DOI: {self.doi}"


class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration

    def __str__(self):
        return f"Podcast -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Host: {self.host}, Duration: {self.duration} mins"



def save_to_file(items, filename):
    with open(filename, 'w') as file:
        for item in items:
            if isinstance(item, Book):
                file.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif isinstance(item, Article):
                file.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif isinstance(item, Podcast):
                file.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")

def load_from_file(filename):
    items = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            item_type = parts[0]
            if item_type == "Book":
                items.append(Book(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
            elif item_type == "Article":
                items.append(Article(parts[1], parts[2], int(parts[3]), parts[4], parts[5]))
            elif item_type == "Podcast":
                items.append(Podcast(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
    return items

def filter_recent(items, years=5):
    return [item for item in items if item.is_recent(years)]

def filter_articles_by_doi(items, doi_prefix="10.1234"):
    return [item for item in items if isinstance(item, Article) and item.doi.startswith(doi_prefix)]

# Sample usage
items = [
    Book("S000", "Book Selen", 2004, "Selen", 1400),
    Article("E000", "Article Ece", 2003, "Ece", "01/a2005"),
    Podcast("B000", "Podcast Burcu", 2005, "Burcu", 21),
    Article("A101", "Article1", 2025, "Journal1", "134/wıqdo9"),
    Podcast("P101", "Podcast1", 2024, "Host1", 200),
    Book("B101", "Book1", 2023, "Author1", 100)
]
save_to_file(items, "archive.txt")
loaded_items = load_from_file("archive.txt")

for item in loaded_items:
    print(item)

print("\nRecent Items:")
recent_items = filter_recent(loaded_items, 5)
if recent_items:
    for item in recent_items:
        print(item)
else:
    print("No items found from that last years.")


print("\nArticles with DOI starting '10.1234':")
articles_with_doi = filter_articles_by_doi(loaded_items)
if articles_with_doi:
    for item in articles_with_doi:
        print(item)
else:
    print("No articles found with that DOI starting.")

N = int(input())
book_titles = []

# Store all book titles in a list
for _ in range(N):
    titles = input().split(", ")
    book_titles.extend(titles)

# Count the frequency of each book title
frequency = {}
for title in book_titles:
    frequency[title] = frequency.get(title, 0) + 1

# Print the frequency of each unique book title
for title in sorted(frequency.keys()):
    print(f"{title}: {frequency[title]}")